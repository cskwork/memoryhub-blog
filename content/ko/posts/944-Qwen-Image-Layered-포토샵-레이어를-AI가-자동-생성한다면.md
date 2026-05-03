---
title: "? Qwen-Image-Layered, 포토샵 레이어를 AI가 자동 생성한다면?"
date: 2025-12-22T01:08:05+09:00
slug: "944-Qwen-Image-Layered-포토샵-레이어를-AI가-자동-생성한다면"
original_url: "https://memoryhub.tistory.com/944"
tistory_id: 944
draft: false
---

```
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║      ┌─────┐   AI    ┌─────┐  ┌─────┐  ┌─────┐   ║
    ║      │IMAGE│  ────►  │ L1  │  │ L2  │  │ L3  │   ║
    ║      │ RGB │  LAYER  │RGBA │  │RGBA │  │RGBA │   ║
    ║      └─────┘         └─────┘  └─────┘  └─────┘   ║
    ║                                                   ║
    ║        QWEN-IMAGE-LAYERED : DECOMPOSITION        ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
```

포토샵에서 이미지 편집할 때 가장 번거로운 작업이 뭘까요? 바로 객체 선택과 마스킹입니다. 배경에서 인물을 분리하고, 텍스트만 따로 빼내고, 그림자를 별도로 조정하려면 최소 30분에서 1시간은 걸립니다. 알리바바 Qwen 팀이 2025년 12월 19일 공개한 Qwen-Image-Layered는 이 과정을 AI가 2~5분 만에 처리합니다. **하나의 평면 이미지를 여러 개의 투명**

**RGBA 레이어로 자동 분해해, 각 요소를 독립적으로 편집할 수 있게 만드는 기술**입니다.

**한줄요약:** 결론부터 말하면, Qwen-Image-Layered는 이미지를 포토샵처럼 여러 레이어로 자동 분해해 각 요소를 독립 편집할 수 있게 하는 오픈소스 AI 모델이다.

## 배경

기존 AI 이미지 편집 도구들은 공통적인 한계를 가지고 있었습니다. 래스터 이미지의 "얽힘(entangled)" 특성 때문입니다.

> 한 줄 정의: 래스터 이미지는 모든 시각적 요소가 단일 캔버스에 융합되어 있어, 한 부분을 수정하면 다른 부분에도 영향을 미친다.

예를 들어 인물 사진에서 배경만 바꾸려고 하면, AI가 인물의 얼굴 특징을 미묘하게 변형시키거나(시맨틱 드리프트), 인물의 위치나 크기가 살짝 어긋나는(기하학적 불일치) 문제가 발생합니다. 이것이 바로 AI 이미지 편집의 "일관성 문제"입니다.

반면 포토샵 같은 전문 디자인 도구는 레이어 구조를 사용합니다. 배경, 인물, 텍스트가 각각 분리된 레이어에 있으니 한 레이어만 수정해도 나머지는 그대로 유지됩니다. Qwen-Image-Layered는 이 원리를 AI에 적용했습니다. 단일 RGB 이미지를 입력하면, 의미적으로 분리된 여러 RGBA 레이어를 자동 생성합니다.

## 핵심 기술 구조

Qwen-Image-Layered는 세 가지 핵심 구성요소로 작동합니다.

**첫째, RGBA-VAE입니다.** RGB(색상 정보)와 RGBA(색상+투명도 정보) 이미지를 통합된 잠재 공간에서 처리할 수 있게 합니다. 일반 이미지와 투명도를 가진 레이어 이미지가 같은 언어로 소통하는 번역기 역할입니다.

**둘째, VLD-MMDiT(Variable Layers Decomposition MMDiT)입니다.** 고정된 레이어 수가 아닌, 이미지 복잡도에 따라 3개에서 8개 이상까지 유동적으로 레이어를 생성합니다.

**셋째, Multi-stage Training 전략입니다.** 기존 이미지 생성 모델을 점진적으로 다층 이미지 분해기로 변환합니다. 학습 데이터는 실제 포토샵 문서(PSD)에서 추출한 고품질 다층 이미지를 사용했습니다. 이 부분이 중요한데, 실제 디자이너들이 작업한 레이어 구조를 학습했기 때문에 의미적 분리가 정확합니다.

## 실습

**1. 환경 설정**

Python 3.10 이상, transformers 4.51.3 이상, 최소 8GB VRAM GPU가 필요합니다. 권장 사양은 24GB VRAM입니다.

```
pip install diffusers transformers torch
```

**2. 기본 사용법 (Python / diffusers)**

```
from diffusers import QwenImageLayeredPipeline
import torch
from PIL import Image

# 모델 로드
pipeline = QwenImageLayeredPipeline.from_pretrained("Qwen/Qwen-Image-Layered")
pipeline = pipeline.to("cuda", torch.bfloat16)

# 이미지 분해
image = Image.open("product.png").convert("RGBA")
inputs = {
    "image": image,
    "layers": 4,                    # 생성할 레이어 수
    "resolution": 640,              # 640 또는 1024
    "num_inference_steps": 50,
    "true_cfg_scale": 4.0,
}

with torch.inference_mode():
    output = pipeline(**inputs)

# 각 레이어 저장
for i, layer in enumerate(output.images[0]):
    layer.save(f"layer_{i}.png")
```

실행 결과로 layer\_0.png(배경), layer\_1.png(주요 객체), layer\_2.png(전경 요소), layer\_3.png(텍스트/장식)처럼 분리된 RGBA 파일들이 생성됩니다.

**3. 분해된 레이어 편집**

분해 후에는 Qwen-Image-Edit를 연동해 개별 레이어를 편집할 수 있습니다. 예를 들어 배경 레이어만 선택해 색상을 변경하거나, 인물 레이어를 다른 사람으로 교체해도 나머지 요소는 완벽하게 유지됩니다.

**4. 재귀적 분해**

특정 레이어가 여전히 복잡하다면 해당 레이어만 다시 분해할 수 있습니다. 이론적으로 무한 분해가 가능해 세밀한 편집 작업에 유용합니다.

## 기존 도구와 비교

| 도구 | 장점 | 한계 |
| --- | --- | --- |
| **Qwen-Image-Layered** | 자동 레이어 분해, 숨겨진 영역 자동 복원, 무료 오픈소스 | GPU 필요, 수동 레이어 지정 불가 |
| **Photoshop** | 정밀한 수동 제어, 전문 기능 풍부 | 구독료 월 $22.99, 수동 마스킹 필요 |
| **Remove.bg** | 빠른 배경 제거, 쉬운 사용 | 배경/전경 2개 레이어만, 유료 |
| **인페인팅 모델** | 특정 영역 채우기 | 레이어 분리 아닌 영역 수정만 |

Remove.bg 같은 도구는 전경과 배경 두 개로만 분리하지만, Qwen-Image-Layered는 텍스트, 그림자, 여러 객체를 각각 독립 레이어로 분리합니다. 또한 전경 객체 뒤에 가려진 배경 영역을 AI가 자연스럽게 채워넣는 "숨겨진 영역 복원" 기능도 포함되어 있습니다.

## 실무 활용 시나리오

**제품 사진 다변화:** 제품 사진 1장을 분해한 뒤, 배경 레이어만 교체해 10개 이상의 상품 이미지를 빠르게 생성합니다. 촬영 비용 절감 효과가 큽니다.

**웹툰/만화 제작:** 말풍선, 캐릭터, 배경을 분리해 각각 편집하거나 애니메이션용 스프라이트로 활용합니다. 색 번짐 문제 없이 깔끔한 투명 배경 스프라이트 제작이 가능합니다.

**영상 편집 전처리:** 영상 프레임을 레이어로 분해해 특정 객체만 제거하거나 이동시킬 때 활용합니다.

## 마치며

- Qwen-Image-Layered는 단일 이미지를 여러 RGBA 레이어로 자동 분해해 포토샵 수준의 독립 편집을 가능하게 합니다.
- Apache 2.0 라이선스로 상업적 사용이 자유롭고, Hugging Face와 ModelScope에서 즉시 사용 가능합니다.
- 실전 팁: 간단한 제품 사진부터 시작해 layers=3~4로 테스트해보고, 결과물의 레이어 분리 품질을 확인해보세요.

## 참고자료

- Qwen-Image-Layered 공식 GitHub (<https://github.com/QwenLM/Qwen-Image-Layered>)
- Hugging Face 모델 페이지 (<https://huggingface.co/Qwen/Qwen-Image-Layered>)
- 논문: Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition (<https://arxiv.org/abs/2512.15603>)
- ComfyUI 워크플로우 가이드 (<https://comfyui-wiki.com/ko/news/2025-12-19-qwen-image-layered-release>)
