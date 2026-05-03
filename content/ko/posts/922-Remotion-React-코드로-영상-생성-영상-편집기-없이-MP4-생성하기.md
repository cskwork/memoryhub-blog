---
title: "? Remotion: React 코드로 영상 생성, 영상 편집기 없이 MP4 생성하기"
date: 2025-12-07T22:38:04+09:00
slug: "922-Remotion-React-코드로-영상-생성-영상-편집기-없이-MP4-생성하기"
original_url: "https://memoryhub.tistory.com/922"
tistory_id: 922
draft: false
categories: ["데브 컨셉"]
tags: ["Tech News"]
---

```
    ╭──────────────────────────────────────╮
    │   ┌─────┐                            │
    │   │ < > │  →  ?  →  ?.mp4          │
    │   │React│     REMOTION               │
    │   └─────┘                            │
    │                                      │
    │   "Code becomes Video"               │
    ╰──────────────────────────────────────╯
```

영상 하나 만들려고 프리미어 프로를 켜본 적 있으신가요? 타임라인에 클립 배치하고, 텍스트 넣고, 렌더링 기다리고. 10개 만들려면 같은 작업을 10번 반복해야 합니다. 그런데 만약 영상을 코드로 만들 수 있다면 어떨까요? 데이터만 바꾸면 1,000개의 맞춤 영상이 자동으로 생성되는 겁니다.

**Remotion은 React 컴포넌트를 실제 MP4 파일로 렌더링하는 프레임워크입니다.**

**한줄요약:** 결론부터 말하면, Remotion은 React 개발자가 CSS, SVG, Canvas 등 웹 기술을 활용해 프로그래밍 방식으로 영상을 제작하고, 로컬 또는 AWS Lambda에서 MP4로 렌더링할 수 있게 해주는 오픈소스 프레임워크다.

---

## 배경

영상 콘텐츠 수요가 폭발적으로 증가하고 있습니다. 마케팅 전문가의 87%가 영상이 웹사이트 트래픽 증가에 기여한다고 응답했고, 78%는 영상이 매출 향상으로 이어진다고 답했습니다. 문제는 영상 제작의 비효율성입니다.

기존 영상 제작 방식의 한계는 명확합니다. 첫째, 반복 작업이 많습니다. 100명의 고객에게 이름이 들어간 맞춤 영상을 보내려면 100번 편집해야 합니다. 둘째, 자동화가 어렵습니다. API 데이터를 받아서 실시간으로 영상을 생성하는 건 기존 편집 도구로는 불가능합니다. 셋째, 개발자와 디자이너 간 협업에 병목이 생깁니다.

| 기존 방식 | Remotion 방식 |
| --- | --- |
| 수동 편집, 반복 작업 | 코드 기반 자동화 |
| 편집 소프트웨어 학습 필요 | React 지식으로 충분 |
| 데이터 연동 어려움 | API, DB 직접 연결 가능 |
| 로컬 렌더링만 가능 | 서버리스 분산 렌더링 지원 |

Remotion은 2021년 Jonny Burger가 만든 오픈소스 프로젝트로, 현재 GitHub 스타 24,000개 이상, 월간 npm 설치 40만 건을 기록하고 있습니다.

---

## 핵심

> 한 줄 정의: Remotion은 React 컴포넌트를 프레임 단위로 캡처하여 FFmpeg로 인코딩, 실제 MP4/WebM 영상 파일을 생성하는 프레임워크다.

Remotion의 작동 원리를 이해하려면 "영상 = 빠르게 넘어가는 이미지들"이라는 사실을 떠올리면 됩니다. 30fps 영상은 1초에 30장의 이미지가 연속 재생되는 것입니다. Remotion은 React 컴포넌트를 각 프레임마다 렌더링하고, 이 스크린샷들을 FFmpeg로 묶어 영상을 만듭니다. 웹페이지를 만드는 것처럼 영상을 만드는 셈입니다.

핵심 개념은 네 가지입니다. **Composition**은 하나의 영상 단위입니다. 해상도, fps, 길이를 정의합니다. **useCurrentFrame**은 현재 몇 번째 프레임인지 알려주는 Hook입니다. 이 값으로 애니메이션을 제어합니다. **Sequence**는 특정 프레임 구간에만 컴포넌트를 표시하는 타임라인 역할을 합니다. **spring**과 **interpolate**는 자연스러운 모션과 값 보간을 담당하는 애니메이션 유틸리티입니다.

```
// remotion v4.x 기준
import { useCurrentFrame, interpolate, Composition } from 'remotion';

const FadeInText: React.FC = () => {
  const frame = useCurrentFrame();
  // 0~30프레임 동안 투명도 0→1로 변화
  const opacity = interpolate(frame, [0, 30], [0, 1]);

  return (
    <div style={{ opacity, fontSize: 60 }}>
      Hello, Remotion!
    </div>
  );
};
```

위 코드에서 `useCurrentFrame()`이 핵심입니다. 영상이 재생되면서 frame 값이 0, 1, 2... 순서로 증가하고, `interpolate`가 이 값을 투명도로 변환합니다. 웹 개발에서 scroll 위치에 따라 애니메이션을 주는 것과 동일한 패턴입니다.

---

## 실습

### ① 프로젝트 생성

터미널에서 다음 명령어를 실행합니다.

```
npx create-video@latest
```

템플릿 선택 화면이 나타나면 "Hello World" 또는 "Blank"를 선택합니다. 설치가 완료되면 `npm run start`로 개발 서버를 실행합니다. 브라우저에서 `localhost:3000`이 열리며 Remotion Studio가 나타납니다. 이 Studio는 After Effects나 Premiere의 타임라인과 유사한 미리보기 환경을 제공합니다.

### ② Composition 등록

src/Root.tsx에서 영상을 등록합니다.

```
import { Composition } from 'remotion';
import { MyVideo } from './MyVideo';

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="MyVideo"
      component={MyVideo}
      durationInFrames={150}  // 30fps 기준 5초
      fps={30}
      width={1920}
      height={1080}
    />
  );
};
```

`durationInFrames`는 **초 단위가 아닌 프레임 단위**입니다. 5초 영상을 만들려면 fps × 5 = 150을 입력합니다. 이 점을 놓치면 예상과 다른 길이의 영상이 생성됩니다.

### ③ 영상 컴포넌트 작성

Sequence를 사용해 여러 장면을 구성합니다.

```
import { AbsoluteFill, Sequence, useCurrentFrame, spring, useVideoConfig } from 'remotion';

export const MyVideo: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // spring 애니메이션으로 자연스러운 등장
  const scale = spring({ frame, fps, config: { damping: 100 } });

  return (
    <AbsoluteFill style={{ backgroundColor: '#0f0f0f' }}>
      {/* 0~60프레임: 인트로 */}
      <Sequence from={0} durationInFrames={60}>
        <div style={{ transform: `scale(${scale})`, color: 'white', fontSize: 80 }}>
          2024 연말결산
        </div>
      </Sequence>

      {/* 60~150프레임: 본문 */}
      <Sequence from={60}>
        <div style={{ color: 'white' }}>통계 데이터가 여기에</div>
      </Sequence>
    </AbsoluteFill>
  );
};
```

`AbsoluteFill`은 영상 전체를 채우는 컨테이너입니다. `Sequence`의 `from`은 해당 장면이 시작되는 프레임 번호입니다.

### ④ 렌더링

개발이 완료되면 MP4로 내보냅니다.

```
npx remotion render src/index.ts MyVideo out/video.mp4
```

로컬에서 렌더링하면 CPU를 많이 사용합니다. 2시간짜리 영상은 일반 PC에서 상당한 시간이 소요됩니다. 이때 Remotion Lambda를 사용하면 AWS에서 병렬 처리되어 2시간 영상도 12분 만에 렌더링이 가능합니다.

---

## 모범사례/패턴 비교

| 사용 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **로컬 렌더링** | 설정 간단, 비용 없음 | 긴 영상은 시간 오래 걸림 |
| **Remotion Lambda** | 병렬 처리로 빠름, 확장성 | AWS 설정 필요, 사용량 기반 과금 |
| **Remotion Player** | 웹앱에 영상 임베드 가능 | 최종 MP4 렌더링은 별도 필요 |
| **Cloud Run** | GCP 환경 지원 | 현재 Alpha 단계 |

실제 서비스에 적용한다면 **Remotion Player로 미리보기 + Lambda로 최종 렌더링** 조합이 일반적입니다. GitHub Unwrapped(연말 개발자 통계 영상)가 이 구조로 수백만 개의 개인화 영상을 생성한 대표 사례입니다.

라이선스 측면에서, 개인 및 3인 이하 조직은 무료입니다. 4인 이상 기업은 월 $100부터 시작하는 Company License가 필요합니다.

---

## 마치며

- Remotion은 React 컴포넌트를 실제 MP4 영상으로 변환하는 프레임워크로, 웹 개발 지식만으로 영상 제작이 가능합니다.
- `useCurrentFrame`, `Sequence`, `spring` 등 핵심 개념을 이해하면 데이터 기반 맞춤 영상을 대량으로 자동 생성할 수 있습니다.
- 실전 팁: `npx create-video@latest`로 프로젝트를 만들고, 간단한 텍스트 애니메이션부터 시작해보세요.

---

## 참고자료

- Remotion 공식 문서 (<https://www.remotion.dev/docs/>)
- Remotion GitHub 저장소 (<https://github.com/remotion-dev/remotion>)
- Remotion Lambda 가이드 (<https://www.remotion.dev/lambda>)
- LogRocket - Remotion Framework 튜토리얼 (<https://blog.logrocket.com/remotion-a-framework-for-making-videos-in-react/>)
