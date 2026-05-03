---
title: "Essential Developer Tool: Ripgrep (rg) 10 Use Cases + macOS Installation Guide"
date: 2025-09-02T16:02:34+09:00
slug: "772-개발자-필수-툴-Ripgrep-rg-10가지-활용법-macOS-설치-방법"
original_url: "https://memoryhub.tistory.com/772"
tistory_id: 772
draft: false
---

Hello! 👋

Today I'm introducing **Ripgrep (rg)**, a tool many developers have started using instead of grep.

It's a truly powerful weapon, especially when you need **fast code search in large projects** ⚡

---

## **🔍 What is Ripgrep?**

- Think of it as an upgraded version of grep.
- **Very fast speed**: Searches much faster than grep.
- **Smart searching**: Automatically recognizes .gitignore and ignores unnecessary folders.
- **Developer-friendly**: Built-in features like language type filtering, extension filtering, line numbers, statistics, and more.

---

## **💻 How to Install Ripgrep on macOS**

Ripgrep is not installed by default on Mac.

You can install it easily via Homebrew 📦

```
# If Homebrew is installed, run this command
brew install ripgrep

# Verify installation
rg --version
```

✓ If rg --version outputs correctly, installation is complete!

---

## **⚡ Ripgrep 10 Practical Tips**

Number | Command | Description

|  |  |  |
| --- | --- | --- |
| 1 | rg "BusinessException" | Search for a string across the entire current directory |
| 2 | rg -n "TODO" | Search **with line numbers** (default but good to remember) |
| 3 | rg -i "error" | Search **case-insensitively** |
| 4 | rg -t java "UserService" | Search only specific **language types** (e.g., Java files) |
| 5 | rg -g "\*.xml" "tchrId" | Search only **specific file extensions** |
| 6 | rg -g "!\*.min.js" "fetch(" | Exclude specific files (e.g., exclude minified JS) |
| 7 | rg -C 3 "SQLException" | Output **3 lines of context** around search results |
| 8 | rg -l "password" | Output **only matching filenames** |
| 9 | rg -v "DEBUG" | Output only lines that don't match (NOT search) |
| 10 | rg --stats "BusinessException" | Output **file count/match count statistics** after search |

---

## **🎯 Power User Tips**

- rg --hidden "pattern" → Search including hidden files (.env, etc.)
- rg -uuu "pattern" → Search everything, ignoring .gitignore
- rg -w "id" → Match **only as whole words**
- rg -e "foo|bar" → **OR condition** search (foo or bar)
- rg --json "pattern" → Output in JSON format (IDE integration possible)

---

## **✅ Summary**

Ripgrep (rg) is a **fast, smart, and developer-friendly search tool**.

Especially in large projects, you can explore source code much more efficiently than with grep.

✨ **One-liner Summary**: "macOS developers, install Ripgrep with Homebrew and use rg instead of grep for searches!"
