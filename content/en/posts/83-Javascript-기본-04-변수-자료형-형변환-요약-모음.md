---
title: "JavaScript Fundamentals 04 - Variables, Data Types, Type Conversion Summary"
date: 2024-05-25T17:57:24+09:00
slug: "83-Javascript-기본-04-변수-자료형-형변환-요약-모음"
original_url: "https://memoryhub.tistory.com/83"
tistory_id: 83
draft: false
---

## Variables and Constants Summary

You can declare variables using var, let, and const. Declared variables can store data.

- let – Modern variable declaration keyword.
- var – Older variable declaration keyword. Not commonly used (global variable).
- const – Similar to let, but the variable's value cannot be changed.

Variable names should clearly indicate what the variable contains.

<https://ko.javascript.info/variables>

## Data Types Summary

JavaScript has eight basic data types.

- Number – Used to represent integers, floating-point numbers, and other numerics. Integer limit is ±2^53.
- bigint – Represent integers without length constraints.
- String – Used for empty strings or strings made of characters. No separate type for single characters.
- Boolean – Used for true and false.
- null – Independent data type for null value alone. null represents an unknown value.
- undefined – Independent data type for undefined value alone. undefined represents an unassigned value.
- Object – Used to express complex data structures.
- Symbol – Used to create unique identifiers for objects.

The typeof operator tells you the data type of an operand.

- Used as typeof x or typeof(x).
- Returns the operand's data type as a string.
- typeof null is "object", which is a language error. null is not an object.

<https://ko.javascript.info/types>

## User Interaction with alert, prompt, confirm

Browsers provide three functions for user interaction.

- **alert** – Display a message.
- **prompt** – Display a message asking user to enter text and provide an input field. When confirmed, prompt returns the string entered by the user; when cancelled or Esc is pressed, it returns null.
- **confirm** – Display a message until the user clicks OK or Cancel. Returns true if OK is clicked, false if Cancel or Esc is pressed.

All these functions display a modal window, and while the modal is open, script execution is paused. Cannot interact with the rest of the page until the user closes the window!

The three functions have two limitations:

1. Modal position is determined by the browser, usually centered.
2. Modal appearance varies by browser. Developers cannot modify the window's appearance.

<https://ko.javascript.info/alert-prompt-confirm>

## Type Conversion

There is conversion to string, number, and boolean types.

**Conversion to String** occurs when outputting something. Using String(value) enables explicit conversion to string. Converting primitive types to strings is mostly explicit and predictable.

**Conversion to Number** occurs during mathematical operations. Number(value) also enables type conversion.

Number conversion follows these rules:

| Value | Result |
| --- | --- |
| undefined | NaN |
| null | 0 |
| true / false | 1 / 0 |
| string | The string is read "as-is", ignoring whitespace at beginning and end. Empty string becomes 0; error results in NaN. |

**Conversion to Boolean** occurs during logical operations. Boolean(value) also enables conversion.

Boolean conversion follows these rules:

| Value | Result |
| --- | --- |
| 0, null, undefined, NaN, "" | false |
| All other values | true |

Exceptions:

- When converting to number, undefined becomes NaN, not 0.
- String "0" and whitespace " " convert to true in boolean conversion.

<https://ko.javascript.info/type-conversions>
