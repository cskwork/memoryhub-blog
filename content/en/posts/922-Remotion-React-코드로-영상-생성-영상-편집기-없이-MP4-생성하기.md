---
title: "Remotion: Generate Videos with React Code, Create MP4 Without a Video Editor"
date: 2025-12-07T22:38:04+09:00
slug: "922-Remotion-React-코드로-영상-생성-영상-편집기-없이-MP4-생성하기"
original_url: "https://memoryhub.tistory.com/922"
tistory_id: 922
draft: false
---

```
    ╭──────────────────────────────────────╮
    │   ┌─────┐                            │
    │   │ < > │  →  VIDEO  →  VIDEO.mp4   │
    │   │React│     REMOTION               │
    │   └─────┘                            │
    │                                      │
    │   "Code becomes Video"               │
    ╰──────────────────────────────────────╯
```

Have you ever opened Premiere Pro just to create one video? Arranging clips on the timeline, adding text, waiting for rendering. To make 10 videos, you repeat the same process 10 times. But what if you could create videos with code? Simply change the data and 1,000 customized videos are automatically generated.

**Remotion is a framework that renders React components into actual MP4 files.**

**Summary:** In short, Remotion is an open-source framework that lets React developers use web technologies like CSS, SVG, and Canvas to programmatically create videos and render them to MP4 locally or on AWS Lambda.

---

## Background

Video content demand is exploding. 87% of marketing professionals report that video contributes to increased website traffic, and 78% say it leads to improved sales. The problem is video production inefficiency.

The limitations of traditional video production are clear. First, there's heavy repetition. To send customized videos with names to 100 customers, you must edit 100 times. Second, automation is difficult. It's impossible with existing editing tools to receive API data and generate videos in real-time. Third, collaboration between developers and designers hits a bottleneck.

| Traditional Approach | Remotion Approach |
| --- | --- |
| Manual editing, repetitive work | Code-based automation |
| Requires learning editing software | React knowledge is sufficient |
| Hard to integrate with data | Direct API and database connection possible |
| Local rendering only | Supports serverless distributed rendering |

Remotion is an open-source project created by Jonny Burger in 2021. It currently has over 24,000 GitHub stars and records 400,000 monthly npm installations.

---

## Core Concepts

> One-line definition: Remotion is a framework that captures React components frame-by-frame, encodes them with FFmpeg, and generates actual MP4/WebM video files.

To understand how Remotion works, remember that "video = rapidly passing images." A 30fps video is 30 images playing continuously per second. Remotion renders React components every frame and stitches these screenshots together with FFmpeg to create video. You make video the way you make a webpage.

There are four core concepts. **Composition** is a single video unit that defines resolution, fps, and duration. **useCurrentFrame** is a Hook that tells you which frame you're on. You control animation with this value. **Sequence** acts like a timeline, displaying components only during specific frame ranges. **spring** and **interpolate** are animation utilities that handle natural motion and value interpolation.

```
// based on remotion v4.x
import { useCurrentFrame, interpolate, Composition } from 'remotion';

const FadeInText: React.FC = () => {
  const frame = useCurrentFrame();
  // Over frames 0-30, opacity changes from 0 to 1
  const opacity = interpolate(frame, [0, 30], [0, 1]);

  return (
    <div style={{ opacity, fontSize: 60 }}>
      Hello, Remotion!
    </div>
  );
};
```

In the code above, `useCurrentFrame()` is key. As the video plays, the frame value increases as 0, 1, 2... in sequence, and `interpolate` converts this value to opacity. This is the same pattern as giving animation based on scroll position in web development.

---

## Practice

### ① Create a Project

Run the following command in terminal:

```
npx create-video@latest
```

When a template selection screen appears, choose "Hello World" or "Blank." Once installation completes, run `npm run start` to start the development server. Your browser opens `localhost:3000` and Remotion Studio appears. This Studio provides a preview environment similar to the timeline in After Effects or Premiere.

### ② Register a Composition

Register your video in src/Root.tsx:

```
import { Composition } from 'remotion';
import { MyVideo } from './MyVideo';

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="MyVideo"
      component={MyVideo}
      durationInFrames={150}  // 5 seconds at 30fps
      fps={30}
      width={1920}
      height={1080}
    />
  );
};
```

`durationInFrames` is **in frames, not seconds**. To create a 5-second video, enter fps × 5 = 150. Missing this will create videos with unexpected lengths.

### ③ Write the Video Component

Use Sequence to compose multiple scenes:

```
import { AbsoluteFill, Sequence, useCurrentFrame, spring, useVideoConfig } from 'remotion';

export const MyVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // spring animation for smooth entrance
  const scale = spring({ frame, fps, config: { damping: 100 } });

  return (
    <AbsoluteFill style={{ backgroundColor: '#0f0f0f' }}>
      {/* Frames 0-60: Intro */}
      <Sequence from={0} durationInFrames={60}>
        <div style={{ transform: `scale(${scale})`, color: 'white', fontSize: 80 }}>
          2024 Year-End Summary
        </div>
      </Sequence>

      {/* Frames 60-150: Body */}
      <Sequence from={60}>
        <div style={{ color: 'white' }}>Statistical data goes here</div>
      </Sequence>
    </AbsoluteFill>
  );
};
```

`AbsoluteFill` is a container that fills the entire video. `Sequence`'s `from` is the frame number where that scene starts.

### ④ Render

Once development is complete, export to MP4:

```
npx remotion render src/index.ts MyVideo out/video.mp4
```

Local rendering uses a lot of CPU. A 2-hour video takes considerable time on a typical PC. Using Remotion Lambda allows AWS parallel processing to render a 2-hour video in 12 minutes.

---

## Best Practices/Pattern Comparison

| Usage Pattern | Advantages | Considerations |
| --- | --- | --- |
| **Local Rendering** | Simple setup, no cost | Long videos take time |
| **Remotion Lambda** | Fast with parallel processing, scalable | AWS setup required, pay-per-use |
| **Remotion Player** | Can embed videos in web apps | Final MP4 rendering requires separate step |
| **Cloud Run** | GCP environment support | Currently Alpha stage |

For real service applications, the **Remotion Player for preview + Lambda for final rendering** combination is standard. GitHub Unwrapped (year-end developer statistics video) is a prime example using this structure to generate millions of personalized videos.

For licensing, individuals and organizations of 3 or fewer are free. Companies with 4+ people require a Company License starting at $100/month.

---

## Final Thoughts

- Remotion is a framework that converts React components into actual MP4 videos, enabling video production with web development knowledge alone
- Understanding core concepts like `useCurrentFrame`, `Sequence`, and `spring` lets you automatically generate large numbers of data-driven customized videos
- Practical tip: Create a project with `npx create-video@latest` and start with simple text animation.

---

## References

- Remotion Official Documentation (https://www.remotion.dev/docs/)
- Remotion GitHub Repository (https://github.com/remotion-dev/remotion)
- Remotion Lambda Guide (https://www.remotion.dev/lambda)
- LogRocket - Remotion Framework Tutorial (https://blog.logrocket.com/remotion-a-framework-for-making-videos-in-react/)
