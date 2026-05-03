---
title: "Architecting an Intuitive and Flexible RAG System"
date: 2025-10-24T23:46:57+09:00
slug: "871-Architecting-an-Intuitive-and-Flexible-RAG-System"
original_url: "https://memoryhub.tistory.com/871"
tistory_id: 871
draft: false
---

Interactive RAG System Design Guide

body {
font-family: 'Inter', sans-serif;
}
.chart-container {
position: relative;
width: 100%;
max-width: 600px;
margin-left: auto;
margin-right: auto;
height: 350px;
max-height: 400px;
}
.nav-tab.active {
background-color: white;
color: #4f46e5;
border-bottom: 2px solid #4f46e5;
}
.nav-tab:not(.active) {
background-color: #f3f4f6;
color: #4b5563;
}
.diagram-step {
cursor: pointer;
padding: 0.75rem 1.25rem;
border: 1px solid #d1d5db;
border-radius: 0.5rem;
background-color: #f9fafb;
transition: all 0.2s ease-in-out;
text-align: center;
font-weight: 500;
}
.diagram-step.active, .diagram-step:hover {
background-color: #eef2ff;
border-color: #4f46e5;
color: #4338ca;
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
.diagram-arrow {
display: flex;
align-items: center;
justify-content: center;
font-size: 1.5rem;
color: #9ca3af;
margin: 0.5rem 0;
}

An interactive guide to building flexible, easy-to-use RAG (Retrieval-Augmented Generation) applications.

Overview
Ingestion Pipeline
Query Pipeline
Tech Stack
Key Principles

This section provides a high-level overview of Retrieval-Augmented Generation (RAG). RAG is a technique that enhances the capabilities of Large Language Models (LLMs) by grounding them in external, up-to-date, or private information. Click on any step in the diagram below to learn more about its role in the overall architecture.

### Core RAG Architecture

1. Your Documents (Knowledge Base)↓2. Ingestion Pipeline (Indexing)↓3. Vector Database↕4. Query Pipeline (Retrieval & Generation)↓5. Final Answer

### Click a diagram step

Select a component from the architecture diagram to see its description here.

The Ingestion Pipeline is the foundation of your RAG system. Its job is to take raw documents and convert them into a structured, searchable format. This process runs "offline" before any user asks a question. Click the steps to see how to build a flexible and effective pipeline.

### Ingestion Pipeline Flow

1. Load Documents↓2. Chunk Documents↓3. Create Embeddings↓4. Store in Vector DB

### Click a diagram step

Select a component from the ingestion diagram to see its description here.

### Visualizing Embeddings

This chart conceptualizes how "Chunking" and "Embedding" work. The embedding model places chunks with similar meanings (e.g., about 'Topic A') close together in a high-dimensional space. We are showing a 2D simplification of that space.

The Query Pipeline is what happens in "real-time" when a user submits a question. This pipeline retrieves relevant information from your vector database and uses it to generate a factual, grounded answer. Click the steps to see this process in action.

### Query Pipeline Flow

1. User Query↓2. Embed Query↓3. Search Vector DB (Retrieval)↓4. Augment Prompt↓5. Generate Answer (LLM)

### Click a diagram step

Select a component from the query diagram to see its description here.

### Visualizing Retrieval

This chart demonstrates the "Search" step. The user's query (★) is embedded into the same space. The vector database finds the 'k' nearest document chunks (highlighted) to the query vector, retrieving the most relevant context.

To build a RAG system that is "easy to use, install, and flexible," choosing the right technologies is crucial. The modern ecosystem provides many lightweight, powerful libraries that are perfect for this. Below are key components and recommended, easy-to-use options.

#### Core Frameworks

These frameworks orchestrate the entire RAG pipeline, connecting all the other components.

- **LangChain:** A highly popular and flexible library for building LLM applications. Large community.
- **LlamaIndex:** A framework specifically focused on data ingestion and retrieval for RAG.

#### Flexibility: Document Loaders

To handle "any document," you need robust loaders. These libraries parse different file types.

- **Unstructured.io:** Excellent library for parsing complex files like PDFs, DOCX, PPTX, HTML, and more.
- **LangChain Loaders:** Has built-in document loaders for many common types (PDF, TXT, CSV, JSON).

#### Embedding Models

These models turn your text chunks into vectors. Choose small, effective, local models for ease of use.

- **SentenceTransformers:** A Python library to easily use embedding models.
  `all-MiniLM-L6-v2` is a great starting model.

#### Easy Install: Vector Stores

You need a database to store and search your vectors. "In-memory" or "local-first" databases are the easiest to install.

- **ChromaDB:** An open-source, local-first vector database. Very easy to get started with Python.
- **FAISS (by Meta):** A highly efficient vector search library. Can run fully in-memory.

#### Easy to Use: LLMs

The "G" in RAG. For ease of use, you can start with an API or a simple local server.

- **Ollama:** The easiest way to run open-source LLMs (like Llama 3) locally on your machine.
- **Gemini / OpenAI API:** Simple REST APIs to use powerful models without local setup, but requires an internet connection and API key.

#### User Interface

To make it "easy to use" for an end-user, you need a simple interface.

- **Streamlit / Gradio:** Python libraries that let you build simple web UIs with just a few lines of code.
- **FastAPI:** A Python library for building a clean, simple API that any frontend (like this HTML page) can talk to.

This section summarizes the key design principles discussed, helping you achieve a system that is simple, intuitive, effective, and flexible as requested.

### Simple & Easy to Install

- Use Python as the core language.
- Rely on lightweight, local-first libraries (ChromaDB, SentenceTransformers).
- Start with in-memory or file-based vector stores; avoid heavy database servers.
- Use Ollama for an all-in-one local LLM server.
- Use Streamlit or Gradio for a "quick and simple" UI.

### Intuitive & Easy to Use (for End-User)

- Design a minimal UI: a chat interface and a simple document uploader/manager.
- Provide clear feedback to the user (e.g., "Processing document...", "Generating answer...").
- (Advanced) Include citations in the answer, showing which document chunks were used.

### Effective (Accurate Answers)

- **Chunking is critical:** Experiment with chunk size and overlap. Too large, and the context is noisy. Too small, and context is missing.
- **Good Embedding Model:** A model like `all-MiniLM-L6-v2` is a good baseline, but domain-specific models can be better.
- **Prompt Engineering:** Your final prompt to the LLM is key. It must clearly instruct the model to answer \*only\* based on the provided context.
- **Retrieve enough context:** Don't just retrieve 1 chunk. Retrieving the top 3-5 chunks (`k=5`) is often more effective.

### Flexible (For Any Document)

- Use a powerful document loading library like `unstructured.io` to handle diverse file types (PDF, DOCX, HTML, etc.).
- Design your ingestion pipeline to be modular, so you can easily add new file parsers.
- Separate the "data" (your vector store) from the "application" so you can easily add, remove, and update your knowledge base.
document.addEventListener('DOMContentLoaded', () => {
const tabs = document.querySelectorAll('.nav-tab');
const tabContents = document.querySelectorAll('.tab-content');
tabs.forEach(tab => {
tab.addEventListener('click', () => {
const target = document.querySelector(tab.dataset.tabTarget);
tabContents.forEach(tc => tc.classList.add('hidden'));
target.classList.remove('hidden');
tabs.forEach(t => t.classList.remove('active'));
tab.classList.add('active');
});
});
const overviewData = {
'documents': {
title: '1. Your Documents',
text: 'This is the raw knowledge base you want your LLM to use. It can be any collection of files: PDFs, text files, Markdown, DOCX, etc. This is your "private" or "external" data.'
},
'ingestion': {
title: '2. Ingestion Pipeline (Indexing)',
text: 'This is an "offline" process. You run this pipeline once to prepare your documents. It loads, chunks, and converts your documents into a searchable format for the database.'
},
'vectordb': {
title: '3. Vector Database',
text: 'A special database designed to store and search "embeddings" (numerical representations of your text). It allows you to find document chunks based on semantic meaning, not just keywords.'
},
'query': {
title: '4. Query Pipeline (Retrieval & Generation)',
text: 'This is the "online" process that runs every time a user asks a question. It retrieves relevant context from the Vector DB and uses it to generate a factual answer.'
},
'answer': {
title: '5. Final Answer',
text: 'The LLM generates a final, "grounded" answer based \*only\* on the context provided by the retrieval step. This makes the answer more accurate and prevents hallucination.'
}
};
const ingestionData = {
'load': {
title: '1. Load Documents',
text: 'The first step is to load your files. To be "flexible," you should use libraries (like Unstructured.io or LangChain loaders) that can parse many file types (PDF, TXT, DOCX, etc.) into raw text.'
},
'chunk': {
title: '2. Chunk Documents',
text: 'You cannot embed an entire 100-page document at once. You must split the text into smaller, meaningful "chunks." A common, simple strategy is a fixed size (e.g., 1000 characters) with some overlap (e.g., 100 characters) to maintain context between chunks.'
},
'embed': {
title: '3. Create Embeddings',
text: 'Each text chunk is passed through an "embedding model" (like SentenceTransformers). This model converts the text into a numerical vector (a list of numbers) that represents its semantic meaning. This vector is what gets stored in the database.'
},
'store': {
title: '4. Store in Vector DB',
text: 'The embedding vector (and the original text chunk it came from) are stored in a Vector Database (like ChromaDB or FAISS). This database is optimized for finding "nearest neighbors" — i.e., finding vectors that are most similar to a new query vector.'
}
};
const queryData = {
'userquery': {
title: '1. User Query',
text: 'The process begins when the user asks a question, for example, "What were the key findings in the 2023 annual report?"'
},
'embedquery': {
title: '2. Embed Query',
text: 'The user\'s query is converted into a vector using the \*exact same\* embedding model that was used during ingestion. This ensures the query and the document chunks are in the same "semantic space".'
},
'search': {
title: '3. Search Vector DB (Retrieval)',
text: 'The database takes the query vector and performs a "k-Nearest Neighbors" (k-NN) search. It instantly finds the top \'k\' (e.g., k=5) document chunks whose vectors are mathematically closest to the query vector. This is the "retrieval" step.'
},
'augment': {
title: '4. Augment Prompt',
text: 'A new prompt is constructed for the LLM. It follows a template like: "Context: [Insert retrieved chunks here]. Question: [Insert user query here]. Answer the question based \*only\* on the provided context."'
},
'generate': {
title: '5. Generate Answer (LLM)',
text: 'This complete prompt (context + question) is sent to an LLM (like Llama 3 or Gemini). The LLM reads the context and generates an answer, which is now "grounded" in your documents, making it accurate and up-to-date.'
}
};
function initInteractiveDiagram(diagramSelector, contentSelector, data) {
const steps = document.querySelectorAll(`${diagramSelector} .diagram-step`);
const contentBox = document.querySelector(contentSelector);
contentBox.innerHTML = `
<h3 class="text-lg font-semibold text-indigo-700">Click a diagram step</h3>
<p class="text-gray-600">Select a component from the diagram to see its description here.</p>
`;
steps.forEach(step => {
step.addEventListener('click', () => {
const stepKey = step.dataset.diagramStep;
if (data[stepKey]) {
const stepData = data[stepKey];
contentBox.innerHTML = `
<h3 class="text-lg font-semibold text-indigo-700 mb-2">${stepData.title}</h3>
<p class="text-gray-700">${stepData.text}</p>
`;
steps.forEach(s => s.classList.remove('active'));
step.classList.add('active');
}
});
});
}
initInteractiveDiagram('#overview-diagram', '#overview-content', overviewData);
initInteractiveDiagram('#ingestion-diagram', '#ingestion-content', ingestionData);
initInteractiveDiagram('#query-diagram', '#query-content', queryData);
function createFakeScatterData() {
let data = [];
function createCluster(x, y, numPoints, label) {
for (let i = 0; i < numPoints; i++) {
data.push({
x: x + (Math.random() - 0.5) \* 15,
y: y + (Math.random() - 0.5) \* 15,
label: label
});
}
}
createCluster(20, 25, 30, 'Topic A');
createCluster(80, 75, 30, 'Topic B');
createCluster(25, 70, 30, 'Topic C');
return data;
}
const baseData = createFakeScatterData();
const queryPoint = { x: 50, y: 50 };
function findNearestNeighbors(data, point, k) {
const distances = data.map((d, index) => ({
index: index,
dist: Math.sqrt(Math.pow(d.x - point.x, 2) + Math.pow(d.y - point.y, 2))
}));
distances.sort((a, b) => a.dist - b.dist);
const neighbors = distances.slice(0, k).map(d => data[d.index]);
const lines = neighbors.map(n => ([{x: point.x, y: point.y}, {x: n.x, y: n.y}]));
return { neighbors, lines };
}
const { neighbors, lines } = findNearestNeighbors(baseData, queryPoint, 3);
const sharedChartOptions = {
responsive: true,
maintainAspectRatio: false,
plugins: {
legend: {
display: false
},
tooltip: {
callbacks: {
label: function(context) {
let label = context.dataset.label || '';
if (label) {
label += ': ';
}
const pointLabel = context.raw.label || 'Document Chunk';
return `${pointLabel}`;
}
}
}
},
scales: {
x: {
title: { display: true, text: 'Embedding Dimension 1' },
min: 0,
max: 100
},
y: {
title: { display: true, text: 'Embedding Dimension 2' },
min: 0,
max: 100
}
}
};
function renderEmbeddingChart() {
const ctx = document.getElementById('embeddingChart');
if (!ctx) return;
new Chart(ctx.getContext('2d'), {
type: 'scatter',
data: {
datasets: [
{
label: 'Document Chunks (Topic A)',
data: baseData.filter(d => d.label === 'Topic A'),
backgroundColor: 'rgba(59, 130, 246, 0.7)'
},
{
label: 'Document Chunks (Topic B)',
data: baseData.filter(d => d.label === 'Topic B'),
backgroundColor: 'rgba(16, 185, 129, 0.7)'
},
{
label: 'Document Chunks (Topic C)',
data: baseData.filter(d => d.label === 'Topic C'),
backgroundColor: 'rgba(239, 68, 68, 0.7)'
}
]
},
options: sharedChartOptions
});
}
function renderQueryChart() {
const ctx = document.getElementById('queryChart');
if (!ctx) return;
let lineDatasets = lines.map((line, i) => ({
type: 'line',
label: `Retrieval Line ${i}`,
data: line,
borderColor: 'rgba(234, 179, 8, 0.6)',
borderWidth: 2,
borderDash: [5, 5],
fill: false,
pointRadius: 0
}));
new Chart(ctx.getContext('2d'), {
data: {
datasets: [
{
type: 'scatter',
label: 'Document Chunks (Topic A)',
data: baseData.filter(d => d.label === 'Topic A'),
backgroundColor: 'rgba(59, 130, 246, 0.3)'
},
{
type: 'scatter',
label: 'Document Chunks (Topic B)',
data: baseData.filter(d => d.label === 'Topic B'),
backgroundColor: 'rgba(16, 185, 129, 0.3)'
},
{
type: 'scatter',
label: 'Document Chunks (Topic C)',
data: baseData.filter(d => d.label === 'Topic C'),
backgroundColor: 'rgba(239, 68, 68, 0.3)'
},
{
type: 'scatter',
label: 'Retrieved Chunks',
data: neighbors,
backgroundColor: 'rgba(234, 179, 8, 1)',
pointRadius: 6,
pointBorderColor: '#fff',
pointBorderWidth: 2,
},
{
type: 'scatter',
label: 'User Query',
data: [queryPoint],
backgroundColor: 'rgba(139, 92, 246, 1)',
pointStyle: 'star',
pointRadius: 10,
pointBorderColor: '#fff',
pointBorderWidth: 2,
},
...lineDatasets
]
},
options: sharedChartOptions
});
}
renderEmbeddingChart();
renderQueryChart();
});
