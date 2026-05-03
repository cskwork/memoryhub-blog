---
title: "ChatGPT Atlas Launch"
date: 2025-10-22T04:27:13+09:00
slug: "866-ChatGPT-Atlas-출시"
original_url: "https://memoryhub.tistory.com/866"
tistory_id: 866
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
cover:
  image: "/images/866-ChatGPT-Atlas-출시/img.png"
  relative: false
  hidden: false
---

![](/images/866-ChatGPT-Atlas-출시/img.png)

Today we're introducing **ChatGPT Atlas**, a new web browser built on ChatGPT at its core.

AI provides a valuable opportunity to reconsider what web browsing means. Last year, we added search to ChatGPT to instantly find the latest information across the entire internet, and it quickly became one of the most-used features. But the browser is where all your tasks, tools, and context come together. A browser with ChatGPT built in brings us one step closer to a true super-assistant that understands your world and helps you achieve your goals.

With Atlas, ChatGPT can be with you anywhere on the web. It provides help right in the window you're working in, understands what you're trying to do, and completes tasks without copy-paste or page switching. ChatGPT Memory is built in, so conversations can leverage past chats and details to handle new tasks.

> "I like to understand course material by using practice problems and real examples. Before, I had to alternate between slides and ChatGPT, taking screenshots to ask questions. Now ChatGPT immediately understands what I'm seeing and helps me check my knowledge as I go."
> — Yogya Kalra, college student and early tester of ChatGPT Atlas

Using Atlas makes ChatGPT smarter and more useful. Through browser memory, ChatGPT remembers the context of sites you visit and recalls it when needed. For example, you can ask: "Find all the job postings I saw last week and write an industry trends summary to help me prepare for interviews." Browser memory in Atlas is completely optional—you can check or archive it anytime in settings, and clearing your search history also clears related browser memory.

ChatGPT can also use agent mode to perform tasks for you in Atlas, working with browsing context to become faster and more useful. Research and analysis, task automation, and event planning or booking while browsing are now more capable. Atlas agent mode is launching today as a preview for Plus, Pro, and Business users.

ChatGPT Atlas launches today worldwide on macOS for Free, Plus, Pro, and Go users. Atlas is also available in beta for Business, and Enterprise and Edu users can use it if enabled by their plan administrator. Versions for Windows, iOS, and Android are coming soon.

Download it at **chatgpt.com/atlas**. Getting started is simple: when you first open Atlas, log into ChatGPT and import bookmarks, saved passwords, and search history from your current browser.

## Optimized for Workflows

The new tab page is your starting point in Atlas. Ask a question or type a URL to see faster, more useful results in one place. Beyond chat, explore tabs for search links, images, videos, and news (where available) for more specific result types.

## Personalized to You

ChatGPT remembers what you've explored and can suggest next steps. You might get suggestions to go back to previous pages, dive deeper into topics, surface related ideas, or automate repetitive tasks.

## More Features, Greater Control

You control what ChatGPT can see and remember while browsing. You can clear specific pages, wipe your entire search history, or open an incognito window to temporarily log out from ChatGPT.

Turning on browser memory makes ChatGPT remember key details of content you've browsed to improve chat responses and provide smarter suggestions. For example, you can create a to-do list from recent activity or continue gift research based on products you've seen.

Browser memory is private to your ChatGPT account and controlled by you. From settings you can review all memory, archive memory that's no longer relevant, and delete memory by clearing your search history. Even with browser memory enabled, you can use the address bar toggle to decide which sites ChatGPT can and can't see. When visibility is off, ChatGPT can't see page content and no memory is created.

By default, your browsed content is not used for model training. You can opt into this in data control settings by enabling "Include web browsing." If you've enabled chat training in your ChatGPT account, training is also enabled in Atlas chats. This includes website content attached from the ChatGPT sidebar and browser memory that informs your chat.

Parental controls also work in Atlas. If parents have set parental controls for ChatGPT, those settings carry over to ChatGPT conversations in Atlas. We've also introduced new parental controls including options for parents to turn off browser memory and agent mode.

## Taking Action Instead of Doing

In Atlas, you can now ask ChatGPT to take action and perform tasks directly in your browser.

We introduced ChatGPT agents earlier this year, and we've now improved them to be faster and work natively in Atlas.

Imagine you're planning a dinner party and have a recipe. You could give the recipe to ChatGPT and ask it to find a grocery store, add all the ingredients to your cart, and have them delivered home. For work, you could ask ChatGPT to open past team documents and read them, perform a new competitive research, and summarize insights into a team briefing.

When you ask, ChatGPT can ask if it's okay to start opening tabs and clicking in your browser to complete the task. You can also start ChatGPT by selecting the agent mode button.

Starting today, agent mode in Atlas launches as a preview for Plus, Pro, and Business users. This is an early experience and can make mistakes in complex workflows. We're rapidly improving reliability, latency, and the success rate of complex tasks.

We've prioritized safety while building Atlas and added safeguards to address new risks that could arise from access to logged-in sites and search history and taking actions on behalf of users. For example:

- Code cannot execute in the browser, files cannot be downloaded, or extensions cannot be installed
- Other apps or the file system on your computer cannot be accessed
- When taking actions at certain sensitive sites like financial institutions, Atlas pauses to confirm you're watching
- You can use the agent in logout mode to limit access to sensitive data and the risk of taking actions on websites as you

ChatGPT's agent capabilities still carry risks. Beyond simple mistakes, agents can be vulnerable to hidden malicious instructions in webpages or emails—instructions that might try to override the intended behavior of ChatGPT agents. This could lead to data theft from logged-in sites or unintended actions on websites.

As noted in the ChatGPT Agent system card, we've run thousands of hours of intensive red team testing with particular focus on protecting ChatGPT from these attacks. This includes designing safeguards that can quickly adapt to new attacks, but as AI agents gain popularity, we won't be able to prevent every attack. Users should consider the tradeoffs when deciding what information to provide to agents, and should take steps to minimize exposure to these risks—such as using ChatGPT agent in logout mode in Atlas and monitoring the agent's activity. We'll continuously monitor for and patch any discovered vulnerabilities.

This launch is a step toward a future where most web usage happens through agent systems. A future where you can delegate routine tasks and focus on what matters most.

## What's Coming

We'll keep improving Atlas, and our roadmap includes multi-profile support, improved developer tools, and ways for Apps SDK developers to increase discoverability of their apps in Atlas. Website owners can also add ARIA tags to improve how ChatGPT agents work with their websites in Atlas.

This is just the beginning. We'll ship new features and improvements frequently, and you can follow along in our release notes.

Try it now at <https://chatgpt.com/atlas?openaicom_referred=true>.

---

**Key Summary**: ChatGPT Atlas is an AI-powered browser that understands context anywhere on the web, can perform tasks on your behalf, and puts you in complete control of your privacy.

<https://openai.com/index/introducing-chatgpt-atlas/>
