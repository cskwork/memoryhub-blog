---
title: "Building Production-Grade Agents with Claude Agent SDK"
date: 2025-10-25T07:19:33+09:00
slug: "874-Claude-Agent-SDK로-프로덕션-수준의-에이전트-구축하기"
original_url: "https://memoryhub.tistory.com/874"
tistory_id: 874
draft: false
---

Claude Agent SDK is Anthropic's verified infrastructure for building autonomous AI agents, powering Claude Code and available to all developers since September 2025. This SDK excels at file access, code execution, and long-running tasks requiring complex reasoning, maintaining focus for **over 30 hours** while automatically managing context. Through built-in tools, fine-grained permission management, and validated multi-agent orchestration patterns, it delivers production-grade capabilities for coding automation, customer support, research workflows, and enterprise applications. This framework has achieved cutting-edge **77.2% performance on SWE-bench Verified**, with users reporting dramatic productivity improvements such as reducing complex document work from 23 hours to 5 hours.

## Core Architecture Powering Autonomous Agents

Claude Agent SDK implements a sophisticated **3-step agent loop** that reflects how professional developers work: gather context → perform action → validate work → repeat. Through this iterative cycle, agents progressively build understanding, make progress through tool use, and self-correct based on validation results. This architecture is built on several foundational components working in harmony.

At the core is **automatic context management**, which prevents token overflow issues that plague other frameworks. The SDK performs automatic compression and summarization during long sessions, allowing agents to maintain consistent state in workflows running for hours without manual intervention. Context engineering leverages the file system itself as a structuring mechanism—folder hierarchies and file organization become part of the agent's mental model. The **CLAUDE.md memory system** provides persistent context at both project level (./.claude/CLAUDE.md) and user level (~/.claude/CLAUDE.md), storing rules, guidelines, and accumulated knowledge across sessions.

The **tool ecosystem** provides comprehensive computer access through built-in capabilities: file operations (Read, Write, Edit, MultiEdit), code execution via Bash commands, search tools (Grep, Glob, WebSearch, WebFetch), process management, and task delegation. Rather than requiring custom implementations for each task, the SDK follows the philosophy of "give Claude the computer"—providing the same tools that programmers use daily. This approach has proven effective not just for coding but also for research, content creation, data analysis, and workflow automation.

**MCP (Model Context Protocol) integration** standardizes connections to external systems through multiple transport mechanisms. SDK MCP servers run in-process without subprocess overhead, providing optimal performance for custom tools. External MCP servers communicate via stdio or SSE (Server-Sent Events), offering stronger isolation when security requirements demand it. The growing ecosystem includes pre-built servers for dozens of other services including Google Drive, Slack, GitHub, Postgres, and Puppeteer.

The **permission system** provides production-grade security controls across multiple dimensions. The allowedTools and disallowedTools parameters create explicit whitelists and blacklists for tool access. Permission modes range from manual (approval required for each action) through acceptEdits (auto-approve file changes) to bypassPermissions (full autonomy for CI/CD). **Hooks** are deterministic Python or TypeScript functions executed at specific points in the agent loop—PreToolUse hooks validate commands before execution, PostToolUse hooks log results and provide feedback.

**Subagents** enable task delegation to specialized agents, unlocking sophisticated multi-agent architectures. Each subagent maintains isolated context and specific tool permissions defined in Markdown files stored in ./.claude/agents/. This isolation enables parallel workflows and separation of concerns while preventing context drift. The orchestrator agent maintains compact global state while subagents handle focused responsibilities.

Installation requires **Python 3.10+ or Node.js 18+**, with the SDK available via pip install claude-agent-sdk or npm install @anthropic-ai/claude-agent-sdk. Authentication uses Anthropic API keys, AWS Bedrock, or Google Vertex AI credentials. The framework provides two interaction modes: simple query() function for one-off tasks and a full-featured ClaudeSDKClient for complex multi-turn conversations with custom tools and session management.

## Engineering Practices That Distinguish Prototype from Production

SDK error handling follows a comprehensive hierarchy with specific exception types for different failure modes. The base ClaudeSDKError catches all SDK-related failures, while CLINotFoundError, CLIConnectionError, ProcessError, and CLIJSONDecodeError enable targeted recovery strategies. Production systems must wrap all agent interactions in try-except blocks that distinguish between retryable failures (connection issues) and fatal errors (missing dependencies):

```python
from claude_agent_sdk import (
    ClaudeSDKError,
    CLINotFoundError,
    ProcessError
)

try:
    async for message in query(prompt="Task description"):
        process(message)
except CLINotFoundError:
    install_claude_code_cli()
except ProcessError as e:
    log_failure(e.exit_code)
    retry_with_backoff()
except ClaudeSDKError as e:
    escalate_to_human(e)
```

**Hook-based safety patterns** provide the most effective defense against risky operations. Pre-tool-use hooks intercept commands before execution, enabling validation against dangerous patterns. The following pattern blocks dangerous bash commands while allowing safe operations:

```python
from claude_agent_sdk import ClaudeAgentOptions, HookMatcher

def validate_bash_commands(event):
    """Prevent execution of dangerous commands"""
    dangerous_patterns = [
        r'rm\s+-rf',
        r'sudo',
        r'curl.*\|\s*sh',
        r'wget.*\|\s*sh',
        r':(){ :|:& };:',  # fork bomb
        r'dd\s+if=.*of=/dev/[sh]d',
        r'mkfs',
        r'>\s*/dev/[sh]d'
    ]

    command = event.tool_input.get('command', '')

    import re
    for pattern in dangerous_patterns:
        if re.search(pattern, command):
            return {
                "block": True,
                "message": f"Command blocked by security policy: {pattern}"
            }

    return {"allow": True}

options = ClaudeAgentOptions(
    hooks=[{
        "matcher": HookMatcher(tool_name="bash"),
        "pre_tool_use": validate_bash_commands
    }]
)
```

**Custom MCP tools** extend the SDK's capabilities with domain-specific tasks. In-process MCP servers provide optimal performance while maintaining type safety. Production implementations require clear error handling, input validation, and comprehensive documentation:

```python
from claude_agent_sdk import create_mcp_server
from mcp.types import Tool, TextContent

# Define in-process server
async def create_customer_tools():
    """MCP tools for customer data operations"""

    @mcp_server.tool()
    async def fetch_customer_data(customer_id: str) -> str:
        """Fetch customer information by ID

        Args:
            customer_id: Unique customer identifier

        Returns:
            Customer data in JSON format
        """
        try:
            # Validation
            if not customer_id.isalnum():
                raise ValueError("Invalid customer_id format")

            # Database query
            customer = await db.customers.find_one({"_id": customer_id})

            if not customer:
                return json.dumps({"error": "Customer not found"})

            return json.dumps({
                "id": customer["_id"],
                "name": customer["name"],
                "tier": customer["tier"],
                "lifetime_value": customer["ltv"]
            })

        except Exception as e:
            logger.error(f"fetch_customer_data failed for customer_id={customer_id}: {e}")
            raise

    @mcp_server.tool()
    async def update_customer_tier(customer_id: str, new_tier: str) -> str:
        """Update customer tier level

        Args:
            customer_id: Unique customer identifier
            new_tier: New tier (bronze/silver/gold/platinum)

        Returns:
            Operation status
        """
        valid_tiers = {"bronze", "silver", "gold", "platinum"}

        if new_tier not in valid_tiers:
            return json.dumps({
                "error": f"Invalid tier. Must be one of {valid_tiers}"
            })

        try:
            result = await db.customers.update_one(
                {"_id": customer_id},
                {"$set": {"tier": new_tier, "updated_at": datetime.now()}}
            )

            if result.modified_count == 0:
                return json.dumps({"error": "Customer not found or update failed"})

            await audit_log.record("customer_tier_update", {
                "customer_id": customer_id,
                "old_tier": "unknown",
                "new_tier": new_tier
            })

            return json.dumps({
                "success": True,
                "customer_id": customer_id,
                "new_tier": new_tier
            })

        except Exception as e:
            logger.error(f"update_customer_tier failed for customer_id={customer_id}: {e}")
            raise

# Integrate into SDK configuration
async def main():
    mcp_server = await create_customer_tools()

    options = ClaudeAgentOptions(
        mcp_servers=[mcp_server],
        allowed_tools=["fetch_customer_data", "update_customer_tier"]
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query("Upgrade customer ID C12345's tier to platinum")
```

The **orchestrator pattern** enables decomposition of complex workflows, distributing the overall task across specialized subagents. The orchestrator maintains compact global state, routes work, and aggregates results:

```python
# ./.claude/agents/coordinator.md
"""
# Customer Onboarding Coordinator

You are a coordinator agent managing the new customer onboarding process.

## Available Subagents

- **data-validator**: Validate customer information and ensure completeness
- **provisioner**: Set up accounts and provision resources
- **notifier**: Send welcome emails and notifications

## Workflow

1. Call data-validator to validate customer data
2. On validation success, call provisioner to set up account
3. On successful provisioning, call notifier to send welcome email
4. Track progress after each step and handle errors

## Constraints

- Do not share context between subagents
- Pass only the result of each step to the next agent
- Escalate to human on failure
"""

# Orchestrator implementation
async def onboard_customer(customer_data: dict):
    """Onboard customer using orchestrator"""

    options = ClaudeAgentOptions(
        subagent_dir="./.claude/agents"
    )

    async with ClaudeSDKClient(options=options) as client:
        # Step 1: Validate
        validation_result = await client.query(
            f"@data-validator Validate this customer data: {customer_data}"
        )

        if "invalid" in validation_result.lower():
            return {"status": "failed", "reason": "Validation failed"}

        # Step 2: Provision
        provisioning_result = await client.query(
            f"@provisioner Set up account for {customer_data['email']}"
        )

        if "error" in provisioning_result.lower():
            return {"status": "failed", "reason": "Provisioning failed"}

        # Step 3: Notify
        notification_result = await client.query(
            f"@notifier Send welcome email to {customer_data['email']}"
        )

        return {
            "status": "success",
            "customer_email": customer_data['email'],
            "steps_completed": ["validation", "provisioning", "notification"]
        }
```

**Context isolation** maintains clear boundaries between subagents. Each subagent receives its own CLAUDE.md file, dedicated tool set, and isolated working directory:

```python
# ./.claude/agents/code-reviewer.md
"""
# Code Reviewer

You are a professional code reviewer examining Pull Requests.

## Tools

- Read, Grep: For code inspection
- WebSearch: For verifying best practices

## Responsibilities

1. Verify adherence to coding standards
2. Check for security vulnerabilities
3. Identify performance issues
4. Validate test coverage

## Output Format

Provide structured review for each PR:
- Severity level (critical/major/minor)
- Specific issues with line numbers
- Improvement recommendations

## Constraints

- Do not fix code, only review
- Return results only to orchestrator
- No direct access to external systems
"""

options = ClaudeAgentOptions(
    subagent_dir="./.claude/agents",
    # Reviewer has read-only access
    allowed_tools_per_subagent={
        "code-reviewer": ["Read", "Grep", "WebSearch"]
    }
)
```

**CLAUDE.md best practices** document project-specific conventions, architectural decisions, and common pitfalls:

```markdown
# Project Context

## Architecture

This codebase uses a microservices architecture:
- `/services/api`: Express.js REST API
- `/services/worker`: Redis Queue worker
- `/services/db`: PostgreSQL schema and migrations

## Coding Standards

- TypeScript strict mode required
- JSDoc comments on all public functions
- 100-character line length limit
- Formatting with Prettier (config: .prettierrc.json)

## Common Mistakes

❌ Don't use direct string concatenation in database queries
✅ Instead use parameterized queries

❌ Don't access environment variables directly via process.env.VAR
✅ Use type-safe getters from config/environment.ts

## Testing

- Unit tests use Jest
- Integration tests use Supertest
- All PRs require 80%+ coverage

## Deployment

- PR merge auto-deploys to staging
- Production deployment requires manual approval
- Rollback procedure: `npm run rollback:prod`
```

**Production permission configuration** implements varying levels of autonomy per subagent:

```python
options = ClaudeAgentOptions(
    # Global default: manual approval
    permission_mode="manual",

    # Per-subagent permissions
    permission_mode_per_subagent={
        "test-writer": "acceptEdits",      # Auto-approve test files
        "code-reviewer": "readOnly",       # Read-only
        "deployer": "manual"                # Explicit approval for deploys
    },

    # Per-subagent tool restrictions
    allowed_tools_per_subagent={
        "test-writer": ["Read", "Write", "Edit", "Bash"],
        "code-reviewer": ["Read", "Grep", "WebSearch"],
        "deployer": ["Bash", "Read"]
    },

    # Hooks for risky commands
    hooks=[{
        "matcher": HookMatcher(
            subagent="deployer",
            tool_name="bash"
        ),
        "pre_tool_use": require_human_confirmation
    }]
)

def require_human_confirmation(event):
    """Require human confirmation for critical operations"""
    command = event.tool_input.get('command', '')

    critical_commands = ['git push', 'npm publish', 'kubectl apply']

    if any(cmd in command for cmd in critical_commands):
        # In real production, integrate proper approval mechanisms
        approval = input(f"Approve execution of '{command}'? (yes/no): ")

        if approval.lower() != 'yes':
            return {
                "block": True,
                "message": "User denied command execution"
            }

    return {"allow": True}
```

## Performance Tuning and Failure Modes That Determine Production Success

**Automatic prompt caching** is a built-in optimization that reduces both latency and cost while improving throughput. This feature is enabled by default without configuration. Research shows that **CLAUDE.md files provide the highest ROI**, achieving approximately 2.5x cost savings compared to MCP-only configurations while delivering better task completion rates. The combination of Claude + CLAUDE.md + MCP provides optimal performance—CLAUDE.md provides direction while MCP enables deep investigation of specific information.

**Context management strategy** prevents token overflow that weakens long-running agents. The SDK performs automatic compression, but developers control what enters context. Implement **selective context loading**, bringing only relevant information into the agent's view. Use **periodic context cleanup** during long sessions, maintaining compact global state with only plans, key decisions, and latest artifacts. Store detailed information in memory files that agents retrieve as needed rather than keeping everything in active context. The file system itself functions as a context structure—meaningful directory hierarchies become part of the agent's mental model.

**In-process MCP servers remove IPC overhead**, providing significant performance improvements over external subprocess servers. They offer simpler deployment (single process), easier debugging, better performance for tool calls, and type safety through direct function calls. Use external MCP servers only when strong isolation is required, servers need to be shared across multiple clients, or you need to leverage existing ecosystem servers. For custom tools, always prefer SDK MCP servers that run in-process.

**Streaming mode** provides real-time feedback, reducing perceived latency for interactive applications. With streaming APIs, users see the agent's reasoning unfold and can halt unproductive paths early. Single-shot mode suits batch jobs and deterministic automation but sacrifices interactivity. Production systems serving end users should universally implement streaming:

```python
async with ClaudeSDKClient(options=options) as client:
    await client.query("Complex analysis task")

    # Stream responses as they arrive
    async for msg in client.receive_response():
        if msg.type == "thinking":
            update_ui_with_reasoning(msg.content)
        elif msg.type == "tool_use":
            show_tool_invocation(msg.tool_name)
        elif msg.type == "result":
            display_final_result(msg.result)
```

**Latency reduction** requires attention to multiple factors. Tool call optimization designs focused tools that return exactly needed information, minimizing round trips. Asynchronous work properly leverages Python's async/await to avoid blocking. Context window management prevents the model from missing information as limits approach. Infrastructure choice matters too—Amazon Bedrock and Google Vertex AI may provide better latency depending on geographic location. Monitor trace-level data to identify bottlenecks in end-to-end request latency versus pure model latency.

**Common pitfalls** undermine agent effectiveness if left unaddressed. **Context overload** occurs when dumping large document files into the context window, crowding out relevant information and increasing costs. Research shows that even subsets of information make CLAUDE.md better at guiding work because agents don't call MCP tools as often as assumed. **Antipatterns and pitfalls** must be explicitly included in CLAUDE.md—agents repeat common mistakes without this guidance. Provide **exploration hints** that tell agents where to find additional information rather than assuming they'll explore comprehensively.

**Permission creep** is the fastest path to unsafe autonomy. Production systems must start with explicit allow-lists per subagent and default-deny basis. Use manual or acceptEdits permission modes—never use acceptAll in production environments. Implement pre-tool hooks that block dangerous commands like rm -rf, sudo, curl | sh. Require human confirmation for sensitive operations including git push, infrastructure changes, and database modifications. Don't expose secrets in context visible to agents. Use short-lived credentials with minimal scope.

**Tool usage problems** occur when agents don't call tools as developers expect. Even when explicitly needed to follow documentation links, agents typically call MCP only once and stop at surface explanations. Counter this tendency with explicit system prompts commanding thorough exploration, CLAUDE.md examples showing expected tool usage patterns, and validation hooks confirming agents have referenced needed resources. Avoid unnecessarily complex solutions with excessive abstractions—simple patterns outperform sophisticated frameworks.

**Architecture antipatterns** create maintenance burden and reliability issues. **Monolithic agents** trying to handle everything suffer from context drift and unclear responsibilities. Replace with orchestrator + specialized subagents following single responsibility principle. **Context sharing between subagents** leads to information leakage and unclear boundaries. Implement strict isolation where each subagent maintains its own context and returns only relevant results to the orchestrator. **Missing human-in-the-loop gates** for critical operations like merging and deploying creates risk. Add explicit confirmation steps for high-impact work. **Unversioned hooks without tests** cause conflicts and malfunctions. Treat hooks as production code with version control, automated tests, and gradual rollout.

**Cost optimization** starts with token management. Remove unnecessary verbosity from prompts and tool outputs. Dedup retrieved text in context to avoid redundant content. Limit tool payload sizes to prevent individual calls from consuming excessive tokens. Set explicit max_tokens limits to prevent runaway generation. Cache results for repeatable tasks. Batch similar operations to reduce total API calls. The Claude Sonnet 4.5 model costs $3/$15 per million tokens (input/output) but delivers substantively better performance, making it cost-effective on a per-task basis despite nominal higher price.

**Parallel agent work** scales throughput by running multiple Claude Code instances simultaneously on different problem aspects, coordinating through shared context and memory files. One practitioner described their role as "keeping as many Claude Code instances busy as possible," coordinating through shared context and memory files. This pattern works especially well when work decomposes into independent components—UI, API, and database layers can proceed in parallel with occasional synchronization.

**Monitoring and debugging** require comprehensive instrumentation. Implement **OpenTelemetry tracing** with custom spans capturing raw requests, internal prompt construction, tool calls, and final output. Track **key metrics**: token usage per request (input and output separately), end-to-end latency versus model latency, tool call success and failure rates, context window utilization, cost per task and session, error rates by type, performance per agent. Set **automated alerts** for context utilization exceeding 80%, error rates above baseline, cost budgets approaching limits, latency SLA violations, repeated tool failures.

**Trace-level evaluation** provides automated quality checks. Implement accuracy evaluation assessing response correctness, tool call validation detecting invalid JSON or missing fields, completeness scoring verifying output meets requirements, and online evaluation running continuously as data arrives. Production monitors must alert on custom span attributes or evaluation metric violations. This observability architecture enables fast diagnosis when agents malfunction—you can reconstruct the exact sequence of prompts, tool calls, and responses that led to a problem.

**Test-first autonomous coding** establishes a validated workflow pattern: a testing subagent writes tests first and confirms failure, an implementer subagent makes tests pass without modifying test files, a code review subagent enforces linting and security standards, a documentation subagent updates READMEs. This pipeline maintains separation of concerns while providing automated verification at each stage. Version-control all configuration including hooks, settings, and subagent manifests. Gate deployments with automated tests and perform gradual rollout behind feature flags. Set rollback triggers for anomaly detection to automatically revert problematic changes.

Production readiness checklist covers: architecture (orchestrator routing only, hooks versioned and validated, clear escalation paths), permissions (allow-list with default-deny, confirmation for sensitive operations, dangerous commands blocked), context (CLAUDE.md defining rules, compact global state with per-subagent isolation), performance (streaming enabled, in-process MCP servers, caching active), workflow (test-first implementation pattern, automated documentation, checkpoint strategy), observability (OpenTelemetry tracing, comprehensive logging, anomaly alerts configured, rollback plan tested), governance (human gates for critical operations, documented escalation thresholds, clear ownership, audit trails maintained).

Teams following these patterns report **dramatic improvements**: 44% faster vulnerability intake, 25% accuracy improvement, workload reduction from 23 hours to 5 hours on complex tasks. The core insight is treating agent development as proper production engineering with appropriate testing, version control, monitoring, and human oversight gates rather than experimental prototyping. Claude Agent SDK provides the infrastructure; engineering discipline determines success.
