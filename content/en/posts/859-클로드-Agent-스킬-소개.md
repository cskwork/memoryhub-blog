---
title: "Introduction to Claude Agent Skills"
date: 2025-10-19T00:03:11+09:00
slug: "859-클로드-Agent-스킬-소개"
original_url: "https://memoryhub.tistory.com/859"
tistory_id: 859
draft: false
---

You've probably already seen Claude skills in the Claude app creating files like spreadsheets or presentations. Now you can create your own skills and use them across Claude app, Claude Code, and the API.

**How Skills Work**  
Claude scans available skills while working and finds the relevant ones. When it finds a matching skill, it loads only the minimum information and files needed, so you get access to specialized knowledge while maintaining speed.

Skill characteristics:

- **Composable**: You can layer multiple skills. Claude automatically coordinates which skills are needed.
- **Portable**: The same format works everywhere. Build once, use across Claude app, Claude Code, and the API.
- **Efficient**: Loads only what's needed when it's needed.
- **Powerful**: Can include executable code for tasks where traditional code execution is more stable than token generation.

Think of skills as customized onboarding materials that package specialized knowledge. They make Claude an expert in the areas most important to you. For technical deep dives into Agent Skills design patterns, architecture, and development best practices, see our engineering blog.

**Using Skills Across All Claude Products**

**Claude App**  
Pro, Max, Team, and Enterprise users can use skills. We provide skills for common tasks like document writing, customizable examples, and skills you create yourself.

Claude automatically runs relevant skills based on your task. No manual selection needed. You can even see Claude using skills in its reasoning process while it works.

Creating skills is simple. The "skill-creator" skill provides an interactive guide. Claude asks about your workflow, generates folder structure, handles SKILL.md file formatting, and bundles necessary resources. No need to edit files yourself.

Enable skills in settings. For Team and Enterprise users, admins need to enable skills organization-wide first.

**Claude Developer Platform (API)**  
You can now add Agent Skills to Messages API requests, and use the new `/v1/skills` endpoint to programmatically manage custom skill versions. Skills require Code Execution Tool beta, which provides the secure environment needed for skill execution.

Using Anthropic-made skills, Claude can read and generate specialized Excel spreadsheets with formulas, PowerPoint presentations, Word documents, and writable PDFs. Developers can create custom skills for their specific use cases to extend Claude's capabilities.

You can also easily create, review, and upgrade skill versions in Claude Console.

See documentation or Anthropic Academy for details.

**Claude Code**  
Add team expertise and workflows to Claude Code with skills. Install skills through plugins in the anthropics/skills marketplace. Claude automatically loads them when relevant. Share skills with your team through version management. You can also manually install by adding to `~/.claude/skills`. Claude Agent SDK also supports the same Agent Skills for building custom agents.

**Getting Started**

- Claude app: User guide & help center
- API developers: Documentation
- Claude Code: Documentation
- Customizable example skills: GitHub repository

**What's Next**  
We're working to simplify the skill creation workflow and improve organization-wide deployment capabilities, making it easier for organizations to deploy skills across their teams.

Note that this feature grants Claude code execution permissions. Powerful, yes—but means you should carefully choose which skills to use. For data safety, only use skills from trusted sources.

<https://www.anthropic.com/news/skills>
