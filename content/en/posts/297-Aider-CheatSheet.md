---
title: "Aider CheatSheet"
date: 2024-06-13T11:10:09+09:00
slug: "297-Aider-CheatSheet"
original_url: "https://memoryhub.tistory.com/297"
tistory_id: 297
draft: false
---

*In this explanation, I'll walk you through the commands available in Aider, an AI-powered assistant for code and project management, by relating each command to its technical function.*

### The Big Picture

Aider is an AI assistant designed to enhance your efficiency in handling coding tasks and managing projects. The commands provided by Aider facilitate various operations, such as editing files, managing version control, and running shell commands.

### Core Concepts

- **/add**: Including specific files in your chat session.
- **/clear**: Deleting all previous chat history.
- **/commit**: Recording changes to the repository.
- **/diff**: Showing the differences between versions of files.
- **/drop**: Removing files from the current session.
- **/exit**: Closing the Aider application.
- **/git**: Executing Git commands.
- **/help**: Displaying information about available commands.
- **/lint**: Checking and fixing code for errors.
- **/ls**: Listing all known files and their status in the chat.
- **/model**: Switching to a different language model.
- **/models**: Searching through available language models.
- **/quit**: Closing the Aider application.
- **/run**: Running shell commands.
- **/test**: Running shell commands and logging errors.
- **/tokens**: Reporting on the number of tokens used in the chat.
- **/undo**: Reverting the last Git commit made by Aider.
- **/voice**: Recording and transcribing voice input.
- **/web**: Scraping webpage content using headless Selenium.

### Detailed Walkthrough

1. **/add**: *Add files to the chat so GPT can edit them or review them in detail.*  
   This command allows you to include specific files in your chat session. Once added, Aider can read, edit, or provide detailed reviews of these files.
2. **/clear**: *Clear the chat history.*  
   This command deletes all previous messages and interactions in the chat session, essentially resetting it.
3. **/commit**: *Commit edits to the repo made outside the chat (commit message optional).*  
   This records all changes made outside the current chat session into your Git repository, optionally allowing you to include a commit message.
4. **/diff**: *Display the diff of the last aider commit.*  
   This shows the differences between the current state of files and their state after the last commit made by Aider, highlighting changes line-by-line.
5. **/drop**: *Remove files from the chat session to free up context space.*  
   This removes specific files from the chat session, which can help manage the context space and keep the session efficient.
6. **/exit**: *Exit the application.*  
   This command closes the Aider application, ending the session.
7. **/git**: *Run a git command.*  
   This allows you to execute Git commands directly within Aider, such as `git status`, `git checkout`, or any other Git operation.
8. **/help**: *Show help about all commands.*  
   This command provides detailed information about all available commands within Aider.
9. **/lint**: *Lint and fix provided files or in-chat files if none provided.*  
   This command checks the provided files (or all files in the chat session if none are specified) for coding errors and automatically fixes them if possible.
10. **/ls**: *List all known files and indicate which are included in the chat session.*  
    This lists all files that Aider is aware of and indicates which ones are currently included in the chat session.
11. **/model**: *Switch to a new LLM.*  
    This command allows you to switch the language model that Aider is using, which can be useful for different types of tasks or optimizations.
12. **/models**: *Search the list of available models.*  
    This command lets you search through and review all available language models that you can switch to within Aider.
13. **/quit**: *Exit the application.*  
    Similar to /exit, this command closes the Aider application and ends the session.
14. **/run**: *Run a shell command and optionally add the output to the chat (alias: !).*  
    This allows you to execute any shell command. You can choose to include the output of this command in the chat for further analysis or discussion.
15. **/test**: *Run a shell command and add the output to the chat on non-zero exit code.*  
    This runs a shell command and only logs the output to the chat if the command exits with a non-zero status, indicating an error.
16. **/tokens**: *Report on the number of tokens used by the current chat context.*  
    This reports the number of tokens (units of conversation) used in the current chat context, helping you manage and optimize resource usage.
17. **/undo**: *Undo the last git commit if it was done by aider.*  
    This reverts the last Git commit made by Aider, useful if you need to roll back changes.
18. **/voice**: *Record and transcribe voice input.*  
    This records spoken input and transcribes it into text, which can then be included in the chat for further processing or discussion.
19. **/web**: *Use headless selenium to scrape a webpage and add the content to the chat.*  
    This uses headless Selenium to scrape content from a specified webpage and add the extracted content to the chat session for analysis or integration into your project.

### Understanding Through an Example

Suppose you're working on a project and need to make some changes to a file. Here's how you can use Aider commands:

- **/add myfile.py**: Include `myfile.py` in the chat session.
- **/lint myfile.py**: Check `myfile.py` for coding errors and automatically fixes them.
- **/diff**: Show the differences between the current state of `myfile.py` and its previous state.
- **/commit "Fixed linting issues"**: Record these changes to the Git repository with a commit message.
- **/ls**: List all files Aider knows about and indicate which ones are in the chat.
- **/undo**: If you made a mistake, revert the last commit.

### Conclusion and Summary

Aider's commands provide a robust set of tools for managing and editing files, interacting with Git repositories, running shell commands, and more. Each command has a specific function that helps streamline and optimize your workflow, making it easier to handle complex projects efficiently.

### Test Your Understanding

1. What command would you use to add a file to your chat session?
2. How would you revert the last Git commit made by Aider?
3. If you wanted to list all known files and see which are included in the chat session, which command would you use?
4. Describe a scenario where the **/lint** command would be useful.

### Reference

For further details, you can refer to the [Aider CheatSheet](https://memoryhub.tistory.com/entry/Aider-CheatSheet).
