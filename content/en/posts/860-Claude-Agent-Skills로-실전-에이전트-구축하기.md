---
title: "Building Production Agents with Claude Agent Skills"
date: 2025-10-19T00:08:23+09:00
slug: "860-Claude-Agent-Skills로-실전-에이전트-구축하기"
original_url: "https://memoryhub.tistory.com/860"
tistory_id: 860
draft: false
  hidden: false
cover:
  image: "/images/860-Claude-Agent-Skills로-실전-에이전트-구축하기/img.webp"
  relative: false
  hidden: false
---

![](/images/860-Claude-Agent-Skills로-실전-에이전트-구축하기/img.webp)

Claude is powerful, but real work requires procedural knowledge and organizational context. Now introducing a new way to build specialized agents: Agent Skills, using files and folders.

As model performance improved, you can now build general-purpose agents that interact with complete computing environments. For example, Claude Code leverages local code execution and the file system to perform complex tasks across multiple domains. But as these agents become more powerful, we need more composable, scalable, and portable ways to provide domain-specific expertise.

This is why we created Agent Skills. Agent Skills are structured instructions, scripts, and resource folders that agents can dynamically discover and load to better perform specific tasks. Skills package your expertise into composable resources for Claude, transforming general-purpose agents into specialized agents tailored to your needs.

Creating skills for agents is like writing an onboarding guide for a new employee. Instead of building separate single-use agents for each scenario, anyone can capture procedural knowledge and share it as composable functionality. This guide explains what Skills are, how they work, and best practices for building your own.

To enable a skill, just write custom guidelines for your agent in a SKILL.md file.

**A Skill** is a directory containing a SKILL.md file—structured instructions, scripts, and resource folders that provide additional capabilities to agents.

## Skill Structure

To understand how skills actually work, let's look at a real example: one of the recently launched skills supporting Claude's document editing capabilities. Claude already knows a lot about understanding PDFs, but its ability to directly manipulate PDFs (like filling forms) is limited. With this PDF skill, you can give Claude these new capabilities.

In its simplest form, a skill is a directory containing a SKILL.md file. This file must start with YAML frontmatter containing required metadata: name and description. At startup, the agent preloads the names and descriptions of all installed skills in the system prompt.

This metadata is the first level of progressive disclosure. Claude gets enough information to know when each skill is relevant without loading all content into context. The actual body of this file is the second detail level. When Claude determines a skill is relevant to the current task, it reads the entire SKILL.md into context and loads the skill.

![](/images/860-Claude-Agent-Skills로-실전-에이전트-구축하기/img_1.webp)

*SKILL.md file structure - includes relevant metadata: name, description, and context related to the specific tasks the skill should perform*

*The SKILL.md file must start with YAML frontmatter containing the file name and description, loaded into the system prompt at startup.*

As skill complexity grows, a single SKILL.md might contain too much context, or some context might only apply to specific scenarios. In these cases, a skill can include additional files within the skill directory and reference them by name in SKILL.md. These additional connected files are the third detail level (and beyond), which Claude can explore and discover as needed.

![](/images/860-Claude-Agent-Skills로-실전-에이전트-구축하기/img_2.webp)

In the PDF skill below, SKILL.md references two additional files (reference.md and forms.md) that the skill author chose to bundle with the core SKILL.md. By moving form-filling guidelines to a separate file (forms.md), the skill author keeps the main skill concise, while Claude will read forms.md only when writing forms.

*How to bundle additional content with the SKILL.md file*

*You can include more context in a skill through additional files, which Claude will trigger based on the system prompt.*

**Progressive Disclosure** is the core design principle that makes Agent Skills flexible and scalable. Like a well-organized manual starting with a table of contents, then specific chapters, and finally detailed appendices, skills let Claude load only the information it needs.

![](/images/860-Claude-Agent-Skills로-실전-에이전트-구축하기/img_3.webp)

*Image showing progressive context disclosure in skills*

With a file system and code execution tools, agents don't need to load entire skills into context when performing specific tasks. This means the amount of context a skill can contain is practically unlimited.

## Skills and Context Window

The following diagram shows how the context window changes when a skill is triggered by a user message:

![](/images/860-Claude-Agent-Skills로-실전-에이전트-구축하기/img_4.webp)

*Image showing how skills trigger within the context window*  
*Skills are triggered through the system prompt in the context window.*

**Steps shown:**

1. Initially, the context window contains the core system prompt, metadata for each installed skill, and the user's initial message
2. Claude calls the Bash tool to read pdf/SKILL.md to trigger the PDF skill
3. Claude chooses to read the forms.md file bundled with the skill
4. Finally, Claude loads relevant guidance from the PDF skill and proceeds with the user's task

## Skills and Code Execution

Skills can also include code that Claude can execute at its discretion as a tool.

Large language models excel at many tasks, but some are better suited to traditional code execution. For example, sorting a list through token generation costs far more than simply running a sorting algorithm. Beyond efficiency, many applications require the deterministic reliability only code can provide.

In our example, the PDF skill includes a pre-written Python script that reads PDFs and extracts all form fields. Claude can run this script without loading the script or PDF into context. Because the code is deterministic, this workflow is consistent and repeatable.

![](/images/860-Claude-Agent-Skills로-실전-에이전트-구축하기/img_5.webp)

*Image showing code execution through skills*

*Skills can include code that Claude can execute as tools, depending on the nature of the task.*

## Skill Development and Evaluation

Helpful guidelines for starting skill writing and testing:

**Start with evaluation**: Run the agent on representative tasks and observe where it struggles or needs additional context, identifying specific gaps in agent capability. Then iteratively build skills to address these shortcomings.

**Structure for scale**: If your SKILL.md becomes unwieldy, split content into separate files and reference them. If specific context is mutually exclusive or rarely used together, keeping paths separate reduces token usage. Finally, code can be both an executable tool and documentation. Be clear whether Claude needs to execute a script directly or read it in context for reference.

**Think from Claude's perspective**: Monitor and observe how Claude actually uses skills in real scenarios, then iterate based on observations. Carefully watch for unexpected paths or over-reliance on specific context. Pay special attention to skill name and description—Claude uses these when deciding whether to trigger a skill in response to current tasks.

**Iterate with Claude**: As you work with Claude, ask it to capture successful approaches and common mistakes as reusable context and code within skills. When taking wrong directions while using skills, ask it to self-reflect on what went wrong. This process helps Claude discover what context it actually needs, rather than you predicting it upfront.

## Security Considerations for Skills

Skills provide Claude with new capabilities through instructions and code. As powerful as this is, malicious skills can introduce vulnerabilities to your environment or instruct Claude to leak data and perform unintended tasks.

We recommend installing skills only from trusted sources. When installing skills from less trusted sources, thoroughly review them before use. Read the contents of files included in skills to understand what they do, and especially watch out for code dependencies and bundled resources like images or scripts. Similarly, be cautious of instructions or code in skills that might direct Claude to connect to potentially untrusted external network sources.

## The Future of Skills

Agent Skills are currently supported across Claude.ai, Claude Code, Claude Agent SDK, and Claude Developer Platform.

Over the coming weeks, we'll continue adding features supporting the full skill lifecycle: creation, editing, discovery, sharing, and usage. We're especially excited about opportunities for skills to help organizations and individuals share their context and workflows with Claude. We're also exploring how skills can complement MCP (Model Context Protocol) servers in teaching agents about more complex workflows involving external tools and software.

Looking further ahead, we want to enable agents to create, edit, and evaluate their own skills, so they can systematize their behavior patterns into reusable capabilities.

Skills are a simple concept with a correspondingly simple format. This simplicity makes it easier for organizations, developers, and end users to build customized agents and provide new capabilities.

<https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>
