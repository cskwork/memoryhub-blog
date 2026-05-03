---
title: "A categorized list of all Java and JVM features since JDK 8 to 21"
date: 2024-06-07T13:49:31+09:00
slug: "204-A-categorized-list-of-all-Java-and-JVM-features-since-JDK-8-to-21"
original_url: "https://memoryhub.tistory.com/204"
tistory_id: 204
draft: false
---

*The information from the requested webpage can be organized by Java version and feature categories.*

Here's a structured summary:

### Java and JVM Features (JDK 8 to 21)

#### **JDK 8**

- **Language**
  - Lambda Expressions: Introduce functional programming with concise syntax.
  - Method References: Provide easy-to-read method pointers.
  - Default Methods: Allow interfaces to have methods with implementations.
- **Libraries**
  - Stream API: Facilitate functional-style operations on collections.
  - Optional Class: Handle nullability more gracefully.
  - New Date-Time API: Replace the outdated java.util.Date and Calendar.
- **JVM**
  - PermGen Removal: Eliminate the permanent generation memory space.

#### **JDK 9**

- **Language**
  - Private Interface Methods: Enable sharing code among non-abstract methods.
- **Libraries**
  - Module System (Project Jigsaw): Introduce modularity to the Java platform.
  - JShell (REPL): Provide an interactive tool to evaluate expressions.
- **JVM**
  - Ahead-of-Time Compilation: Precompile bytecode into native code.
  - Garbage Collector Interface: Improve flexibility for different garbage collectors.

#### **JDK 10**

- **Language**
  - Local-Variable Type Inference (var): Simplify variable declarations.
- **Libraries**
  - Collectors.toUnmodifiableList: Create unmodifiable lists from streams.
- **JVM**
  - Application Class-Data Sharing: Improve startup performance and memory footprint.

#### **JDK 11**

- **Language**
  - Local-Variable Syntax for Lambda Parameters: Allow var in lambda parameters.
- **Libraries**
  - HttpClient API: Modernize HTTP communication.
  - String Methods (lines, strip, etc.): Enhance string processing capabilities.
- **JVM**
  - Epsilon: A No-Op Garbage Collector for performance testing.

#### **JDK 12**

- **Language**
  - Switch Expressions (Preview): Simplify and extend switch statements.
- **Libraries**
  - Compact Number Formatting: Format numbers in a compact, human-readable form.
- **JVM**
  - Shenandoah Garbage Collector: Reduce GC pause times.

#### **JDK 13**

- **Language**
  - Text Blocks (Preview): Simplify multi-line string literals.
- **Libraries**
  - Reimplementation of the Legacy Socket API: Improve maintainability and performance.
- **JVM**
  - Dynamic CDS Archives: Improve class-data sharing at runtime.

#### **JDK 14**

- **Language**
  - Records (Preview): Provide a compact syntax for data carrier classes.
  - Pattern Matching for instanceof (Preview): Simplify type checks and casts.
- **Libraries**
  - Helpful NullPointerExceptions: Improve debugging with better exception messages.
- **JVM**
  - NUMA-Aware Memory Allocation: Optimize memory allocation for NUMA systems.

#### **JDK 15**

- **Language**
  - Sealed Classes (Preview): Restrict which classes can extend or implement them.
- **Libraries**
  - Hidden Classes: Support frameworks that generate classes at runtime.
- **JVM**
  - ZGC: A Scalable Low-Latency GC: Improve performance and scalability.

#### **JDK 16**

- **Language**
  - Records: Finalize the compact data carrier class feature.
  - Pattern Matching for instanceof: Simplify type checks and casts.
- **Libraries**
  - Vector API (Incubator): Provide SIMD programming capabilities.
- **JVM**
  - Concurrent Thread-Stack Processing for ZGC: Improve garbage collection efficiency.

#### **JDK 17**

- **Language**
  - Sealed Classes: Finalize the feature to restrict class hierarchies.
- **Libraries**
  - Enhanced Pseudo-Random Number Generators: Offer better random number generation.
- **JVM**
  - Context-Specific Deserialization Filters: Improve security during deserialization.

#### **JDK 18**

- **Language**
  - UTF-8 by Default: Set UTF-8 as the default charset.
- **Libraries**
  - Simple Web Server: Provide a minimal web server for prototyping.
- **JVM**
  - Vector API (Second Incubator): Continue development of SIMD programming.

#### **JDK 19**

- **Language**
  - Pattern Matching for switch (Preview): Enhance switch statements with pattern matching.
- **Libraries**
  - Foreign Function & Memory API (Preview): Interoperate with native code and memory.
- **JVM**
  - Virtual Threads (Preview): Simplify concurrency with lightweight threads.

#### **JDK 20**

- **Language**
  - Record Patterns (Preview): Enable pattern matching for record types.
- **Libraries**
  - Scoped Values (Incubator): Facilitate safe, efficient access to variables.
- **JVM**
  - Generational ZGC: Introduce generational support in ZGC.

#### **JDK 21**

- **Language**
  - String Templates (Preview): Simplify string formatting and embedding expressions.
- **Libraries**
  - Sequenced Collections: Introduce new collection interfaces for sequence handling.
- **JVM**
  - Unnamed Patterns and Variables (Preview): Enhance pattern matching flexibility.

For more detailed information, visit [A categorized list of all Java and JVM features since JDK 8 to 21](https://advancedweb.hu/a-categorized-list-of-all-java-and-jvm-features-since-jdk-8-to-21/).
