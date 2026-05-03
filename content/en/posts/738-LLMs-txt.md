---
title: "LLMs.txt"
date: 2025-08-05T07:23:03+09:00
slug: "738-LLMs-txt"
original_url: "https://memoryhub.tistory.com/738"
tistory_id: 738
draft: false
---

## 1. What is LLMs.txt?

- **Definition** – LLMs.txt is a simple Markdown file placed at the root of a website (/llms.txt) that helps AI language models easily and accurately understand the content of a site, functioning as an **AI-specific sitemap**. Like robots.txt for search engines, it provides concisely structured information for LLMs.
- **Necessity** – LLMs struggle to read complex web pages with HTML, JavaScript and other elements. llms.txt summarizes the site's purpose, structure, and key documents, enabling efficient use of the LLM's context window.

## 2. LLMs.txt File Structure

llms.txt must use Markdown format and include the following elements:

1. **H1 Title** – Begin the first line with the site or project name using #.
2. **Summary Block (Blockquote)** – Use > symbol to provide a brief introduction to the site. Write concisely with only essential information.
3. **Detailed Information** – Provide important notes, features, usage guidelines and other additional information in paragraph or list format.
4. **Links List Section** – Use ## heading to organize related resource lists. Each item is formatted as [Link Title](URL): brief description.
5. **Optional Section** – Less important information goes in ## Optional section. LLMs may skip this section.

## 3. Tips to Consider When Writing

- **Conciseness and clarity** – Avoid unnecessary terminology and select only core information.
- **Link descriptions** – Attach brief descriptions to each link so LLMs understand the document's purpose.
- **Testing** – After writing, test with LLMs like Claude or GPT to verify it works correctly.

## 4. Practical LLMs.txt Example: Korean Civil Act

Below is an example that a website about civil law could post at /llms.txt. In practice, civil law articles should be written as Markdown .md files and linked.

> **Note** – Explanations and article information about civil law reference Wikipedia's "Civil Code of the Republic of Korea" document.

```
# Korean Civil Act

> The Korean Civil Act (Law No. 471, 1958) is one of three fundamental laws of the Republic of Korea alongside criminal law and constitutional law. The Civil Act consists of five parts: General Provisions, Property Rights, Claims, Relatives, and Inheritance, establishing the basic norms of civil relations. This file guides important articles of the Civil Act and reference documents.

Important Matters:
- **Article 1 (Sources of Law)** – When there is no civil law, customary law applies; when there is no customary law, legal principles (rational reasoning) apply. This is the "sources of law" provision.
- **Article 2 (Good Faith and Honest Dealing)** – The exercise of rights and performance of duties must be done in good faith and honestly, and the abuse of rights is prohibited.
- **Article 303 (Jeonse Right)** – The jeonse right regulated in the Property Rights section is the right to use and enjoy another's real estate by paying a deposit.
- **Article 750 (Tort Liability)** – A person who causes damage to another intentionally or negligently is liable for damages.

## Parts of the Civil Act
- [General Provisions](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_1:_General_Provisions): Basic provisions including types of sources of law, natural persons and juridical persons, things, legal acts, periods, and extinctive prescription.
- [Property Rights](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_2:_Property_Rights): Regulates nine property rights including ownership, possession, jeonse right, pledge, and mortgage. Changes in real property rights become effective through registration.
- [Claims](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_3:_Claims): Regulates claim relationships including contracts, agency, unjust enrichment, and torts. Article 750 stipulates liability for damages from torts.
- [Relatives](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_4:_Relatives): Provides for marriage, parent-child relationships, guardianship, and family scope. The 2005 amendment abolished the patriarchal family system (hojuze).
- [Inheritance](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_5._Inheritance): Governs commencement of inheritance, heirs, wills, and reserved portions.

## Optional
- [Full Civil Act Translation (Unofficial)](https://example.com/civil-act-en.md): English translation that may not reflect the latest amendments.
- [Explanation of Good Faith Principle](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_1:_General_Provisions): Explanation of Article 2 Good Faith Principle.
```

By creating llms.txt as shown above and deploying it at the site root, LLM-based search tools and chatbots can reference it when summarizing civil law or answering questions about specific articles. If each part of the Civil Act is provided as a Markdown .md file, AI can directly read and analyze the content. Therefore, linked documents should be kept as simple and clear as possible.

## 5. Practical Usage

1. **Document Preparation** – Organize summary information and each article in Markdown files. For example, organize general provisions content in a general-provisions.md file.
2. **Write llms.txt** – Create an llms.txt file including summary, important articles, and link list as shown in the example above.
3. **Deploy at Server Root** – Upload llms.txt to the website root (/) and also deploy the linked .md files on the same domain.
4. **Testing** – Load <https://example.com/llms.txt> in an LLM like Claude or ChatGPT, then test with questions like "Explain Article 2 Good Faith Principle" to verify it works as intended.

Through this process, LLMs can easily understand laws and technical documents, allowing you to provide more accurate answers to users.
