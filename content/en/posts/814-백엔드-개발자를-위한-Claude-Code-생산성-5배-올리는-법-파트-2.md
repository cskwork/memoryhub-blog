---
title: "5x Productivity Boost for Backend Developers Using Claude Code Part 2"
date: 2025-10-01T23:18:43+09:00
slug: "814-백엔드-개발자를-위한-Claude-Code-생산성-5배-올리는-법-파트-2"
original_url: "https://memoryhub.tistory.com/814"
tistory_id: 814
draft: false
---

### ⑥ Connect to Real Database with MCP

**Problem**

During API development, verifying actual data structure or validating query results requires switching between different tools.

**Solution**

Model Context Protocol (MCP) is an open standard connecting AI with external data sources. Claude can directly access hundreds of tools including Postgres, GitHub, Slack, JIRA, etc.

```
# Add Postgres MCP server
claude mcp add postgres \
  -e DATABASE_URL=postgresql://user:pass@localhost:5432/mydb \
  -- npx @modelcontextprotocol/server-postgres

# Now request Claude directly
Prompt:
"Query Postgres and get a list of users who signed up 
in the last 7 days and haven't made an order yet.
Also write a marketing email template to send to them."
```

Claude Code can read JIRA issues, implement features, create GitHub PRs, analyze monitoring data from Sentry, and automate workflows.

**Essential MCPs for Backend Developers**

MCP Server Usage Configuration Example

|  |  |  |
| --- | --- | --- |
| **Postgres** | DB schema analysis, query optimization | Official MCP server repository provides it |
| **GitHub** | PR creation, issue management, code review | Requires Personal Access Token |
| **Context7** | Automatically search latest library documentation | Free, registration required |
| **Claude Context** | Index entire codebase with semantic search | Vector DB connection |

---

### ⑦ Pass API Documentation Directly via Screenshots

**Problem**

Complex API specs or architecture diagrams described in text lead to misunderstandings.

**Solution**

Claude excels at processing images and diagrams. You can paste or drag-and-drop screenshots.

```
# macOS shortcut: Cmd+Ctrl+Shift+4 (screenshot to clipboard)
# Paste in terminal with Ctrl+V (not Cmd+V!)

Prompt:
"Look at this Swagger documentation screenshot and 
implement the same API endpoints in Node.js + Express.
Include validation, error handling, and OpenAPI comments."
```

**Usage Examples**

- Postman response screen → Error debugging
- ERD diagram → Database schema generation
- Design mockup → Admin panel UI implementation
- Performance monitoring graph → Optimization direction analysis

Especially effective for developing UI based on design mockups or debugging by analyzing charts.

---

### ⑧ URL Paste for Latest Framework Documentation

**Problem**

Claude may not know the latest APIs of fast-updating frameworks like Next.js 15, Prisma 6, etc.

**Solution**

Paste URLs directly in prompts and Claude fetches the page.

```
Prompt:
"https://nextjs.org/docs/app/api-reference/functions/cookies
Based on this official documentation, write an API middleware
to read and set cookies in Next.js 15."
```

**Productivity Tip**

Use /permissions to add frequently used domains to the allowlist, allowing automatic access without permission prompts.

```
claude
/permissions

# Add domains to allow
docs.nestjs.com
docs.spring.io
prisma.io/docs
```

Now pasting NestJS or Prisma documentation URLs immediately generates code based on the latest information.

---

### ⑨ Large-Scale Migration with Checklist Method

**Problem**

Large-scale work like changing hundreds of file import paths, removing legacy APIs, fixing lint errors causes Claude to stop mid-way or miss items.

**Solution**

Use Markdown files or GitHub issues as checklist workspaces.

```
Prompt:
"Step 1: Run linting and write all errors including filename 
and line number as a checklist in LINT_ERRORS.md.

Step 2: Fix each item on the checklist one by one, 
and check the box when done.

Step 3: Run linting again after each fix to confirm errors are gone.

Step 4: Repeat until all checkboxes are completed."
```

**LINT_ERRORS.md Example**

```
# Lint Error Fix Checklist

## Type Errors
- [ ] src/api/users.ts:45 - 'User' type missing 'email' property
- [ ] src/api/orders.ts:128 - Cannot assign 'Promise<void>' type to 'number'
- [x] src/utils/date.ts:12 - 'Date' type parameter missing ✅

## Unused imports
- [ ] src/services/auth.ts:3 - 'bcrypt' import unused
...
```

Improves performance on complex multi-step work like code migration, build script execution, and fixing numerous lint errors.

---

### ⑩ Auto-Generate Commit Messages and PR Descriptions

**Problem**

Focusing on code writing leads to superficial commit messages and PR descriptions.

**Solution**

Claude excels at writing clear PR descriptions and meaningful commit messages. Its perfect memory ensures nothing is missed.

```
# After work completion
Prompt:
"Organize the payment system changes implemented so far
into meaningful units and commit them.

Format each commit message using Conventional Commits:
- feat: new feature
- fix: bug fix
- refactor: refactoring
- test: test addition

Also write a GitHub PR description. Include:
- Summary of changes
- Technical implementation details
- How to test
- Related JIRA ticket numbers"
```

**Generation Example**

```
# Git commands Claude automatically runs

git add src/payment/tosspayments.service.ts
git commit -m "feat: Implement Toss Payments API integration service

- Add payment request/approval/cancellation methods
- Implement webhook signature verification logic
- Include retry logic (max 3 attempts)"

git add src/payment/payment.entity.ts src/payment/dto/
git commit -m "feat: Define Payment entity and DTOs

- Add Payment table to Prisma schema
- Payment status enum (PENDING/COMPLETED/FAILED)
- Include refund-related fields"

git add tests/payment/tosspayments.spec.ts
git commit -m "test: Write Toss Payments service integration tests

- Normal payment scenario
- Payment failure handling
- Webhook validation test"
```

Often writes better commit messages than humans, and collaboration communication becomes smoother.

---

## Bonus: Architecture-Level Questions

Claude understands architecture-level queries beyond simple searches.

```
Prompt Examples:
"Show me how user authentication flows throughout the app"
"Find all components that depend on UserContext"
"Track how product data flows from API calls to UI rendering"
"Find circular dependencies in the module structure"
```

Such high-level questions save enormous time in understanding legacy code or refactoring complex systems.

---

## Conclusion

**5 Additional Learnings**

- Remove context switching by directly connecting MCP to database, GitHub, JIRA
- Inject real-time information to Claude via screenshots and URL pastes
- Checklist method reliably completes large-scale migrations
- Commit/PR automation improves code history quality across the team
- Architecture questioning ability lets you use Claude like a senior consultant

**Final Practical Tip**  
The Claude Code Max Plan ($100/month) pays for itself saving 2 hours monthly, and unlimited use without token concerns is the key to productivity. For backend developers, the MCP + multi-instance + TDD combination is most powerful.

---

## Updated References

- [Anthropic - MCP Official Introduction](https://www.anthropic.com/news/model-context-protocol)
- [Claude Code MCP Integration Guide](https://docs.claude.com/en/docs/claude-code/mcp)
- [MCP Server Repository (Postgres, GitHub, etc.)](https://github.com/modelcontextprotocol/servers)
- [Context7 MCP - Automatic Latest Documentation Search](https://context7.com/)
