---
title: "Google Calendar MCP Server Code Detailed Analysis"
date: 2025-03-21T14:41:56+09:00
slug: "494-Google-Calendar-MCP-서버-코드-상세-분석"
original_url: "https://memoryhub.tistory.com/494"
tistory_id: 494
draft: false
categories: ["Dev Util"]
tags: ["Google Integration"]
---

This code implements a Node.js server based on Model Context Protocol (MCP) that enables large language models (LLMs) to interact directly with the Google Calendar API. Through complex OAuth2 authentication handling and standardized tool interfaces, it allows AI systems to safely manage user calendars.

#### Reference Code:

<https://github.com/MCP-Mirror/GongRzhe_Calendar-MCP-Server>

## 1. Technical Architecture and Key Components

### 1.1 Model Context Protocol (MCP) Structure

MCP is a standardized protocol for AI models to interact with external tools.

```
Client (AI Model)   <-->   MCP Server   <-->   External Service (Google Calendar)
    Request/Response        Request/Response
```

### 1.2 Key Library Composition

- **@modelcontextprotocol/sdk**: Core library for implementing MCP servers
  - `Server`: Creates MCP server instances
  - `StdioServerTransport`: Standard input/output-based communication layer
  - `CallToolRequestSchema`, `ListToolsRequestSchema`: Request schema definitions
- **googleapis**: Official client library for accessing Google APIs
  - `google.calendar`: Calendar API v3 client
- **zod**: Runtime type validation library
  - Data structure schema definition and validation
- **google-auth-library**: OAuth2 authentication handling
  - `OAuth2Client`: OAuth 2.0 authentication flow management

## 2. Authentication Mechanism Detailed Analysis

### 2.1 OAuth2 Authentication Setup

```
const CLIENT_ID = process.env.GOOGLE_CLIENT_ID;
const CLIENT_SECRET = process.env.GOOGLE_CLIENT_SECRET;
const REFRESH_TOKEN = process.env.GOOGLE_REFRESH_TOKEN;
const REDIRECT_URI = 'http://localhost';
```

- **Environment Variables**: Separates sensitive authentication information from code for enhanced security
- **Refresh Token Usage**: Maintains long-term API access rights (eliminates need for user re-authentication)

### 2.2 OAuth2 Client Initialization

```
const oauth2Client = new OAuth2Client(
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI
);

oauth2Client.setCredentials({
    refresh_token: REFRESH_TOKEN
});
```

- **Authentication Flow**:
  1. Automatically refresh access tokens using refresh token
  2. Handle expired token automatic renewal
  3. Attach valid access token with each API request

## 3. Schema System In-Depth Analysis

### 3.1 Zod Schema Definition

Each API operation's input structure is strictly defined.

```
const CreateEventSchema = z.object({
    summary: z.string().describe("Event title"),
    start: z.object({
        dateTime: z.string().describe("Start time (ISO format)"),
        timeZone: z.string().optional().describe("Time zone"),
    }),
    end: z.object({
        dateTime: z.string().describe("End time (ISO format)"),
        timeZone: z.string().optional().describe("Time zone"),
    }),
    description: z.string().optional().describe("Event description"),
    location: z.string().optional().describe("Event location"),
});
```

- **Required/Optional Field Distinction**: `.optional()` marks optional fields
- **Field Documentation**: `.describe()` documents each field's purpose
- **Nested Objects**: Accurately models complex data structures

### 3.2 JSON Schema Conversion

```
inputSchema: zodToJsonSchema(CreateEventSchema)
```

- **Purpose**: Converts Zod schema to JSON schema for use in MCP
- **Benefits**:
  1. Provides schema information to clients (AI models)
  2. Maintains consistency between TypeScript/JavaScript development environment and MCP

## 4. Tool Implementation Detailed Analysis

### 4.1 Tool Registration Process

```
server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: [
        {
            name: "create_event",
            description: "Creates a new event in Google Calendar",
            inputSchema: zodToJsonSchema(CreateEventSchema),
        },
        // Other tools...
    ],
}));
```

- **Tool Metadata**: Structured information including name, description, and input schema
- **Tool Discovery**: AI models dynamically discover available tools and usage methods

### 4.2 Tool-Specific Detailed Function Analysis

#### 4.2.1 create_event

```
case "create_event": {
    const validatedArgs = CreateEventSchema.parse(args);
    const response = await calendar.events.insert({
        calendarId,
        requestBody: validatedArgs,
    });
    return {
        content: [
            {
                type: "text",
                text: `Event created with ID: ${response.data.id}\n` +
                      `Title: ${validatedArgs.summary}\n` +
                      `Start: ${validatedArgs.start.dateTime}\n` +
                      `End: ${validatedArgs.end.dateTime}`,
            },
        ],
    };
}
```

- **Input Validation**: Validates input values through Zod and enforces types
- **API Call**: Calls Google Calendar API with validated parameters
- **Response Formatting**: Formats user-friendly response messages

#### 4.2.2 get_event

Returns detailed event information for a specific event ID in JSON format.

#### 4.2.3 update_event

Sends only selected fields to be updated along with the event ID.

```
const { eventId, ...updates } = validatedArgs;
const response = await calendar.events.patch({
    calendarId,
    eventId,
    requestBody: updates,
});
```

- **Partial Updates**: Uses object destructuring to send only changed fields
- **Efficiency**: Minimizes unnecessary data transmission

#### 4.2.4 delete_event

Validates the event ID and performs deletion.

#### 4.2.5 list_events

```
const response = await calendar.events.list({
    calendarId,
    timeMin: validatedArgs.timeMin,
    timeMax: validatedArgs.timeMax,
    maxResults: validatedArgs.maxResults || 10,
    orderBy: validatedArgs.orderBy || 'startTime',
    singleEvents: true,
});
```

- **Default Values**: Provides defaults for optional parameters
- **Single Event Conversion**: `singleEvents: true` expands recurring events into individual events

## 5. Request Processing Flow Detailed Analysis

### 5.1 Tool Call Request Handling

```
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    try {
        switch (name) {
            // Case handling for each tool
        }
    } catch (error) {
        return {
            content: [
                {
                    type: "text",
                    text: `Error: ${error instanceof Error ? error.message : String(error)}`,
                },
            ],
            isError: true,
        };
    }
});
```

- **Request Parsing**: Extracts tool name and arguments
- **Tool Dispatch**: Routes to appropriate handler based on tool name
- **Error Handling**: Catches all exceptions and converts to structured error responses
  - **Error Classification**: Distinguishes between Error instances and other exceptions
  - **Error Indication**: Explicitly marks error state with `isError: true` flag

### 5.2 Data Flow Steps

1. **Input Reception**: Receives MCP request (tool name, arguments)
2. **Schema Validation**: Validates and type-converts arguments through Zod
3. **API Call**: Calls Google Calendar API
4. **Response Transformation**: Transforms API response to MCP response format
5. **Result Return**: Returns structured response or error

## 6. Server Communication Method

```
const transport = new StdioServerTransport();
server.connect(transport).catch((error) => {
    console.error("Fatal error running server:", error);
    process.exit(1);
});
```

- **StdioServerTransport**: Communication through standard input/output (stdin/stdout)
  - **Advantage**: Easy integration across various environments
  - **Operation Method**: Reads JSON format messages from stdin and writes to stdout
- **Error Handling**: Logs errors and exits server on fatal errors

## 7. Security Considerations

### 7.1 Authentication and Authorization Management

- **OAuth2 Authentication**: Uses standard authentication protocol
- **Limited Permission Scope**: Requests only minimum required permissions for Google Calendar API
- **Environment Variables**: Separates sensitive authentication information from code

### 7.2 Input Validation and Sanitization

- **Schema Validation**: Strict structure and type validation for all inputs
- **Runtime Validation**: Runtime data validation through Zod

## 8. Scalability and Maintainability

### 8.1 Modular Structure

- **Tool Separation**: Implements each function as an independent tool
- **Schema-Driven Design**: Clarifies data structures for clear interfaces

### 8.2 Future Extensibility

- **New Tool Addition**: Easily integrates additional Calendar API features
- **Other Google API Integration**: Can extend to Gmail, Drive, etc. using similar patterns

## 9. Conclusion

This code provides a safe and structured interface between AI models and Google Calendar API through Model Context Protocol. It ensures high reliability through strict type validation, error handling, and OAuth2 authentication. This implementation approach provides the essential technical link for AI systems to transform user natural language requests into actual calendar operations.
