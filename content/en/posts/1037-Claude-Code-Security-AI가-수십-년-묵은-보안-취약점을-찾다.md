---
title: "Claude Code Security: AI Finds Decades-Old Security Vulnerabilities"
date: 2026-02-21T09:11:23+09:00
slug: "1037-Claude-Code-Security-AI가-수십-년-묵은-보안-취약점을-찾다"
original_url: "https://memoryhub.tistory.com/1037"
tistory_id: 1037
draft: false
---

```
  ╔═══════════════════════════════════════════════════╗
  ║                                                   ║
  ║     ┌─────────┐    ┌─────────────────────┐        ║
  ║     │  { }    │───▶│  AI Security Scan   │        ║
  ║     │ Source  │    │  ┌───┐ ┌───┐ ┌───┐  │        ║
  ║     │  Code   │    │  │ ! │ │ ! │ │ ? │  │        ║
  ║     └─────────┘    │  └───┘ └───┘ └───┘  │        ║
  ║                    └──────────┬──────────┘        ║
  ║                               │                   ║
  ║                    ┌──────────▼──────────┐        ║
  ║                    │   Verified Patch    │        ║
  ║                    │   ✓ Human Review    │        ║
  ║                    └─────────────────────┘        ║
  ║                                                   ║
  ║        CLAUDE CODE SECURITY                       ║
  ║        "AI Reading Code As Security Researcher"   ║
  ║                                                   ║
  ╚═══════════════════════════════════════════════════╝
```

"Running security tools should be enough." Many development teams trust static analysis tools and feel reassured. But when Anthropic scanned open-source projects with its AI, over 500 high-risk vulnerabilities poured out of code that had passed expert review for decades.

Things existing tools missed.

**The era of rule-based pattern matching is ending, and the era of AI security that "reads and reasons about" code is beginning.**

**One-liner summary:** In short, Claude Code Security is a new type of code security tool that finds complex vulnerabilities AI reasoning would miss in existing static analysis tools and proposes patches.

---

## Background

On February 20, 2026, Anthropic released **Claude Code Security** as a limited research preview. After the announcement, CrowdStrike's stock fell 7.56% and Cloudflare fell 8.09%, sending shockwaves through the cybersecurity industry.

It wasn't just a new product launching—the market interpreted it as a signal that an AI company was seriously entering the existing security industry's domain.

Why at this point? The reality security teams face is clear. In 2024 alone, over 40,000 CVEs (publicly disclosed vulnerabilities) were reported. Vulnerabilities are increasing, but the security personnel to analyze and patch them are chronically understaffed. Existing static analysis tools work by "matching known patterns," so they catch formalized issues like exposed passwords or outdated encryption, but

they often miss context-dependent vulnerabilities like business logic flaws or authentication bypasses.

> Static Analysis is a security testing method that inspects source code itself on a rule-based basis without executing it. It can be compared to an inspector with a checklist going through items one by one.

Here emerges a critical question: "Who finds problems not on the checklist?" Until now, only experienced security researchers could do this. Claude Code Security is an attempt to fill this gap with AI.

---

## What Makes Claude Code Security Different

The greatest difference between existing security tools and Claude Code Security is **a fundamental shift in approach**. To make an analogy: if existing tools are "a safety inspector checking whether a building has fire extinguishers with a checklist," Claude Code Security is "a fire engineer who understands the building's structure and reasons about how fire would spread in case of a fire."

Specifically, there are three key differentiators.

**First**, it "reads and reasons about" code. Rather than rule matching, it understands interactions between components and traces how data flows through the application. Logan Graham, leader of Anthropic's Frontier Red Team, explained in a Fortune interview that thanks to Claude Opus 4.6's agentic capabilities, the AI can investigate security flaws and use various tools to test code. It's like a junior security researcher exploring a codebase step-by-step, but operating at much faster speed.

**Second**, it undergoes a multi-stage verification process. Claude attempts to contradict its own findings. By going through the process of proving or disproving its discoveries, it filters out false positives before reporting results to analysts. It also provides severity ratings and confidence scores.

**Third**, humans retain final decision-making authority. Claude Code Security identifies issues and proposes patches, but actual application requires developers to review and approve them in a dashboard. This goes beyond a simple safety mechanism—it's a structure where humans supplement contextual nuances difficult to judge from source code alone.

---

## How It Works in Practice

Let's examine how Claude Code Security actually works step-by-step.

**Step 1: Connect GitHub Repository**

Connect a GitHub repository in Claude Code on the Web and request a scan. It operates within Claude Code's existing interface without separate tool setup or custom scaffolding.

**Step 2: Analyze Entire Codebase**

Claude reads the entire codebase, understanding interactions between components and data flows. It focuses on high-risk vulnerabilities like memory corruption, injection flaws, authentication bypass, and complex logic errors.

**Step 3: Adversarial Self-Verification**

Claude raises counterarguments to each discovered vulnerability. It's a process where the AI questions itself: "Is this really an exploitable vulnerability?" False positives are filtered out at this stage.

**Step 4: Dashboard Reporting**

Findings that pass verification appear in a dashboard. Each item includes severity rating, confidence score, and natural language explanation.

**Step 5: Patch Suggestion and Human Approval**

Below each vulnerability, a "Suggest Fix" button allows Claude to generate patches, which developers review and approve. No automatic application occurs.

The key aspect to note throughout this process is the **permission model**. Claude Code operates in read-only mode by default, and file modifications or command execution require explicit approval.

---

## 500 Vulnerabilities: The Context

The most striking number from this announcement is "over 500." It's the number of vulnerabilities discovered by Anthropic's Frontier Red Team (about 15 researchers) using Claude Opus 4.6 on operating open-source codebases. These went undetected despite decades of expert review.

This result draws even more attention because it was achieved without special tools or custom prompting.

It means this level of vulnerability detection is possible with just the model's basic reasoning capability.

However, practical limitations exist. According to CyberScoop reporting, threat researchers indicate that AI's security capabilities have clearly improved but are most effective at finding low-impact bugs, with experienced human operators still needed for high-level threats.

Anthropic itself explicitly states on its official page: "Claude can make mistakes, so proposed patches should always be reviewed, especially for critical systems."

---

## AI Security Tool Competitive Landscape

Claude Code Security didn't appear in a vacuum. AI companies' entry into code security has already formed a competitive landscape.

| Tool | Developer | Core Approach | Current Status |
| --- | --- | --- | --- |
| Claude Code Security | Anthropic | Code reasoning + self-verification + patch suggestion | Limited research preview (2026.02) |
| Aardvark | OpenAI | Threat modeling + sandbox verification + Codex patching | Private beta (2025.10~) |
| CodeMender | Google | Gemini Deep Think-based autonomous debugging | Launched (2025.10) |
| Vuln.AI | Microsoft | AI-based vulnerability management | Launched (2025.10) |

OpenAI's Aardvark, powered by GPT-5, monitors code commits to identify vulnerabilities and even tests exploitability in isolated sandboxes. In benchmark tests, it detected 92% of known vulnerabilities and discovered 10 CVEs in open-source projects which it disclosed.

The biggest difference between Claude Code Security and Aardvark is verification method.

If Aardvark's approach is "attack simulation" that attempts actual exploitation in a sandbox, Claude Code Security takes an "adversarial self-verification" approach where the AI logically contradicts its own findings.

Which method is more effective can only be judged as real-world data accumulates.

---

## Dual-Use Dilemma: Between Defense and Attack

This technology carries an unavoidable tension. AI's ability to find vulnerabilities is useful to both defenders and attackers.

Anthropic acknowledges this problem directly, stating that its strategy is "putting this power first in the hands of defenders."

Access restrictions are also clear. It's currently available only to Enterprise and Team customers, and can only be used on code the company owns and has scanning rights for. Use on third-party or licensed code is prohibited. For open-source maintainers, free priority access is provided, but through a separate application process.

Whether this approach is sufficient will likely remain debated in the industry. What's certain is that the flow of AI involvement in code security is difficult to reverse. In Anthropic's words, "a significant portion of the world's code will be scanned by AI in the near future."

---

## Conclusion

- Claude Code Security is a new type of security tool that goes beyond rule-based pattern matching, with AI reading and reasoning about code to find context-dependent vulnerabilities.
- As Anthropic, OpenAI, Google, and Microsoft all enter the AI code security space, the landscape of the existing security industry is rapidly being reshaped.
- However, AI security tools are a supplementary tool, not a replacement. High-level threat analysis and final judgment remain human domains.
- Practical tip: If you're using an Enterprise or Team plan, apply for the research preview at claude.com/contact-sales/security, and if you're an open-source project maintainer, apply for free priority access.

---

## References

- Making frontier cybersecurity capabilities available to defenders - Anthropic Official Blog (<https://www.anthropic.com/news/claude-code-security>)
- Claude Code Security Product Page (<https://claude.com/solutions/claude-code-security>)
- AI can now hunt software bugs on its own - Fortune (<https://fortune.com/2026/02/20/exclusive-anthropic-rolls-out-ai-tool-that-can-hunt-software-bugs-on-its-own-including-the-most-dangerous-ones-humans-miss/>)
- Anthropic rolls out embedded security scanning for Claude - CyberScoop (<https://cyberscoop.com/anthropic-claude-code-security-automated-security-review/>)
- Cybersecurity stocks drop after Anthropic debuts Claude Code Security - SiliconANGLE (<https://siliconangle.com/2026/02/20/cybersecurity-stocks-drop-anthropic-debuts-claude-code-security/>)
- Introducing Aardvark: OpenAI's agentic security researcher (<https://openai.com/index/introducing-aardvark/>)
