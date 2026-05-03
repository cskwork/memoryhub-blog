---
title: "RAG (Retrieval-Augmented Generation) and the Magic of Contextual Retrieval"
date: 2024-11-04T12:34:57+09:00
slug: "357-RAG-Retrieval-Augmented-Generation-와-문맥-검색의-마법"
original_url: "https://memoryhub.tistory.com/357"
tistory_id: 357
draft: false
categories: ["Dev Database"]
tags: ["RAG"]
---

Hello! Today, we'll explore RAG and contextual retrieval, methods that help AI find and understand information more intelligently.

## What is RAG?

RAG is like a library librarian!

- A librarian (RAG) searches through vast collections of books (knowledge base)
- Finds content related to your question
- Passes it to AI - a smart system!

### How It Works

1. **Breaking Down Knowledge**

   - Divide long documents into small chunks
   - Like dividing a book into chapters and sections!
2. **Vector Conversion**

   - Convert text into numbers (embedding)
   - Like expressing a book's content as coordinates!
3. **Search and Usage**

   - When a question comes in, find related content
   - Pass to AI to generate answers

## What Are the Problems with Traditional RAG?

```
Example Situation:
Q: "What was ACME company's Q2 2023 revenue growth rate?"
A: "The company's revenue increased 3% compared to the previous quarter."
```

- With just this answer, you can't tell **which company**
- Or **when** the data is from!
- This is called "context loss"

## Solving with Contextual Retrieval!

### What is Contextual Retrieval?

A magical technique that adds **background information** to information chunks!

```
Before: "The company's revenue increased 3% compared to the previous quarter."

After: "This content is excerpted from ACME company's Q2 2023 performance report.
Previous quarter's revenue was $314 million.
The company's revenue increased 3% compared to the previous quarter."
```

### Advantages

1. **Improved Accuracy**

   - 49% reduction in search failures
   - 67% reduction when reranking is applied
2. **Smarter Answers**

   - Understands all necessary context
   - Enables accurate and specific answers
3. **Cost-Effective**

   - Leverage Claude's prompt caching
   - Process for approximately $1.02 per million tokens

## Real-World Usage Examples

```
# Adding context
original = "Revenue increased 3%."
with_context = """
This content is from ACME's 2023 Q2 report.
Previous quarter's revenue: $314 million
Current content: Revenue increased 3%.
"""
```

## Considerations for Implementation

1. **Set Chunk Size**

   - Too large: processing inefficiency
   - Too small: insufficient context
2. **Choose Embedding Model**

   - Recommend Gemini or Voyage
   - Need to select model suited to use case
3. **Customize Contextualization**

   - Add industry or field-specific
   - Special terminology and background

## Conclusion

Contextual retrieval is an innovative technology that helps AI provide more accurate and useful answers. It's like giving AI glasses—enabling it to see information more clearly!

---

If you have any more questions, please leave a comment!
