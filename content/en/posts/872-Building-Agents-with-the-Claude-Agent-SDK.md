---
title: "Building Agents with the Claude Agent SDK"
date: 2025-10-25T00:11:04+09:00
slug: "872-Building-Agents-with-the-Claude-Agent-SDK"
original_url: "https://memoryhub.tistory.com/872"
tistory_id: 872
draft: false
---

Claude Agent SDK - Interactive Guide

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap');
body {
font-family: 'Inter', sans-serif;
background-color: #fdfcf9;
color: #2d3748; /\* gray-800 \*/
}
.chart-container {
position: relative;
width: 100%;
max-width: 800px;
margin-left: auto;
margin-right: auto;
height: 350px;
max-height: 450px;
}
@media (min-width: 768px) {
.chart-container {
height: 400px;
}
}
pre[data-lang="python"] {
background-color: #2d3748; /\* gray-800 \*/
color: #e2e8f0; /\* gray-200 \*/
padding: 1rem;
border-radius: 0.5rem;
overflow-x: auto;
font-family: 'Courier New', Courier, monospace;
font-size: 0.875rem;
}
.tab-btn {
transition: background-color 0.2s, color 0.2s, border-color 0.2s;
}
.tab-btn.active {
background-color: #4fd1c5; /\* teal-400 \*/
color: #1a202c; /\* gray-900 \*/
border-color: #4fd1c5; /\* teal-400 \*/
}
.tab-btn.inactive {
background-color: #fdfcf9;
color: #4a5568; /\* gray-600 \*/
border-color: #cbd5e0; /\* gray-400 \*/
}
.nav-btn {
transition: color 0.2s, border-color 0.2s;
}
.nav-btn.active {
color: #4fd1c5; /\* teal-400 \*/
border-bottom: 2px solid #4fd1c5;
}
.nav-btn.inactive {
color: #4a5568; /\* gray-600 \*/
border-bottom: 2px solid transparent;
}
.code-btn.active {
background-color: #4fd1c5; /\* teal-400 \*/
color: #1a202c; /\* gray-900 \*/
}
.code-btn.inactive {
background-color: #4a5568; /\* gray-600 \*/
color: #e2e8f0; /\* gray-200 \*/
}

Claude Agent SDKOverview
Core Concepts
How to Build
Use Cases

# Building Agents with the Claude Agent SDK

This interactive guide explores the Claude Agent SDK (formerly the Claude Code SDK), a powerful framework from Anthropic for building autonomous agents. We'll analyze its core philosophy, key components, and most effective use cases based on developer documentation and reports. The goal is to understand how you can build, customize, and extend Claude's capabilities to create sophisticated agents for a variety of tasks.

## The Core Philosophy

The central idea behind the SDK is to **"Give Claude a Computer."** Instead of just responding with text, this framework allows agents to interact with a real computing environment using the same tools a human developer would:

- File System Access (Read, Write, Grep)
- Terminal & Bash Commands
- Code Execution
- Web Search & API Calls

## Key Features

The SDK provides a complete toolkit for building production-ready agents.

- **Python & TypeScript SDKs:** Integrate with your existing backend or data science stack.
- **Built-in Tooling:** Out-of-the-box access to files, code, and the web.
- **Custom Tools (MCP):** Register your own functions or APIs using the Model Context Protocol.
- **Context Management:** Automatic compaction and summarization to handle long-running tasks.

# Core Concepts

This section breaks down the fundamental building blocks of the SDK. Understanding these concepts is key to designing and controlling your agent's behavior. Click the tabs below to explore each concept.

The Agent Loop

Key Components

Tooling & Permissions

Context & Skills

## The Agent Loop

Agents operate in a continuous feedback loop, mimicking a human's workflow. This cycle allows the agent to build context, try solutions, and self-correct.

1. Gather Context

Agentic search, read files, etc.

→2. Take Action

Use a tool, write code, call API.

→3. Verify Work

Run tests, check output, lint.

→4. Repeat

Continue until task is complete.

## Key SDK Components

The SDK provides a few key classes and functions to control your agent.

- **`query()`:** A simple, async function for basic text generation or streaming. It's best for lightweight tasks and does not support tools.
- **`ClaudeAgentClient`:** The main class for building full-featured agents. It manages sessions, tool use, permissions, and long-running context.
- **`ClaudeAgentOptions`:** A configuration object passed to the client to define the agent's behavior. This is where you set the system prompt, allowed tools, permissions, and working directory. See the 'How to Build' section for a code example.

## Tooling & Permissions

This is the most powerful feature of the SDK. You have granular control over what the agent can and cannot do.

### Tool Types

- **Built-in Tools:** Ready-to-use tools like `Read`, `Write`, `Grep`, `Bash`, `WebFetch`, and `Git`.
- **Custom Tools (MCP):** Register your own Python functions or external APIs using the Model Context Protocol (MCP) to give the agent domain-specific abilities (e.g., `fetch\_user\_data`, `post\_to\_slack`).

### Permission Model

You control agent autonomy via the `permission\_mode` option:

- **`"manual"` (Default):** The agent must ask for user approval before every action.
- **`"acceptEdits"`:** The agent can automatically read files and write/edit files, but must ask for permission for other actions (like running code).
- **`"acceptAll"`:** Fully autonomous mode. The agent can use any allowed tool without asking. Use with caution.

## Context & Skills

Managing context and knowledge is critical for effective agents.

### Automatic Context Management

For long-running tasks, the agent's context window can fill up. The SDK automatically handles this by "compacting" or summarizing older parts of the conversation, keeping the agent on-track without losing critical information.

### Agent Skills

A newer feature that allows you to provide agents with specialized, reusable knowledge. A "Skill" is a directory (e.g., `.claude/skills/my\_skill`) containing a `SKILL.md` file. This file acts as an "onboarding guide" or instruction manual, giving the agent procedural knowledge for a specific domain (e.g., "how to debug our production React app").

# How to Build: A Quick-Start Guide

This is a simplified step-by-step guide to get your first agent running using Python. It covers installation, authentication, and the basic code structure.

## 1. Prerequisites & Installation

You'll need Python 3.10+ and Node.js 18+. First, install the main `claude-code` CLI, then install the Python SDK.

```
# 1. Install the Claude Code CLI (used by the SDK)
npm install -g @anthropic-ai/claude-code

# 2. Install the Python Agent SDK
pip install claude-agent-sdk
```

## 2. Authentication

Set your Anthropic API key as an environment variable.

```
export ANTHROPIC_API_KEY="your_api_key_here"
```

## 3. Write Your Agent Code

You can start with a simple query or build a full agent. Use the buttons below to toggle between a basic example and a more powerful agent configuration.

Simple Query
Basic Agent

# Top Use Cases

The SDK's ability to combine code, file systems, and web access unlocks powerful applications. The chart below shows common use cases. **Click on a bar in the chart** to see detailed examples and implementation notes for that category.

Please click on a use case in the chart above to see more details.

Interactive Guide generated from research on the Claude Agent SDK.

document.addEventListener('DOMContentLoaded', () => {
const sections = {
overview: document.getElementById('overview'),
concepts: document.getElementById('concepts'),
build: document.getElementById('build'),
'use-cases': document.getElementById('use-cases')
};
const navButtons = document.querySelectorAll('.nav-btn');
function showSection(sectionId) {
Object.values(sections).forEach(section => {
section.classList.add('hidden');
});
if (sections[sectionId]) {
sections[sectionId].classList.remove('hidden');
}
navButtons.forEach(btn => {
if (btn.dataset.section === sectionId) {
btn.classList.add('active');
btn.classList.remove('inactive');
} else {
btn.classList.add('inactive');
btn.classList.remove('active');
}
});
}
navButtons.forEach(button => {
button.addEventListener('click', (e) => {
const sectionId = e.currentTarget.dataset.section;
showSection(sectionId);
});
});
const tabButtons = document.querySelectorAll('.tab-btn');
const tabPanels = document.querySelectorAll('.tab-panel');
tabButtons.forEach(button => {
button.addEventListener('click', (e) => {
const tabId = e.currentTarget.dataset.tab;
tabPanels.forEach(panel => {
if (panel.id === tabId) {
panel.classList.remove('hidden');
} else {
panel.classList.add('hidden');
}
});
tabButtons.forEach(btn => {
if (btn.dataset.tab === tabId) {
btn.classList.add('active');
btn.classList.remove('inactive');
} else {
btn.classList.add('inactive');
btn.classList.remove('active');
}
});
});
});
const codeSnippets = {
simple: `import anyio
from claude\_agent\_sdk import query, Message, AssistantMessage, TextBlock
async def main():
messages: list[Message] = []
prompt = "Write a python function to add two numbers."
async for message in query(prompt=prompt):
messages.append(message)
if isinstance(message, AssistantMessage):
for block in message.content:
if isinstance(block, TextBlock):
print(block.text, end="", flush=True)
print()
if \_\_name\_\_ == "\_\_main\_\_":
anyio.run(main)`,
agent: `import anyio
from claude\_agent\_sdk import ClaudeAgentClient, ClaudeAgentOptions
async def main():
client = ClaudeAgentClient()
options = ClaudeAgentOptions(
system\_prompt=(
"You are a helpful assistant that can write files. "
"You are running in a project located at the current working directory."
),
# Use a safe permission mode that asks for approval
permission\_mode="manual",
# Explicitly allow only file system tools
allowed\_tools=["Read", "Write", "Grep"],
max\_turns=10
)
prompt = "Please create a new file named 'hello.txt' with the content 'Hello, Agent!'"
# query\_agent streams all messages (ToolUse, ToolResult, Assistant, etc.)
async for message in client.query\_agent(prompt=prompt, options=options):
print(message)
if \_\_name\_\_ == "\_\_main\_\_":
anyio.run(main)`
};
const codeSwitcherButtons = document.querySelectorAll('.code-btn');
const codeDisplay = document.getElementById('code-display-pre');
function setCodeDisplay(codeId) {
codeDisplay.textContent = codeSnippets[codeId];
codeDisplay.dataset.lang = 'python';
codeSwitcherButtons.forEach(btn => {
if (btn.dataset.codeId === codeId) {
btn.classList.add('active');
btn.classList.remove('inactive');
} else {
btn.classList.add('inactive');
btn.classList.remove('active');
}
});
}
codeSwitcherButtons.forEach(button => {
button.addEventListener('click', (e) => {
setCodeDisplay(e.currentTarget.dataset.codeId);
});
});
setCodeDisplay('simple');
const useCaseDetails = document.getElementById('use-case-details');
const useCaseData = {
'Coding Agents': {
title: 'Coding Agents',
description: 'This is the primary use case, leveraging the SDKs origin as a code assistant. Agents can read, understand, and modify complex codebases.',
examples: [
'<strong>Refactoring & Debugging:</strong> Scan code, identify side effects, and propose refactor plans.',
'<strong>Test-Driven Development (TDD):</strong> Write unit and integration tests based on specifications, then write the implementation code to make the tests pass.',
'<strong>Migrations:</strong> Perform complex migrations, such as from one web framework to another or updating database schemas.'
]
},
'SRE & DevOps': {
title: 'SRE & DevOps',
description: 'Agents can act as assistants for site reliability engineers, diagnosing issues and performing routine checks.',
examples: [
'<strong>Incident Triage:</strong> Read logs, run diagnostic scripts (using `Bash`), and correlate data to identify the root cause of an issue.',
'<strong>Automated Checks:</strong> Run scheduled health checks on services and propose remediation steps with human approval.',
'<strong>Code Review Bot:</strong> Audit code for security vulnerabilities or style guide adherence.'
]
},
'Data Analysis': {
title: 'Data Analysis',
description: 'By combining file access (`Read` for CSVs/JSON) and code execution (Python), agents can perform on-the-fly data analysis.',
examples: [
'<strong>Conversational Analytics:</strong> "Read `sales.csv`, calculate the total revenue by region, and plot a bar chart."',
'<strong>Data Cleaning:</strong> Write and execute scripts to clean and transform raw data files.',
'<strong>Report Generation:</strong> Analyze data and write a summary report to a new file.'
]
},
'Customer Support': {
title: 'Customer Support',
description: 'Agents can handle ambiguous customer requests by integrating with internal systems via custom tools (MCP).',
examples: [
'<strong>Smart Triage:</strong> Understand a customer ticket, retrieve user data from an internal API, and categorize the issue.',
'<strong>Automated Responses:</strong> Provide answers for common questions by searching internal knowledge bases.',
'<strong>Escalation:</strong> Escalate complex issues to a human agent, providing a full summary of the problem.'
]
},
'Deep Research': {
title: 'Deep Research',
description: 'Agents can perform comprehensive research tasks by reading multiple documents, searching the web, and synthesizing information.',
examples: [
'<strong>Report Synthesis:</strong> Read a directory of PDF/text files, extract key themes, and write a consolidated summary.',
'<strong>Web Research:</strong> Use `WebFetch` to gather information from multiple sources and generate a detailed report.',
'<strong>Competitive Analysis:</strong> Analyze public data to compare products or strategies.'
]
},
'Workflow Orchestration': {
title: 'Workflow Orchestration',
description: 'Agents can manage multi-step business processes that require sequential tasks and approvals.',
examples: [
'<strong>Content Pipeline:</strong> "Generate a blog post draft" (Action) -> "Validate draft against style guide" (Verify) -> "File for review" (Action).',
'<strong>Personal Assistant:</strong> "Check my calendar" (Tool) -> "Find open slots" (Logic) -> "Book travel via API" (Tool).',
'<strong>Finance:</strong> "Pull portfolio data" (Tool) -> "Run calculations" (Code) -> "Generate PDF report" (Tool).'
]
}
};
const ctx = document.getElementById('useCasesChart').getContext('2d');
const useCasesChart = new Chart(ctx, {
type: 'bar',
data: {
labels: [
'Coding Agents',
'SRE & DevOps',
'Data Analysis',
'Customer Support',
'Deep Research',
'Workflow Orchestration'
],
datasets: [{
label: 'Relative Impact & Versatility (Illustrative)',
data: [9, 8, 7, 7.5, 6, 8.5],
backgroundColor: [
'rgba(79, 209, 197, 0.6)', // teal-400
'rgba(99, 179, 237, 0.6)', // blue-400
'rgba(246, 224, 94, 0.6)', // yellow-300
'rgba(147, 197, 253, 0.6)', // blue-300
'rgba(182, 247, 233, 0.6)', // teal-200
'rgba(113, 163, 221, 0.6)' // blue-500
],
borderColor: [
'rgba(79, 209, 197, 1)',
'rgba(99, 179, 237, 1)',
'rgba(246, 224, 94, 1)',
'rgba(147, 197, 253, 1)',
'rgba(182, 247, 233, 1)',
'rgba(113, 163, 221, 1)'
],
borderWidth: 1
}]
},
options: {
indexAxis: 'y',
responsive: true,
maintainAspectRatio: false,
scales: {
x: {
beginAtZero: true,
title: {
display: true,
text: 'Illustrative Impact / Versatility'
}
}
},
plugins: {
legend: {
display: false
},
tooltip: {
callbacks: {
label: function(context) {
return ' Click to see details';
}
}
}
},
onClick: (evt) => {
const points = useCasesChart.getElementsAtEventForMode(evt, 'nearest', { intersect: true }, true);
if (points.length) {
const firstPoint = points[0];
const label = useCasesChart.data.labels[firstPoint.index];
const data = useCaseData[label];
if (data) {
let examplesHtml = data.examples.map(ex => `<li class="text-gray-700">${ex}</li>`).join('');
useCaseDetails.innerHTML = `
<h3 class="text-2xl font-semibold mb-3 text-gray-800">${data.title}</h3>
<p class="text-gray-700 mb-4">${data.description}</p>
<h4 class="text-lg font-medium text-gray-800 mb-2">Examples:</h4>
<ul class="list-disc list-inside space-y-1">${examplesHtml}</ul>
`;
}
}
}
}
});
showSection('overview');
});
