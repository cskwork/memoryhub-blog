---
title: "LLMs.txt"
date: 2025-08-05T07:23:03+09:00
slug: "738-LLMs-txt"
original_url: "https://memoryhub.tistory.com/738"
tistory_id: 738
draft: false
---

## 1. LLMs.txt란 무엇인가?

- **정의** – LLMs.txt는 웹사이트 루트(/llms.txt)에 두는 간단한 마크다운 파일로, AI 언어 모델이 사이트의 콘텐츠를 쉽고 정확하게 이해할 수 있도록 도와주는 **AI 전용 사이트맵**입니다. 로봇 검색엔진을 위한 robots.txt처럼, LLM을 위해 정보를 간결하게 구조화해 제공합니다.
- **필요성** – LLM은 HTML·JavaScript 등 복잡한 요소를 포함한 웹 페이지를 모두 읽기 어렵습니다. llms.txt는 사이트의 목적과 구조, 주요 문서를 요약해 LLM의 컨텍스트 윈도우를 효율적으로 사용하게 합니다.

## 2. LLMs.txt 파일 구조

llms.txt는 반드시 마크다운 형식을 사용하며 다음과 같은 요소를 포함해야 합니다:

1. **H1 제목** – 첫 줄에 사이트나 프로젝트 이름을 #으로 시작하여 작성합니다.
2. **요약 블록 (Blockquote)** – > 기호로 사이트의 간략한 소개를 적습니다. 핵심 정보만 포함하도록 간결하게 씁니다.
3. **상세 정보** – 중요 주의사항, 특징, 사용 지침 등 추가 정보를 단락이나 리스트 형태로 제공합니다.
4. **링크 목록 섹션** – ## 제목을 사용하여 관련 리소스 목록을 구분합니다. 각 항목은 [링크 제목](URL): 간단한 설명 형식으로 작성합니다.
5. **선택적 섹션(옵셔널)** – 덜 중요한 정보는 ## Optional 섹션에 넣습니다. LLM은 이 섹션을 스킵해도 됩니다.

## 3. 작성 시 고려해야 할 팁

- **간결성과 명확성** – 불필요한 용어를 피하고 핵심 정보를 선별합니다.
- **링크 설명** – 링크마다 간단한 설명을 붙여 LLM이 문서의 용도를 이해할 수 있게 합니다.
- **테스트** – 작성 후 Claude, GPT 등 LLM에서 실제로 질문을 던져 제대로 작동하는지 확인합니다.

## 4. LLMs.txt 실제 활용 예제: 대한민국 민법

아래 예시는 민법 관련 웹사이트가 /llms.txt에 게재할 수 있는 예시입니다. 실제로는 민법 조문을 마크다운 .md 파일 형태로 작성하여 링크해야 합니다.

> **참고** – 민법에 대한 설명과 조문 정보는 Wikipedia의 “Civil Code of the Republic of Korea” 문서를 참조하였습니다.

```
# Korean Civil Act (민법)

> 대한민국 민법(Law No. 471, 1958)은 형법·헌법과 함께 대한민국의 3대 기본법 중 하나입니다. 민법은 총칙, 물권, 채권, 친족, 상속의 5편으로 구성되며:contentReference[oaicite:13]{index=13}, 민사 관계의 기본 규범을 제시합니다. 이 파일은 민법의 중요한 조문과 참고 문서를 안내합니다.

중요 사항:
- **제1조(법원)** – 민사에 관한 법률이 없으면 관습법을, 관습법도 없으면 조리(합리적 이치)를 적용한다는 ‘법원(法源) 규정’입니다:contentReference[oaicite:14]{index=14}.
- **제2조(신의성실)** – 권리의 행사와 의무의 이행은 신의에 좇아 성실히 해야 하며, 권리 남용을 금지합니다:contentReference[oaicite:15]{index=15}.
- **제303조(전세권)** – 물권편에서 규정하는 전세권은 보증금을 지급하고 타인의 부동산을 사용·수익할 수 있는 권리입니다:contentReference[oaicite:16]{index=16}.
- **제750조(불법행위)** – 타인에게 고의 또는 과실로 손해를 가한 자는 손해배상의 책임을 진다고 정의합니다:contentReference[oaicite:17]{index=17}.

## Parts of the Civil Act
- [총칙 (General Provisions)](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_1:_General_Provisions): 법원의 종류, 자연인·법인, 물건, 법률행위, 기간, 소멸시효 등 기본 규정:contentReference[oaicite:18]{index=18}.
- [물권 (Property Rights)](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_2:_Property_Rights): 소유권·점유권·전세권·질권·저당권 등 9개의 물권을 규정하고, 부동산 권리 변동은 등기로 효력이 발생함을 명시:contentReference[oaicite:19]{index=19}.
- [채권 (Claims)](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_3:_Claims): 계약, 사무관리, 부당이득, 불법행위 등 채권 관계를 규율하며, 제750조는 불법행위에 대한 손해배상 책임을 규정합니다:contentReference[oaicite:20]{index=20}.
- [친족 (Relatives)](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_4:_Relatives): 혼인, 부모와 자녀, 후견, 가족의 범위 등을 규정하며, 2005년 개정으로 호주제도(남성 가장 제도)가 폐지되었습니다:contentReference[oaicite:21]{index=21}.
- [상속 (Inheritance)](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_5._Inheritance): 상속의 개시, 상속인, 유언 및 유류분 등을 규율합니다:contentReference[oaicite:22]{index=22}.

## Optional
- [민법 전문 번역본 (비공식)](https://example.com/civil-act-en.md): 영어 번역본이며 최신 개정 내용은 반영되지 않을 수 있습니다.
- [신의성실 원칙 해설](https://en.wikipedia.org/wiki/Civil_Code_of_the_Republic_of_Korea#Part_1:_General_Provisions): 제2조 신의성실 원칙에 대한 설명:contentReference[oaicite:23]{index=23}.
```

위와 같이 llms.txt를 작성하여 사이트 루트에 배포하면, LLM 기반 검색 도구나 챗봇이 민법을 요약하거나 특정 조문에 대한 질문에 답할 때 참고할 수 있습니다. 민법의 각 편을 Markdown 형태의 .md 파일로 제공하면 AI가 직접 본문을 읽어 분석할 수 있으므로, 링크된 문서는 가능한 한 간단하고 명료하게 구성하는 것이 좋습니다.

## 5. 실제 사용 방법

1. **문서 준비** – 요약 정보와 각 조문을 마크다운 파일로 정리합니다. 예를 들어 general-provisions.md 파일에 총칙 내용을 정리합니다.
2. **llms.txt 작성** – 위 예시처럼 요약, 중요 조문, 링크 목록을 포함하는 llms.txt 파일을 만듭니다.
3. **서버 루트에 배포** – 웹사이트 루트(/)에 llms.txt를 업로드하고, 링크한 .md 파일들도 동일 도메인에 배포합니다.
4. **테스트** – Claude나 ChatGPT 등 LLM에서 <https://example.com/llms.txt>를 불러온 뒤 “제2조 신의성실 원칙을 설명해줘” 같이 질문하여 의도대로 동작하는지 확인합니다.

이러한 과정을 통해 법령이나 기술 문서를 LLM이 쉽게 이해하게 할 수 있으며, 사용자에게 보다 정확한 답변을 제공할 수 있습니다.
