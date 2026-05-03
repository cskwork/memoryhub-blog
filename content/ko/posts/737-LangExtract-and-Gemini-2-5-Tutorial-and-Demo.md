---
title: "LangExtract and Gemini 2.5 – Tutorial and Demo"
date: 2025-08-05T07:21:24+09:00
slug: "737-LangExtract-and-Gemini-2-5-Tutorial-and-Demo"
original_url: "https://memoryhub.tistory.com/737"
tistory_id: 737
draft: false
---

## Introduction

**LangExtract** is a Python library from Google designed to turn unstructured text (e.g., clinical notes, news stories or long reports) into **structured, grounded information**. It is built on top of large language models (LLMs) but addresses some of their weaknesses. In particular, LangExtract ensures that every extraction is tied back to the exact character offsets in the source document for traceability[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=information%20extraction%3A), enforces a consistent output schema via few‑shot prompts[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=,analysis%20of%20Romeo%20and%20Juliet) and uses a chunking and multi‑pass strategy to maintain high recall on long documents[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=%2A%20Optimized%20long,passes%20over%20smaller%2C%20focused%20contexts). The library is open source[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=Today%2C%20we%27re%20excited%20to%20introduce,ensuring%20both%20flexibility%20and%20traceability) and supports both cloud‑hosted models (such as Google’s Gemini family) and local LLMs through Ollama[raw.githubusercontent.com](https://raw.githubusercontent.com/google/langextract/main/README.md#:~:text=5.%20%20,in%20Ollama%20interface). It can also generate an interactive HTML visualization to explore extracted entities[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=,for%20exploring%20thousands%20of%20annotations).

**Gemini 2.5** is Google’s “thinking” model family introduced in 2025. It builds on the multimodal, long‑context Gemini architecture but adds an internal reasoning process: before responding, the model can reason through its thought steps, leading to enhanced performance on complex tasks[blog.google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/#:~:text=Now%2C%20with%20Gemini%202,aware%20agents). The 2.5 family includes:

- **Gemini 2.5 Pro** – a state‑of‑the‑art model for complex tasks. In early benchmarks it topped the LMArena human‑preference leaderboard and excelled in coding, math and science tasks[blog.google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/#:~:text=Introducing%20Gemini%202). The Pro model offers a 1‑million‑token context window (with 2 million coming soon)[blog.google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/#:~:text=Gemini%202,audio%2C%20images%2C%20video%20and%20even) and is available to developers in Google AI Studio and the Gemini app[blog.google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/#:~:text=Gemini%202,limits%20for%20scaled%20production%20use).
- **Gemini 2.5 Flash** – a fast, cost‑effective model for high throughput tasks. It is now generally available with pricing designed for production workloads[developers.googleblog.com](https://developers.googleblog.com/en/gemini-2-5-thinking-model-updates/#:~:text=Over%20the%20last%20year%2C%20our,which%20led%20to%20developer%20confusion).
- **Gemini 2.5 Flash‑Lite** – an even lower‑latency version introduced in preview. Flash‑Lite is designed for classification and summarization tasks at scale. It offers dynamic control of the **“thinking” budget** via an API parameter and has lower latency with better performance than earlier Flash models[developers.googleblog.com](https://developers.googleblog.com/en/gemini-2-5-thinking-model-updates/#:~:text=Introducing%20Gemini%202.5%20Flash).

All 2.5 models are **thinking models** that allow developers to choose how much reasoning the model does before generating an answer[developers.googleblog.com](https://developers.googleblog.com/en/gemini-2-5-thinking-model-updates/#:~:text=Gemini%202,%E2%80%9Cthinks%E2%80%9D%20before%20generating%20a%20response). This ability enables tasks requiring more reliability or deeper reasoning but also introduces cost/latency trade‑offs.

## Why use LangExtract with Gemini 2.5?

LangExtract’s design complements the capabilities of Gemini 2.5 models:

- **Reliable structured outputs** – LangExtract enforces a user‑defined schema via its data representation and few‑shot examples[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=,analysis%20of%20Romeo%20and%20Juliet). Gemini’s controlled generation features ensure the model follows the schema precisely, reducing “schema drift.”
- **Precise grounding and traceability** – each entity extracted by LangExtract is linked back to the source text offsets[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=information%20extraction%3A), which is crucial for auditing in sensitive domains. Gemini’s long context window (up to 1 million tokens) allows processing of very long documents without losing context[blog.google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/#:~:text=Gemini%202,audio%2C%20images%2C%20video%20and%20even).
- **Optimized long‑document extraction** – LangExtract uses chunking, parallel processing and multi‑pass extraction to maintain high recall[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=%2A%20Optimized%20long,passes%20over%20smaller%2C%20focused%20contexts). Combined with Gemini’s large context, this strategy yields high‑quality extractions even from novels or lengthy reports[raw.githubusercontent.com](https://raw.githubusercontent.com/google/langextract/main/README.md#:~:text=).
- **Interactive visualization** – results can be saved as .jsonl and visualized as an interactive HTML file[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=,for%20exploring%20thousands%20of%20annotations).
- **Flexible deployment** – you can switch between Gemini 2.5 Pro, Flash or Flash‑Lite depending on the task. LangExtract’s API exposes the model\_id parameter to choose the model (e.g. gemini-2.5-flash for speed or gemini-2.5-pro for deeper reasoning)[raw.githubusercontent.com](https://raw.githubusercontent.com/google/langextract/main/README.md#:~:text=model_id%3D%22gemini).

## Installation and Setup

LangExtract is available on PyPI and can be installed with pip:

```
pip install langextract
```

For isolated environments, create a virtual environment and install the library inside it[raw.githubusercontent.com](https://raw.githubusercontent.com/google/langextract/main/README.md#:~:text=). If you plan to use cloud‑hosted Gemini models, you’ll need an API key. Obtain a key from Google AI Studio or Vertex AI and set the LANGEXTRACT\_API\_KEY environment variable:

```
export LANGEXTRACT_API_KEY="<YOUR-GEMINI-API-KEY>"
```

Alternatively, create a .env file and add LANGEXTRACT\_API\_KEY=<your-key>[raw.githubusercontent.com](https://raw.githubusercontent.com/google/langextract/main/README.md#:~:text=). LangExtract will read this automatically when you run your script.

### Choosing a model

When calling lx.extract you must specify a model\_id. The LangExtract README recommends gemini-2.5-flash as a balanced default and gemini-2.5-pro for more complex tasks[raw.githubusercontent.com](https://raw.githubusercontent.com/google/langextract/main/README.md#:~:text=model_id%3D%22gemini). You can also use gemini-2.5-flash-lite (preview) for fast classification/summarization[developers.googleblog.com](https://developers.googleblog.com/en/gemini-2-5-thinking-model-updates/#:~:text=Introducing%20Gemini%202.5%20Flash). For local inference, LangExtract includes support for **Ollama**, allowing you to run open‑source models on your own machine without an API key[raw.githubusercontent.com](https://raw.githubusercontent.com/google/langextract/main/README.md#:~:text=When%20using%20LangExtract%20with%20cloud,by%20updating%20the%20inference%20endpoints).

## Tutorial: Extracting structured information from unstructured text

The core workflow in LangExtract consists of three steps:

1. **Define the extraction task** – Write a concise prompt describing what you want to extract. Provide at least one high‑quality example showing the desired output schema[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=Next%2C%20define%20your%20extraction%20task,example%20to%20guide%20the%20model). The example guides the model to follow your schema.
2. **Run the extraction** – Use lx.extract to process your input text (or list of documents). Specify the prompt, examples, and model\_id[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=,pro%22%2C). LangExtract will call the underlying LLM (Gemini) and return a result object containing the entities.
3. **Save and visualize** – Save the result to a JSONL file using lx.io.save\_annotated\_documents, then create an interactive HTML file with lx.visualize[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=The%20result%20object%20contains%20the,file%2C%20viewable%20from%20your%20browser).

### Step‑by‑Step code example

Below is a complete Python example that extracts information about companies, financial metrics and market sentiment from a short news snippet. The code follows the hands‑on example from the ADaSci tutorial[adasci.org](https://adasci.org/information-extraction-through-googles-langextract/#:~:text=Hands).

```
import os
import textwrap
import langextract as lx

# 1. Define your extraction prompt
prompt = textwrap.dedent(
    """
    Extract the company name, specific financial metrics, and market sentiment from the text.
    Use exact text for extractions. Do not paraphrase or overlap entities.
    Provide meaningful attributes for each entity to add context.
      - For companies, include the stock ticker.
      - For financial metrics, specify the type and value.
      - For market sentiment, classify it as 'bullish', 'bearish', or 'neutral'.
    """
)

# 2. Provide a few-shot example
examples = [
    lx.data.ExampleData(
        text=(
            "AlphaTech (AT) announced a quarterly profit of $2.5 billion, "
            "exceeding analyst expectations and signaling a strongly bullish trend for the sector."
        ),
        extractions=[
            lx.data.Extraction(
                extraction_class="company",
                extraction_text="AlphaTech",
                attributes={"stock_ticker": "AT"},
            ),
            lx.data.Extraction(
                extraction_class="financial_metric",
                extraction_text="quarterly profit of $2.5 billion",
                attributes={"metric_type": "profit", "value": "$2.5 billion"},
            ),
            lx.data.Extraction(
                extraction_class="market_sentiment",
                extraction_text="strongly bullish trend",
                attributes={"sentiment": "bullish"},
            ),
        ],
    )
]

# 3. Input text to process
input_text = (
    "Global Dynamics Inc. (GDI) reported a staggering quarterly revenue of $15 billion, "
    "but its stock dipped 2%, leading to a neutral but cautious market outlook."
)

# 4. Run the extraction (change model_id as needed)
result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt,
    examples=examples,
    model_id="gemini-2.5-pro",  # or 'gemini-2.5-flash' for faster but cheaper inference
)

# 5. Save results and visualize
lx.io.save_annotated_documents([result], output_name="extraction_results.jsonl")

html_content = lx.visualize("extraction_results.jsonl")
with open("visualization.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Extraction completed and visualization.html generated.")
```

**What this code does:**

1. It installs LangExtract (not shown) and defines the prompt to extract companies, financial metrics and market sentiment.
2. It provides a **few‑shot example** that illustrates the expected output schema[adasci.org](https://adasci.org/information-extraction-through-googles-langextract/#:~:text=examples%20%3D%20,). The example contains three extraction objects: a company with a stock ticker, a financial metric with its type and value, and a market sentiment classification.
3. It defines the input text about **Global Dynamics Inc.** and calls lx.extract with model\_id="gemini-2.5-pro" to leverage the deeper reasoning of the Pro model.
4. It saves the result to a JSONL file and generates an interactive visualization.

### Scaling to long documents

To process longer documents – such as entire novels or large reports – LangExtract can download text directly from URLs and run multiple extraction passes. For example, processing the full text of Romeo and Juliet (over 147,000 characters) is as simple as:

```
result = lx.extract(
    text_or_documents="https://www.gutenberg.org/files/1513/1513-0.txt",
    prompt_description=prompt,
    examples=examples,
    model_id="gemini-2.5-flash",
    extraction_passes=3,  # 여러 번의 패스로 재현율 향상
    max_workers=20,  # 병렬 처리로 속도 향상
    max_char_buffer=1000  # 더 작은 컨텍스트로 정확도 향상
)
```

This approach uses chunking and multi‑pass processing to maintain high recall [raw.githubusercontent.com](https://raw.githubusercontent.com/google/langextract/main/README.md#:~:text=) and can extract hundreds of entities in a few minutes.

### Visualization and exploration

After extraction, use lx.visualize to produce a self‑contained HTML file. The visualization highlights each extraction in the original text and allows interactive browsing of thousands of annotations [developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=,for%20exploring%20thousands%20of%20annotations). The HTML file can be opened locally or embedded in a web app.

## Demo Project Idea: Structured Analysis of Earnings Reports

To illustrate how LangExtract and Gemini 2.5 can be used in a real‑world scenario, consider building a **structured analysis tool for quarterly earnings reports**.

### Project overview

1. **Data collection** – Fetch unstructured earnings call transcripts or press releases from a company’s investor relations site.
2. **Define extraction schema** – Identify the key pieces of information you want to extract, such as:
   - Company name and stock ticker.
   - Financial metrics (revenue, net income, EPS) with their values.
   - Forward‑looking statements (e.g., guidance).
   - Market sentiment expressed by executives or analysts.
3. **Create few‑shot examples** – For each entity type, prepare short segments of text with annotated extractions. Use LangExtract’s ExampleData and Extraction classes to define the examples.
4. **Write a prompt** – In natural language, instruct the model to extract the desired entities, enforce non‑overlapping spans, and produce attributes like metric type and sentiment.
5. **Run extraction** – Use lx.extract with model\_id set to gemini-2.5-flash for fast throughput, or gemini-2.5-pro when higher reasoning is required. If processing dozens of reports, run multi‑pass extraction and parallel workers to improve recall.
6. **Store and analyze** – Save the extractions in JSONL or convert to a relational database. Use the interactive HTML to audit results and adjust the prompt/examples as needed. Downstream, the structured data can power dashboards, financial models or RAG (Retrieval‑Augmented Generation) systems.

### Implementation tips

- **Balance cost and quality** – Use Flash or Flash‑Lite for high‑volume extraction where speed and cost are paramount. Switch to Pro for complex tasks that require deeper reasoning or code generation[developers.googleblog.com](https://developers.googleblog.com/en/gemini-2-5-thinking-model-updates/#:~:text=Over%20the%20last%20year%2C%20our,which%20led%20to%20developer%20confusion).
- **Iteratively refine the prompt** – Start with a simple prompt and one or two examples. Evaluate the output via the visualization and add more examples or clarify instructions to handle edge cases. Avoid paraphrasing or overlapping entities as LangExtract enforces exact spans[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=Extract%20characters%2C%20emotions%2C%20and%20relationships,each%20entity%20to%20add%20context).
- **Leverage Gemini’s world knowledge carefully** – LangExtract can optionally use the model’s world knowledge to infer attributes not explicitly in the text[developers.googleblog.com](https://developers.googleblog.com/en/introducing-langextract-a-gemini-powered-information-extraction-library/#:~:text=,chosen%20LLM%27s%20capabilities%20and%20the). Use this feature judiciously and include clear guidance in your prompt.
- **Monitor model versions** – Gemini models have defined retirement dates and pricing tiers[raw.githubusercontent.com](https://raw.githubusercontent.com/google/langextract/main/README.md#:~:text=%3E%20,latest%20stable%20and%20legacy%20versions). Check the official model version documentation to stay up to date and adjust model\_id accordingly.

## Conclusion

LangExtract offers developers a powerful, reproducible pipeline to extract grounded, structured data from unstructured text. When paired with Google’s Gemini 2.5 models, it combines schema‑driven extraction with advanced reasoning capabilities and a massive context window. Whether you’re analyzing literary works, medical reports or financial documents, LangExtract and Gemini 2.5 allow you to define custom extraction tasks, process long documents efficiently, and produce interactive visualizations for auditing and presentation.

By following the tutorial and demo project outlined above, you can build your own information‑extraction application using the latest tools available. Adjust the prompt and examples to your specific domain, choose the appropriate Gemini model for your workload, and let LangExtract transform wall‑of‑text into actionable insights.
