---
title: "'Nano-Banana' = Gemini 2.5 Flash Image"
date: 2025-08-27T08:54:56+09:00
slug: "766-나노바나나-Gemini-2-5-Flash-Image"
original_url: "https://memoryhub.tistory.com/766"
tistory_id: 766
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
cover:
  image: "/images/766-나노바나나-Gemini-2-5-Flash-Image/img.png"
  relative: false
  hidden: false
---

![](/images/766-나노바나나-Gemini-2-5-Flash-Image/img.png)

Released today (August 27 Korea time), **Gemini 2.5 Flash Image (nickname 'Nano-Banana')** is Google's latest model that handles image **generation and editing** in one go, with enhanced **character consistency, selective editing, and multi-image composition**. Developers can use it immediately through **AI Studio/Vertex/Gemini API**, with **approximately $0.039 per image**.

---

## **Core Features**

- **Official Release & Model Name**: *Gemini 2.5 Flash Image* (community nickname: **Nano-Banana**).
- **4 Key Capabilities**
  1. **Character Consistency**: Maintain the same person across various scenes and angles
  2. **Prompt-Based Selective Editing**: Local corrections like background blur, blemish removal, pose adjustment
  3. **Multi-Image Composition**: Seamlessly blend multiple images into one
  4. **World Knowledge Integration**: Understand sketches/diagrams, educational explanations and semantic-based editing

→ Official examples and templates are provided on the developer blog.

- **Available Channels & Status**: **Gemini API**, **Google AI Studio** (developer), **Vertex AI** (enterprise). Currently offered as **Preview** with stability planned. Model ID example: gemini-2.5-flash-image-preview.
- **Pricing**: **$30 per 1 million output tokens → approximately 1,290 tokens per image ≈ $0.039** (roughly 25 images for $1).
- **Watermarking**: All generated/edited images automatically include **SynthID** invisible watermark.

![](/images/766-나노바나나-Gemini-2-5-Flash-Image/blob.jpg)

---

## **Get Started (3 Steps)**

1. **Visit Google AI Studio** → Select **Gemini 2.5 Flash Image (preview)** as your model.
2. **Write Your Prompt** → Upload original image if needed (for selective editing or composition).
3. **Review Results & Re-prompt** → Fine-tune by adjusting character consistency, color, background.

> Quick testing starts easily with **template apps in AI Studio (photo editing/character consistency/multi-composition)**.

## **Recommended Prompt Examples**

- "**Keep the person the same** and change the **background to a café interior**. Make it feel like natural light."
- "Merge these two photos and **naturally place product A on the desk in photo B**. Match the shadows too."
- "**Maintain identical character** and create **4 seasonal posters** (spring/summer/fall/winter) with different vibes."
- "Apply **natural color** to this black-and-white family photo and **remove blemishes**."

---

## **Pricing & Access Summary Table**

| Item | Details |
| --- | --- |
| Model Name | Gemini 2.5 Flash Image *(aka 'Nano-Banana')* |
| Status | Preview – Stabilization expected soon |
| Access Paths | Gemini API / Google AI Studio / Vertex AI |
| Billing | $30 per 1 million output tokens |
| Cost Per Image | **~1,290 tokens ≈ $0.039/image** (1024x1024 standard) |
| Watermark | **SynthID** invisible watermark auto-applied |

---

## **Best Use Cases**

- **Brand/Marketing**: Quickly produce varied visuals while maintaining **character and product consistency**.
- **E-Commerce**: **Multi-image composition** for background changes, product placement, and creative combinations.
- **Education/Explanation**: Sketch/diagram understanding → automatic **explanation image** enhancement/editing.

> Note: Some media and creative tools have announced **integrated support** (e.g., Adobe Firefly/Express integration). Choose based on your workflow.

---

## **Practical Tips (Quality & Speed Combined)**

- **Write role + style + constraints together**: "Like an art director… / magazine cover style / natural skin texture"
- **Selective editing over re-rolling**: **Regional specification and local fixes** are more efficient than full regeneration.
- **Provide all materials at once**: For composition, include all originals in one request and specify **light sources, perspective, color temperature**.
- **Verify policy and attribution**: SynthID watermark is inserted; confirm your team's policy on source attribution when distributing.

## **Quick Q&A**

**Q. Is it free?**

A. API/cloud billing follows the table above. AI Studio trial availability varies by timing and policy—check pricing in your console.

**Q. What's the model code?**

A. In *AI Studio* it appears as gemini-2.5-flash-image-preview.

**Q. Is today's release confirmed?**

A. Google Developer Blog post (local 8/26) and official release notes (8/26) are confirmed, corresponding to 8/27 Korea time.

---

> **Conclusion:** *Nano-Banana is a practical model that bundles "fast and accurate image generation and editing" into one—start using it today!* 🎨

![](/images/766-나노바나나-Gemini-2-5-Flash-Image/Image.jpeg)

<https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/>

[Introducing Gemini 2.5 Flash Image, our state-of-the-art image model- Google Developers Blog

Today, we're excited to introduce Gemini 2.5 Flash Image (aka nano-banana), our state-of-the-art image generation and editing model. This update enables you to blend multiple images into a single image, maintain character consistency for rich storytellin

developers.googleblog.com](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/)
