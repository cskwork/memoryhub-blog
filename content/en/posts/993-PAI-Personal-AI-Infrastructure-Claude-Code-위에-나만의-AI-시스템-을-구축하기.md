---
title: "🏗️ PAI (Personal AI Infrastructure): Building Your Own AI System on Claude Code"
date: 2026-01-27T07:08:51+09:00
slug: "993-PAI-Personal-AI-Infrastructure-Claude-Code-위에-나만의-AI-시스템-을-구축하기"
original_url: "https://memoryhub.tistory.com/993"
tistory_id: 993
draft: false
---

```
    ╔═══════════════════════════════════════════════╗
    ║   ┌─────────────────────────────────────┐     ║
    ║   │     PAI: Personal AI Infrastructure │     ║
    ║   │   ┌───┐  ┌───┐  ┌───┐  ┌───┐       │     ║
    ║   │   │ T │──│ E │──│ L │──│ O │──│ S │ │     ║
    ║   │   └───┘  └───┘  └───┘  └───┘  └───┘ │     ║
    ║   │         Your Goals, Your AI         │     ║
    ║   └─────────────────────────────────────┘     ║
    ╚═══════════════════════════════════════════════╝
```

While using Claude Code or Cursor, ever thought: "Why explain the same context every time?" "Why doesn't it remember my project structure?" **PAI was born specifically to solve these problems.**

Not just a prompt collection. Infrastructure where AI "remembers" your goals and preferences, work history, and improves itself.

**One-sentence summary:** PAI is a personalization layer built on top of agent AI like Claude Code, making AI your "digital assistant" through file system-based Context management and modular Skill/Hook systems.

## Background

### Claude Code Is Engine, PAI Is Everything Else

Agent AI tools like Claude Code, Cursor, Windsurf are exploding in popularity. They provide powerful capabilities: reading files, writing code, executing commands. But they have one critical limitation.

> PAI Core Philosophy: "AI is fundamentally about Context management.   
> How information and knowledge move within the system is key."

Most agent systems are **tool-centric**, treating users as secondary. Also **task-based** rather than goal-based. PAI flips this paradigm.

| Distinction | Existing Agent AI | PAI |
| --- | --- | --- |
| Center | Tools/Functions | User/Goals |
| Approach | Task execution | Goal-based reasoning |
| Memory | Dies at session end | Persists and learns |
| Personalization | None | 6-layer customization |

To use an analogy, **Claude Code is the engine, PAI is everything making that engine 'your car.'**

### What PAI Provides

PAI adds to Claude Code:

First, **persistent memory**. Your DA remembers past sessions, decisions, learnings.

Second, **custom skills**. Specialized functions for tasks you do frequently.

Third, **your context**. Never re-explain goals, contacts, preferences.

Fourth, **intelligent routing**. Say "research this" and appropriate workflow triggers automatically.

Fifth, **self-improvement**. The system corrects itself based on what it's learned.

## PAI's Core Architecture

### USER/SYSTEM Separation Structure

One of PAI's most important design principles is **separating USER and SYSTEM directories**. This preserves user settings even when PAI upgrades.

```
$PAI_DIR/  (~/.claude/)
├── USER/                    # User customization (preserved on upgrade)
│   ├── ABOUTME.md          # Who you are
│   ├── DAIDENTITY.md       # AI personality and voice
│   ├── TECHSTACKPREFERENCES.md  # Preferred tech stack
│   ├── CONTACTS.md         # People you work with
│   └── TELOS/              # Life OS (detailed below)
│
├── SYSTEM/                  # PAI infrastructure (upgrade target)
│   ├── skills/             # Feature modules
│   └── hooks/              # Event automation
│
├── MEMORY/                  # History, learning, state
│   ├── History/
│   ├── Learning/
│   └── Signals/
│
└── settings.json           # Configuration
```

This structure enables **portable identity**. Backing up ~/.claude/ lets you reproduce identical AI experience on any machine.

### TELOS: Core of Goal-Based Context

TELOS is PAI's most distinctive concept. **Defines who you are and what you pursue as structured markdown files**. At each session start, this Context loads so AI understands your goals before beginning.

```
TELOS/
├── MISSION.md      # Core life purpose
├── GOALS.md        # Specific goals
├── CHALLENGES.md   # Current obstacles
├── STRATEGIES.md   # Strategies overcoming obstacles
├── BELIEFS.md      # Beliefs about the world
├── FRAMES.md       # Mental frameworks you use
├── MODELS.md       # Understanding of how world works
├── LEARNED.md      # Hard-won lessons
├── WISDOM.md       # Collected insights
├── WRONG.md        # Things you changed mind on
├── BOOKS.md        # Books forming your thinking
└── PREDICTIONS.md  # Future predictions
```

For example, with "Complete API redesign by Q1" in GOALS.md, AI can ask "How does this legacy migration task connect to Q1 goals?" when you're spending time on unrelated work.

### Memory System: 3-Tier Architecture

PAI Memory System is designed **Hot/Warm/Cold 3-layer structure**. Every interaction captures signals, with system continuously improving based on these.

| Layer | Content | Access Frequency |
| --- | --- | --- |
| Hot | Current session, active context | Real-time |
| Warm | Recent history, frequent patterns | Session start |
| Cold | Archived past data | Search as needed |

```
MEMORY/
├── History/        # Session logs, decision records
├── Learning/       # Success/failure pattern analysis
│   ├── Phase1/     # Initial learning
│   ├── Phase2/     # Pattern reinforcement
│   └── Phase3/     # Self-improvement application
└── Signals/        # Ratings, sentiment, validation results
```

**Continuous learning's core** is Signals directory. Capturing both explicit feedback (thumbs up/down) and implicit (whether modified, re-requested), DA becomes increasingly user-tailored.

### Skill System: Deterministic Priority Layers

PAI Skill System follows **"CODE -> CLI -> PROMPT -> SKILL"** layers. This principle prioritizes consistent results.

> "If solvable with bash script, don't use AI. If solvable with SQL query, don't use AI. Use AI only where intelligence is actually needed."

This principle saves costs and increases reliability.

```
skills/
├── CORE/               # Core routing and identity
├── pai-research-skill/ # Multi-source research
├── pai-browser-skill/  # Playwright browser automation
├── pai-telos-skill/    # Life OS and goal tracking
└── ...
```

Each skill is **self-contained**. Includes code, workflows, setup instructions, validation tests so AI can directly read and install.

### Hook System: 8 Event Types

Hook System **reacts to lifecycle events**. Supports 8 event types including session start, tool use, task completion.

| Event | Description | Usage Example |
| --- | --- | --- |
| session_start | Session start | Auto-load context |
| tool_use | Tool invocation | Security validation |
| task_complete | Task completion | Voice notification, session capture |
| pre_command | Before command execution | AllowList validation |

```
// Example: Load TELOS context at session start
hooks.on('session_start', async () => {
  await loadContext('USER/TELOS/');
  await loadContext('USER/ABOUTME.md');
});

// Example: Block dangerous commands
hooks.on('pre_command', async (cmd) => {
  if (!isAllowed(cmd)) {
    throw new SecurityError('Command not in AllowList');
  }
});
```

Through Hooks, smooth workflow is possible without `--dangerously-skip-permissions`. PAI's security hooks validate commands before execution, blocking dangerous work while smoothing normal workflow.

## Practice: PAI Installation and Basic Setup

### Step 1: Install Full Release (Recommended)

Get fastest-working PAI system this way.

```
# Clone repository
git clone https://github.com/danielmiessler/PAI.git
cd PAI/Releases/v2.4

# Backup existing Claude Code config if present
[ -d ~/.claude ] && mv ~/.claude ~/.claude-backup-$(date +%Y%m%d)

# Copy PAI installation
cp -r .claude ~/

# Run setup wizard
cd ~/.claude && bun run PAIInstallWizard.ts
```

The wizard asks your name, DA name (e.g., Kai), timezone, environment variable setup (bash/zsh auto-detected), voice preference (optional).

After installation, **restart Claude Code** to activate Hooks.

### Step 2: Configure TELOS

Edit files in ~/.claude/USER/TELOS/ directory. Recommended to complete at least these three:

```
<!-- MISSION.md example -->
# Core Mission
- Innovate developer experience (DX) tools
- Share technical knowledge accessibly

<!-- GOALS.md example -->
# 2026 Q1 Goals
- [ ] Open-source project v2.0 release
- [ ] Technical blog monthly 4 posts
- [ ] Improve English technical writing ability

<!-- CHALLENGES.md example -->
# Current Obstacles
- Time management: sleep shortage from night coding
- Technical: need large refactoring but test coverage insufficient
```

### Step 3: Selectively Install Individual Packs

Install only needed features. Ask Claude Code:

```
Install this Pack. Set PAI_DIR="~/.claude" and 
configure hooks, save code, verify operation.
```

Recommended Skill Pack list: pai-research-skill (multi-source research) for research, pai-browser-skill (Playwright automation) for development, pai-telos-skill (goal tracking) for productivity.

## 6-Layer Customization

PAI is customizable across 6 layers. Start with defaults and modify incrementally as needed.

| Layer | File Location | Purpose |
| --- | --- | --- |
| Identity | USER/DAIDENTITY.md | AI name, personality, voice |
| Preferences | USER/TECHSTACKPREFERENCES.md | Tech stack, tools |
| Workflows | skills/\*/workflow.md | Skill execution method |
| Skills | skills/ | Feature definition |
| Hooks | hooks/ | Event handling method |
| Memory | MEMORY/ | Capture targets |

## Conclusion

- PAI is open-source infrastructure transforming agent AI like Claude Code into 'your personal digital assistant.'
- Core is file system-based Context management (TELOS), 3-layer Memory System, deterministic Skill layers.
- Modular design lets you install only needed features, and USER/SYSTEM separation preserves settings through upgrades.

**Practical tip:** Write just ~/.claude/USER/TELOS/GOALS.md file today. That alone makes AI start understanding your context.

## References

- PAI GitHub Repository (https://github.com/danielmiessler/Personal_AI_Infrastructure)
- Building a Personal AI Infrastructure - Daniel Miessler Blog (https://danielmiessler.com/blog/personal-ai-infrastructure)
- A Personal AI Maturity Model - Daniel Miessler Blog (https://danielmiessler.com/blog/personal-ai-maturity-model)
