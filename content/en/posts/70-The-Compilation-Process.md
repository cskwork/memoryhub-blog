---
title: "The Compilation Process"
date: 2024-05-25T17:43:12+09:00
slug: "70-The-Compilation-Process"
original_url: "https://memoryhub.tistory.com/70"
tistory_id: 70
draft: false
categories: ["Dev Concepts"]
tags: ["Theory Notes"]
  hidden: false
cover:
  image: "/images/70-The-Compilation-Process/img.png"
  relative: false
  hidden: false
---

### Source Code

- Parsing step (scanned, split up, grouped) aka. lexical (isolation from the sentence containing it) analysis. (grammar or meaning of text not taken into context. Just the meaning of the words themselves)

### Lexical Analysis phase

1 Scans code

- Source text is considered as a chunk of string text.
- Scanner reads the text one character at a time.
- For each character, it marks the line and position of where the character was found in source text.

2 Evaluates (lexing/tokenization)

- The lexer/tokenizer determines what type of token it has found

![](/images/70-The-Compilation-Process/img.png)

#### Example of how compiler lexes a phrase

![](/images/70-The-Compilation-Process/img_1.png)

#### token

- Represented as a pair consisting of a token name and some (optional) value

#### lexemes

- Words of a program
- Substring of source code.
- Grouping of smallest sequence of characters.

![](/images/70-The-Compilation-Process/img_2.png)

### Sources

<https://medium.com/basecs/reading-code-right-with-some-help-from-the-lexer-63d0be3d21d>
