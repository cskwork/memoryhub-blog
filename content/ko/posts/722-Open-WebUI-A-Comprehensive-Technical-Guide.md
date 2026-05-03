---
title: "Open WebUI: A Comprehensive Technical Guide"
date: 2025-07-08T23:42:37+09:00
slug: "722-Open-WebUI-A-Comprehensive-Technical-Guide"
original_url: "https://memoryhub.tistory.com/722"
tistory_id: 722
draft: false
---

**TL;DR** — Install Open WebUI locally (pip or Docker), connect any LLM (Ollama, OpenAI, Claude, etc.), then super-charge the platform with **Tools** (skills for the model), **Functions** (features for the UI), and **MCP** (Anthropic-style tool servers). This post walks you through every step and includes ready-to-run code snippets.

---

## **Table of Contents**

1. [Why Open WebUI?](#why-openwebui)
2. [Installing Open WebUI](#installing-openwebui)
3. [First-Run Tour](#first-run-tour)
4. [Adding & Switching Models](#adding--switching-models)
5. [Extensibility Primer: Tools vs. Functions vs. MCP](#extensibility-primer)
6. [Deep-Dive 1 — Tools](#deep-dive-1--tools)
7. [Deep-Dive 2 — Functions](#deep-dive-2--functions)
8. [Deep-Dive 3 — MCP Integration](#deep-dive-3--mcp-integration)
9. [Choosing the Right Extension](#choosing-the-right-extension)
10. [Best Practices & Security](#best-practices--security)
11. [Next Steps](#next-steps)
12. [Glossary (kid-friendly)](#glossary)

## **1. Why Open WebUI?**

- **Self-hosted & offline-capable:** keep data on-prem or on your laptop.
- **Model-agnostic:** local GPU (Ollama) or remote APIs (OpenAI, Azure, Claude, together.ai).
- **Modern UX:** chat UI with markdown/LaTeX, code highlighting, mobile-responsive.
- **Plugin architecture:** extend with Python scripts (Tools/Functions) or external services (MCP).

---

## **2. Installing Open WebUI**

**Scenario****Command****Notes**

|  |  |  |
| --- | --- | --- |
| **Python (pip)** | bash<br>pip install open-webui<br>open-webui serve<br> | Requires Python 3.11+; runs on <http://localhost:8080>. |
| **Docker (all-in-one)** | bash<br>docker pull ghcr.io/open-webui/open-webui:main<br>docker run -d -p 8080:8080 ghcr.io/open-webui/open-webui:main<br> | Zero host-side dependencies; great for NAS/home-lab. |
| **Kubernetes** | Helm chart available in community repo. | For multi-user clusters; bring your own ingress & PVC. |

> **Troubleshooting tip:** if the UI appears blank after first run, confirm that the OPENWEBUI\_DATABASE\_URL env var points to a writable location.

---

## **3. First-Run Tour**

1. **Login** (default admin account is printed to the console on first start).
2. **Workspace → Models:** lists every model Open WebUI knows about.
3. **Start Chat:** select a model, type a prompt, enjoy markdown answers with code blocks rendered.
4. **Side Drawer:** switch between conversations, view token usage, or enable “Multiple-Models” mode to compare answers live.

---

## **4. Adding & Switching Models**

### **4-A Local (Ollama)**

1. Install Ollama & run ollama pull llama3.
2. In Open WebUI **Models → + Add Model**, choose **Ollama** and enter llama3.
3. One-click **Update All** keeps every Ollama model up-to-date.

### **4-B Remote (OpenAI/Claude/Azure)**

1. Save your API key under **Settings → Credentials**.
2. Press **+ Add Model**, choose provider, fill model ID (gpt-4o-mini, claude-3-haiku-2024-05-16, etc.).
3. The new model now appears in the chat model picker.

> **Multi-Model Chats:** open **New Chat → Enable Multiple Models** to ask the same question to several models at once—great for benchmarking.

---

## **5. Extensibility Primer**

**Extension Type****Scope****Trigger****Typical Use-Case**

|  |  |  |  |
| --- | --- | --- | --- |
| **Tool** | Adds *skills* to the LLM | LLM decides | Weather, stock quotes, calculator |
| **Function** | Adds *features* to WebUI | System / user click | New model backend, UI button, global filter |
| **MCP Tool** | External tool server bridged by **mcpo** | LLM decides | Local file access, hardware sensors |

### **Three Ways to “Solve the Same Problem” (pick one)**

- **Quick & simple:** write a *Tool* (Python) directly in Workspace.
- **Platform-wide:** write a *Function* if you need UI buttons or global filters.
- **High isolation/Anthropic ecosystem:** wrap an existing MCP tool with **mcpo** and plug it in.

---

## **6. Deep-Dive 1 — Tools**

### **6-A How They Work**

1. You enable a Tool for the chat.
2. Open WebUI describes the Tool’s functions to the LLM.
3. The model decides to call tool\_fn(args) (function-calling).
4. Open WebUI runs the Python code, returns JSON.
5. Model incorporates the fresh info into its answer.

### **6-B Authoring a Custom Tool (complete, testable)**

```
# time_tool.py
"""
GetTime Tool
-------------
Provides the current local time. 
"""

from datetime import datetime
from openwebui.tools import tool  # core base class

class GetTime(tool.Tool):
    name = "get_time"
    description = "현재 시간을 ISO-8601 형식으로 반환합니다."  # 한국어 설명

    def run(self) -> str:
        """? LLM이 호출하면 이 함수가 실행됩니다."""
        now = datetime.now().isoformat()
        return now
```

**설치 방법**

```
Workspace → Tools → + Add → Paste code → Save
New Chat → ➕ icon → enable **get_time**
```

Ask “What time is it?” and GPT-4o will invoke get\_time() automatically.

---

## **7. Deep-Dive 2 — Functions**

Open WebUI defines **Pipe**, **Filter**, and **Action** functions. 

### **7-A Sample Action Function: One-Click Summarizer**

```
# summarize_action.py
"""
Adds a 'Summarize' button under every user message.
"""

from openwebui.functions import action
from openwebui.sdk import chat

class Summarize(action.Action):
    button_label = "? Summarize"

    async def run(self, message_id: str):
        # ? 한국어 주석: 메시지 내용을 읽어 요약 프롬프트를 생성
        original = await chat.get_message(message_id)
        prompt = f"Summarize the following:\n\n{original.content}"
        summary = await chat.ask_llm(prompt, model="gpt-4o-mini")
        await chat.post_message(summary)
```

*Import in* ***Admin Panel → Functions****, enable, then attach it to the model.*

### **7-B Filter & Pipe Quick Examples**

- **Filter** — prepend a hidden system prompt (“You are a pirate…”).
- **Pipe** — send a query to two models and merge answers (llama3 + gpt-4o for hybrid RAG).

---

## **8. Deep-Dive 3 — MCP Integration**

### **8-A What Is MCP?**

A CLI-level protocol (STDIN/STDOUT) that lets LLMs call local tools securely—think “USB-C for AI.”

### **8-B Open WebUI + mcpo**

```
# 1️⃣ Run an MCP server (example: time)
mcp-server-time &

# 2️⃣ Wrap it with mcpo
mcpo --port 8000 -- mcp-server-time
```

Open <http://localhost:8000/docs> to verify the auto-generated OpenAPI spec.

Add http://localhost:8000/time under **Settings → Tools → + Add Tool Server**. 

The LLM now sees get\_time() exactly like the earlier Python Tool, but it executes in a separate process—ideal for sandboxing or cross-language tooling. Medium has a full walk-through if you want to build your own MCP servers. 

---

## **9. Choosing the Right Extension**

**Need****Best Choice****Why**

|  |  |  |
| --- | --- | --- |
| **Fresh data inside answers** | *Tool* | Model calls it when needed. |
| **New backend or UI button** | *Function* | Runs inside WebUI; no model context needed. |
| **Reuse Anthropic tool or isolate code** | *MCP (+ mcpo)* | Language-agnostic, sandboxed process. |

---

## **10. Best Practices & Security**

1. **Install gradually** — enable one new Tool/Function at a time and test with simple prompts.
2. **Check model compatibility** — make sure your LLM supports function calling before expecting Tools to fire.
3. **Review code** — Tools & Functions run arbitrary Python; stick to trusted sources.
4. **Lock down ports** — if mcpo listens on 0.0.0.0, restrict with a firewall or reverse proxy.

---

## **11. Next Steps**

- ? **Try it now:** install the sample **GetTime** tool above and ask “What time is it in Seoul?”
- ? **Explore community libraries:** dozens of ready-made Tools & Functions are a click away.
- ?️ **Build your own:** write a Filter that appends usage-cost metadata to every answer, or a Pipe that fuses web search + LLM summarization.
- ? **Measure impact:** enable Multi-Model chats to benchmark latency, cost, and answer quality side-by-side.

---

## **12. Glossary**

**Term****Easy Explanation**

|  |  |
| --- | --- |
| **LLM** | A super-smart robot brain that chats with you. |
| **Tool** | A mini-app the robot can use (like a calculator). |
| **Function (Open WebUI)** | An upgrade that adds new buttons or rules to the chat website. |
| **MCP** | A special language that helps robots talk to other mini-apps safely. |
| **mcpo** | A translator that lets Open WebUI understand MCP tools. |

---

### **Past ↔ Present Contrast**

- **Past:** Chatbots were stuck with whatever knowledge they memorised during training.
- **Present:** With Tools/MCP, they fetch *live* data or run code, making answers up-to-the-minute.
- **Past:** Customising an AI interface meant forking the codebase.
- **Present:** Drop-in Functions let you add buttons, filters, or whole model backends without touching core code.

Happy hacking—may your prompts be short and your answers long!
