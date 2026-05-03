---
title: "Setup Composio's mcp servers to Claude Desktop App"
date: 2025-03-08T00:36:55+09:00
slug: "461-Setup-Composio-s-mcp-servers-to-Claude-Desktop-App"
original_url: "https://memoryhub.tistory.com/461"
tistory_id: 461
draft: false
---

### Overview

Adding a Composio MCP (Model Context Protocol) server to the Claude Desktop app allows you to enhance Claude’s capabilities by integrating with over 250 tools managed by Composio, such as Gmail, Notion, and GitHub. This process involves setting up the Composio CLI, obtaining necessary credentials, and configuring the Claude app. It’s a technical task that may require familiarity with command-line tools and JSON configuration, but it can significantly boost productivity for daily use.

### Prerequisites

Before starting, ensure you have:

- A Composio account (sign up at <https://composio.dev>).
- The Claude Desktop app installed (download from <https://claude.ai/download>).
- Node.js installed (get it from <https://nodejs.org>, LTS version recommended).
- Terminal access (e.g., Terminal on macOS, Command Prompt/PowerShell on Windows).

### Steps to Add the Server

1. **Get Your Composio API Key**: Sign in to <https://composio.dev> and retrieve your API key from your account settings.
2. **Install Composio CLI**: Open your terminal and run `npm install -g composio-core@rc` to install the Composio CLI tool.
3. **Select and Note the MCP Server URL**: Visit Composio’s MCP directory (e.g., <https://mcp.composio.dev>) to choose a server (e.g., Notion) and note its specific URL, which will look like `https://mcp.composio.dev/notion/your-server-id`.
4. **Configure Claude Desktop**: Locate the `claude_desktop_config.json` file:
   - On macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - On Windows: `%appdata%\Claude\claude_desktop_config.json`
   - If it doesn’t exist, create it in the specified directory.
5. **Edit the Configuration File**: Add the following JSON, replacing placeholders with your details:

   ```
   {
     "mcpServers": {
       "composio-notion": {
         "command": "npx",
         "args": ["composio-core@rc", "mcp", "<server-url>", "--client", "claude"],
         "env": {
           "COMPOSIO_API_KEY": "<your_api_key>"
         }
       }
     }
   }
   ```

   - Replace `<server-url>` with the URL from step 3.
   - Replace `<your_api_key>` with your Composio API key.
6. **Save and Restart**: Save the file and restart the Claude Desktop app. A hammer icon should appear, indicating the server is connected.
7. **Test the Connection**: Try a prompt related to the connected app (e.g., “List my Notion pages”) to verify functionality.

### Unexpected Detail

An unexpected aspect is that Composio offers fully managed servers with built-in authentication (e.g., OAuth, API keys), simplifying the setup compared to building your own MCP server, which might otherwise require more technical expertise.

---

### Comprehensive Guide to Installing Popular Composio’s MCP Servers for Daily Use

This guide provides a detailed, step-by-step process for integrating Composio’s Model Context Protocol (MCP) servers with the Claude Desktop app, enabling seamless interaction with over 250 tools for daily productivity tasks. As of March 07, 2025, Composio’s platform supports integrations like Gmail, Notion, GitHub, and more, with managed authentication and optimized tool accuracy, making it ideal for automating workflows.

#### Background and Context

Composio is an AI agent toolset that equips large language models (LLMs) and AI agents with access to 250+ applications through MCP servers, as detailed on their website ([Composio](https://composio.dev)). The Model Context Protocol, developed by Anthropic, facilitates secure connections between AI assistants like Claude and external data sources, enhancing capabilities such as email management, task automation, and document processing. The Claude Desktop app, available at <https://claude.ai/download>, supports MCP servers, allowing users to extend functionality beyond basic chat interactions.

Composio’s MCP servers are fully managed, offering built-in authentication support (e.g., OAuth, API keys, JWT) and improved function-calling accuracy, as noted in their documentation ([Composio MCP](https://composio.dev/mcp/)). This is particularly useful for daily tasks, such as managing emails in Gmail, organizing notes in Notion, or collaborating on GitHub, without needing to build custom integrations.

#### Prerequisites and Setup

Before proceeding, ensure you meet the following requirements:

- **Composio Account**: Sign up at <https://composio.dev> to obtain an API key, essential for authentication with MCP servers.
- **Claude Desktop App**: Download and install the latest version from <https://claude.ai/download>. Ensure it’s the official app, as unofficial versions may lack MCP support.
- **Node.js**: Install the LTS version from <https://nodejs.org> and verify with `node --version` and `npm --version` in your terminal.
- **Terminal Access**: Use Terminal on macOS or Command Prompt/PowerShell on Windows for CLI commands.
- **Developer Mode (Optional)**: In Claude Desktop, go to `Menu > Help > Enable Developer Mode` for logs and debugging if needed.

#### Step-by-Step Installation Process

The process involves installing the Composio CLI, selecting a server, configuring the Claude app, and testing the integration. Below is a detailed breakdown:

##### Step 1: Install Composio CLI

Composio provides a command-line tool (`composio-core`) to manage MCP servers. Install it using:

```
npm install -g composio-core@rc
```

- The `@rc` tag ensures you get the release candidate version, which supports the latest MCP features as of March 2025.
- Verify installation with `composio --version`. If this fails, ensure Node.js is correctly installed and added to your system PATH.

##### Step 2: Obtain Composio MCP Server Details

Composio offers prebuilt MCP servers for popular apps like Gmail, Notion, GitHub, Slack, and more, accessible via their MCP directory (<https://mcp.composio.dev>). To proceed:

1. Log in to your Composio account at <https://composio.dev>.
2. Navigate to the MCP server section (likely under “Features” or “MCP Servers”).
3. Select the desired server (e.g., “notion”).
4. Copy the provided Server-Sent Events (SSE) URL, which will look like `https://mcp.composio.dev/notion/30c7242b-9a14-45d2-bca7-5012dd77fc11`. This URL is an example; yours will differ based on your account and chosen server.

##### Step 3: Configure Claude Desktop

Claude Desktop uses a JSON configuration file (`claude_desktop_config.json`) to register MCP servers. Follow these steps:

1. **Locate the Config File**:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%appdata%\Claude\claude_desktop_config.json` (paste into File Explorer’s address bar to navigate).
   - If the file doesn’t exist, create it in the specified directory.
2. **Edit the Config File**:  
   Open the file in a text editor (e.g., VS Code, Notepad). Add an entry for the Composio MCP server under the `"mcpServers"` key. Use the following template:

   ```
   {
     "mcpServers": {
       "composio-notion": {
         "command": "npx",
         "args": ["composio-core@rc", "mcp", "https://mcp.composio.dev/notion/30c7242b-9a14-45d2-bca7-5012dd77fc11", "--client", "claude"],
         "env": {
           "COMPOSIO_API_KEY": "your-api-key-here"
         }
       }
     }
   }
   ```

   - Replace `https://mcp.composio.dev/notion/30c7242b-9a14-45d2-bca7-5012dd77fc11` with the URL you copied in Step 2.
   - Replace `your-api-key-here` with your Composio API key.
   - `"composio-notion"` is a custom name; you can change it (e.g., `"notion"`).
   - Ensure the JSON is valid (no trailing commas, proper syntax).
3. **Save and Validate**:  
   Save the file and ensure there are no syntax errors.

##### Step 4: Restart Claude Desktop

Close and reopen the Claude Desktop app to apply the changes. If configured correctly:

- A hammer icon should appear next to the input field, indicating MCP servers are detected.
- Click the icon to see the registered server (e.g., “composio-notion”).

##### Step 5: Test the Connection

Test the MCP server by sending a prompt related to the connected app. For example, if you added the Notion server:

- Prompt: “Can you list my Notion pages?”
- Claude should request permission to use the MCP server. Approve it, and it will interact with Notion via Composio’s server.

#### Troubleshooting and Tips for Daily Use

If the server doesn’t appear or fails:

- **Check Logs**: Enable Developer Mode in Claude Desktop (`Menu > Help > Enable Developer Mode`), then go to `Developer > Open MCP Log File` to view errors (e.g., “Could not attach to MCP” or path issues).
- **Verify Paths**: Ensure `node` and `npx` are in your PATH (`where node` on Windows, `which node` on macOS). Test the command manually in your terminal (e.g., `npx composio-core@rc mcp <url> --client claude`).
- **Update Software**: Ensure Claude Desktop and Node.js are up to date.
- **Contact Composio Support**: If issues persist, check Composio’s documentation (<https://docs.composio.dev>) or support channels for updated instructions.

For daily use, consider setting up multiple servers for different apps (e.g., Gmail for email management, GitHub for code collaboration) to streamline workflows. Regularly update the composio-core CLI (`npm update -g composio-core@rc`) to access new features and bug fixes.

#### Popular Composio MCP Servers for Daily Tasks

Here’s a table of popular Composio MCP servers and their typical use cases, based on available information:

| Server Name | Typical Use Case | Example Prompt |
| --- | --- | --- |
| Notion | Manage notes, docs, and tasks | “List my Notion pages” |
| Gmail | Send and manage emails | “Draft an email to my team” |
| GitHub | Code repository management | “Star the composiohq/composio repo” |
| Slack | Team communication and file sharing | “Post a message in #general” |
| Google Sheets | Spreadsheet automation | “Update row 5 in my budget sheet” |

These servers leverage Composio’s managed authentication, reducing setup complexity for daily tasks.

#### Additional Considerations

An unexpected detail is that Composio’s MCP servers are fully managed with built-in authentication, which simplifies the process compared to building your own server, potentially saving hours of setup time. However, the configuration requires editing JSON files and using the command line, which may be challenging for non-technical users. For such users, Composio’s documentation (<https://docs.composio.dev/mcp/overview>) provides further guidance, and community forums (e.g., Reddit’s r/mcp) may offer support.

This setup is particularly useful for professionals who rely on AI for productivity, such as developers, researchers, and knowledge workers, as highlighted in various Medium articles ([How to Use MCP Tools on Claude Desktop App](https://medium.com/@pedro.aquino.se/how-to-use-mcp-tools-on-claude-desktop-app-and-automate-your-daily-tasks-1c38e22bc4b0)).

---

### Key Citations

- [Composio equip's your AI agents & LLMs with 100+ high-quality integrations via function calling](https://github.com/ComposioHQ/composio)
- [Composio - Access 250+ apps in just one line of code](https://composio.dev/)
- [Download Claude for your desktop or mobile device](https://claude.ai/download)
- [Composio MCP: Connect LLMs, IDEs, & Claude with 250+ MCP Server](https://composio.dev/mcp/)
- [Composio MCP Server directory](https://mcp.composio.dev/)
- [Node.js official download page](https://nodejs.org)
- [How to Use MCP Tools on Claude Desktop App and Automate Your Daily Tasks Medium article](https://medium.com/@pedro.aquino.se/how-to-use-mcp-tools-on-claude-desktop-app-and-automate-your-daily-tasks-1c38e22bc4b0)
- [Composio MCP overview documentation](https://docs.composio.dev/mcp/overview)
