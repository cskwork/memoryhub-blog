---
title: "Claude Code Prompt Writing: Real-World Strategies to Triple Development Productivity"
date: 2025-11-08T19:42:47+09:00
slug: "902-Claude-Code-프롬프트-작성법-개발-생산성-3배-높이는-실전-전략"
original_url: "https://memoryhub.tistory.com/902"
tistory_id: 902
draft: false
---

```
     _____  _                 _         _____            _      
    / ____|| |               | |       / ____|          | |     
   | |     | |  __ _  _   _  __| | ___ | |      ___   __| | ___ 
   | |     | | / _` || | | |/ _` |/ _ \| |     / _ \ / _` |/ _ \
   | |____ | || (_| || |_| | (_| |  __/| |____| (_) | (_| |  __/
    \_____||_| \__,_| \__,_|\__,_|\___| \_____|\___/ \__,_|\___|

    Development automation through prompts
```

A junior developer asked me last week why Claude Code keeps not delivering the desired results. They said they asked for code but got only explanations, or requested a simple fix and the tool flipped the entire file upside down. It turned out the problem was the prompt. A good prompt turns Claude Code into a smart senior developer; a bad prompt makes it a confused intern. After reading this article, you'll learn how to dramatically shorten development time through systematic prompt writing.

Claude Code is not just a coding tool but an AI development partner that works in the terminal. With the right prompt strategy, you can automate everything from bug fixes to new feature development.

## Background

As of 2025, the AI coding tool market is rapidly changing. While GitHub Copilot and Cursor focus on code auto-completion, Claude Code manages the entire development workflow. Claude Code, launched by Anthropic in 2025, is based on Claude Sonnet 4.5 and Opus 4.1 models and handles everything from multi-file editing to Git workflows through natural language commands while understanding complex codebases.

But the more powerful the tool, the more important its usage becomes. Prompt engineering is the key technology that determines Claude Code's performance. Incorrect prompts lead to token waste and incorrect implementations, while systematic prompts can reduce development time by 30-90%.

| Term | Description |
| --- | --- |
| Claude Code | Anthropic's terminal-based AI coding tool |
| CLAUDE.md | Memory file that stores project context |
| MCP | Model Context Protocol, external tool integration protocol |
| SubAgent | Specialized AI assistant focused on specific tasks |
| Checkpoint | Undo feature that auto-saves code state |

## Core Points

> Claude Code is a development automation system controlled through prompts, and systematic prompt strategy is key to productivity.

**There are 6 core principles for writing Claude Code prompts.**

**First**, understanding before action. Allow Claude to explore the codebase sufficiently before requesting code modifications.

**Second**, clear goal setting. Specify concrete deliverables instead of vague requests.

**Third**, step-by-step approach. Divide complex tasks into exploration, planning, implementation, and validation stages.

**Fourth**, leverage CLAUDE.md. Document project rules and commands to avoid repeated explanations.

**Fifth**, question first. Guide Claude to ask clarifying questions for unclear parts.

**Sixth**, track progress. Visualize work progress with checklists.

According to Anthropic's official documentation, effective prompts optimize context collection, reduce token usage, and ensure accurate results. The Checkpoint feature added in the October 2025 update allows incorrect implementations to be easily reverted, enabling more bold prompt experiments.

## Practice

### 1. Setting up CLAUDE.md Project Memory

The heart of Claude Code is the CLAUDE.md file. Creating this file at the project root allows Claude to automatically read it at the start of each conversation to understand context.

**Content to include in CLAUDE.md:**

- Basic commands: build, test, development server startup methods
- Code style: preferred syntax, module systems, naming conventions
- Workflow: Git branching strategy, commit rules
- Cautions: files not to modify, known bugs
- Project structure: major directories and file roles

When creating for the first time, run `claude /init` in the terminal and Claude automatically generates a template. As you work, if Claude repeatedly makes mistakes, explicitly add them to CLAUDE.md.

For example, if in a React project Claude keeps trying to create SVG icons directly, add this to CLAUDE.md:

```
# Icon Usage Rules
- lucide-react library is mandatory
- Direct SVG writing is forbidden
- Import in form: import { IconName } from 'lucide-react'
```

### 2. Structuring Effective Prompts

Good prompts have clear structure. Follow the 4-stage workflow recommended by Anthropic:

Stage 1 - Exploration: "Analyze the current authentication system structure. Find and read 3-5 related files."

Stage 2 - Planning: "I want to add JWT token refresh functionality. Which files need modification and in what order should work proceed? Create a plan."

Stage 3 - Implementation: "Write the code according to the plan. Check if each step is testable as you progress."

Stage 4 - Validation: "Commit the written code and create a PR. Also update the CHANGELOG."

Using Plan Mode enables deeper planning. Enter Plan Mode by pressing `Shift+Tab` twice, or adjust analysis depth with keywords like "think hard" or "ultrathink".

### 3. Optimizing Commands and Context

Claude Code automatically collects context, but this process consumes time and tokens. Optimize through efficient prompt writing.

Clear file specification:

- Bad example: "Fix authentication-related code"
- Good example: "Modify the refreshToken function in src/auth/jwt.ts file"

Specific requirements:

- Bad example: "Improve performance"
- Good example: "Add an index to the users table query to reduce query time by 50%"

Actionable instructions:

- Bad example: "Add test cases"
- Good example: "Write 3 Jest test cases for the user registration API: normal case, duplicate email case, invalid password case"

### 4. Delegating Specialized Work with SubAgent

For complex projects, leverage SubAgent. SubAgent is an AI assistant specialized in specific tasks.

Create SubAgent with `/agents` command in terminal. For example, a code review specialist SubAgent:

```
---
name: code-reviewer
description: Reviewer analyzing code quality and maintainability
model: sonnet
tools: read, grep, diff
---

Code review priorities:
1. Logic errors and bugs
2. Security vulnerabilities
3. Performance issues
4. Maintainability
5. Coding conventions
```

SubAgent can be explicitly called in the form `@code-reviewer`, or Claude Code automatically delegates based on analyzing the prompt content. Particularly useful for complex tasks requiring parallel processing.

### 5. Automating Repetitive Tasks with Slash Commands

Save frequently used prompts as Slash Commands. Create `.claude/commands` directory at project root and define commands as Markdown files.

`.claude/commands/optimize.md`:

```
Analyze the performance of this code and suggest three concrete optimizations:
1. Database query optimization
2. Memory usage improvement
3. Algorithm complexity reduction

Include expected performance improvements for each suggestion.
```

Now just typing `/optimize` executes the saved prompt. Share team-wide commands by including them in Git.

### 6. Structured Input with XML Tags

Use XML tags when passing complex data. Claude understands XML-tagged information more accurately.

```
<requirement>
Implement a user profile page.
</requirement>

<specifications>
- Profile image upload feature
- Name, email, bio editable
- Password change form
- Recent activity display
</specifications>

<constraints>
- Authenticated users only
- Other user profiles read-only
- Image size limit 5MB
</constraints>

<tech_stack>
React 18, TypeScript, TailwindCSS, React Query
</tech_stack>
```

### 7. Improving Quality with Few-shot Prompting

Including examples significantly improves consistency and quality of results. Provide 3-5 real examples wrapped in `<example>` tags.

```
Add API endpoints following the same pattern as these examples:

<example>
POST /api/users
- Create new user
- Request: { email, password, name }
- Response: { id, email, name, createdAt }
- Validation: email format, password min 8 chars
</example>

<example>
GET /api/users/:id
- Retrieve user info
- Auth: Bearer token required
- Response: { id, email, name, createdAt }
- Error: 404 if not found
</example>

Now create the products endpoint following the same pattern.
```

## Best Practices/Pattern Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Exploration → Planning → Implementation | Reduces mistakes, enables structural approach | Overhead for simple tasks |
| CLAUDE.md centralization | No repeated explanations, maintains consistency | Requires regular updates |
| SubAgent usage | Parallel processing, specialized task quality | Initial setup cost |
| Plan Mode + ultrathink | Improved complex architecture decisions | Increased token consumption |
| XML tag structuring | Clear communication of complex requirements | Unnecessary for simple requests |
| Slash Command | Repetitive task automation, easy team sharing | Requires command management |
| Checkpoint usage | Safe experimentation, easy undo | Recommended to use alongside Git |

## Conclusion

Claude Code is a development automation system controlled through prompts. By managing project context with CLAUDE.md, following the exploration-planning-implementation-validation workflow, and systematizing complex tasks with SubAgent and Slash Commands, development productivity improves dramatically. Clear and structured prompts turn Claude into a smart senior developer, and systematic configuration enhances team efficiency.

The key in practice is starting with small projects, gradually improving CLAUDE.md, and sharing effective prompt patterns with team members.

## References

- Claude Code Official Documentation (<https://docs.claude.com/en/docs/claude-code/overview>)
- Anthropic Claude Code Best Practices (<https://www.anthropic.com/engineering/claude-code-best-practices>)
- Hyperithm Claude Code Usage Guide (<https://tech.hyperithm.com/claude_code_guides>)
- Sparta AI Blog Claude Prompt Writing (<https://b2b.spartaclub.kr/blog/claude-%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%EC%9E%91%EC%84%B1%EB%B2%95>)
- Cooking with Claude Code: The Complete Guide (<https://www.siddharthbharath.com/claude-code-the-complete-guide/>)
- ClaudLog - Claude Code Best Practices (<https://claudelog.com/>)
- Anthropic Official GitHub Repository (<https://github.com/anthropics/claude-code>)
