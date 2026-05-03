---
title: "?️ Qwen3-TTS, ElevenLabs보다 정확한 오픈소스 음성합성 모델이 나왔다"
date: 2026-01-23T23:01:42+09:00
slug: "989-Qwen3-TTS-ElevenLabs보다-정확한-오픈소스-음성합성-모델이-나왔다"
original_url: "https://memoryhub.tistory.com/989"
tistory_id: 989
draft: false
---

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ██████╗ ██╗    ██╗███████╗███╗   ██╗██████╗               ║
║   ██╔═══██╗██║    ██║██╔════╝████╗  ██║╚════██╗              ║
║   ██║   ██║██║ █╗ ██║█████╗  ██╔██╗ ██║ █████╔╝              ║
║   ██║▄▄ ██║██║███╗██║██╔══╝  ██║╚██╗██║ ╚═══██╗              ║
║   ╚██████╔╝╚███╔███╔╝███████╗██║ ╚████║██████╔╝              ║
║    ╚══▀▀═╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═══╝╚═════╝               ║
║                                                              ║
║              ████████╗████████╗███████╗                      ║
║              ╚══██╔══╝╚══██╔══╝██╔════╝                      ║
║                 ██║      ██║   ███████╗                      ║
║                 ██║      ██║   ╚════██║                      ║
║                 ██║      ██║   ███████║                      ║
║                 ╚═╝      ╚═╝   ╚══════╝                      ║
║                                                              ║
║     [ 3-Second Voice Cloning | 97ms Ultra-Low Latency ]      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

# 

음성 클로닝 서비스에 월 수십만 원을 지불하고 계신가요? 유튜브 나레이션, 게임 NPC 음성, 고객센터 TTS를 위해 비싼 API 요금을 감당하고 계신가요? 2026년 1월, 알리바바 Qwen 팀이 공개한 Qwen3-TTS는 이 판도를 완전히 뒤집었습니다.

500만 시간 이상의 음성 데이터로 학습된 이 모델은 ElevenLabs와 MiniMax를 벤치마크에서 앞서면서도,

**Apache 2.0 라이선스로 완전히 무료**입니다.

**한줄요약:** 결론부터 말하면, Qwen3-TTS는 3초 음성 클로닝, 자연어 음성 디자인, 97ms 초저지연을 갖춘 오픈소스 TTS로, 상용 서비스 수준의 품질을 무료로 제공합니다.

## 배경

TTS 시장은 오랫동안 양분되어 있었습니다. 한쪽에는 ElevenLabs, MiniMax 같은 고품질 유료 서비스가, 다른 쪽에는 품질이 아쉬운 오픈소스 모델이 있었죠. 개발자들은 "품질을 원하면 돈을 내고, 무료를 원하면 품질을 포기하라"는 선택지밖에 없었습니다.

Qwen3-TTS는 이 공식을 깨뜨렸습니다. 알리바바 클라우드의 Qwen 팀은 2026년 1월 22일, 10개 언어와 9개 중국어 방언을 지원하는 TTS 모델 시리즈를 공개했습니다. 더 놀라운 점은 벤치마크 결과입니다.

> Qwen3-TTS는 텍스트를 음성으로 변환할 때 발생하는 단어 오류율(WER)에서 ElevenLabs와 MiniMax를 능가하며, 상용 서비스 수준의 자연스러움을 구현한 오픈소스 음성합성 모델입니다.

## 왜 Qwen3-TTS인가

기존 오픈소스 TTS와 Qwen3-TTS의 차이는 단순한 품질 개선이 아닙니다. 근본적인 아키텍처 혁신이 있습니다.

첫째, **Dual-Track LM 아키텍처**입니다. 기존 TTS는 언어 모델(LM)이 텍스트를 처리한 뒤, 별도의 Diffusion 모델이 음성을 생성하는 방식이었습니다. 이 과정에서 정보 손실과 지연이 발생했죠. Qwen3-TTS는 단일 모델 내에서 텍스트 입력과 오디오 출력을 동시에 스트리밍 처리합니다. 한 글자만 입력되어도 즉시 음성 출력이 시작되는 것이 가능한 이유입니다.

둘째, **Qwen3-TTS-Tokenizer-12Hz**입니다. 음성을 디지털로 변환할 때 초당 몇 개의 토큰으로 표현하느냐가 품질과 속도를 결정합니다. Qwen3-TTS는 초당 12.5개 토큰이라는 극단적인 압축률을 달성하면서도 음성의 감정, 억양, 화자 특성을 온전히 보존합니다. 덕분에 경량 ConvNet만으로도 고품질 음성 재구성이 가능해졌고, 첫 패킷 전송 지연이 97ms까지 줄었습니다.

셋째, **자연어 음성 제어**입니다. "따뜻하고 부드러운 30대 남성 목소리로 천천히 말해줘"라고 입력하면, 모델이 해당 특성의 음성을 생성합니다. 미리 정의된 음성 프리셋에서 고르는 것이 아니라, 원하는 음성을 자연어로 설계할 수 있습니다.

## 핵심 기능 3가지

### 1. 3초 음성 클로닝 (Voice Clone)

3초 분량의 음성 샘플만 있으면 해당 화자의 목소리를 복제할 수 있습니다. 복제된 음성은 10개 언어로 합성이 가능합니다. 한국어로 녹음한 음성을 영어, 일본어, 독일어로 말하게 할 수 있다는 뜻입니다.

Seed-TTS 벤치마크에서 Qwen3-TTS-12Hz-1.7B-Base 모델은 영어 WER 1.24%를 기록했습니다. 이는 CosyVoice 3(1.45%), MiniMax-Speech(1.65%)보다 낮은 수치입니다.

### 2. 음성 디자인 (Voice Design)

존재하지 않는 음성을 자연어 설명만으로 생성합니다. "17세 남성, 테너 음역대, 긴장하면 발음이 살짝 경직되는 목소리"라고 입력하면, 모델이 해당 특성의 가상 음성을 만들어냅니다.

InstructTTSEval 벤치마크에서 Qwen3-TTS-12Hz-1.7B-VoiceDesign 모델은 설명-음성 일관성(DSD) 81.1점을 기록하며, GPT-4o-mini-tts(52.3점)와 Hume(75.3점)을 크게 앞섰습니다.

### 3. 97ms 초저지연 스트리밍

실시간 대화 AI, 라이브 더빙, 인터랙티브 음성 응답(IVR) 시스템에서 지연은 치명적입니다. Qwen3-TTS는 첫 음성 패킷을 97ms 만에 출력합니다. 일반적인 TTS가 300ms 이상 걸리는 것과 비교하면 체감 속도 차이가 큽니다.

## 모델 구성과 선택 가이드

| 모델명 | 파라미터 | 주요 기능 | 권장 용도 |
| --- | --- | --- | --- |
| Qwen3-TTS-12Hz-1.7B-CustomVoice | 17억 | 9종 프리미엄 음색 + 자연어 스타일 제어 | 프로덕션 TTS, 다양한 캐릭터 음성 |
| Qwen3-TTS-12Hz-1.7B-VoiceDesign | 17억 | 자연어 음성 설계 | 새로운 음성 캐릭터 생성 |
| Qwen3-TTS-12Hz-1.7B-Base | 17억 | 3초 음성 클로닝, 파인튜닝 베이스 | 특정 화자 복제, 커스텀 모델 개발 |
| Qwen3-TTS-12Hz-0.6B-CustomVoice | 6억 | 9종 프리미엄 음색 | 리소스 제한 환경, 경량 배포 |
| Qwen3-TTS-12Hz-0.6B-Base | 6억 | 3초 음성 클로닝 | 경량 음성 클로닝 |

CustomVoice 모델에는 한국어 네이티브 화자(Sohee)를 포함한 9종의 프리미엄 음색이 내장되어 있습니다. 한국어, 영어, 일본어, 중국어 네이티브 화자가 모두 포함되어 있어 아시아 시장 서비스에 적합합니다.

## 실습: Python으로 음성 생성하기

개발 환경부터 구축합니다.

① **환경 설정**

```
conda create -n qwen3-tts python=3.12 -y
conda activate qwen3-tts
pip install -U qwen-tts
pip install -U flash-attn --no-build-isolation  # GPU 메모리 최적화
```

② **CustomVoice로 한국어 음성 생성**

```
# Python 3.12, qwen-tts 최신 버전
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)

wavs, sr = model.generate_custom_voice(
    text="안녕하세요, Qwen3-TTS로 생성한 한국어 음성입니다.",
    language="Korean",
    speaker="Sohee",  # 한국어 네이티브 여성 화자
    instruct="따뜻하고 친근한 어조로",
)
sf.write("korean_output.wav", wavs[0], sr)
```

실행 결과: `korean_output.wav` 파일이 생성됩니다. Sohee 음색의 따뜻한 한국어 음성이 저장됩니다.

③ **3초 음성 클로닝**

```
# Python 3.12, qwen-tts 최신 버전
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-Base",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)

# 3초 분량의 참조 음성과 해당 텍스트
ref_audio = "reference_voice.wav"  # 로컬 파일 또는 URL
ref_text = "이것은 참조 음성의 원본 텍스트입니다."

wavs, sr = model.generate_voice_clone(
    text="복제된 음성으로 새로운 문장을 합성합니다.",
    language="Korean",
    ref_audio=ref_audio,
    ref_text=ref_text,
)
sf.write("cloned_output.wav", wavs[0], sr)
```

실행 결과: 참조 음성의 화자 특성이 반영된 새로운 음성이 `cloned_output.wav`로 저장됩니다.

④ **음성 디자인으로 가상 캐릭터 음성 생성**

```
# Python 3.12, qwen-tts 최신 버전
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)

wavs, sr = model.generate_voice_design(
    text="오늘 날씨가 정말 좋네요. 산책하기 딱 좋은 날이에요.",
    language="Korean",
    instruct="20대 초반 여성, 밝고 경쾌한 음색, 약간 높은 톤으로 활기차게",
)
sf.write("designed_voice.wav", wavs[0], sr)
```

실행 결과: 자연어 설명에 맞는 가상 캐릭터 음성이 생성됩니다.

## 성능 비교: 상용 서비스 vs Qwen3-TTS

| 언어 | Qwen3-TTS-12Hz-1.7B | MiniMax | ElevenLabs |
| --- | --- | --- | --- |
| 중국어 WER | 0.928% | 2.252% | 16.026% |
| 영어 WER | 0.934% | 2.164% | 2.339% |
| 한국어 WER | 1.755% | 1.747% | 1.865% |
| 일본어 WER | 3.823% | 3.519% | 10.646% |

WER(Word Error Rate)은 낮을수록 좋습니다. Qwen3-TTS는 대부분의 언어에서 상용 서비스와 동등하거나 더 나은 성능을 보입니다. 특히 중국어에서 ElevenLabs 대비 17배 낮은 오류율을 기록한 점이 눈에 띕니다.

## 적용 시나리오별 모범사례

| 시나리오 | 권장 모델 | 설정 팁 |
| --- | --- | --- |
| 유튜브 나레이션 | CustomVoice 1.7B | 일관된 음색 유지를 위해 단일 speaker 고정 |
| 게임 NPC 다양한 캐릭터 | VoiceDesign 1.7B | 캐릭터별 자연어 설명 템플릿 미리 작성 |
| 고객센터 IVR | CustomVoice 0.6B | 낮은 지연이 중요하면 경량 모델 사용 |
| 오디오북 특정 성우 스타일 | Base 1.7B + 파인튜닝 | 성우의 장시간 샘플로 파인튜닝 |
| 실시간 AI 대화 | CustomVoice + 스트리밍 모드 | `stream=True` 설정으로 97ms 지연 활용 |

## 마치며

- Qwen3-TTS는 3초 음성 클로닝, 자연어 음성 디자인, 97ms 초저지연을 Apache 2.0 라이선스로 제공하는 오픈소스 TTS입니다.
- 벤치마크에서 ElevenLabs, MiniMax 등 상용 서비스와 동등하거나 더 나은 성능을 보이며, 특히 중국어와 영어에서 두드러집니다.
- 실전 팁: 오늘 당장 `pip install qwen-tts` 명령으로 설치하고, 한국어 네이티브 화자 Sohee로 첫 음성을 생성해보세요.

## 참고자료

- Qwen3-TTS GitHub (<https://github.com/QwenLM/Qwen3-TTS>)
- Qwen3-TTS Technical Report (<https://arxiv.org/abs/2601.15621>)
- Alibaba Cloud Model Studio TTS 문서 (<https://www.alibabacloud.com/help/en/model-studio/qwen-tts>)
- Hugging Face Qwen3-TTS Demo (<https://huggingface.co/spaces/Qwen/Qwen3-TTS-Demo>)
