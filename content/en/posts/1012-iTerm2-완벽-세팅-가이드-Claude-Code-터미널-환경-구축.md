---
title: "iTerm2 Complete Setup Guide: Building a Claude Code Terminal Environment"
date: 2026-02-07T13:46:00+09:00
slug: "1012-iTerm2-완벽-세팅-가이드-Claude-Code-터미널-환경-구축"
original_url: "https://memoryhub.tistory.com/1012"
tistory_id: 1012
draft: false
---

```
  ╔═══════════════════════════════════════════════════════════╗
  ║                                                           ║
  ║    ┌──────────────────────────────────────────────┐       ║
  ║    │  $ claude                                    │       ║
  ║    │  ╭──────────────────────────────────────╮    │       ║
  ║    │  │ > Plan mode (Shift+Tab)              │    │       ║
  ║    │  │ > Analyzing codebase...              │    │       ║
  ║    │  │ > 5 sessions running in parallel     │    │       ║
  ║    │  ╰──────────────────────────────────────╯    │       ║
  ║    │                                              │       ║
  ║    │  [Tab1:claude] [Tab2:claude] [Tab3:dev]      │       ║
  ║    │   ██ Backend    ██ Frontend   ██ Testing      │       ║
  ║    │                                              │       ║
  ║    │  iTerm2 + Oh My Zsh + Claude Code            │       ║
  ║    └──────────────────────────────────────────────┘       ║
  ║                                                           ║
  ║     Why the terminal is most important in AI coding era   ║
  ╚═══════════════════════════════════════════════════════════╝
```

Do you think a terminal is just a black screen where you type characters? Claude Code developer Boris Cherny opens 5 tabs in iTerm2 and runs Claude simultaneously on each. While backend code is being written in one tab, frontend code is auto-completing in another.

The starting point of this workflow isn't flashy AI, but a properly configured terminal environment.

**Terminal configuration determines 80% of AI coding tool performance.**

**TLDR:** Bottom line: configuring iTerm2 with Oh My Zsh, Powerlevel10k, essential plugins, and Claude Code-specific settings more than doubles perceived AI coding productivity.

---

## Background

macOS comes with a default Terminal app. It's sufficient for simple commands, but has clear limitations for serious AI coding tool use.

> iTerm2 is an open-source terminal emulator replacing macOS's default Terminal.app, providing essential developer features like screen splitting, hotkey windows, Shell Integration, and AI Chat.

The default terminal has three problems.

**First**, you can't receive notifications when Claude Code completes tasks. You have to switch tabs back and forth to check completion status.

**Second**, screen splitting is inconvenient or impossible. To run AI agents in parallel, you need to open multiple separate terminal windows.

**Third**, scrolling through long output or searching past commands is underdeveloped.

iTerm2 solves all these problems. The latest version 3.6, released in September 2025, even includes built-in AI Chat.

LLMs can read terminal content, explain commands, or even execute them directly.

But this article focuses on **settings that directly improve AI coding productivity**, not "flashy features."

| Comparison | Terminal.app | iTerm2 |
| --- | --- | --- |
| Screen Splitting | Not possible | Free vertical/horizontal splitting |
| System Notifications | Not supported | Task completion notifications |
| Shift+Enter | Manual setup needed | Natively supported |
| Hotkey Window | None | Instant global shortcut |
| Scrollback | Limited | Unlimited configurable |
| tmux Integration | Basic | Native window/tab conversion |
| Shell Integration | None | Command tracking, directory history |

---

## Hands-On Practice

### 1. Install iTerm2

If Homebrew is installed, one line is enough. If not, install it first.

```
# Install Homebrew (skip if already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install iTerm2
brew install --cask iterm2
```

When launching iTerm2 for the first time, you'll see a warning about "app downloaded from the internet." Click "Open" to proceed.

At this point, you won't feel much difference from the default terminal. The difference comes from configuration.

### 2. Install Oh My Zsh

Since macOS Catalina (10.15), the default shell is Zsh. Oh My Zsh is a framework for easy Zsh configuration management, offering 200+ plugins and 140+ themes.

```
# Check current shell
echo $SHELL
# Should output /bin/zsh

# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

After installation, a `.zshrc` file is created in your home directory. This file becomes the center of all shell configuration going forward.

### 3. Install Powerlevel10k Theme

Oh My Zsh's default theme (robbyrussell) is simple but information-poor. Powerlevel10k displays Git branches, execution time, error codes, and more in the prompt in real-time. When using AI coding tools, seeing the current branch and work status at a glance is important.

```
# Install Powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

After installation, change the theme in the `.zshrc` file.

```
# Edit .zshrc (use vi, nano, or VS Code)
code ~/.zshrc   # VS Code
# or
nano ~/.zshrc   # Terminal built-in editor
```

Find and modify this line:

```
# Before change
ZSH_THEME="robbyrussell"

# After change
ZSH_THEME="powerlevel10k/powerlevel10k"
```

After saving and restarting iTerm2, the Powerlevel10k setup wizard runs automatically.

When the wizard asks about installing Meslo Nerd Font, **definitely select "y"**. Without this font, icons appear as question marks.

The options in the setup wizard are purely preference. You can reconfigure anytime with the `p10k configure` command, so proceed without hesitation.

### 4. Install 3 Essential Plugins

Oh My Zsh's true value lies in plugins.

Out of hundreds, install just 3 that practically help AI coding workflow.

**zsh-autosuggestions** - Auto-completion based on history

```
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

It suggests previously typed commands in dimmed text. No need to type repeat commands like `git commit` or `docker compose up` every time. Accept with the right arrow key.

**zsh-syntax-highlighting** - Real-time syntax highlighting

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

Valid commands appear in green, invalid ones in red. Catch typos before pressing Enter, especially useful when composing complex pipeline commands.

**autojump** - Quick directory navigation

```
brew install autojump
```

Instead of `cd ~/Projects/my-app/src/components`, just type `j components`.

It learns visit frequency and jumps to your most-visited directory.

After installing all three plugins, modify the plugins section in `.zshrc`:

```
# Find and modify the plugins line in .zshrc
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  autojump
)
```

Apply changes:

```
source ~/.zshrc
```

### 5. Five Essential iTerm2 Settings

Installation alone isn't enough.

Apply 5 settings that make a real difference when using AI coding tools.

**① Unlimited Scrollback**

Claude Code often outputs large amounts of code. The default scrollback buffer loses previous output.

Path: Settings > Profiles > Terminal > Scrollback Buffer  
Check "Unlimited scrollback."

**② System Notifications**

Receive macOS notifications when Claude Code completes long tasks. Without this, you constantly switch tabs to check completion.

Path: Settings > Profiles > Terminal  
Check "Silence bell" and enable "Send escape sequence-generated alerts" in Filter Alerts.

Additionally, go to macOS System Settings > Notifications > iTerm2 to allow notifications.

**③ Option Key Setting**

Needed if you want to use `Option+Enter` for newlines in Claude Code.

Path: Settings > Profiles > Keys > General  
Change Left Option key to "Esc+".

**④ Register Hotkey Window**

Summon the terminal instantly from any app with a single hotkey. Useful when reading code and wanting to quickly ask Claude Code a question.

Path: Settings > Keys > Hotkey > "Show/hide all windows with a system-wide hotkey"  
Register your preferred hotkey. `Option+Space` is common.

**⑤ Enable Status Bar**

Display current CPU, memory usage, and battery status at the bottom of the terminal. Good for monitoring system resources when Claude Code runs heavy workloads.

Path: Settings > Profiles > Session > Check "Status bar enabled"  
In "Configure Status Bar," drag and add desired components.

### 6. Claude Code-Specific Settings

After basic iTerm2 setup, add Claude Code-optimized configuration.

**Shift+Enter Newlines**

iTerm2 natively supports Shift+Enter. Multi-line input in Claude Code works without additional setup. In other terminals like Warp or Alacritty, you need to run `/terminal-setup` in Claude Code, but

iTerm2 users don't need this step.

**Notification Hooks**

If you need more sophisticated notifications than default system alerts, use Claude Code's hook system.

For example, to show a macOS notification dialog on task completion, add this to your project's `.claude/settings.json`:

```
{
  "hooks": [
    {
      "matcher": "Notification",
      "hooks": [{
        "type": "command",
        "command": "osascript -e 'display notification \"Task complete\" with title \"Claude Code\"'"
      }]
    }
  ]
}
```

**Running Parallel Sessions**

To run multiple Claude sessions simultaneously like Claude Code developer Boris Cherny, numbering tabs in iTerm2 is effective. Adjust tab bar location in Settings > Appearance > Tab bar location, and

assign role-specific names to each tab like "Backend," "Frontend," "Test."

Change tab name: Double-click the tab or open session info with `Cmd+Shift+I` and enter the role name in Badge.

**Using CLAUDE.md**

Claude Code automatically reads the `CLAUDE.md` file at the project root to understand project context.

Recording coding rules, project structure, and common mistakes in this file noticeably improves AI code quality. Having the entire team manage one `CLAUDE.md` in git and continuously update it is best practice.

### 7. Productivity Enhancement Tools

Three CLI tools to elevate terminal experience.

```
# bat: syntax-highlighted cat replacement
brew install bat

# lsd: icon-enhanced ls replacement
brew install lsd

# fzf: fuzzy search (Ctrl+R to search command history)
brew install fzf
$(brew --prefix)/opt/fzf/install
```

bat improves readability when reviewing code output from Claude Code. fzf lets you press `Ctrl+R` to fuzzy-search past commands, particularly useful for repeatedly running complex Docker or kubectl commands.

---

## Best Practices/Pattern Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Tab-based Claude session separation | Parallel backend/frontend development | Increased system resource consumption, memory monitoring needed |
| Screen splitting (Split Panes) | See code and execution results simultaneously | Reduced readability on small screens |
| Hotkey window usage | Access terminal instantly without app switching | May conflict with other app hotkeys |
| tmux integration | Session persists across SSH disconnections, good for remote work | Learning curve exists, may be overkill for local work |
| Notification hook setup | Never miss long task completion | Excessive notifications can hurt focus |

---

## Closing Thoughts

- iTerm2 isn't just a "pretty terminal," it's infrastructure that maximizes AI coding tool performance
- With Oh My Zsh + Powerlevel10k + 3 essential plugins (autosuggestions, syntax-highlighting, autojump), achieve base productivity, and complete your AI coding workflow with Claude Code-specific notifications and parallel session settings
- Practical tip: Install iTerm2 today and follow sections 1-7 of the "Hands-On Practice" sequentially. Takes 30 minutes.

---

## References

- iTerm2 Official Site (<https://iterm2.com/>)
- iTerm2 GitHub Repository (<https://github.com/gnachman/iTerm2>)
- Oh My Zsh Official Site (<https://ohmyz.sh/>)
- Powerlevel10k GitHub (<https://github.com/romkatv/powerlevel10k>)
- Claude Code Terminal Configuration Official Documentation (<https://code.claude.com/docs/en/terminal-config>)
- Boris Cherny's Claude Code Workflow (<https://twitter-thread.com/t/2007179832300581177>)
