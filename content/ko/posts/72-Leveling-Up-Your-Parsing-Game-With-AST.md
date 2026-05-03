---
title: "Leveling Up Your Parsing Game With AST"
date: 2024-05-25T17:44:49+09:00
slug: "72-Leveling-Up-Your-Parsing-Game-With-AST"
original_url: "https://memoryhub.tistory.com/72"
tistory_id: 72
draft: false
---

![](/images/72-Leveling-Up-Your-Parsing-Game-With-AST/img.png)

> Being able to understand how something is abstracted away and why can make you a better programmer

## 용어

### Parse

- Resolve Component parts and describe their syntactic roles

### Tree

- Abstract data type that simulates hierarchical tree structure

### Parse Tree

- Every developer needs to make sure their code is understood by machines
- This is one of the underlying abstractions that allow the code that we write to become readable by computers.
- A pictorial version of the grammatical structure of a sentence.
- Gives a concrete idea of the syntax of the particular sentence.
- Used in pedagogy(study of teaching) to teach students how to identify parts of a sentence.

#### Sentence Diagramming (Sentence breaking into smallest parts) example

![](/images/72-Leveling-Up-Your-Parsing-Game-With-AST/img_1.png)

#### Code Diagramming

- All of our code can be simplified into sets of expressions.
- EX) Calculator program

SYNTAX

![](/images/72-Leveling-Up-Your-Parsing-Game-With-AST/img_2.png)

APPLIED

![](/images/72-Leveling-Up-Your-Parsing-Game-With-AST/img_3.png)

### AST (abstract syntax tree)

- A simplified, condensed parse tree / syntax tree
- contains info. related to analyzing source text
- ignores extra syntactic info. used in parsing text

## 출처

<https://www.geeksforgeeks.org/parse-tree-in-compiler-design/>

<https://medium.com/basecs/grammatically-rooting-oneself-with-parse-trees-ec9daeda7dad>

<https://medium.com/basecs/leveling-up-ones-parsing-game-with-asts-d7a6fc2400ff>
