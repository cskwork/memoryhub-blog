---
title: "Claude Code Sandboxing Features"
date: 2025-10-21T08:55:41+09:00
slug: "863-Claude-Code-샌드박스-기능"
original_url: "https://memoryhub.tistory.com/863"
tistory_id: 863
draft: false
categories: ["Dev Library"]
tags: ["Claude"]
  hidden: false
cover:
  image: "/images/863-Claude-Code-샌드박스-기능/claude_code_sandboxing.gif"
  relative: false
  hidden: false
---

![](/images/863-Claude-Code-샌드박스-기능/claude_code_sandboxing.gif)

Claude Code's new sandboxing features, bash tools, and web-based Claude Code reduce permission prompts and enhance user safety through two critical boundaries: filesystem and network isolation.

In Claude Code, Claude writes, tests, and debugs code alongside you. It explores codebases, edits multiple files, and executes commands to validate work. Granting Claude broad access to your codebase and files can create risks, especially with prompt injection attacks.

To solve this problem, we introduced two new sandboxing-based features to Claude Code.

Both features are designed to provide developers with a safer working environment while allowing Claude to operate more autonomously and reduce permission requests. Internal testing confirmed that sandboxing reduces permission requests by 84% safely.

By defining clear boundaries where Claude can work freely, we improve both security and autonomy.

## Maintaining User Security in Claude Code

Claude Code operates with a permission-based model. By default it's read-only and asks for permission before modifications or command execution. There are exceptions: safe commands like echo or cat are automatically allowed, but most operations still require explicit approval.

Continuously clicking "approve" slows down development cycles and leads to "approval fatigue." When users stop carefully monitoring what they're approving, development actually becomes less safe.

We launched sandboxing for Claude Code to address this.

## Sandboxing: A Safer, More Autonomous Approach

Sandboxing creates pre-defined boundaries where Claude can work freely instead of requesting permission for each task. Enabling sandboxing dramatically reduces permission requests while increasing safety.

The sandboxing approach implements two boundaries based on OS-level features:

**Filesystem isolation** ensures Claude only accesses or modifies specific directories. This is particularly important for preventing compromised Claude Code from modifying critical system files during prompt injection attacks.

**Network isolation** ensures Claude only connects to approved servers. This prevents compromised Claude Code from exfiltrating sensitive information or downloading malware during prompt injection attacks.

Both filesystem and network isolation are essential for effective sandboxing. Without network isolation, a compromised agent can exfiltrate sensitive files like SSH keys. Without filesystem isolation, a compromised agent can easily escape the sandbox and access the network. Using both techniques together provides Claude Code users with a safer and faster agent experience.

## Two New Sandboxing Features for Claude Code

### Sandbox Bash Tool: Safe Bash Execution Without Permission Requests

We're launching a new sandbox runtime in beta research preview. You can precisely define which directories and network hosts the agent can access without the overhead of setting up and managing containers. You can sandbox arbitrary processes, agents, and MCP servers—and we're also providing it as an open-source research preview.

Claude Code uses this runtime to sandbox the bash tool, allowing Claude to execute commands within the limits you've set. Within the safe sandbox, Claude operates more autonomously and can execute commands safely without permission requests. If Claude tries to access something outside the sandbox, you're immediately notified and can decide whether to allow it.

We built this on OS-level primitives like Linux bubblewrap and macOS seatbelt. These restrictions are enforced at the OS level and cover not just Claude Code's direct interactions but also scripts, programs, and subprocesses created by commands. As described above:

This sandbox applies both:

**Filesystem isolation**: Allows read and write access to the current working directory, but blocks modifications outside it.

**Network isolation**: Only allows internet access through a Unix domain socket connected to a proxy server running outside the sandbox. This proxy server enforces restrictions on which domains the process can connect to and handles user verification for newly requested domains. If you need stronger security, you can customize this proxy to apply arbitrary rules to outgoing traffic.

Both components are configurable. You can easily allow or block specific file paths or domains.

![](/images/863-Claude-Code-샌드박스-기능/img.webp)

Claude Code's sandboxing architecture isolates code execution through filesystem and network controls, automatically allowing safe operations, blocking malicious ones, and requesting permissions only when necessary.

Sandboxing ensures that even if a prompt injection succeeds, it remains fully isolated and doesn't impact your overall user security. A compromised Claude Code can't steal SSH keys or send information to an attacker's server.

To use this feature, run `/sandbox` in Claude Code and check out the detailed technical documentation on the security model.

We've open-sourced this feature so other teams can build safer agents. We encourage other teams to adopt this technology to strengthen their agent security posture.

### Web-Based Claude Code: Safely Running Claude Code in the Cloud

Today we're launching web-based Claude Code. You can run Claude Code in isolated sandboxes in the cloud. Web-based Claude Code runs each session in an isolated sandbox where Claude has full access to the server safely and securely. We've designed it so sensitive credentials like git credentials or signing keys never enter the sandbox alongside Claude Code. Even if code running in the sandbox is compromised, users remain protected from additional damage.

Web-based Claude Code uses a custom proxy service to transparently handle all git interactions. Inside the sandbox, the git client authenticates to this service with carefully scoped credentials. The proxy verifies these credentials and the content of git interactions (for example, ensuring pushes only go to configured branches), then attaches the correct authentication token before sending requests to GitHub.

![](/images/863-Claude-Code-샌드박스-기능/img_1.webp)

Claude Code's Git integration routes commands through a security proxy that validates authentication tokens, branch names, and repository destinations, preventing unauthorized pushes while providing secure version control workflows.

## Getting Started

The new sandbox bash tool and web-based Claude Code provide significant improvements in both security and productivity when using Claude for engineering work.

To start using the tools:

- Run `/sandbox` in Claude and check the documentation for how to configure your sandbox.
- Go to claude.com/code to try web-based Claude Code.
- Or if you're building your own agents, check out the open-source sandboxing code and consider integrating it into your work. We're excited to see what you build.

For more details on web-based Claude Code, check out the launch blog post.

<https://www.anthropic.com/engineering/claude-code-sandboxing>

[Making Claude Code more secure and autonomous with sandboxing

Learn how Claude Code's new sandboxing feature protects developers with filesystem and network isolation, reducing permission prompts and increasing user safety.

www.anthropic.com](https://www.anthropic.com/engineering/claude-code-sandboxing)
