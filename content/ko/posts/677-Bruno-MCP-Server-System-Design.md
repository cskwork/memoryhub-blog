---
title: "Bruno MCP Server System Design"
date: 2025-06-10T22:41:34+09:00
slug: "677-Bruno-MCP-Server-System-Design"
original_url: "https://memoryhub.tistory.com/677"
tistory_id: 677
draft: false
---

## 1 Purpose

The **Bruno MCP Server** is a thin façade that exposes Bruno’s API-testing capabilities to any LLM that speaks the *Model Context Protocol (MCP)*.  
It lets an agent (e.g. Claude) **run collections** or **generate test scaffolds** on demand through a strict, type-safe interface.

---

## 2 High-Level Architecture

```
┌────────────────────┐
│      LLM Client    │  ← Claude / GPT / etc.
└─────────┬──────────┘
          │  MCP (JSON-RPC over stdio)
┌─────────▼──────────┐
│   Bruno MCP Server │  ← this project
└─────────┬──────────┘
          │  CLI (child_process)
┌─────────▼──────────┐
│     Bruno CLI      │  (@usebruno/cli)
└────────────────────┘
```

*Layers & boundaries are explicit:*  
LLM never shells out; Bruno CLI never parses MCP.

---

## 3 Component Breakdown

| # | Module | Responsibility | Notes / Patterns |
| --- | --- | --- | --- |
| 1 | **`index.ts`** | *Entry point & lifecycle management* | • create `StdioServerTransport`  • wire signals (`SIGINT`, `SIGTERM`)  • top-level exception fence (sets exit codes) |
| 2 | **`server.ts`** | *Protocol adapter* | • registers tools via **`ListTools`**  • routes **`CallTool`** → runner  • validates messages with Zod  **Pattern:** *Adapter + Dependency Injection* |
| 3 | **`runner.ts`** | *Business logic* | • `runCollection()` spawn Bruno CLI, capture JSON report  • `writeTestScript()` emit JS test file  **Pattern:** *Command* (each public method = command) |
| 4 | **`types.ts`** | *Single source of truth for schemas* | • runtime-safe via Zod  • exported TypeScript types for compile-time safety |
| 5 | **`utils.ts`** | *Cross-cutting helpers* | • `withReportFile()` *Template Method* for tmp file lifecycle  • safe mkdirp, auto-cleanup |

---

## 4 Runtime Data Flow (Sequence Diagram)

```
LLM ──ListTools──────────────▶ Server
LLM ◀─available tools─────────┘
LLM ──CallTool:run-collection▶ Server ─validate─▶ Runner
Runner ─spawn───────────────▶ Bruno CLI
Bruno CLI ─results.json──────▶ Runner ─parse────▶ Server
Server ─MCP response─────────▶ LLM
```

Error bubbles are caught at each hop, wrapped in an MCP-compliant error object, and surfaced to the LLM with actionable messages.

---

## 5 Non-Functional Requirements

| Concern | Guarantee / Mitigation |
| --- | --- |
| **Type Safety** | Zod validation on ingress + strong TS types end-to-end. |
| **Graceful Shutdown** | Signal handlers detach child processes, flush stdio, then `process.exit(0)`. |
| **Security** | Runner executes only whitelisted Bruno commands; no arbitrary shell interpolation. |
| **Observability** | Structured logs (JSON) emitted at INFO / ERROR; optional `--verbose` flag. |
| **Extensibility** | Adding a new tool = implement method in `runner.ts`, register schema in `server.ts`. |
| **Portability** | Pure Node.js ≥ 18, no native deps; published as single-file `bin` in npm package. |

---

## 6 Deployment & Ops

| Step | Detail |
| --- | --- |
| **Build** | `tsc && chmod +x dist/index.js` |
| **Package** | `npm publish` – sets `"bin": "dist/index.js"` |
| **Integration** | In Claude Desktop, add MCP server: `bruno-mcp start` (spawns over stdio) |
| **Runtime Config** | Environment vars:  • `BRUNO_MCP_TMPDIR` – override tmp path  • `LOG_LEVEL` – default `info` |
| **CI** | • unit tests for Runner logic (mock Bruno CLI)  • contract tests for MCP schemas |
| **Monitoring** | Exit code ≠ 0 interpreted by host as failure; logs consumed by stdout collector. |

---

## 7 Future Enhancements

1. **gRPC transport** (retain stdio as fallback).
2. **Streaming partial results** for long-running collections via MCP chunked messages.
3. **Pluggable reporters** – forward Bruno JUnit output directly to CI dashboards.
4. **Caching layer** – skip unchanged collections by hashing workspace.

---

## 8 Glossary

| Term | Definition |
| --- | --- |
| **MCP** | *Model Context Protocol* – lightweight JSON-RPC for tool-calling from LLMs. |
| **Bruno** | Open-source HTTP API client & test runner. |
| **Tool** | A callable operation exposed to the LLM (e.g. `run-collection`). |

---

### TL;DR

The Bruno MCP Server is a **stateless adapter**:  
stdin/stdout JSON ↔ child-process Bruno CLI, wrapped in solid TypeScript types and guarded by Zod.  
Drop it next to any LLM that understands MCP, and it instantly gains first-class API-testing skills.
