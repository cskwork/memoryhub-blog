---
title: "Claude Code Plugin, Standardize Your Entire Team's AI Development Environment in 5 Minutes"
date: 2025-12-08T22:15:17+09:00
slug: "924-Claude-Code-Plugin-팀-전체-AI-개발환경을-5분-만에-통일하는-법"
original_url: "https://memoryhub.tistory.com/924"
tistory_id: 924
draft: false
---

```
     ┌─────────────────────────────────────┐
     │    ┌───┐  ┌───┐  ┌───┐             │
     │    │ P │  │ L │  │ U │  MARKETPLACE │
     │    │ L │→ │ U │→ │ G │  ═══════════ │
     │    │ U │  │ G │  │ I │   /plugin    │
     │    │ G │  │ I │  │ N │   install    │
     │    └───┘  └───┘  └───┘              │
     │         CLAUDE CODE                 │
     │    ┌──────────────────────┐         │
     │    │  PLUGIN → MCP → TEAM │         │
     │    └──────────────────────┘         │
     └─────────────────────────────────────┘
```

"Claude Code settings differ from team member to team member, making collaboration confusing."
"I want to share useful slash commands I created with colleagues, but the process is cumbersome."

If you've experienced this, the Plugin Marketplace has the answer.

**The Claude Code Plugin Marketplace is a system like a smartphone app store that lets you search for, install, and deploy AI coding tool extensions across your team from one place.**

**Summary:** In short, the Plugin Marketplace is a JSON-based catalog system that standardizes and deploys Claude Code slash commands, agents, MCP servers, and hooks across teams.

## Background

On October 9, 2025, Anthropic released the Claude Code Plugin system in public beta. Previously, developers had to configure slash commands and agents manually, and sharing them with teammates meant copying configuration files individually or providing documentation. The Plugin Marketplace solves this problem fundamentally.

There are three reasons the marketplace is needed.

First, team standardization. All team members can use identical code review agents and deployment automation commands.

Second, version management. You can manage plugin updates centrally and apply them automatically.

Third, ecosystem expansion. You can immediately use 243+ plugins created by the community.

Key terminology is as follows:

| Term | Explanation |
| --- | --- |
| Plugin | A package bundling slash commands, agents, MCP servers, and hooks |
| Marketplace | A JSON file containing plugin listings and installation information |
| MCP Server | An external tool connection server based on the Model Context Protocol |
| Hooks | Automation scripts executed at specific points in Claude Code operation |

## Core Concepts

> One-line definition: A marketplace is a JSON file containing plugin names, sources, and version information, hosted in a Git repository or local path.

The Plugin Marketplace is easy to understand if you compare it to a smartphone app store. Just as an app store organizes thousands of apps by category and provides one-click installation, Claude Code's marketplace gathers plugins in one place so you can install them with a single `/plugin install` command. The difference is that anyone can create their own marketplace for internal team use.

The basic structure of a marketplace file looks like this:

```
{
  "name": "team-tools",
  "owner": {
    "name": "DevOps Team",
    "email": "devops@company.com"
  },
  "plugins": [
    {
      "name": "code-formatter",
      "source": "./plugins/formatter",
      "description": "Auto-format code on save",
      "version": "2.1.0"
    }
  ]
}
```

**Remember just three core fields.** `name` is the marketplace identifier, `owner` is admin info, and `plugins` is the list of installable plugins. Each plugin can specify a local path, GitHub repository, or any Git URL as its source.

Plugin source type configuration methods vary:

| Source Type | Configuration Example | When to Use |
| --- | --- | --- |
| Local path | `"source": "./plugins/my-plugin"` | Plugins within same repository |
| GitHub | `"source": {"source": "github", "repo": "owner/repo"}` | Public GitHub repositories |
| Git URL | `"source": {"source": "url", "url": "https://..."}` | GitLab and other Git hosting |

## Practice

### ① Add a Marketplace

There are three ways to add external marketplaces to Claude Code. To add a GitHub repository, use the `/plugin marketplace add owner/repo` format. To specify a Git URL directly, enter `/plugin marketplace add https://gitlab.com/company/plugins.git` with the full address. To test in local development, specify directory path as `/plugin marketplace add ./my-marketplace`.

Let's add one of the popular marketplaces from the community:

```
# Add Anthropic official example marketplace
/plugin marketplace add anthropics/claude-code
```

### ② Install Plugins

After adding the marketplace, you can install individual plugins. To install a specific plugin directly, use the `/plugin install plugin-name@marketplace-name` format. If you don't know which plugins are available, open an interactive browser with `/plugin` command to explore.

```
# Install code review plugin
/plugin install code-review@anthropics

# Install frontend design plugin
/plugin install frontend-design@anthropics
```

### ③ Set Up Auto-Installation for Team Projects

To force all team members to use identical plugins, specify the marketplace in the project's `.claude/settings.json` file. When team members trust the project folder, Claude Code automatically installs the specified marketplace and plugins.

```
{
  "extraKnownMarketplaces": {
    "team-tools": {
      "source": {
        "source": "github",
        "repo": "your-org/claude-plugins"
      }
    }
  },
  "enabledPlugins": ["code-formatter", "deployment-tools"]
}
```

The critical part of this configuration is the `enabledPlugins` field. Plugins listed here are automatically activated when team members open the repository.

### ④ Create Your Own Marketplace

To deploy company-exclusive plugins, you need to build your own marketplace. Create a `.claude-plugin/marketplace.json` file at the Git repository root. Write required fields—`name`, `owner`, `plugins`—and specify the source path for each plugin. Push the repository to GitHub or GitLab, and teammates can add it with the `/plugin marketplace add` command.

It's good practice to validate the marketplace before deployment:

```
# Validate JSON syntax
claude plugin validate .

# Local testing
/plugin marketplace add ./path/to/marketplace
/plugin install test-plugin@marketplace-name
```

## Best Practices/Pattern Comparison

| Pattern | Advantages | Considerations |
| --- | --- | --- |
| GitHub Hosting | Built-in version control, issue tracking, collaboration | Private repos require access permission setup |
| Local Marketplace | Quick testing before deployment | Can't share with team, development use only |
| settings.json Auto-Install | Team standardization applied automatically | Folder trust setting required, initial guidance needed |
| strict: false Setting | Works with marketplace entries without plugin.json | Unsuitable for complex plugins |

## Final Thoughts

- Plugin Marketplace is a JSON-based catalog for centrally managing Claude Code extensions and deploying them across teams
- You can add external marketplaces with `/plugin marketplace add` and configure team auto-installation with `.claude/settings.json`
- Practical tip: Run `/plugin marketplace add anthropics/claude-code` right now to install official example plugins.

## References

- Claude Code Plugin Marketplaces Official Documentation (https://code.claude.com/docs/en/plugin-marketplaces)
- Anthropic Official Plugin Announcement (https://www.anthropic.com/news/claude-code-plugins)
- Claude Code Plugins Marketplace Community (https://claudecodemarketplace.com/)
- Claude Plugins CLI (https://claude-plugins.dev/)
