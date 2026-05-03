---
title: "Troubleshooting Claude Desktop's Brave Search MCP Server on Mac ?"
date: 2025-03-13T20:54:18+09:00
slug: "471-Mac에서-Claude-Desktop의-Brave-Search-MCP-서버-문제-해결하기"
original_url: "https://memoryhub.tistory.com/471"
tistory_id: 471
draft: false
---

Let me show you how to solve the problem of Claude Desktop application's Brave Search MCP server not working in Mac environment.

## What is MCP Server and Brave Search? ?

MCP (Model Context Protocol) server is an interface that allows Claude AI to communicate with external tools.

- It's like giving Claude eyes to browse the internet!
- Brave Search MCP allows Claude to search for latest information on the web.
- Without this feature, Claude must only answer with its own training data.

## What Causes the Problem? ?

Main causes of Brave Search MCP server not working on Mac:

1. **Node.js Environment Issues**

   - Claude Desktop cannot find Node.js and npx
   - PATH setting is incorrect
2. **Configuration File Errors**

   - Configuration file is in wrong location
   - JSON format is incorrect
   - Required environment variables are missing
3. **API Key Issues**

   - Brave Search API key is missing or configured incorrectly

## Troubleshooting Methods ?

### 1. Verify Node.js Installation

```
# Check Node.js and npm installation from terminal
node -v
npm -v

# If not installed, install with nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.zshrc  # Or source ~/.bash_profile
nvm install --lts  # Install LTS version
```

### 2. Find Correct Path

```
# Find full path of npx
which npx
# Example: /Users/username/.nvm/versions/node/v18.12.1/bin/npx

# Find Node.js path
which node
# Example: /Users/username/.nvm/versions/node/v18.12.1/bin/node
```

### 3. Get Brave Search API Key

1. Visit [Brave Search API](https://brave.com/search/api/) website
2. Create developer account or log in
3. Generate and copy API key

### 4. Modify Configuration File

1. Find file location:

   ```
   /Users/username/Library/Application Support/Claude/claude_desktop_config.json
   ```

   - Replace `username` with your actual Mac username.
2. Create file if it doesn't exist:

   ```
   mkdir -p ~/Library/Application\ Support/Claude/
   touch ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```
3. Add the following content to configuration file:

   ```
   {
     "mcpServers": [
       {
         "name": "brave-search",
         "command": "full_path_to_npx_here",
         "args": ["-y", "@modelcontextprotocol/server-brave-search"],
         "env": {
           "BRAVE_API_KEY": "enter_api_key_here",
           "PATH": "node_path_here:/usr/local/bin:/usr/bin:/bin",
           "NODE_PATH": "node_modules_path_here"
         }
       }
     ]
   }
   ```
4. Modify with actual paths:

   ```
   {
     "mcpServers": [
       {
         "name": "brave-search",
         "command": "/Users/username/.nvm/versions/node/vversion_number/bin/npx",
         "args": ["-y", "@modelcontextprotocol/server-brave-search"],
         "env": {
           "BRAVE_API_KEY": "enter_api_key_here",
           "PATH": "/Users/username/.nvm/versions/node/vversion_number/bin:/usr/local/bin:/usr/bin:/bin",
           "NODE_PATH": "/Users/username/.nvm/versions/node/vversion_number/lib/node_modules"
         }
       }
     ]
   }
   ```

### 5. Install MCP Server Package

```
# Install package globally
npm install -g @modelcontextprotocol/server-brave-search
```

### 6. Restart Claude Desktop

1. Completely close Claude Desktop
2. Restart the application

## Troubleshooting Case Study ?️

Here's a successful troubleshooting method shared by a Reddit user:

```
{
  "mcpServers": [
    {
      "name": "brave-search",
      "command": "/Users/username/.nvm/versions/node/v23.3.0/bin/npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "enter_api_key_here",
        "PATH": "/Users/username/.nvm/versions/node/v23.3.0/bin:/usr/local/bin:/usr/bin:/bin",
        "NODE_PATH": "/Users/username/.nvm/versions/node/v23.3.0/lib/node_modules"
      }
    }
  ]
}
```

## Common Errors and Solutions ⚠️

### 1. `spawn npx ENOENT` Error

- **Cause**: Claude Desktop cannot find npx
- **Solution**: Specify full path of npx in configuration file

### 2. API Key Related Errors

- **Cause**: API key is incorrect
- **Solution**: Issue new API key and enter it accurately

### 3. MCP Server Start Failure

- **Cause**: Package installation issue
- **Solution**: Re-run `npm install -g @modelcontextprotocol/server-brave-search`

### 4. Configuration File Not Recognized

- **Cause**: File location or format error
- **Solution**: Verify correct path and JSON format

## Cautions ⚠️

1. **Node.js Installation Method**: It's recommended to install using Node version manager (nvm). Path management is easier than using an installer.
2. **Path Accuracy**: All paths (PATH) used in the configuration file must exactly match your actual environment. Pay special attention to username and Node.js version.
3. **JSON Format**: Configuration file must be in correct JSON format. Verify there are no errors with commas, quotes, etc.
4. **API Key Security**: Brave Search API key is personal information. Don't share it in public places.
5. **File Permissions**: Configuration file and Node.js-related directories must have appropriate read/write permissions.

---

I hope this guide helps you resolve the Brave Search MCP server issue in Claude Desktop on Mac! Feel free to ask questions anytime. ?

## References

1. [Reddit - Resolved MCP Brave Search Issue](https://www.reddit.com/r/ClaudeAI/comments/1h758o0/resolved_mcp_brave_search_issue/)
2. [GitHub - Model Context Protocol Servers Issues](https://github.com/modelcontextprotocol/servers/issues/63)
3. [Stack Overflow - Could not start MCP server for Brave Search](https://stackoverflow.com/questions/79262030/could-not-start-mcp-server-for-brave-search-in-computer-use-and-claude-desktop)
4. [Medium - MCP Integration: How Brave Search and Claude Desktop Enhance AI Assistant](https://medium.com/@richardhightower/mcp-integration-how-brave-search-and-claude-desktop-enhance-ai-assistant-agentic-capabilities-c840590fa100)
