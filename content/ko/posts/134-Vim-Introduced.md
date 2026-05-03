---
title: "Vim Introduced"
date: 2024-05-28T23:05:55+09:00
slug: "134-Vim-Introduced"
original_url: "https://memoryhub.tistory.com/134"
tistory_id: 134
draft: false
categories: ["데브 옵스"]
tags: ["Vim"]
---

*Vim is a highly configurable text editor that allows efficient text editing through keyboard commands, offering powerful features for programmers and power users.*

### The Big Picture

Imagine you're a musician playing an instrument. When you first start, you might need sheet music and guidance, but as you get better, you can play by memory and improvisation, making your performance fluid and efficient. Vim, a text editor, works similarly for programmers and text editors. It's like the musical instrument that, once mastered, allows you to compose, edit, and navigate text files swiftly without needing to take your hands off the keyboard.

### Core Concepts

1. **Modes**: Vim operates in several modes, each serving a specific purpose:

   - **Normal Mode**: For navigating and manipulating text.
   - **Insert Mode**: For inserting and editing text.
   - **Visual Mode**: For selecting blocks of text.
   - **Command Mode**: For running commands.
2. **Commands**: In Normal Mode, you can execute commands that can do everything from moving the cursor to performing complex text transformations.
3. **Configuration**: Vim can be customized extensively through configuration files, allowing users to tailor it to their specific needs.

### Detailed Walkthrough

1. **Modes**:

   - **Normal Mode**: This is the default mode when you open Vim. Here, keys don't insert text but perform commands. For example, pressing `h`, `j`, `k`, or `l` moves the cursor left, down, up, and right, respectively.
   - **Insert Mode**: Press `i` in Normal Mode to switch to Insert Mode. Now, you can type text as you would in a regular text editor.
   - **Visual Mode**: Press `v` in Normal Mode to start selecting text. You can then manipulate this selection with commands.
   - **Command Mode**: Press `:` in Normal Mode to enter Command Mode. Here you can run commands like `:w` to save or `:q` to quit.
2. **Commands**:

   - Moving around: `h`, `j`, `k`, `l`
   - Editing text: `x` deletes a character, `dd` deletes a line, `yy` yanks (copies) a line
   - Combining commands: `d3w` deletes the next three words
   - Search and replace: `:%s/old/new/g` replaces all occurrences of "old" with "new" in the entire file
3. **Configuration**:

   - **vimrc**: Vim reads configuration from a `.vimrc` file. Here you can set options like syntax highlighting, line numbers, and custom key mappings.
   - Example `.vimrc`:

     ```
     set number              " Show line numbers
     syntax on               " Enable syntax highlighting
     set tabstop=4           " Set tab width to 4 spaces
     set shiftwidth=4        " Set indentation width to 4 spaces
     set expandtab           " Use spaces instead of tabs
     ```

### Understanding Through an Example

Let's say you want to change all instances of the word "foo" to "bar" in a text file:

1. Open the file in Vim:

   ```
   vim filename.txt
   ```
2. Press `:` to enter Command Mode and type the following command:

   ```
   :%s/foo/bar/g
   ```

   This tells Vim to search (`s`) through the entire file (`%`) and globally (`g`) replace "foo" with "bar".

### Conclusion and Summary

Vim is a powerful and efficient text editor that, when mastered, can significantly speed up text editing and manipulation tasks. Its unique modal editing approach and extensive customization options make it a favorite among programmers and power users.

### Test Your Understanding

1. What are the different modes in Vim and what is each used for?
2. How would you copy an entire line in Vim?
3. What command would you use to save and quit Vim?

### Reference

For more detailed information, you can refer to the official Vim documentation: [Vim Documentation](https://www.vim.org/docs.php)
