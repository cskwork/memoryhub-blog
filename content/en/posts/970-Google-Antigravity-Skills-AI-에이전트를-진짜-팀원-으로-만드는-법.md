---
title: "Google Antigravity Skills: How to Make AI Agents Your Real Teammates"
date: 2026-01-15T10:53:31+09:00
slug: "970-Google-Antigravity-Skills-AI-에이전트를-진짜-팀원-으로-만드는-법"
original_url: "https://memoryhub.tistory.com/970"
tistory_id: 970
draft: false
---

```
  ╔════════════════════════════════════════════════════════════════╗
  ║                                                                ║
  ║     ┌──────────────────────────────────────────────────────┐   ║
  ║     │                    SKILL.md                          │   ║
  ║     │  ┌────────────────────────────────────────────────┐  │   ║
  ║     │  │  ---                                           │  │   ║
  ║     │  │  name: deploy-staging                          │  │   ║
  ║     │  │  description: Deploy to staging server...      │  │   ║
  ║     │  │  ---                                           │  │   ║
  ║     │  │                                                │  │   ║
  ║     │  │  # Instructions                                │  │   ║
  ║     │  │  1. Run tests                                  │  │   ║
  ║     │  │  2. Execute deploy script                      │  │   ║
  ║     │  │  3. Verify health check                        │  │   ║
  ║     │  └────────────────────────────────────────────────┘  │   ║
  ║     └──────────────────────────────────────────────────────┘   ║
  ║                            │                                   ║
  ║                            ▼                                   ║
  ║     ┌──────────────────────────────────────────────────────┐   ║
  ║     │              ANTIGRAVITY AGENT                       │   ║
  ║     │     ┌─────────┐  ┌─────────┐  ┌─────────┐            │   ║
  ║     │     │ Discover│→ │ Evaluate│→ │ Execute │            │   ║
  ║     │     │  Skills │  │Relevance│  │  Steps  │            │   ║
  ║     │     └─────────┘  └─────────┘  └─────────┘            │   ║
  ║     └──────────────────────────────────────────────────────┘   ║
  ║                                                                ║
  ║            GOOGLE  ANTIGRAVITY  AGENT  SKILLS                  ║
  ╚════════════════════════════════════════════════════════════════╝
```

If you keep repeating phrases like "always run tests first, check it on staging, then..." to your AI coding assistant, you can stop now. Google Antigravity's Agent Skills, officially announced on January 14, 2025, directly solves this problem.

**It's a system where a workflow defined once is automatically recognized by the AI and applied contextually.**

What's even more amazing is that these Skills are an open standard—they work identically across Claude Code, Gemini CLI, OpenCode, and other platforms.

**One-line summary:** Agent Skills are a standardized way to teach AI agents your team's work rules and procedures through a single SKILL.md file.

## Background

The biggest limitation of AI coding assistants was "memory." No matter how powerful the model, starting a new conversation makes it forget all the team conventions, deployment procedures, and code review standards explained before. Developers had to either repeat the same instructions or copy-paste long system prompts every time.

> Agent Skill is an "on-demand specialized knowledge package" that AI agents load only when needed.

This is the crucial difference from traditional system prompts. System prompts are always loaded in context, consuming tokens, but Skills are loaded in full only when the agent determines the current task is relevant. Thanks to this "progressive disclosure" design, you can register dozens of Skills without performance degradation.

Skills originated with Anthropic. After Claude Code introduced this format and it became an open standard (agentskills.io), Google Antigravity, OpenCode, and Gemini CLI adopted the same specification. This ensures interoperability—a Skill created once can be reused across multiple platforms.

## Understanding Skill Structure

A Skill is essentially a **folder-based package**. It consists of the required SKILL.md file and optional resources (scripts, templates, reference documents).

```
my-skill/
├── SKILL.md           # Required: definition file
├── scripts/           # Optional: execution scripts
│   ├── deploy.sh
│   └── validate.py
├── templates/         # Optional: code templates
└── references/        # Optional: reference documents
```

The SKILL.md file has two parts: a YAML frontmatter (metadata) and markdown body (detailed instructions).

```
---
name: deploy-staging
description: Deploys the current branch to staging environment. 
  Use when user asks to "deploy", "push to staging", or "test on staging server".
---

# Deploy to Staging

## Prerequisites
1. Ensure `git status` is clean
2. Run `npm run test` to verify no regressions

## Deployment Steps
1. Run `./scripts/deploy.sh staging`
2. Wait for health check to return 200 OK
3. Notify user with staging URL
```

Here, **the description field is most important**. When a conversation starts, the agent only reads the name and description of all Skills. When it determines the current task is relevant to a specific Skill, it loads the full SKILL.md. Therefore, the description must be easy for AI to understand and include clear trigger keywords.

| Description Quality | Example |
| --- | --- |
| Good | "Generates REST API endpoint handlers in FastAPI following internal security and logging conventions. Use when creating new API endpoints." |
| Poor | "Help create APIs" |

## Skill Storage Locations

Antigravity supports Skills at two scopes.

| Location | Scope | Purpose |
| --- | --- | --- |
| `<project>/.agent/skills/` | Workspace | Project-specific workflows, team sharing (Git-committed) |
| `~/.gemini/antigravity/skills/` | Global | Personal utilities, used across all projects |

In practice, test new Skills first at the project level (.agent/skills/). Once validated as useful across multiple projects, move to global or create a symbolic link. This prevents polluting other projects during experimentation.

## Hands-On: Creating Your First Skill

Let's create a Skill to solve one of the most common problems: inconsistent commit messages.

### Step 1: Create Folder Structure

```
mkdir -p .agent/skills/git-commit-formatter
touch .agent/skills/git-commit-formatter/SKILL.md
```

### Step 2: Write SKILL.md

```
---
name: git-commit-formatter
description: Formats git commit messages according to Conventional Commits 
  specification. Use when user asks to commit changes or write a commit message.
---

# Git Commit Formatter

When writing a git commit message, follow the Conventional Commits specification.

## Format
```

```
## Allowed Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only
- **style**: Formatting, no code change
- **refactor**: Code restructuring
- **test**: Adding tests
- **chore**: Maintenance tasks

## Rules
1. Type is mandatory and lowercase
2. Scope is optional, in parentheses
3. Description starts lowercase, no period at end
4. Description must be under 72 characters
5. Body explains "what" and "why", not "how"

## Examples
- `feat(auth): add OAuth2 login support`
- `fix: resolve null pointer in user service`
- `docs(readme): update installation instructions`

## Decision Tree
- If adding new functionality → use `feat`
- If fixing a bug → use `fix`
- If changing documentation only → use `docs`
- If changing code style without logic change → use `style`
```

### Step 3: Test

Start a new conversation in Antigravity and request "write a commit message." Verify the agent automatically follows Conventional Commits format. You can also force-call by saying "use the git-commit-formatter Skill to commit."

## Hands-On: Skill with Scripts

Beyond simple instructions, create a Skill that executes actual scripts. Staging deployment automation is a good example.

### Folder Structure

```
.agent/skills/deploy-staging/
├── SKILL.md
└── scripts/
    └── deploy.sh
```

### SKILL.md

```
---
name: deploy-staging
description: Deploys current branch to staging environment. Use when 
  user asks to "deploy to staging", "push to staging", or "test on staging".
---

# Deploy to Staging

## Prerequisites
1. Verify `git status` is clean (no uncommitted changes)
2. Run `npm run test` and ensure all tests pass

## Deployment Process
Execute the deployment script:
```bash
./scripts/deploy.sh staging

Post-Deployment Verification
Wait for health check endpoint to return HTTP 200
Verify staging URL is accessible
Report staging URL to user
Rollback
If deployment fails:
```

```
./scripts/deploy.sh rollback
```

```
### scripts/deploy.sh

```bash
#!/bin/bash
ENV=$1

if [ "$ENV" = "staging" ]; then
    echo "Deploying to staging..."
    # Actual deployment logic
    kubectl apply -f k8s/staging/
    echo "Deployment complete. URL: https://staging.example.com"
elif [ "$ENV" = "rollback" ]; then
    echo "Rolling back..."
    kubectl rollout undo deployment/app -n staging
fi
```

Write scripts atomically. Each script should perform one task so the agent can call it unambiguously.

## Best Practices and Pattern Comparison

| Pattern | Advantage | Caution |
| --- | --- | --- |
| Single responsibility | Agents easily judge when to use | Avoid "do everything" mega-Skills |
| Trigger keywords in description | Improves auto-activation accuracy | Write from AI perspective (3rd person, clear verbs) |
| Project Skills first | Shareable with team via Git | Promote to global after validation |
| Script separation | Deterministic execution, token-efficient | Document script arguments/flags clearly |
| Include Decision Tree | Clarifies conditional logic | Make "If...then...else" structure explicit |

## Differences from Rules and Workflows

Antigravity has Skills, Rules, and Workflows. They're easy to confuse, so let's clarify.

| Type | Load Timing | Purpose | Storage |
| --- | --- | --- | --- |
| Rules | Always (like system prompt) | Enforce code style, required conventions | `.agent/rules/`, `~/.gemini/GEMINI.md` |
| Workflows | User calls via `/command` | Saved prompt sequences | `.agent/workflows/` |
| Skills | When agent judges relevance | Reusable specialized knowledge | `.agent/skills/`, `~/.gemini/antigravity/skills/` |

Rules suit requirements that must apply without exception, like "always use TypeScript" or "docstrings required."

Workflows are useful for multi-step tasks like "new feature development" that you run once with `/new-feature`. Skills are "on-demand expertise" that agents apply by their own judgment.

## Conclusion

- Agent Skills are an open standard solving the problem of repetitive AI instructions—program agent behavior with a single SKILL.md file
- Workspace Skills (.agent/skills/) are shared team-wide via Git, while Global Skills apply your personal workflows to all projects
- Practical tip: Create one SKILL.md for your most frequent instructions today and test whether the agent automatically recognizes it

## References

- Google Antigravity Skills Documentation (<https://antigravity.google/docs/skills>)
- Agent Skills Open Standard (<https://agentskills.io/home>)
- Anthropic Skills Repository (<https://github.com/anthropics/skills>)
- How to Build Custom Skills in Google Antigravity - Google Cloud Community (<https://medium.com/google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d>)
- Easily Extend Your AI with Google Antigravity Agent Skills (<https://www.xugj520.cn/en/archives/google-antigravity-agent-skills-guide-2.html>)
