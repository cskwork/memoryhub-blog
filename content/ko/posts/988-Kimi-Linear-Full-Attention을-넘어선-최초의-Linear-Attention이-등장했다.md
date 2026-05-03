---
title: "? Kimi Linear, Full Attention을 넘어선 최초의 Linear Attention이 등장했다"
date: 2026-01-23T22:57:08+09:00
slug: "988-Kimi-Linear-Full-Attention을-넘어선-최초의-Linear-Attention이-등장했다"
original_url: "https://memoryhub.tistory.com/988"
tistory_id: 988
draft: false
---

```
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║     ██╗  ██╗██╗███╗   ███╗██╗                        ║
║     ██║ ██╔╝██║████╗ ████║██║                        ║
║     █████╔╝ ██║██╔████╔██║██║                        ║
║     ██╔═██╗ ██║██║╚██╔╝██║██║                        ║
║     ██║  ██╗██║██║ ╚═╝ ██║██║                        ║
║     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝                        ║
║                                                       ║
║     ██╗     ██╗███╗   ██╗███████╗ █████╗ ██████╗     ║
║     ██║     ██║████╗  ██║██╔════╝██╔══██╗██╔══██╗    ║
║     ██║     ██║██╔██╗ ██║█████╗  ███████║██████╔╝    ║
║     ██║     ██║██║╚██╗██║██╔══╝  ██╔══██║██╔══██╗    ║
║     ███████╗██║██║ ╚████║███████╗██║  ██║██║  ██║    ║
║     ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ║
║                                                       ║
║     [ Selective Forget + Precise Update = O(n) ]     ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

"Linear Attention은 빠르지만 성능이 떨어진다"는 AI 업계의 통념이 있었습니다. 100만 토큰을 처리할 때 Full Attention은 메모리가 폭발하고, Linear Attention은 정보를 잃어버리는 딜레마가 있었기 때문입니다. 그런데 2025년 10월, Moonshot AI가 이 공식을 깨뜨렸습니다. **Kimi Linear는 공정한 비교에서 Full Attention의 성능을 능가하면서도, 메모리는 75% 절감하고 디코딩 속도는 6배 향상시켰습니다.** 도대체 어떻게 불가능해 보이던 두 마리 토끼를 잡았을까요?

**한줄요약:** 결론부터 말하면, Kimi Linear는 '채널별 선택적 망각'과 '델타 룰 기반 정밀 업데이트'를 결합한 Kimi Delta Attention(KDA)으로, 효율성과 성능의 트레이드오프를 처음으로 극복한 하이브리드 아키텍처다.

---

## 배경: Transformer의 아킬레스건, O(n²)의 저주

Transformer의 핵심인 Softmax Attention은 강력하지만 치명적인 약점이 있습니다. 시퀀스 길이 n에 대해 연산량이 n²으로 증가한다는 점입니다.

> Softmax Attention은 모든 토큰이 다른 모든 토큰을 참조하기 때문에 문맥 이해력이 뛰어나지만, 시퀀스가 길어지면 연산량과 메모리가 기하급수적으로 증가한다.

구체적인 예시로 살펴보겠습니다. 1,000개 토큰을 처리할 때 약 100만 번의 연산이 필요합니다. 그런데 100만 토큰을 처리한다면 연산 횟수는 1조 번으로 폭발합니다. 여기에 KV Cache라는 메모리 비용까지 선형으로 증가하니, 긴 문맥 처리는 사실상 벽에 부딪힙니다.

이 문제를 해결하기 위해 **Linear Attention**이 제안되었습니다. 핵심 아이디어는 Softmax 연산을 제거하고, Query와 Key의 연산 순서를 바꿔 O(n)의 선형 복잡도를 달성하는 것입니다. 그러나 Linear Attention에도 근본적인 한계가 있었습니다.

---

## Linear Attention의 딜레마: 무한정 쌓이는 기억

Linear Attention을 호텔 컨시어지에 비유해 보겠습니다. Full Attention 컨시어지는 모든 손님의 대화를 완벽하게 녹음합니다. 정확하지만 녹음 테이프가 무한정 필요합니다. 반면 Linear Attention 컨시어지는 하나의 메모장에 정보를 계속 덧씁니다. 공간은 절약되지만 문제가 있습니다. **오래된 정보를 지울 수 없습니다.**

기술적으로 말하면, Linear Attention은 Key-Value 쌍을 행렬 형태의 "상태(State)"에 누적합니다. 새 정보는 계속 더해지지만, 이전 정보를 삭제하는 메커니즘이 없습니다. 시퀀스가 길어질수록 상태가 포화되고, 최근 정보와 과거 정보가 뒤섞여 "검색 오류"가 누적됩니다.

신경과학자 David Eagleman의 말을 빌리면, "기억의 적은 시간이 아니라 다른 기억들이다."

Linear Attention이 바로 이 문제에 직면했습니다.

---

## Kimi Delta Attention(KDA): 선택적 망각의 과학

Kimi Linear의 핵심은 **Kimi Delta Attention(KDA)**입니다. KDA는 기존 Gated DeltaNet을 개선한 Linear Attention 모듈로, 두 가지 핵심 메커니즘을 결합합니다.

**첫째, Delta Rule 기반 정밀 업데이트입니다.** Delta Rule은 신경망 학습의 고전적 원리로, "예측값과 목표값의 차이(Delta)만큼 가중치를 조정한다"는 개념입니다. 아이에게 과녁 맞추기를 가르치는 상황을 생각해 보세요. 화살이 왼쪽으로 빗나갔다면 오른쪽으로 조준을 수정하라고 알려줍니다. 빗나간 정도(Delta)에 비례해서 수정하는 것입니다.

KDA는 이 원리를 메모리 업데이트에 적용합니다. 새로운 Key-Value가 들어오면, 기존 상태에서 해당 Key와 연관된 이전 Value를 먼저 "삭제"하고, 새로운 Value로 "교체"합니다. 단순히 더하는 것이 아니라 **덮어쓰기**가 가능해진 것입니다.

**둘째, 채널별 세분화 게이팅입니다.** 기존 Gated DeltaNet은 각 Attention Head마다 하나의 망각률(α)을 사용했습니다. 그러나 KDA는 각 특징 채널마다 별도의 망각률을 부여합니다. 호텔 컨시어지가 "손님 이름은 빨리 잊어도 되지만, 알레르기 정보는 오래 기억해야 한다"고 구분하는 것과 같습니다.

수식으로 표현하면 다음과 같습니다.

```
S_t = (I - β_t × k_t × k_t^T) × Diag(α_t) × S_(t-1) + β_t × k_t × v_t^T
```

여기서 **Diag(α\_t)**가 채널별 망각률을 나타내는 대각 행렬입니다. 단일 스칼라 대신 채널마다 다른 α 값을 사용해 메모리를 더 정밀하게 제어합니다.

---

## 하이브리드 아키텍처: 3:1의 황금비율

KDA가 아무리 강력해도 Linear Attention에는 본질적 한계가 있습니다. 정확한 메모리 검색과 복사(copy) 작업에서 Full Attention보다 취약합니다. Kimi Linear는 이를 보완하기 위해 **하이브리드 아키텍처**를 채택했습니다.

구체적으로, KDA 레이어 3개마다 Multi-Head Latent Attention(MLA) 레이어 1개를 배치합니다. MLA는 DeepSeek-V2에서 도입된 효율적인 Full Attention 변형으로, KV Cache를 압축해 메모리 효율을 높인 방식입니다.

| 아키텍처 | Train PPL | Val PPL | 특징 |
| --- | --- | --- | --- |
| Full Attention (0:1) | 9.45 | 5.77 | 기준선 |
| KDA:MLA = 1:1 | 9.29 | 5.66 | 균등 혼합 |
| **KDA:MLA = 3:1** | **9.23** | **5.65** | 최적 비율 |
| KDA:MLA = 7:1 | 9.23 | 5.70 | 효율 우선 |
| KDA:MLA = 15:1 | 9.34 | 5.82 | 품질 저하 시작 |

3:1 비율이 성능과 효율성의 최적 균형점입니다. 이 구성으로 **KV Cache를 75% 절감**하면서도

Full Attention 대비 더 낮은 Perplexity를 달성합니다.

흥미로운 점은 Kimi Linear가 MLA 레이어에서 위치 인코딩(Positional Encoding)을 사용하지 않는다는 것입니다.

모든 위치 정보 처리를 KDA 레이어에 위임했습니다. 이는 아키텍처 단순화와 함께 연산 효율성 향상에도 기여합니다.

---

## 벤치마크 결과: 숫자가 증명하는 성능

Kimi Linear는 1.4조 토큰으로 학습한 48B 파라미터(3B 활성화) 모델입니다. 동일한 학습 레시피로 Full Attention MLA 및 Gated DeltaNet Hybrid(GDN-H)와 비교한 결과가 놀랍습니다.

**일반 태스크 성능에서** MMLU-Pro, BBH, GPQA-Diamond 등 전 영역에서 Kimi Linear가 최고점을 기록했습니다. 특히 어려운 추론 벤치마크인 GPQA-Diamond에서 MLA 대비 2.1% 향상을 보였습니다.

**수학 및 코딩 태스크에서** AIME 2025, HMMT 2025, LiveCodeBench 등 난이도 높은 벤치마크에서도 우위를 점했습니다. RL 학습 시 수렴 속도도 MLA보다 빨랐습니다. MATH500에서 Kimi Linear는 최종 정확도 90%를 달성한 반면, MLA는 84%에 그쳤습니다.

**128K 긴 문맥 태스크에서** RULER 벤치마크 84.3점, RepoQA 68.5점으로 MLA와 GDN-H를 큰 차이로 앞섰습니다. 긴 문맥에서의 선택적 정보 검색 능력이 뛰어나다는 의미입니다.

**추론 효율성 측면에서** 100만 토큰 문맥 기준, 디코딩 처리량이 Full Attention 대비 6배 향상되었습니다. Token Per Output Time(TPOT)도 대폭 감소해 실시간 서비스 적용 가능성이 높아졌습니다.

---

## 실습: Kimi Linear 모델 사용하기

Moonshot AI는 모델 체크포인트와 KDA 커널을 오픈소스로 공개했습니다. Hugging Face와 vLLM을 통해 바로 사용할 수 있습니다.

**1. 환경 설정**

권장 환경은 Python 3.10 이상, PyTorch 2.4 이상, CUDA 12.4입니다. transformers 라이브러리가 trust\_remote\_code를 지원해야 합니다.

**2. 모델 로드 및 추론**

```
# Python 3.10+, transformers 최신 버전 필요
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "moonshotai/Kimi-Linear-48B-A3B-Instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Kimi Linear의 핵심 혁신은 무엇인가요?"}
]

input_ids = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

output = model.generate(inputs=input_ids, max_new_tokens=500)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

**3. vLLM을 통한 API 서버 배포**

프로덕션 환경에서는 vLLM을 사용해 OpenAI 호환 API 엔드포인트를 구축할 수 있습니다. vLLM 최신 버전이 Kimi Linear를 공식 지원합니다.

---

## 아키텍처 비교: Full Attention vs Linear Attention vs Kimi Linear

| 항목 | Full Attention | 기존 Linear Attention | Kimi Linear (KDA) |
| --- | --- | --- | --- |
| 시간 복잡도 | O(n²) | O(n) | O(n) |
| KV Cache 증가 | 선형 증가 | 고정 | 고정 (75% 절감) |
| 망각 메커니즘 | 없음 (전체 보존) | 없음 (누적만) | 채널별 선택적 망각 |
| 정밀 업데이트 | 완전 재계산 | 불가 | Delta Rule 기반 |
| 긴 문맥 성능 | 우수 | 저하 | Full Attention 능가 |
| 추론 속도 | 기준선 | 3배 이상 | 6배 이상 |

Kimi Linear의 핵심 차별점은 **효율성 향상이 성능 저하로 이어지지 않았다**는 점입니다. 기존 Linear Attention의 "빠르지만 부정확하다"는 공식을 깨뜨렸습니다.

---

## 마치며

- Kimi Linear는 Kimi Delta Attention(KDA)을 통해 Linear Attention의 고질적 문제인 "정보 포화"를 해결했습니다. 채널별 세분화 게이팅과 Delta Rule 업데이트가 핵심입니다.
- 3:1 KDA-MLA 하이브리드 구조로 KV Cache 75% 절감, 디코딩 6배 속도 향상을 달성하면서도 Full Attention 성능을 능가했습니다. 이는 공정한 비교에서 Linear Attention이 Full Attention을 이긴 최초의 사례입니다.
- 실전 팁: 오픈소스 체크포인트가 공개되어 있으니, 긴 문맥 처리가 필요한 프로젝트에서 Kimi Linear를 테스트해 보세요. vLLM 지원으로 프로덕션 배포도 가능합니다.

---

## 참고자료

- Kimi Linear: An Expressive, Efficient Attention Architecture - arXiv (<https://arxiv.org/abs/2510.26692>)
- MoonshotAI/Kimi-Linear - GitHub (<https://github.com/MoonshotAI/Kimi-Linear>)
- moonshotai/Kimi-Linear-48B-A3B-Instruct - Hugging Face (<https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct>)
- Gated Delta Networks: Improving Mamba2 with Delta Rule - ICLR 2025 (<https://arxiv.org/abs/2412.06464>)
- Flash Linear Attention Library (<https://github.com/fla-org/flash-linear-attention>)
