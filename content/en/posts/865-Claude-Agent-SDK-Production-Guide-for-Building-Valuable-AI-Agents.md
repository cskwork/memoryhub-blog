---
title: "Claude Agent SDK: Production Guide for Building Valuable AI Agents"
date: 2025-10-21T20:55:28+09:00
slug: "865-Claude-Agent-SDK-Production-Guide-for-Building-Valuable-AI-Agents"
original_url: "https://memoryhub.tistory.com/865"
tistory_id: 865
draft: false
---

Claude Agent SDK has emerged as **Anthropic's production framework** for building autonomous AI agents, powering Claude Code's **$500M+ revenue run-rate** and serving **115,000+ developers** who process **195 million lines of code weekly**. The SDK transforms Claude from a conversational AI into an autonomous system with access to file systems, terminal commands, web search, and custom tools—enabling developers to build everything from coding assistants to business automation agents.

This guide provides actionable implementation instructions with working code examples, real-world company usage, and proven patterns for building production-ready agents.

## Companies using Claude Agent SDK in production

The SDK enables sophisticated agent workflows across multiple industries, with quantified business impact ranging from 70-90% time savings to complete workflow automation.

### Enterprise implementations demonstrate scale

**Palo Alto Networks** deployed Claude across 2,500+ developers for secure software development, achieving **20-30% velocity increases** in feature development and **70% faster integration** tasks for junior developers. Their CI/CD pipeline includes an AI post-processing system that automatically improves code quality, while onboarding time dropped from months to weeks.

**Novo Nordisk** built NovoScribe using Claude Agent SDK on Amazon Bedrock, reducing clinical study documentation from **10+ weeks to 10 minutes**—a **90% time reduction**. Complete study booklets that previously required entire departments now generate in under one minute, with 50% fewer review cycles. At $15M per day in drug development costs, these time savings translate to massive ROI.

**IG Group** (financial services) achieved **70 hours weekly saved** in analytics teams with **doubled productivity** in certain workflows and **triple-digit speed-to-market improvements** in marketing. The company reached **full ROI within 3 months** of deployment.

### Development tool integrations expand reach

**JetBrains** integrated Claude Agent directly into their IDEs (PyCharm, IntelliJ IDEA) using the SDK's agent harness, becoming the first third-party agent in JetBrains' ecosystem. The integration provides multi-file operations, diff previews, approval-based editing, and Plan mode for step-by-step implementation—all included in JetBrains AI subscriptions at no additional cost.

**GitHub Copilot** leverages Claude Sonnet 4.5 (the model optimized for agentic workflows) to power multi-step reasoning and complex, codebase-spanning tasks. GitHub reports "significant improvements in multi-step reasoning and code comprehension" over previous models.

### Startups achieve enterprise scale with small teams

**Lindy AI** built a no-code workflow automation platform on Claude Agent SDK with **5,000+ app integrations**, achieving **10X ARR growth** in 2025 with only 25 employees. Their agents automate lead qualification (reducing 3 hours to minutes), provide 24/7 customer support, and handle meeting automation across sales, support, and operations.

**Gradient Labs** created AI customer support agents for regulated financial institutions using Claude for intent classification, reasoning, and response generation. They achieved **80-90% automation rates**, **40-60% resolution from day one**, and **80+ CSAT scores** (98% in optimal implementations), reaching **£1M ARR in 3 months** with 11-12 paying customers.

**Circleback** built meeting intelligence using Claude Haiku 3.5 and Sonnet 4 throughout their platform, providing automatic transcription, action items, and custom automations like creating Linear tasks from feature requests. Customers report hours saved daily redirected to high-impact work.

## Real-world usage patterns by category

### Development assistants transform coding workflows

**Code generation and implementation** agents handle multi-file operations with contextual awareness. The official **Claude Code GitHub Action** enables @claude mentions to trigger automatic code analysis, PR reviews, and bug fixes. Community implementations include 100+ specialized agents organized in production-ready collections covering backend architecture, database design, frontend development, test automation, security audits, and deployment engineering.

**Code review and quality assurance** agents implement OWASP-aligned security analysis triggered on critical file changes. Anthropic's internal deployment achieved **0% error rate** on code editing benchmarks (down from 9%) and enables **5 pull requests per engineer per day** versus industry norms of 1-2. Teams report **67% increase in PR throughput** even as team sizes doubled.

**SRE and incident response** agents diagnose production issues, triage incidents, and audit code for vulnerabilities autonomously. Hai security agents demonstrated **44% faster vulnerability intake** with **25% improved accuracy** compared to manual processes.

### Workflow automation eliminates manual processes

**Task orchestration** systems like Lindy's platform connect 5,000+ apps for cross-platform automation. Implementations include sales automation (lead research, personalized outreach, call analysis), meeting automation (note-taking, action items, insight distribution), and email processing with dynamic context construction from file systems.

**Document processing pipelines** implement 7-agent workflows where one agent extracts diagrams, another generates images, others compile to Word/PDF formats, with an orchestrator managing flow. Rick Hightower's implementation reduced complex documentation workflows from **23 hours to 5 hours** (78% reduction).

**Meeting intelligence** agents from Circleback provide automatic transcription with speaker identification, topic-grouped notes, assigned action items, and agentic search across meeting history. Custom workflows identify feature requests, create tasks in Linear, and update CRMs automatically.

### Business tools deliver specialized capabilities

**Document processing** implementations like Novo Nordisk's NovoScribe use semantic search with domain expert-approved text for regulatory-grade documentation generation. Claude writes Python scripts to create Excel, PowerPoint, and Word documents with consistent formatting and complex functionality.

**Data analysis and reporting** agents perform portfolio analysis, investment evaluation via API access, and complex calculations through code execution. Financial analysis agents hook into APIs, pull market data, run calculations, and generate investment-grade insights requiring less human review.

**Customer support** systems like Gradient Labs combine knowledge graphs with Claude for intent classification, executing standard operating procedures while detecting vulnerable customers and preventing unauthorized financial advice. **HappyFox** achieved **40% increase in automated ticket resolution** and **30% increase in support agent productivity** with their AI Agent Copilot.

## Core concepts explained simply

The Claude Agent SDK provides production-ready infrastructure for building autonomous agents without custom framework development—eliminating the **3+ months** developers typically spend building agent infrastructure from scratch.

### The agent feedback loop

Every Claude agent operates in a three-step cycle: **gather context** (search files, read logs, fetch data), **take action** (execute tools, write code, call APIs), and **verify work** (check output, run tests, validate results). This loop continues until the task completes or reaches configured limits.

The SDK manages this loop automatically, handling context overflow through automatic compaction, maintaining session state for multi-turn conversations, and providing streaming or single-shot execution modes based on your needs.

### Tools enable agent capabilities

Built-in tools include **file operations** (Read, Write, Edit, MultiEdit, Glob, Grep), **execution** (Bash commands with output capture), **web capabilities** (WebSearch, WebFetch), and **specialized tools** (Task planning, Jupyter notebooks, todo tracking). Tools are the primary interface for agent actions—design them to be small, focused, and composable.

The Model Context Protocol (MCP) extends tool capabilities through standardized integrations. **SDK MCP servers** run in-process for custom Python/TypeScript tools with no subprocess overhead, while **external MCP servers** connect to services like GitHub, Slack, Google Drive, and databases through the open MCP standard.

### Hooks provide safety and control

Hooks intercept the agent loop at specific points: **PreToolUse** (before execution, can block/modify), **PostToolUse** (after execution for logging/validation), and other lifecycle events. Implement hooks to block dangerous commands, add automated validation, log tool usage for auditing, or inject additional context.

### Permission modes balance autonomy and safety

Three permission modes control agent behavior: **default** prompts users for each action (recommended for production), **acceptEdits** auto-approves file changes (for trusted contexts), and **acceptAll** auto-accepts all actions (development only). Fine-grained controls include tool allowlists/denylists, directory restrictions, and custom permission callbacks.

## Step-by-step implementation guide

### Installation and setup

Install the Claude Code CLI and SDK in under 5 minutes:

```
# Install Claude Code CLI (requires Node.js)
npm install -g @anthropic-ai/claude-code

# Verify installation
claude doctor

# Install Python SDK
pip install claude-agent-sdk

# Set API key
export ANTHROPIC_API_KEY="your-api-key-here"
```

Get your API key from <https://console.anthropic.com/>. Alternative authentication for **AWS Bedrock** (`CLAUDE_CODE_USE_BEDROCK=1`) and **Google Vertex AI** (`CLAUDE_CODE_USE_VERTEX=1`) is also supported.

### Project structure for production agents

Organize agent projects with clear separation of concerns:

```
my-agent-project/
├── .claude/
│   ├── agents/              # Subagent definitions
│   │   ├── researcher.md
│   │   ├── analyzer.md
│   │   └── writer.md
│   ├── commands/            # Custom slash commands
│   ├── settings.json        # Configuration
│   └── CLAUDE.md           # Project memory/conventions
├── src/
│   ├── agent.py            # Main agent code
│   ├── tools/              # Custom tools
│   │   ├── search.py
│   │   └── database.py
│   └── utils/              # Helper functions
├── tests/
│   └── test_agent.py
├── .env                    # Environment variables
└── requirements.txt
```

Create `.claude/CLAUDE.md` to define project conventions the agent should follow:

```
# Project Conventions
- Use Python 3.10+
- Follow PEP 8 style guide
- All functions must have docstrings
- Tests must pass before commits
- Never use `rm -rf` commands
```

## Complete code examples for practical agents

### Example 1: Code review agent

This agent automatically reviews code for security vulnerabilities, style compliance, and best practices:

```
import anyio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, HookMatcher
from claude_agent_sdk import AssistantMessage, TextBlock, ToolUseBlock
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def block_dangerous_commands(input_data, tool_use_id, context):
    """Safety hook to block dangerous bash commands"""
    tool_name = input_data["tool_name"]

    if tool_name != "Bash":
        return {}

    command = input_data["tool_input"].get("command", "")
    dangerous_patterns = ["rm -rf", "sudo", "chmod 777", "dd if="]

    for pattern in dangerous_patterns:
        if pattern in command:
            logger.warning(f"Blocked dangerous command: {command}")
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": f"Dangerous pattern blocked: {pattern}"
                }
            }
    return {}

async def log_tool_usage(input_data, tool_use_id, context):
    """Log all tool invocations for audit trail"""
    logger.info({
        "tool": input_data["tool_name"],
        "input": input_data["tool_input"],
        "tool_use_id": tool_use_id
    })
    return {}

async def code_review_agent(repo_path: str, files_to_review: list[str]):
    """
    Agent that reviews code for security, quality, and best practices

    Args:
        repo_path: Path to code repository
        files_to_review: List of file paths to review
    """

    system_prompt = """You are an expert code reviewer focused on:

1. Security vulnerabilities (OWASP Top 10)
   - SQL injection, XSS, CSRF
   - Authentication and authorization issues
   - Sensitive data exposure

2. Code quality
   - Adherence to style guide (check CLAUDE.md)
   - Function complexity and maintainability
   - Proper error handling
   - Test coverage

3. Best practices
   - Performance optimization opportunities
   - Documentation completeness
   - Naming conventions

For each issue found:
- Specify the file and line number
- Explain the problem clearly
- Suggest specific fixes
- Rate severity (critical/high/medium/low)

Output your review as a structured report with sections for each category."""

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        allowed_tools=["Read", "Grep", "Glob", "WebSearch"],  # Read-only
        permission_mode="default",
        cwd=repo_path,
        max_turns=15,
        setting_sources=["project"],  # Load CLAUDE.md
        hooks={
            "PreToolUse": [
                HookMatcher(matcher="*", hooks=[block_dangerous_commands])
            ],
            "PostToolUse": [
                HookMatcher(matcher="*", hooks=[log_tool_usage])
            ]
        }
    )

    files_list = "\n".join(f"- {f}" for f in files_to_review)
    prompt = f"""Please review the following files for security issues, code quality, and best practices:

{files_list}

1. Read each file carefully
2. Analyze for security vulnerabilities, quality issues, and best practices
3. Use WebSearch if you need to verify security patterns or latest best practices
4. Provide a comprehensive review report"""

    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)

        review_report = []
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        review_report.append(block.text)
                        print(block.text)
                    elif isinstance(block, ToolUseBlock):
                        print(f"? Reading: {block.input.get('file_path', block.name)}")

        return "\n".join(review_report)

# Usage
if __name__ == "__main__":
    async def main():
        report = await code_review_agent(
            repo_path="/path/to/repository",
            files_to_review=[
                "src/auth.py",
                "src/api/users.py",
                "src/database.py"
            ]
        )

        # Save report
        with open("code_review_report.md", "w") as f:
            f.write(report)

        print("\n✅ Review complete! Report saved to code_review_report.md")

    anyio.run(main)
```

### Example 2: Document processing workflow agent

This agent processes documents through a multi-step pipeline with custom tools:

```
import anyio
from claude_agent_sdk import (
    tool, create_sdk_mcp_server,
    ClaudeSDKClient, ClaudeAgentOptions,
    AssistantMessage, TextBlock
)
import json
from pathlib import Path
from typing import Dict, List

# Define custom tools
@tool("extract_metadata", "Extract metadata from documents", {
    "file_path": str
})
async def extract_metadata(args):
    """Extract metadata like title, author, date from documents"""
    file_path = Path(args["file_path"])

    # Simple metadata extraction (extend with actual logic)
    metadata = {
        "filename": file_path.name,
        "size": file_path.stat().st_size if file_path.exists() else 0,
        "extension": file_path.suffix
    }

    return {
        "content": [{
            "type": "text",
            "text": json.dumps(metadata, indent=2)
        }]
    }

@tool("generate_summary", "Generate summary of processed documents", {
    "documents": str,  # JSON string of document list
    "output_path": str
})
async def generate_summary(args):
    """Generate a summary report of all processed documents"""
    output_path = Path(args["output_path"])

    summary = f"""# Document Processing Summary

Processed documents:
{args["documents"]}

Generated: {output_path}
"""

    output_path.write_text(summary)

    return {
        "content": [{
            "type": "text",
            "text": f"Summary saved to {output_path}"
        }]
    }

@tool("validate_output", "Validate processed document output", {
    "output_path": str,
    "expected_sections": str  # JSON array of expected sections
})
async def validate_output(args):
    """Validate that output contains expected sections"""
    output_path = Path(args["output_path"])

    if not output_path.exists():
        return {
            "content": [{
                "type": "text",
                "text": f"❌ Validation failed: {output_path} does not exist"
            }]
        }

    content = output_path.read_text()
    expected = json.loads(args["expected_sections"])

    missing = [s for s in expected if s not in content]

    if missing:
        return {
            "content": [{
                "type": "text",
                "text": f"⚠️ Missing sections: {', '.join(missing)}"
            }]
        }

    return {
        "content": [{
            "type": "text",
            "text": "✅ Validation passed: All expected sections present"
        }]
    }

async def document_processing_agent(
    input_dir: str,
    output_dir: str,
    document_type: str = "research"
):
    """
    Agent that processes documents through a workflow pipeline

    Args:
        input_dir: Directory containing input documents
        output_dir: Directory for processed output
        document_type: Type of documents (research, technical, business)
    """

    # Create MCP server with custom tools
    doc_tools = create_sdk_mcp_server(
        name="document-tools",
        version="1.0.0",
        tools=[extract_metadata, generate_summary, validate_output]
    )

    system_prompt = f"""You are a document processing specialist handling {document_type} documents.

Your workflow:
1. Scan input directory to find all documents
2. Extract metadata from each document using extract_metadata tool
3. Read and analyze document content
4. Process each document (extract key information, structure data)
5. Generate output files in the output directory
6. Create a summary report using generate_summary tool
7. Validate output using validate_output tool

Quality standards:
- Preserve all critical information
- Maintain consistent formatting
- Include proper citations and references
- Ensure output is well-structured and readable"""

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        allowed_tools=[
            "Read", "Write", "Grep", "Glob",
            "mcp__document-tools__extract_metadata",
            "mcp__document-tools__generate_summary",
            "mcp__document-tools__validate_output"
        ],
        permission_mode="acceptEdits",  # Auto-accept file writes
        cwd=input_dir,
        mcp_servers={"document-tools": doc_tools},
        max_turns=25
    )

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    prompt = f"""Process all documents in the current directory ({input_dir}).

Expected sections in output: Introduction, Key Findings, Methodology, Conclusion

Output processed documents to: {output_dir}

Follow the complete workflow including validation."""

    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(block.text)

# Usage
if __name__ == "__main__":
    async def main():
        await document_processing_agent(
            input_dir="./input_docs",
            output_dir="./processed_docs",
            document_type="research"
        )

        print("\n✅ Document processing complete!")

    anyio.run(main)
```

### Example 3: Customer support agent with escalation

This agent handles customer inquiries with intelligent escalation:

```
import anyio
from claude_agent_sdk import (
    tool, create_sdk_mcp_server,
    ClaudeSDKClient, ClaudeAgentOptions,
    AssistantMessage, TextBlock, HookMatcher
)
import json
from datetime import datetime
from typing import Dict, Optional

# Simulated customer database
CUSTOMER_DB = {
    "C001": {
        "name": "Alice Johnson",
        "tier": "premium",
        "issues": ["Previous refund request resolved"],
        "satisfaction": 4.5
    },
    "C002": {
        "name": "Bob Smith",
        "tier": "basic",
        "issues": [],
        "satisfaction": 5.0
    }
}

# Define custom tools
@tool("lookup_customer", "Look up customer information", {
    "customer_id": str
})
async def lookup_customer(args):
    """Look up customer details from database"""
    customer_id = args["customer_id"]
    customer = CUSTOMER_DB.get(customer_id)

    if not customer:
        return {
            "content": [{
                "type": "text",
                "text": f"Customer {customer_id} not found"
            }]
        }

    return {
        "content": [{
            "type": "text",
            "text": json.dumps(customer, indent=2)
        }]
    }

@tool("create_ticket", "Create support ticket", {
    "customer_id": str,
    "issue_type": str,
    "description": str,
    "priority": str
})
async def create_ticket(args):
    """Create a support ticket in the system"""
    ticket_id = f"TICKET-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    ticket = {
        "ticket_id": ticket_id,
        "customer_id": args["customer_id"],
        "issue_type": args["issue_type"],
        "description": args["description"],
        "priority": args["priority"],
        "status": "open",
        "created": datetime.now().isoformat()
    }

    # In production, save to database
    print(f"? Created ticket: {json.dumps(ticket, indent=2)}")

    return {
        "content": [{
            "type": "text",
            "text": f"Ticket created: {ticket_id}"
        }]
    }

@tool("escalate_to_human", "Escalate to human agent", {
    "reason": str,
    "customer_id": str,
    "context": str
})
async def escalate_to_human(args):
    """Escalate issue to human agent"""
    escalation = {
        "timestamp": datetime.now().isoformat(),
        "reason": args["reason"],
        "customer_id": args["customer_id"],
        "context": args["context"]
    }

    # In production, notify human agent
    print(f"? ESCALATION: {json.dumps(escalation, indent=2)}")

    return {
        "content": [{
            "type": "text",
            "text": f"Escalated to human agent. Reason: {args['reason']}"
        }]
    }

# Escalation hook
async def check_escalation_needed(input_data, tool_use_id, context):
    """Automatically escalate refund requests"""
    tool_name = input_data["tool_name"]
    tool_input = input_data["tool_input"]

    # Auto-escalate refund requests
    if tool_name == "mcp__support-tools__create_ticket":
        if "refund" in tool_input.get("issue_type", "").lower():
            print("⚠️ Refund request detected - auto-escalating")
            # Allow ticket creation but trigger escalation

    return {}

async def customer_support_agent(
    customer_id: str,
    inquiry: str
):
    """
    Customer support agent with intelligent escalation

    Args:
        customer_id: Customer identifier
        inquiry: Customer's question or issue
    """

    # Create MCP server with support tools
    support_tools = create_sdk_mcp_server(
        name="support-tools",
        version="1.0.0",
        tools=[lookup_customer, create_ticket, escalate_to_human]
    )

    system_prompt = """You are a professional customer support agent. Your goal is to help customers efficiently while maintaining high satisfaction.

Guidelines:
1. Always look up customer information first
2. Be empathetic and professional in all responses
3. Provide clear, actionable solutions
4. Create tickets for issues requiring follow-up

Escalation rules (MUST escalate):
- Refund requests
- Account security issues
- Legal or compliance questions
- Angry customers (indicated by hostile language)
- Issues outside your knowledge

For non-escalation issues:
- Provide direct solutions
- Create tickets for tracking
- Offer alternatives when possible
- Follow up on resolution

Tone: Professional, empathetic, solution-focused"""

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        allowed_tools=[
            "mcp__support-tools__lookup_customer",
            "mcp__support-tools__create_ticket",
            "mcp__support-tools__escalate_to_human"
        ],
        permission_mode="acceptAll",  # Auto-execute support actions
        mcp_servers={"support-tools": support_tools},
        max_turns=10,
        hooks={
            "PostToolUse": [
                HookMatcher(matcher="*", hooks=[check_escalation_needed])
            ]
        }
    )

    prompt = f"""Customer {customer_id} has the following inquiry:

"{inquiry}"

Please:
1. Look up their customer information
2. Address their inquiry appropriately
3. Create a ticket if needed
4. Escalate if required by escalation rules

Provide your response to the customer."""

    response_text = []

    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        response_text.append(block.text)
                        print(f"\n{block.text}")

    return "\n".join(response_text)

# Usage
if __name__ == "__main__":
    async def main():
        # Test case 1: Regular inquiry
        print("=== Test Case 1: Regular Inquiry ===")
        await customer_support_agent(
            customer_id="C002",
            inquiry="How do I reset my password?"
        )

        print("\n\n=== Test Case 2: Refund Request (Auto-escalation) ===")
        await customer_support_agent(
            customer_id="C001",
            inquiry="I want a refund for my recent purchase. It doesn't work as advertised."
        )

    anyio.run(main)
```

### Example 4: Research agent with multi-turn exploration

This agent conducts deep research across sources:

```
import anyio
from claude_agent_sdk import (
    ClaudeSDKClient, ClaudeAgentOptions,
    AssistantMessage, TextBlock, ToolUseBlock
)
from pathlib import Path

async def research_agent(
    research_topic: str,
    output_file: str,
    max_depth: int = 3
):
    """
    Research agent that explores a topic deeply and creates a comprehensive report

    Args:
        research_topic: Topic to research
        output_file: Path to save the research report
        max_depth: Maximum depth of research exploration
    """

    system_prompt = """You are a thorough research analyst. Your goal is to produce comprehensive, well-cited research reports.

Research methodology:
1. Break down the topic into key questions
2. Search for authoritative sources using WebSearch
3. Fetch and analyze relevant sources using WebFetch
4. Cross-reference information from multiple sources
5. Synthesize findings into a coherent narrative
6. Include citations with source URLs

Quality standards:
- Prioritize authoritative sources (academic, government, established media)
- Verify facts across multiple sources
- Note conflicting information or uncertainties
- Distinguish between facts and opinions
- Include publication dates when available

Report structure:
- Executive Summary
- Key Findings (with citations)
- Detailed Analysis (organized by subtopic)
- Methodology
- Sources

Write in clear, professional prose suitable for decision-makers."""

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        allowed_tools=["WebSearch", "WebFetch", "Write", "Read"],
        permission_mode="acceptEdits",
        max_turns=max_depth * 10,  # Allow deep exploration
    )

    prompt = f"""Conduct comprehensive research on: {research_topic}

Requirements:
1. Identify 3-5 key questions about this topic
2. Search for authoritative sources for each question
3. Fetch and analyze the most relevant sources
4. Synthesize findings into a well-structured report
5. Include all sources with URLs
6. Save the final report to: {output_file}

Begin your research."""

    research_progress = []

    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(block.text)
                        research_progress.append(block.text)
                    elif isinstance(block, ToolUseBlock):
                        if block.name == "WebSearch":
                            query = block.input.get("query", "")
                            print(f"? Searching: {query}")
                        elif block.name == "WebFetch":
                            url = block.input.get("url", "")
                            print(f"? Fetching: {url}")
                        elif block.name == "Write":
                            path = block.input.get("file_path", "")
                            print(f"? Writing: {path}")

    print(f"\n✅ Research complete! Report saved to {output_file}")
    return research_progress

# Usage
if __name__ == "__main__":
    async def main():
        await research_agent(
            research_topic="Current state and future of quantum computing",
            output_file="quantum_computing_research.md",
            max_depth=3
        )

    anyio.run(main)
```

### Example 5: Multi-agent orchestrator system

This demonstrates coordinating specialized subagents:

```
import anyio
from claude_agent_sdk import (
    ClaudeSDKClient, ClaudeAgentOptions,
    AssistantMessage, TextBlock
)
from pathlib import Path
from typing import List, Dict

async def run_subagent(
    name: str,
    task: str,
    allowed_tools: List[str],
    system_prompt: str,
    cwd: str = "."
) -> str:
    """Run a specialized subagent"""

    options = ClaudeAgentOptions(
        system_prompt=system_prompt,
        allowed_tools=allowed_tools,
        permission_mode="acceptEdits",
        cwd=cwd,
        max_turns=15
    )

    result = []
    async with ClaudeSDKClient(options=options) as client:
        await client.query(task)

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        result.append(block.text)

    return "\n".join(result)

async def software_development_orchestrator(
    feature_request: str,
    project_dir: str
):
    """
    Orchestrates multiple specialized agents for software development

    Workflow: Analyst → Architect → Implementer → Tester → Documenter
    """

    print("? Starting multi-agent software development workflow...\n")

    # Phase 1: Requirements Analysis
    print("? Phase 1: Requirements Analysis")
    analyst_prompt = """You are a business analyst specializing in software requirements.

Your task:
1. Analyze the feature request
2. Identify functional requirements
3. Identify non-functional requirements
4. Define acceptance criteria
5. Note potential edge cases

Output a structured requirements document."""

    requirements = await run_subagent(
        name="analyst",
        task=f"Analyze this feature request and create detailed requirements:\n\n{feature_request}",
        allowed_tools=["Read", "Write"],
        system_prompt=analyst_prompt,
        cwd=project_dir
    )

    print(f"✅ Requirements defined\n")

    # Phase 2: Architecture Design
    print("?️ Phase 2: Architecture Design")
    architect_prompt = """You are a software architect specializing in system design.

Your task:
1. Review the requirements
2. Design the architecture (components, interfaces, data flow)
3. Select appropriate design patterns
4. Consider scalability and maintainability
5. Document technical decisions

Output an architecture design document."""

    architecture = await run_subagent(
        name="architect",
        task=f"""Based on these requirements, design the architecture:

{requirements}

Create an architecture design document with:
- Component diagram (ASCII or description)
- Key interfaces
- Data flow
- Technology choices""",
        allowed_tools=["Read", "Write"],
        system_prompt=architect_prompt,
        cwd=project_dir
    )

    print(f"✅ Architecture designed\n")

    # Phase 3: Implementation
    print("? Phase 3: Implementation")
    implementer_prompt = """You are an expert software engineer.

Your task:
1. Review requirements and architecture
2. Implement the feature following best practices
3. Write clean, maintainable code
4. Include error handling
5. Follow project conventions (check CLAUDE.md)

Write production-quality code."""

    implementation = await run_subagent(
        name="implementer",
        task=f"""Implement the feature based on:

REQUIREMENTS:
{requirements}

ARCHITECTURE:
{architecture}

Write the necessary code files.""",
        allowed_tools=["Read", "Write", "Bash", "Grep"],
        system_prompt=implementer_prompt,
        cwd=project_dir
    )

    print(f"✅ Feature implemented\n")

    # Phase 4: Testing
    print("? Phase 4: Testing")
    tester_prompt = """You are a software testing specialist.

Your task:
1. Review the implementation
2. Write comprehensive unit tests
3. Write integration tests if needed
4. Verify all acceptance criteria are covered
5. Run tests and report results

Ensure high test coverage and quality."""

    tests = await run_subagent(
        name="tester",
        task=f"""Create comprehensive tests for the implementation.

REQUIREMENTS:
{requirements}

Run the tests and report results.""",
        allowed_tools=["Read", "Write", "Bash"],
        system_prompt=tester_prompt,
        cwd=project_dir
    )

    print(f"✅ Tests created and run\n")

    # Phase 5: Documentation
    print("? Phase 5: Documentation")
    documenter_prompt = """You are a technical documentation specialist.

Your task:
1. Review all artifacts (requirements, architecture, code, tests)
2. Update README with feature documentation
3. Add inline code documentation if needed
4. Create usage examples
5. Document any new APIs or interfaces

Write clear, user-friendly documentation."""

    documentation = await run_subagent(
        name="documenter",
        task="""Update documentation to reflect the new feature:

1. Update README.md with feature description and usage
2. Add code examples
3. Document any new APIs

Ensure documentation is complete and user-friendly.""",
        allowed_tools=["Read", "Write"],
        system_prompt=documenter_prompt,
        cwd=project_dir
    )

    print(f"✅ Documentation updated\n")

    # Final Summary
    print("=" * 60)
    print("? Multi-agent workflow complete!")
    print("=" * 60)
    print(f"""
Phases completed:
1. ✅ Requirements Analysis
2. ✅ Architecture Design
3. ✅ Implementation
4. ✅ Testing
5. ✅ Documentation

Check {project_dir} for all generated artifacts.
""")

# Usage
if __name__ == "__main__":
    async def main():
        await software_development_orchestrator(
            feature_request="""
            Add user authentication to our web application:
            - Users should be able to register with email/password
            - Users should be able to log in and log out
            - Include password reset functionality
            - Use JWT for session management
            - Follow security best practices (password hashing, etc.)
            """,
            project_dir="./my_project"
        )

    anyio.run(main)
```

## Best practices for production deployment

### Adopt the orchestrator pattern for complex workflows

Structure agents hierarchically with a **single-responsibility principle**: one orchestrator handles routing and planning while specialized subagents handle execution. This pattern, used successfully at companies like Anthropic (67% PR throughput increase) and Novo Nordisk (90% time savings), prevents context contamination and enables parallel execution.

Orchestrators should have minimal permissions (read and route only), while implementer subagents receive necessary write permissions restricted to specific directories. Security subagents operate read-only for auditing.

### Implement defense-in-depth security

Start from a **deny-all baseline** and allowlist only required commands and directories. Block dangerous patterns (`rm -rf`, `sudo`, system modifications) using PreToolUse hooks. Use short-lived tokens with automatic rotation, never placing secrets in agent-visible context.

```
async def security_hook(input_data, tool_use_id, context):
    """Multi-layer security checks"""
    tool_name = input_data["tool_name"]
    tool_input = input_data["tool_input"]

    # Block dangerous commands
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        if any(p in command for p in ["rm -rf", "sudo", "curl | sh"]):
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "Dangerous command blocked"
                }
            }

    # Restrict file operations to safe directories
    if tool_name in ["Write", "Edit"]:
        file_path = tool_input.get("file_path", "")
        safe_dirs = ["/project/src", "/project/tests"]
        if not any(file_path.startswith(d) for d in safe_dirs):
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": f"File path outside safe directories"
                }
            }

    return {}
```

### Build comprehensive observability

Implement structured logging for every tool invocation with inputs, outputs, timestamps, and session IDs. Use OpenTelemetry for distributed tracing across subagents. Track key metrics: success rate, tool usage frequency, token consumption, latency per task type, and cost per task.

```
import logging
import json
from datetime import datetime

logger = logging.getLogger(__name__)

async def observability_hook(input_data, tool_use_id, context):
    """Log all agent actions for audit trail"""
    logger.info(json.dumps({
        "event": "tool_execution",
        "tool_name": input_data["tool_name"],
        "tool_input": input_data["tool_input"],
        "tool_use_id": tool_use_id,
        "timestamp": datetime.now().isoformat(),
        "session_id": context.get("session_id"),
        "agent_id": context.get("agent_id")
    }))
    return {}
```

Set up real-time alerting on anomalies: unusual tool usage patterns, high error rates, cost spikes, or security violations. Maintain dashboards showing agent health, performance trends, and business impact metrics.

### Adopt test-first development patterns

Follow the **TestWriter → Implementer → Reviewer** workflow used successfully at Anthropic. First, a testing-focused subagent writes failing tests based on requirements. Then an implementation subagent makes tests pass without modifying the tests themselves. Finally, a review subagent enforces linting, complexity bounds, and security standards.

```
# Test-first workflow
async def test_first_workflow(feature_spec: str, project_dir: str):
    # 1. Write failing tests first
    tests = await run_subagent(
        name="test-writer",
        task=f"Write comprehensive tests for: {feature_spec}",
        allowed_tools=["Write", "Bash"],
        system_prompt="Write tests that cover all requirements. Tests should fail initially."
    )

    # 2. Verify tests fail
    test_result = subprocess.run(["pytest"], capture_output=True)
    assert test_result.returncode != 0, "Tests should fail initially"

    # 3. Implement to make tests pass
    implementation = await run_subagent(
        name="implementer",
        task=f"Implement code to make the tests pass. DO NOT modify tests.",
        allowed_tools=["Write", "Read", "Bash"],
        system_prompt="Write minimal code to make tests pass. Follow TDD principles."
    )

    # 4. Verify tests pass
    test_result = subprocess.run(["pytest"], capture_output=True)
    assert test_result.returncode == 0, "Tests should pass after implementation"
```

### Manage context effectively

The SDK automatically compacts context when approaching limits, but you can optimize further. Use **CLAUDE.md files** for persistent project conventions rather than repeating instructions. Leverage **agentic search** (grep, find) over RAG for dynamic context construction—this eliminates constant re-indexing and reduces token usage.

For long-running workflows, isolate subagent contexts so each specialist has a clean window. Store only compact global state in the orchestrator while subagents handle detailed work.

### Deploy with feature flags and gradual rollout

Test agents locally with canned prompts before production deployment. Use feature flags to enable agent features gradually, starting with 5% of traffic and monitoring for anomalies before expanding. Define clear rollback triggers: error rate thresholds, cost overruns, or security violations.

```
# Production deployment pattern
options = ClaudeAgentOptions(
    # Production security
    permission_mode="default",  # Require approval
    allowed_tools=["Read", "specific_safe_tools"],

    # Cost controls
    max_turns=10,  # Prevent runaway execution

    # Monitoring
    hooks={
        "PreToolUse": [safety_hooks],
        "PostToolUse": [logging_hooks]
    },

    # Graceful degradation
    setting_sources=["project"],  # Load CLAUDE.md
)
```

## Business value and ROI

### Time savings drive immediate ROI

Organizations report **44-90% reductions** in task completion time across workflows. Novo Nordisk reduced documentation from 10+ weeks to 10 minutes. IG Group saves 70 hours weekly in analytics teams. Content creators cut complex projects from 23 hours to 5 hours—a 78% reduction.

At **$15M per day** in drug development costs, Novo Nordisk's time savings translate to massive financial impact. For IG Group, **full ROI was achieved within 3 months** despite the implementation effort.

### Quality improvements compound over time

Security implementations show **44% faster vulnerability intake with 25% improved accuracy**. Anthropic's internal use achieved **0% error rate** on code editing benchmarks (down from 9%). These quality improvements prevent costly errors and reduce rework cycles.

Gradient Labs maintains **98% QA pass rates** while achieving **80-90% automation** in customer support for regulated financial services—demonstrating that automation doesn't sacrifice quality when properly implemented.

### Scale without proportional headcount growth

Lindy AI achieved **10X ARR growth** with only 25 employees by leveraging agent automation. Anthropic saw **67% increase in PR throughput** despite doubling team size, indicating that agents amplify rather than replace human capabilities.

Small teams can deliver enterprise-scale capabilities: Novo Nordisk's 11-person dev team avoided scaling up while handling dramatically increased workload. This pattern enables startups to compete with enterprises on capability while maintaining lean operations.

### Cost structure favors high-value tasks

Eliminating custom framework development saves **3+ months** of engineering time versus building from scratch. No ongoing maintenance of RAG pipelines, boilerplate code, or hand-rolled agent loops. API pricing at **$3/$15 per million tokens** makes agents cost-effective for tasks that previously required human hours.

Customer support implementations like Gradient Labs achieve **75% cost reduction** while maintaining or improving quality. The key is deploying agents for high-volume, well-defined tasks while keeping humans in the loop for complex judgment calls.

### Adoption indicates market validation

Claude Code (powered by the SDK) reached **$500M+ annual run-rate revenue** within months of launch, with **10x usage growth** in three months. **115,000+ developers** actively use the platform, processing **195 million lines of code weekly**. This adoption across individual developers and enterprises validates the value proposition.

Enterprise customers include Figma, Rakuten, Intercom, Notion, Palo Alto Networks (2,500+ developers), and integrated development tools like JetBrains IDEs and GitHub Copilot.

## Key resources and next steps

### Start with official documentation

The **official Python SDK** (github.com/anthropics/claude-agent-sdk-python) provides installation, API reference, and basic examples. The **Building Agents blog post** (anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) offers architectural thinking and design philosophy directly from the engineering team.

For hands-on learning, **kenneth-liao/claude-agent-sdk-intro** provides 7 progressive modules from basic querying to multi-agent systems. This is the recommended starting point for developers new to the SDK.

### Leverage community resources

The **wshobson/agents repository** contains 84+ production-ready specialized agents organized in 63 plugins, covering architecture, programming languages, infrastructure, security, data science, and business operations. These provide templates for common use cases.

**davila7/claude-code-templates** offers 100+ ready-to-use configurations accessible via `npx claude-code-templates@latest`. For language-specific needs, unofficial ports exist for Rust and Go alongside official Python and TypeScript SDKs.

### Follow proven implementation patterns

**For simple tasks** (one-time questions, independent operations), use the `query()` function for straightforward implementation. **For complex workflows** (multi-turn conversations, follow-up questions), use `ClaudeSDKClient` for session management and context retention.

**For production systems**, adopt the orchestrator pattern with specialized subagents. Implement security hooks before deployment. Build observability from day one. Start with manual permission mode and gradually relax controls as you validate safety.

### Evaluate build vs. buy decisions

The SDK excels for **highly specific use cases requiring customization**, **R&D and experimental projects**, and **core product feature development** in organizations with strong engineering teams. It requires Python/TypeScript proficiency and custom security implementation.

For **quick customer support automation** or **teams without specialized AI engineering**, turnkey platforms may be more appropriate despite higher per-seat costs. The SDK's flexibility comes with implementation responsibility.

### Begin with a pilot project

Select a **well-defined, high-value task** for your first implementation: code review automation, document processing pipeline, or research assistance. Start small with limited permissions and manual approval. Instrument thoroughly with logging and metrics. Iterate based on real-world feedback before scaling.

Deploy one production implementation to learn more than ten perfect prototypes. The SDK's production-ready infrastructure lets you focus on agent behavior rather than building framework plumbing—but success still requires thoughtful design, security controls, and continuous monitoring.

The path to valuable AI agents combines the SDK's technical capabilities with domain expertise, security discipline, and willingness to iterate based on real-world results.
