---
title: "Making Payment Integration Easier with AI: Building Toss Payments MCP Server"
date: 2025-10-24T03:33:21+09:00
slug: "868-Making-Payment-Integration-Easier-with-AI-Building-Toss-Payments-MCP-Server"
original_url: "https://memoryhub.tistory.com/868"
tistory_id: 868
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
cover:
  image: "/images/868-Making-Payment-Integration-Easier-with-AI-Building-Toss-Payments-MCP-Server/img.png"
  relative: false
  hidden: false
---

## Summary

To make Toss Payments API integration easier and faster, we're providing an MCP server that helps AI-powered coding tools generate more accurate integration code. For detailed information, check out the Toss Payments Integration Guide.

Using the Toss Payments MCP server increases code generation accuracy compared to using AI coding tools alone.

This MCP server started from a small discussion within our guild and may have limited context information available to AI models at the time of writing. We'll continue improving it to enhance the Toss Payments API integration experience.

---

## Background

From the very beginning, Toss Payments has been deeply concerned with making payment system integration easier for our merchants. We needed to break the perception that payment system integration is complex and cumbersome for developers.

To solve this problem, we created intuitive APIs and SDKs, built a Developer Center for developers integrating Toss Payments, and performed various other activities. We received positive feedback from developers.

However, many people still faced difficulties with payment system integration - especially small merchants without development teams and business owners who outsource development. We thought, "Could AI-powered coding tools make Toss Payments integration easier?" We tried writing Toss Payments integration code, but found the generated code accuracy was poor.

While pondering how to solve this problem, we discovered MCP (Model Context Protocol) - a method to provide context information that AI models can understand. We decided to try using it.

---

## What is MCP?

[What is Model Context Protocol (MCP)? How it simplifies AI integrations compared to APIs | AI Agents That Work

Model Context Protocol (MCP) is an open standard that connects AI models to tools and data sources efficiently. This guide breaks down MCP's architecture, benefits, and how it differs from traditional APIs

norahsakal.com](https://norahsakal.com/blog/mcp-vs-api-model-context-protocol-explained/)

![](/images/868-Making-Payment-Integration-Easier-with-AI-Building-Toss-Payments-MCP-Server/img.png)

MCP is a standard method proposed by Anthropic that helps AI models (LLMs) better understand various situations and contexts. Just as USB created a standard for easily connecting computers and peripherals, MCP helps AI models naturally connect with various environments. Thanks to MCP, you can conveniently use various AI tools (like Cursor, Claude, Windsurf, etc.) from a single server. We're using MCP to create a "vibe coding" environment where developers can work more easily and enjoyably.

---

## Preparing Quality Content

The most important thing in MCP is delivering content that AI can understand well. But creating content individually for every product takes too much time and money. Fortunately, we already operated an MDX-based Developer Center with a structure deployed to CDN during the CI/CD process. We thought that if the MCP server accessed this content, it would naturally follow document version updates. Based on this, we quickly built a prototype by creating an llms.txt file that

LLMs could understand well. Frontend Chapter's Jiho Shin was particularly helpful in this process.

**llms.txt** is a proposed standard file that helps Large Language Models better understand and interact with website content. This file provides information about how LLMs should interact with a website's documents, codebase, etc., and is used to improve the efficiency of LLM-based tools and services.

*Reference: <https://llmstxt.org/>*

---

## Deciding on MCP Transport

Initially, we considered Remote MCP based on Websocket or SSE, but decided to implement a local-based MCP server.

The advantages we gained from using a local-based MCP server were:

- **SSOT (Single Source of Truth)** achieved by basing on Developer Center documents uploaded to CDN
- **No server costs** as it runs on each user's local device even as user numbers grow
- **STDIO Transport** exists in the MCP specification
- **No additional management costs** by deploying to NPM and using an already verified package manager

---

## First Version

We implemented a method to search documents based on predefined keywords from llms.txt.

### Tool List

The prototype supported 4 tools, and the LLM uses these tools to explore Toss Payments Developer Center documents:

1. **get-keywords**
2. **documents-by-keywords**
3. **documents-by-link**
4. **document-by-id**

### get-keywords

A tool that returns a predefined keyword list. The LLM looks at the retrieved keyword list, analyzes the user query, extracts appropriate keywords, and then calls docs-by-keywords.

### documents-by-keywords

When the LLM properly extracts and queries keywords, the MCP server traverses documents, calculates scores based on various conditions, and returns the top 10 documents.

### documents-by-link

A tool to explore documents based on links. When the LLM encounters documents expressed as Markdown links while exploring documents, it performs exploration.

### document-by-id

A tool to query documents based on IDs assigned within the MCP server. When finding documents matching user queries using get-keywords, documents-by-keywords, or documents-by-link tools, this tool queries the documents.

---

## Results and Review

The first version searched documents based on predefined keywords. However, in actual operation, the AI model often produced incorrect results (Hallucination) or missed important information. LLM call frequency also increased.

We suspected the cause was that document lengths varied greatly, with the longest exceeding 5,000 lines. Important information seemed to be lost during the process of LLMs querying such documents multiple times while creating checkpoints or summarizing conversations. We needed to think of a new method, so we discussed with our friends Gemini and GPT to explore other approaches.

---

## Second Version

While having many conversations with Gemini, we discovered the BM25 keyword and decided to switch to that method.

### What is BM25?

**BM25** stands for Best Matching 25, derived from the probabilistic information retrieval model Okapi BM25. This model works by measuring how relevant a specific document is to a given query.

**Basic Concepts:**

- The more frequently a query term appears in a document, the higher the relevance
- But terms appearing too frequently have their weight reduced (IDF: Inverse Document Frequency)
- Frequency impact is adjusted according to document length

**Use Cases:**

- **Search Engines:** Sorting documents or web pages most relevant to user queries
- **Document Recommendation Systems:** Measuring similarity between documents with similar content
- **RAG (Retrieval-Augmented Generation):** Pre-filtering stage for providing documents to LLMs

### Using BM25

JavaScript doesn't have a well-implemented BM25 like Python, so we quickly created one with GPT's help. However, we couldn't use that code directly due to Korean language characteristics.

For example, consider this sentence:

```
"BM25는 정보 검색에 사용되는 랭킹 함수입니다."
```

English-style tokenization produces:

```
["bm25는", "정보", "검색에", "사용되는", "랭킹", "함수입니다"]
```

**Problems That Occurred:**

- Not broken down into meaningful units
- Particles (는, 에) and endings (는, 다) included as-is, resulting in many duplicate and unnecessary tokens
- Sentences with the same meaning don't match depending on expression

To tokenize Korean sentences consistently and meaningfully, we needed a morphological analysis library. However, morphological analysis libraries require additional environment setup like Java or C, and we determined these external dependencies could degrade local MCP usability, so we excluded them. Fortunately, this problem could be solved in a simpler way.

In the MCP execution environment, the LLM is the decision-maker for everything. The LLM decides which tools to use and with what parameters to execute them; users only choose whether to call tools. By tokenizing user queries into meaningful forms through the LLM and applying regular expressions to these tokenized queries to calculate BM25 scores each time, we could effectively index documents similar to the question.

However, this method alone doesn't solve all problems. While the idea of applying BM25 to Korean-based documents was clear, the fundamental issue was that documents were large. Therefore, additional work was needed to cut documents into meaningful chunks.

---

## Creating Meaningful Chunks for Each Document

Since over-fragmenting chunks can lose important information, we improved by cutting documents based on Markdown headers (#, ##) and then calculating scores based on BM25.

Various libraries can parse Markdown, but I used three libraries - unist-util-visit, remark-parse, and unified - to convert Markdown into chunks.

### Process

1. Convert markdown to AST tree using unified and remark-parse:
2. `const tree = unified().use(remarkParse).parse(markdown);`
3. Traverse the tree using unist-util-visit:
4. `visit(tree, (node) => {
   if (node.type === "heading" && node.depth <= 2) {
   chunks.push(...)
   }
   ...
   });`

Through this process, we can cut each markdown document based on headers (#, ##).

Finally, we also merge chunks below a certain size, as chunks that are too small can lose meaningful information or become meaningless data.

```
export function joinShortChunks(chunks: string[], minWords = 30): string[] {
  const result: string[] = [];

  let buffer = "";
  let bufferCount = 0;

  for (const chunk of chunks) {
    const wc = chunk.split(/\s+/).length;
    if (wc < minWords) {
      buffer += (buffer ? "\n\n" : "") + chunk;
      bufferCount += wc;
      continue;
    }

    if (buffer) {
      result.push(buffer.trim());
      buffer = "";
      bufferCount = 0;
    }

    result.push(chunk.trim());
  }

  if (buffer) {
    result.push(buffer.trim());
  }

  return result;
}
```

---

## Applying Regular Expressions and Chunk Documents to BM25

Now we're ready. We prepare a Document class to manage chunks and a Calculator to convert user-entered keywords into regular expressions and calculate scores.

```
export class TossPaymentsDocument {
  private readonly chunks: DocumentChunk[] = [];

  constructor(
    private readonly keywordSet: Set<string>,
    private readonly remoteMarkdownDocument: RemoteMarkdownDocument,
    private readonly _version: string | undefined,
    public readonly id: number
  ) {
    remoteMarkdownDocument.chunks.forEach((chunk, index) => {
      this.chunks.push({
        id: this.id,
        chunkId: this.id * 1000 + index,
        originTitle: remoteMarkdownDocument.metadata.title,
        text: chunk,
        wordCount: chunk.split(/\s+/).length,
      });
    });
  }

  getChunkWithWindow(chunkId: number, windowSize: number): DocumentChunk[] {
    const chunkIndex = this.chunks.findIndex(
      (chunk) => chunk.chunkId === chunkId
    );
    if (chunkIndex === -1) {
      return [];
    }

    const start = Math.max(0, chunkIndex - windowSize);
    const end = Math.min(this.chunks.length, chunkIndex + windowSize + 1);

    return this.chunks.slice(start, end);
  }

  // Additional methods...
}
```

The BM25 Calculator implementation:

```
export class TossPaymentsBM25Calculator {
  private readonly allChunks: DocumentChunk[];
  private readonly totalCount: number;
  private readonly averageDocLength: number;
  private readonly N: number;

  constructor(
    private readonly documents: TossPaymentsDocument[],
    private readonly k1: number = 1.2,
    private readonly b: number = 0.75
  ) {
    this.allChunks = documents.flatMap((doc) => doc.getChunks());
    this.totalCount = this.allChunks.reduce(
      (count, doc) => count + doc.wordCount,
      0
    );
    this.averageDocLength = this.totalCount / this.allChunks.length;
    this.N = this.allChunks.length;
  }

  calculate(keywords: string): Result[] {
    const { termFrequencies, docFrequencies } =
      this.calculateFrequencies(keywords);

    const scores = this.calculateScore(termFrequencies, docFrequencies);

    scores.sort((a, b) =>
      b.score !== a.score ? b.score - a.score : b.totalTF - a.totalTF
    );

    return scores.map(({ id, score, chunkId }) => ({ id, chunkId, score }));
  }

  // Additional calculation methods...
}
```

You might wonder about the getChunkWithWindow function. Returning only a single chunk may provide insufficient context. While each chunk is divided by headers, answers to actual questions need to be delivered with adjacent content to convey complete meaning. To solve this, we use the getChunkWithWindow(chunkId, windowSize) method to bundle adjacent chunks around the chunk most similar to the query and deliver them to the LLM. This approach helps the LLM understand richer context, effectively reducing Hallucination and improving response accuracy.

---

## Final Tool List

- **get-v1-documents**
- **get-v2-documents**
- **document-by-id**

### get-v2-documents

This tool queries documents based on user-provided keywords and returns relevant chunks.

### get-v1-documents

Similar to get-v2-documents, but for V1 API documentation.

### document-by-id

A tool to query documents based on IDs assigned within the MCP server. The LLM calls this when it wants to explore a document in more detail from chunks retrieved by get-v1-documents and get-v2-documents.

---

## Implementation Review

In this implementation, we gained the following pros and cons:

**Pros:**

- Based on queries, we can comprehensively search related information with just one query by retrieving similar chunks
- While not as precise as Vector DB, it was useful in that we could implement a RAG system locally without external dependencies
- We confirmed the effect of reducing unnecessary information and decreasing Hallucination by targeting only information similar to queries

**Cons:**

- The first method had the advantage of less initial loading cost and memory usage because it accessed each document lazily, while the second method had the disadvantage of increased memory consumption and bootstrap costs by loading all documents included in the llms.txt file at startup

Based on this experience, we once again felt that choosing the appropriate method and strategy according to the situation is important.

---

## Testing Results: AI Coding Tools Combined with MCP

We needed to confirm what improvements occur when integrating the Toss Payments payment system using the developed MCP server. Our Technical Account Manager, who helps solve technical problems related to Toss Payments integration, conducted experiments under the following conditions:

### Test Conditions

1. **Cursor alone** (No Context)
2. **Cursor + Docs Context** combination
3. **Cursor + MCP** combination

### Prompt Used (Same prompt for all conditions)

```
Create payment widget integration using Toss Payments V2 SDK in index.html file. 
Use test_gck_xxxxxxxxx as the client key.
Create logic for the successUrl side too.
Call the approval API.
```

---

## Test Results Summary

### 1. Cursor Alone

In this case, even the most basic code like the JS SDK address that becomes the starting point of payment integration was not generated correctly. While it generated the basic flow of payment processing - authentication and approval flow - somewhat correctly, it failed to generate code that matched exact specifications and sometimes implemented some logic itself incorrectly.

### 2. Cursor + Docs Context

Despite providing additional context information, it couldn't accurately identify the JS SDK address. Ironically, even though additional information was provided compared to the Cursor-only use case, it showed implementation that violated the basic payment processing flow, such as calling the payment approval API on the client side (web screen). Also, the Secret Key that should absolutely never be exposed to clients was implemented to be exposed in client code.

### 3. Cursor + MCP

We confirmed that code was generated with:

- Client code generation
- Improved problem of not finding SDK address
- Code generation that exactly matches detailed integration specifications
- Code with no problems in the overall payment processing flow

In particular, we could confirm that it provides security-advantageous guidance while processing the "Call the approval API" prompt. (Output that Secret Key must be kept safe and not exposed externally, so the approval API must be called from the backend server)

---

## Conclusion

While directly implementing local-based MCP, we could experiment and think about many things. There are still many shortcomings and areas that clearly need improvement. For example, we could improve by adjusting BM25 scores based on weights for specific keywords, or separating development-related questions and tech blog documents (like Toss Payments blog) and categorizing them to distinguish tools. These items are already organized in the backlog and contain future development possibilities.

Since AI-generated code isn't 100% perfect, it won't immediately solve all difficulties, but we expect it will help reduce difficulties for more people as it develops. We hope this experience provides practical help to those with similar concerns. Thank you for reading this long post.

---

## Key Takeaway

By implementing an MCP server with BM25-based document chunking and retrieval, we improved AI code generation accuracy for payment integration from unreliable to production-ready, while maintaining zero server costs through local execution.

Reference:

<https://toss.tech/article/tosspayments-mcp>

[토스페이먼츠 결제 시스템 연동을 돕는 MCP 서버 구현기

AI 기반 코딩 도구를 활용해서 토스페이먼츠 결제 시스템을 쉽고 빠르게 연동할 수 있도록, MCP 서버를 구현한 과정과 인사이트를 공유합니다.

toss.tech](https://toss.tech/article/tosspayments-mcp)
