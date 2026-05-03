---
title: "Google Lyria 3: Create Music from Text and Photos in Gemini App"
date: 2026-02-19T05:45:48+09:00
slug: "1035-Google-Lyria-3-Gemini-앱에서-텍스트와-사진으로-음악을-만든다"
original_url: "https://memoryhub.tistory.com/1035"
tistory_id: 1035
draft: false
---

![](/images/1035-Google-Lyria-3-Gemini-앱에서-텍스트와-사진으로-음악을-만든다/img.jpg)

If you thought "AI draws pictures, makes videos, and now creates music too?" you're absolutely right. On February 18, 2026, Google DeepMind unveiled Lyria 3 and integrated music generation into the Gemini app.

A single line of text creates a 30-second track with lyrics and vocals, and uploading a single photo automatically composes music that matches its mood. It supports Korean as well.

**Lyria 3 is the first case of integrating music generation into a general-purpose AI assistant, and a variable that can reshape the AI music market.**

**One-liner summary:** In short, Google Lyria 3 is DeepMind's latest AI music model that generates high-quality 30-second music with lyrics when you input text, photos, or videos in the Gemini app.

---

## Background

AI music generation has been a field experiencing explosive growth since 2024. Suno and Udio dominated the market, making "create a song with one prompt" a reality. However, they are independent platforms. You need to sign up on separate sites, purchase credits, and go through distinct workflows.

Google took a different strategy. It embedded music generation directly into the Gemini app, which is already used by over 750 million people.

No separate sign-up needed, no additional app required. It maintains the existing input methods of text, images, and videos while expanding the output to "music."

> Lyria is a suite of AI music generation models developed by Google DeepMind. It generates high-quality audio including instrument performance, vocals, and lyrics from text prompts.

Understanding Lyria's evolution clarifies Lyria 3's position.

**Lyria (2023):** The original model developed in collaboration with YouTube. It started generating 30-second soundtracks for YouTube Shorts through the Dream Track experiment. It garnered attention by demonstrating AI-generated voice styles of artists like Charlie Puth and T-Pain.

**Lyria 2 (2025):** Evolved into a high-fidelity model that generates professional 48kHz stereo audio.

It became the core engine of Music AI Sandbox, a tool for professional artists, and began being offered as a developer API through Vertex AI. Fine control became possible over key, BPM, instruments, and more.

**Lyria RealTime (2025):** A model exploring a completely different direction—real-time music generation.

The MusicLM architecture was adapted using block autoregression.

When users adjust the prompt, the music changes within 2 seconds.

At Google I/O 2025, musician Toro y Moi showcased a live performance using a MIDI controller.

It was released as an open-source API, allowing anyone to create their own music interface.

**Lyria 3 (February 18, 2026):** The most advanced latest model. Three key improvements exist.

First, **automatic lyrics generation**. In previous models, users had to input lyrics manually. Lyria 3 understands the context of the prompt and automatically writes lyrics.

Second, **multimodal input**. Beyond text, uploading photos or videos generates music that matches the mood.

Upload a photo of waves crashing on a beach and you get surf rock; upload a neon sign alley photo and you get cyberpunk electronic music.

Third, **multilingual support**. It supports 8 languages total: English, German, Spanish, French, Hindi, Japanese, **Korean**, and Portuguese.

---

## Core Features of Lyria 3

**Text-to-Track**

Express genre, mood, personal memories, or even jokes in a prompt and a 30-second track with lyrics is generated. Looking at examples from Google's official blog, even a long description like "a nostalgic Afrobeat track about childhood memories with mother and longing for homemade plantain" gets converted to music. If you only want instrumental music, that's possible too.

**Visual-to-Track (Image/Video)**

Upload a photo or video clip, and Gemini analyzes the visual content to compose music that matches the mood. This is a differentiator unique to Lyria 3. Suno or Udio cannot do this.

This reveals the technological expertise Google has accumulated in the multimodal AI field.

**Automatic Cover Art Generation**

The Nano Banana model automatically creates cover art for generated music. You can download it or copy the share link to post directly to SNS, reducing the content creation workflow by one step.

**SynthID Watermark**

All generated music automatically includes a SynthID watermark. It's not audible to human ears but can be detected by software. The watermark persists even after processing like MP3 compression, speed changes, or noise addition.

Uploading an audio file to the Gemini app lets you check whether it was AI-generated.

---

## AI Music Generation Tool Comparison

The arrival of Lyria 3 means a major player is now seriously entering the already competitive AI music market.

| Category | Lyria 3 (Google) | Suno (v4.5) | Udio |
| --- | --- | --- | --- |
| Output Length | 30 seconds | Up to 4 minutes | 30-second units expandable (max 15 minutes) |
| Vocals/Lyrics | Auto-generated (8 languages) | Auto-generated | Auto-generated |
| Input Methods | Text, images, video | Text, audio | Text, audio, style reference |
| Accessibility | Built-in Gemini app (free available) | Separate web/app (free plan: 50 songs/day) | Separate web/app (free plan: 3 songs/day) |
| Detail Control | Style, vocals, tempo | Genre, lyrics, structure | Stem separation, remix, inpainting |
| Copyright Response | SynthID watermark + existing content contrast filter | Major label agreement in progress | Major label agreement in progress |
| Key Strength | Multimodal input, existing ecosystem integration | High-quality full songs, ease of use | Fine control for producers |
| Key Weakness | 30-second limit, features in early stage | Copyright lawsuit risk | Generation speed (90+ seconds) |

Lyria 3's greatest strength is **accessibility and multimodal input**. If you're already using Gemini, you can use it immediately without additional cost or sign-up. However, the 30-second length limit and early-stage detail control features make its limitations clear as a professional music production tool.

Suno excels at generating complete high-quality songs, while Udio shines with producer-friendly features like stem downloads and remixes. Lyria 3 is positioning itself less as a direct competitor and more as a **"tool for everyday self-expression."**

The fact that Google explicitly stated in its official blog "making musical masterpieces is not the goal, but rather fun and unique self-expression" supports this positioning.

---

## Use Cases

Lyria 3 has greater practical value for content creators and general users than professional music producers.

**Step 1: Access the Gemini App**

Go to gemini.google.com or the Gemini mobile app and select "Music" from the Tools menu. Desktop access begins February 18, with mobile rollout in the coming days.

**Step 2: Enter Prompt**

Describe the music you want using text. The more specifically you write the genre, mood, and subject, the better the results.

Alternatively, upload a photo or video and request "create music that matches this mood."

**Step 3: Confirm Results and Share**

A 30-second track and cover art are generated. You can download it or copy the share link to post immediately to SNS.

**Usage Scenarios:**

- Generate background music on the spot for YouTube Shorts or Instagram Reels
- Insert custom BGM for presentations or video projects
- Create personalized music gifts for special occasions like birthdays or anniversaries
- Automatically generate mood-matching soundtracks for travel photos

---

## Copyright Issues and Safety Measures

The most sensitive topic in AI music is copyright. In 2024, Universal Music Group, Sony Music, and Warner Music Group sued Suno and Udio for copyright infringement. While some settlements followed, the copyright issue of AI music training data remains an ongoing debate.

Google stated that Lyria 3's training process "carefully considered copyright and partner agreements."

Specifically, training was conducted on music for which usage rights existed according to YouTube and Google's service terms, partner agreements, and relevant laws. However, this statement is somewhat vague, and the specific composition of training data has not been disclosed.

The safety measures applied in actual use are as follows. If you include a specific artist's name in the prompt, it creates "similar style or mood" rather than imitation. Generated results go through a contrast filter against existing content.

A SynthID watermark is automatically inserted. However, Google acknowledged that "this approach may not be perfect."

---

## Conclusion

- Lyria 3 is Google DeepMind's latest AI music model that generates high-quality 30-second tracks with lyrics when text, photos, or videos are input into the Gemini app.
- It's the first case of integrating music generation into a general-purpose AI assistant and supports 8 languages including Korean. It's optimized for everyday self-expression and content creation rather than professional production.
- Practical tip: Visit gemini.google.com right now and try typing "create an emotional K-pop style track about my pet."

---

## References

- Google Official Blog: Lyria 3 Announcement (<https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/>)
- Google DeepMind Lyria Model Page (<https://deepmind.google/models/lyria/>)
- Lyria RealTime API Introduction (<https://magenta.withgoogle.com/lyria-realtime>)
- Vertex AI Lyria Documentation (<https://docs.cloud.google.com/vertex-ai/generative-ai/docs/music/generate-music>)
- Music AI Sandbox Update (<https://deepmind.google/blog/music-ai-sandbox-now-with-new-features-and-broader-access/>)
- Google Cloud Blog: Lyria 2 on Vertex AI (<https://cloud.google.com/blog/products/ai-machine-learning/announcing-veo-3-imagen-4-and-lyria-2-on-vertex-ai>)
