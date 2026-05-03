---
title: "? Stable Diffusion, 모델 3대장 분석: Base, Refiner, LoRA 파헤치기"
date: 2024-11-23T23:51:53+09:00
slug: "408-Stable-Diffusion-모델-3대장-분석-Base-Refiner-LoRA-파헤치기"
original_url: "https://memoryhub.tistory.com/408"
tistory_id: 408
draft: false
categories: ["데브 유틸"]
tags: ["Stable Diffusion"]
---

```
                    +-----------------+
                    |      BASE       |
                    |      MODEL      |
                    +--------+--------+
                             |
                             v
+------------+      +-----------------+      +----------+
|    LoRA    |----->|   Image Gen     |----->| Refiner  |
|  (Style)   |      |   (Denoising)   |      | (Detail) |
+------------+      +-----------------+      +----------+
                             |
                             v
                    +-----------------+
                    |  FINAL  IMAGE  |
                    +-----------------+
```

Stable Diffusion으로 그림을 뽑다 보면 이런 경험, 다들 한 번쯤 있으시죠? "분명 같은 프롬프트를 썼는데, 왜 어제랑 다른 그림이 나오지?", "모델을 바꿨더니 화풍은 좋은데 캐릭터 얼굴이 무너지네..." 저도 처음에는 체크포인트, LoRA, VAE 등등 쏟아지는 용어들 속에서 길을 잃곤 했습니다.

이 글은 바로 그런 분들을 위해 준비했습니다. Stable Diffusion 이미지 생성의 핵심을 이루는 Base Model, Refiner, LoRA의 역할을 명확히 구분하고, 언제 어떻게 사용해야 최고의 결과물을 얻을 수 있는지 알려드립니다.

⚡ **TL;DR**

- **Base Model (체크포인트):** 이미지의 뼈대를 만드는 기본 모델입니다. 어떤 Base를 쓰냐에 따라 그림의 전반적인 스타일과 품질이 결정됩니다.
- **Refiner & LoRA:** Base Model 위에 추가하는 '업그레이드 파츠'입니다. Refiner는 디테일을, LoRA는 특정 스타일이나 캐릭터를 더합니다.

---

### 목차

1. 배경: 왜 이렇게 모델 종류가 많을까?
2. 핵심 개념 정리: Base, Refiner, LoRA 완전 정복
3. 실전 활용법: 언제 어떻게 써야 할까?
4. 한눈에 보는 비교: 베스트 프랙티스
5. 마치며 & 참고자료

---

## 1. 배경: 왜 이렇게 모델 종류가 많을까?

Stable Diffusion은 텍스트 프롬프트를 이미지로 변환하는 강력한 오픈소스 AI 모델입니다[1]. 핵심 원리는 간단합니다. 완전한 노이즈(잡음) 상태의 이미지에서 점차 노이즈를 제거하며 우리가 원하는 이미지를 '드러내는' 방식이죠[2][3].

이때, 어떤 스타일의 노이즈를 어떻게 제거할지를 학습한 데이터 덩어리가 바로 **모델**입니다. 사용자들이 특정 화풍(애니메이션, 실사 등)이나 특정 캐릭터, 의상 등을 더 잘 그리도록 기존 모델을 추가로 학습시키면서 수많은 파생 모델이 생겨났습니다[4].

✅ **관련 용어 정리**

- **체크포인트(Checkpoint):** 모델의 학습된 가중치를 저장한 파일(.ckpt, .safetensors)로, 보통 Base Model을 지칭합니다[1].
- **Latent Space (잠재 공간):** 이미지를 고차원 픽셀 공간이 아닌, 특징만 압축된 저차원 공간에서 다룹니다. Stable Diffusion은 이 잠재 공간에서 노이즈 제거 작업을 수행하여 메모리 효율을 높입니다[5][3].
- **U-Net:** 노이즈 예측을 담당하는 Stable Diffusion의 핵심 신경망 구조입니다[6]. LoRA는 이 U-Net의 일부를 수정하여 작동합니다[6].
- **Cross-Attention (교차 인지):** 텍스트 프롬프트의 의미와 이미지의 시각적 요소를 연결하는 중요한 부분입니다[7][8]. LoRA가 주로 이 부분을 미세 조정합니다[7][2].

## 2. 핵심 개념 정리: Base, Refiner, LoRA 완전 정복

### **Base Model (기반 모델, 체크포인트)**

> **이미지 생성의 모든 것, 그 시작과 끝을 책임지는 '뼈대'**

베이스 모델은 이미지 생성의 가장 근간이 되는 모델입니다[1]. 어떤 베이스 모델을 선택하느냐에 따라 생성되는 이미지의 전반적인 화풍, 품질, 피사체 표현 능력이 결정됩니다[4][1]. Stability AI가 공개한 `v1.4`, `SDXL` 등이 대표적인 공식 베이스 모델이며, 전 세계 개발자들이 이를 기반으로 특정 스타일에 특화된 수천 개의 커스텀 모델을 만들어 공유하고 있습니다[4].

- **역할:** 텍스트 프롬프트를 해석해 전반적인 이미지의 구성과 스타일을 설정합니다[2].
- **특징:** 용량이 2GB에서 7GB에 달할 정도로 크며, 방대한 데이터를 학습한 결과물입니다[7][6]. 실사, 반실사, 애니메이션 등 특정 장르에 특화된 모델들이 많습니다[1].

### **Refiner (리파이너)**

> **화룡점정, 이미지의 디테일을 끌어올리는 '마감 전문가'**

Refiner는 이름 그대로 이미지를 '정제'하고 '개선'하는 역할을 합니다[9]. 주로 SDXL 모델과 함께 사용되며, 베이스 모델이 이미지의 전체적인 구성을 80% 정도 완성하면, 나머지 20%의 마무리 단계에서 투입됩니다[10][9]. 노이즈가 거의 제거된 상태에서 작동하며, 이미지의 질감, 눈매, 주름 등 미세한 디테일을 보완해 완성도를 높입니다[10][9][3].

- **역할:** 베이스 모델이 생성한 이미지의 세부 묘사를 강화하고 품질을 향상시킵니다[9][3].
- **작동 원리:** 이미지 생성 과정의 마지막 노이즈 제거 단계(low-noise steps)에 개입하여 이미지를 더 정교하게 다듬습니다[10].
- **주의사항:** 효과가 미미하게 느껴질 수도 있으며, Refiner를 적용하는 과정에서 시간이 추가로 소요될 수 있습니다[9].

### **LoRA (Low-Rank Adaptation)**

> **원하는 스타일만 쏙! 가볍고 유연한 '스타일 필터'**

LoRA는 거대한 베이스 모델 전체를 재학습시키는 대신, 모델의 일부(주로 Cross-Attention 레이어)에 소규모 신경망을 덧붙여 미세 조정하는 기법입니다[7][8]. 덕분에 원본 모델을 그대로 두면서 특정 캐릭터의 외형, 옷 스타일, 그림체 등을 '주입'할 수 있습니다[6][11].

- **역할:** 베이스 모델에 특정 스타일, 캐릭터, 의상, 포즈 등을 추가로 적용하는 플러그인 같은 역할을 합니다[11].
- **장점:**
  - **작은 파일 크기:** 2~200MB 수준으로, 체크포인트 모델의 1/10 ~ 1/100 크기라 부담 없이 수집하고 사용할 수 있습니다[7].
  - **유연성:** 베이스 모델을 손상시키지 않는 '플러그 앤 플레이' 방식이라 여러 LoRA를 조합하거나 가중치를 조절해 세밀하게 적용할 수 있습니다[6].
- **비유:** LoRA는 마치 카메라 앱의 '필터'와 같습니다. 원본 사진(베이스 모델의 결과물)에 필터(LoRA)를 씌워 독특한 분위기를 연출하는 것과 비슷합니다[6].

## 3. 실전 활용법: 언제 어떻게 써야 할까?

실제 이미지 생성 과정에서 이 세 가지 컴포넌트는 다음과 같이 활용됩니다.

**① 기본 이미지 생성 (Base Model)**

모든 작업의 시작입니다. 만들고 싶은 이미지 스타일에 맞는 베이스 모델(체크포인트)을 먼저 고릅니다.

**② 특정 스타일 적용 (LoRA)**

베이스 모델만으로는 표현하기 힘든 특정 캐릭터나 의상을 그리고 싶을 때 LoRA를 사용합니다. 프롬프트 창에 `` 형식으로 추가하여 적용합니다[11].

```
# diffusers 라이브러리에서 LoRA 가중치 로드 예시
# 먼저 기본 파이프라인(Base Model)을 로드합니다.
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)

# 그 다음, pipe의 U-Net에 LoRA 가중치를 불러옵니다.
# 이 한 줄만으로 LoRA가 적용됩니다.
pipe.unet.load_attn_procs("path/to/your/lora/weights")
pipe.to("cuda")

# 이제 프롬프트를 실행하면 LoRA 스타일이 적용된 이미지가 생성됩니다.
image = pipe("A pokemon with green eyes", num_inference_steps=25).images[0]
```

**③ 디테일 강화 (Refiner)**

SDXL 베이스 모델을 사용했다면, Refiner를 추가로 적용해 이미지 품질을 한 단계 더 끌어올릴 수 있습니다. WebUI에서는 Refiner 선택 메뉴에서 해당 모델을 지정해주기만 하면 됩니다[9].

```
# diffusers 라이브러리에서 Base + Refiner 앙상블 파이프라인 예시

# n_steps: 전체 노이즈 제거 스텝 수
# high_noise_frac: 전체 스텝 중 Base 모델이 담당할 비율 (높은 노이즈 구간)
n_steps = 40
high_noise_frac = 0.8 # Base 모델이 80%, Refiner가 20%를 담당

# Base 모델을 먼저 실행
image = base(
    prompt=prompt,
    num_inference_steps=n_steps,
    denoising_end=high_noise_frac, # 0.8 지점까지만 노이즈 제거
    output_type="latent",
).images

# Base의 결과물을 받아 Refiner가 나머지 구간을 처리
image = refiner(
    prompt=prompt,
    num_inference_steps=n_steps,
    denoising_start=high_noise_frac, # 0.8 지점부터 시작
    image=image,
).images[0]
```

## 4. 한눈에 보는 비교: 베스트 프랙티스

| 컴포넌트 | 역할 | 장점 | 주의점 |
| --- | --- | --- | --- |
| **Base Model** | 이미지의 뼈대와 전반적인 스타일을 결정하는 핵심 모델[1][2] | 원하는 화풍의 이미지를 안정적으로 생성 가능 | 파일 크기가 매우 크고(2~7GB), 특정 디테일 표현에는 한계가 있을 수 있음[7][12] |
| **Refiner** | 생성된 이미지의 디테일과 선명도를 향상시키는 후처리 모델[9][3] | 이미지의 완성도를 높여줌 | SDXL 등 특정 모델과 함께 사용해야 하며, 변화가 미미하거나 처리 시간이 늘어날 수 있음[9] |
| **LoRA** | 특정 콘셉트(캐릭터, 의상, 화풍)를 주입하는 가벼운 추가 모델[7][11] | 파일이 작고(2~200MB) 유연하며, 여러 개를 조합해 사용 가능[7] | 가중치를 너무 높게 주면 이미지가 깨질 수 있고, 베이스 모델과 궁합이 중요함[12] |

## 5. 마치며

이제 Base Model, Refiner, LoRA의 차이가 명확해지셨나요?

- **Base Model**로 원하는 그림의 큰 그림을 그리고,
- **LoRA**로 내가 원하는 캐릭터나 스타일이라는 '색'을 입히고,
- **Refiner**로 디테일이라는 '광택'을 내는 과정을 기억하세요.

실제 프로젝트에 적용할 때는 먼저 다양한 베이스 모델을 테스트하며 자신의 스타일에 맞는 '주력 모델'을 찾고, 그 위에 필요한 LoRA들을 하나씩 더해가며 자신만의 레시피를 만들어가는 것이 좋습니다. 이 세 가지를 자유자재로 다루게 된다면 여러분도 Stable Diffusion의 '조물주'가 될 수 있을 겁니다[11].

이 글이 여러분의 창작 활동에 도움이 되셨다면 **❤️ 하트**와 **댓글** 부탁드립니다!

---

**참고자료**

- Hugging Face Docs: Stable Diffusion XL
- Stable Diffusion - 체크포인트 모델에 관한 모든 것 (internetmap.kr)
- Stable Diffusion - LoRA 모델 사용법 (internetmap.kr)

[1] <https://aitoolhub.tistory.com/37>  
[2] <https://velog.io/@king_of_potato/Stable-Diffusion-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0>  
[3] <https://mvje.tistory.com/257>  
[4] <https://www.internetmap.kr/entry/Stable-Diffusion-Everything-about-models>  
[5] <https://ffighting.net/deep-learning-paper-review/diffusion-model/stable-diffusion/>  
[6] <https://generative-ai-everything.tistory.com/entry/Stable-Diffusion-LoRA-%EA%B8%B0%EB%B3%B8-%EA%B0%80%EC%9D%B4%EB%93%9C1>  
[7] <https://www.internetmap.kr/entry/How-to-LoRA-Model>  
[8] <https://dhpark1212.tistory.com/entry/LoRA-for-Efficient-Stable-Diffusion-Fine-Tuning>  
[9] <https://flatsun2.com/17740/>  
[10] <https://huggingface.co/docs/diffusers/v0.26.2/ko/api/pipelines/stable_diffusion/stable_diffusion_xl>  
[11] <https://softwind.tistory.com/entry/stable-diffusion-Lora-%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC>  
[12] <https://richdaddy101.com/%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%83%9D%EC%84%B1-ai-2024%EB%85%84-%EC%B5%9C%EC%8B%A0-15%EA%B0%80%EC%A7%80-stable-diffusion-%EC%B6%94%EC%B2%9C-%EB%AA%A8%EB%8D%B8/>  
[13] <https://ai-designer-allan.tistory.com/entry/SD-15-refiner-%EB%AA%A8%EB%8D%B8-%ED%99%9C%EC%9A%A9-%EB%B0%A9%EB%B2%95>  
[14] <https://www.youtube.com/watch?v=afsJPn1ZdXc&vl=ko>  
[15] <https://marcus-story.tistory.com/55>  
[16] <https://fastcampus.co.kr/media_data_sdxl>  
[17] <https://www.youtube.com/watch?v=1uyYkyGy0hY>  
[18] <https://leeporter.tistory.com/entry/Stable-Diffusion%EC%8A%A4%ED%85%8C%EC%9D%B4%EB%B8%94-%EB%94%94%ED%93%A8%EC%A0%84-WebUI-06-Lora-%EC%82%AC%EC%9A%A9>  
[19] <https://ai-designer-allan.tistory.com/entry/%EC%8A%A4%ED%85%8C%EC%9D%B4%EB%B8%94-%EB%94%94%ED%93%A8%EC%A0%84-Checkpoint-lora-vae-embedding-%EC%99%84%EB%B2%BD%EC%A0%95%EB%A6%AC>  
[20] <https://www.toolify.ai/ko/ai-news-kr/lora-stable-diffusion-ai-3495603>  
[21] <https://www.youtube.com/watch?v=e7r_xT-sM4o>  
[22] <https://www.youtube.com/watch?v=uO5kX4-hc30>  
[23] <https://www.reddit.com/r/StableDiffusion/comments/15amidh/do_we_really_need_the_refiner_for_sdxl/?tl=ko>  
[24] <https://hipposdata.tistory.com/85>  
[25] <https://ffighting.net/deep-learning-paper-review/diffusion-model/diffusion-model-basic/>  
[26] <https://velog.io/@luis_j/17%EC%9D%BC%EC%B0%A8-%EA%B0%95%EC%9D%98-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%83%9D%EC%84%B1-AI-Stable-Diffusion>  
[27] <https://pitas.tistory.com/9>  
[28] <https://aws.amazon.com/ko/blogs/tech/finetune-text2image-amazon-sagemaker-jumpstart-stable-diffusion/>  
[29] <https://wikidocs.net/233899>  
[30] <https://www.internetmap.kr/entry/StableDiffusion-The-Basics-of-ComfyUI-3>  
[31] <https://ai.shop2world.net/stable-diffusion-%EC%98%B5%EC%85%98-%EC%84%A4%EB%AA%85-%EB%B0%8F-txt2img-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-1/>  
[32] <https://arca.live/b/aiart/88328675>  
[33] <http://blog.rksna.com/index.php?route=blog%2Fpost&post_id=14>  
[34] <https://blog.naver.com/trend-checker/223176207007>  
[35] <https://selgyun.tistory.com/entry/Stable-Diffusion-%EB%A1%9C%EB%9D%BCLora-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EC%A0%81%EC%9A%A9%ED%95%98%EB%8A%94-%EB%B2%95-SD-5>  
[36] <https://contentstailor.com/entry/LoRA%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8-Stable-Diffusion-Fine-Tuning>  
[37] <https://kimjy99.github.io/%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/lcm-lora/>
