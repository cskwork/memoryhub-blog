---
title: "Anthropic's Model Context Protocol (MCP) Complete Guide ?"
date: 2025-02-26T23:09:50+09:00
slug: "456-Anthropic의-Model-Context-Protocol-MCP-완벽-가이드"
original_url: "https://memoryhub.tistory.com/456"
tistory_id: 456
draft: false
categories: ["Dev Library"]
tags: ["Claude"]
---

Hello! Today, let's explore the Model Context Protocol (MCP) developed by Anthropic, and introduce you to popular servers that developers can actually use and their uses.

## What is MCP? ?

Imagine you asked your AI assistant, "Please read the files on my computer."

- Normally, AI cannot access files on your computer
- But with MCP? You can safely read and process files!

Model Context Protocol (MCP) does exactly this!

- A standardized protocol that allows AI models (Claude) to safely access external tools or data sources
- Like providing AI with a USB-C port ✨

## How Does It Work? ?

### Basic Architecture

```
User → Claude → MCP Client → MCP Server → External Service/Data → Claude → User
```

1. User asks: "Analyze the receipt.pdf file in my documents folder"
2. Claude forwards the request to the file system MCP server
3. MCP server safely reads the file from your computer
4. Claude provides analysis results to the user based on received information

## 10+ Popular Real MCP Servers ?

### 1. File System MCP

```
npx @modelcontextprotocol/server-filesystem /path/to/allowed/files
```

- **Feature**: Provides ability to read, write, and search local files
- **Developer Usage**: Project file analysis, code review, document processing automation

### 2. Code Interpreter MCP

```
npx @anthropic-ai/mcp-code-interpreter
```

- **Feature**: Provides Python code execution, data analysis, visualization capabilities
- **Developer Usage**: Data analysis, algorithm prototyping, problem-solving automation

### 3. Git MCP

```
uvx mcp-server-git
```

- **Feature**: Provides Git repository reading, searching, comparison capabilities
- **Developer Usage**: Code change history analysis, PR review, codebase understanding

### 4. GitHub MCP

```
npx @modelcontextprotocol/server-github
```

- **Feature**: Provides GitHub repository management, issue management, PR creation capabilities
- **Developer Usage**: Issue management automation, document updates, code review assistance

### 5. Web Browser MCP (Puppeteer)

```
npx @modelcontextprotocol/server-puppeteer
```

- **Feature**: Provides web page navigation, screenshots, automation capabilities
- **Developer Usage**: Web test automation, data collection, UI analysis

### 6. PostgreSQL MCP

```
npx @modelcontextprotocol/server-postgres
```

- **Feature**: Provides PostgreSQL database queries, schema inspection capabilities
- **Developer Usage**: Data analysis, query optimization, schema design assistance

### 7. SQLite MCP

```
npx @modelcontextprotocol/server-sqlite
```

- **Feature**: Provides SQLite database access, querying, analysis capabilities
- **Developer Usage**: Local data analysis, database design, report generation

### 8. Memory MCP

```
npx @modelcontextprotocol/server-memory
```

- **Feature**: Provides knowledge graph-based permanent memory system
- **Developer Usage**: Long-term conversation context maintenance, project knowledge storage

### 9. Web Content Fetching (Fetch MCP)

```
npx @modelcontextprotocol/server-fetch
```

- **Feature**: Provides web content fetching and LLM-optimized conversion
- **Developer Usage**: API documentation reference, web content analysis, information retrieval

### 10. Google Drive MCP

```
npx @modelcontextprotocol/server-gdrive
```

- **Feature**: Provides Google Drive file access, search, management capabilities
- **Developer Usage**: Document management, team document analysis, content summarization

### 11. Slack MCP

```
npx @modelcontextprotocol/server-slack
```

- **Feature**: Provides Slack channel management, message sending, search capabilities
- **Developer Usage**: Team communication automation, notification management, information tracking

### 12. Docker MCP (Community)

```
npx mcp-server-docker
```

- **Feature**: Provides Docker container, image, volume management capabilities
- **Developer Usage**: Container management automation, deployment process simplification

## Developer Usage Methods ?

### 1. Code Review and Analysis Assistance

```
// Code review workflow using Git and GitHub MCP
// 1. Clone and analyze repository
await gitServer.cloneRepository('https://github.com/user/repo.git');
await gitServer.analyzeChanges('main', 'feature-branch');

// 2. Create GitHub PR and comments
await githubServer.createPullRequestComment({
  owner: 'user',
  repo: 'repo',
  pull_number: 123,
  body: 'Code analysis results: 3 performance improvement opportunities found'
});
```

### 2. Database Work Automation

```
-- Database optimization using PostgreSQL MCP
-- 1. Analyze schema
SELECT * FROM information_schema.tables WHERE table_schema = 'public';

-- 2. Identify performance problem queries
SELECT query, total_time, calls
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;

-- 3. Index suggestions
-- Claude automatically generates index creation scripts
```

### 3. Local Development Environment Support

```
# Example combining File System MCP and Code Interpreter MCP
npx @modelcontextprotocol/server-filesystem ~/projects
npx @anthropic-ai/mcp-code-interpreter

# Request to Claude:
# "Find parts in my project code with potential memory leaks"
# "Create a visualization for this dataset"
```

### 4. Web Service Integration and Automation

```
// Example of GitHub and Slack MCP integration
async function createWeeklyReport() {
  // 1. Get weekly commit information from GitHub
  const commits = await githubServer.getCommits({
    owner: 'team',
    repo: 'project',
    since: getLastWeek()
  });

  // 2. Analyze commits and generate report
  const report = analyzeCommits(commits);

  // 3. Send report to Slack
  await slackServer.postMessage({
    channel: 'dev-team',
    text: 'Weekly Development Status Report',
    blocks: formatReportForSlack(report)
  });
}
```

## Real-World Usage Scenarios ?

### 1. Full-Stack Development Assistance

Use file system, Git, code interpreter, database MCP together to:

- Simultaneously analyze frontend and backend code
- Verify API endpoints and database schema consistency
- Generate code snippets for new feature implementation

```
"Find all user authentication-related code in my project and check for security vulnerabilities"
```

### 2. Data Pipeline Construction

Leverage PostgreSQL, code interpreter, file system MCP to:

- Analyze database query results
- Transform and process data with Python
- Save results to files and create visualizations

```
"Fetch last month's sales data from the DB, generate a graph of sales trends by region, and write a report"
```

### 3. Documentation and Knowledge Management

Combine Memory MCP, file system, GitHub MCP to:

- Automatically generate project documentation
- Update README based on code changes
- Build team knowledge base

```
"Analyze all code changed in the last sprint and update the API documentation"
```

## MCP Server Installation and Configuration ?

### 1. Using MCP in Claude Desktop

```
// Create config.json file
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

### 2. Creating Your Own MCP Server

```
// Creating a simple MCP server in TypeScript
import { createServer, Tools } from '@modelcontextprotocol/typescript-sdk';

// Define tools
const tools: Tools = {
  getWeather: {
    description: 'Get current weather information for a specific city',
    parameters: {
      type: 'object',
      properties: {
        city: { type: 'string', description: 'City name (e.g., Seoul)' }
      },
      required: ['city']
    },
    handler: async ({ city }) => {
      // Weather API call logic
      return { temperature: '23°C', condition: 'Clear' };
    }
  }
};

// Start server
const server = createServer({ tools });
server.listen(3000, () => {
  console.log('MCP server running on port 3000');
});
```

## Cautions ⚠️

1. **Security Considerations**

   - Since MCP servers can access local resources, be careful with access permission settings
   - Use only MCP servers from trustworthy sources
   - Manage API keys and authentication tokens safely using environment variables
2. **Resource Management**

   - When running multiple MCP servers simultaneously, monitor system resource usage
   - Run resource-intensive servers like browser automation only when needed
3. **Compatibility Considerations**

   - MCP servers may have port conflicts with other applications
   - Update to the latest MCP SDK version to maintain compatibility

## Conclusion ?

Model Context Protocol (MCP) serves as a powerful bridge connecting AI and the external world. For developers, it can be a reliable assistant that automates repetitive tasks and helps solve complex problems.

This protocol continues to evolve, and the developer community creates, shares, and develops various MCP servers. Why not try creating your own MCP server and expand the possibilities of AI!

---

Feel free to leave any questions in the comments! ?

#Anthropic #Claude #ModelContextProtocol #MCP #AI Development #AITools

---

### Reference Materials

1. Model Context Protocol Official Site: <https://modelcontextprotocol.io>
2. MCP GitHub Repository: <https://github.com/modelcontextprotocol>
3. Anthropic Claude Documentation: <https://docs.anthropic.com/claude/docs/agents-and-tools/mcp>
4. MCP Example Server Collection: <https://modelcontextprotocol.io/examples>
