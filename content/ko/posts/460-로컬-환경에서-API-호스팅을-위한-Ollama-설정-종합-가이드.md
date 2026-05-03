---
title: "로컬 환경에서 API 호스팅을 위한 Ollama 설정 종합 가이드"
date: 2025-03-02T22:41:12+09:00
slug: "460-로컬-환경에서-API-호스팅을-위한-Ollama-설정-종합-가이드"
original_url: "https://memoryhub.tistory.com/460"
tistory_id: 460
draft: false
---

## 1 | Ollama란?

- **오프라인 LLM** : 인터넷 없이 개인 PC에서 대규모 언어 모델 실행
- **간편 CLI** : `ollama pull·run·ps·stop` 등 직관적 명령어
- **REST API** : 11434 포트 기본, `/api/generate·chat` 등 엔드포인트 제공
- **CPU·GPU 자동 가속** : NVIDIA CUDA·Apple Silicon Metal 지원
- **모델 라이프사이클 관리** : 다운로드·실행·중지·삭제 내장

## 2 | 시스템 요구 사항

| 구분 | 최소 | 권장 |
| --- | --- | --- |
| RAM | **8 GB** (7B 모델) | **16 GB+** (13B 모델) |
| GPU | 선택사항 | NVIDIA CUDA ≥ 11 또는 Apple Silicon GPU |
| 저장공간 | 4 GB(바이너리) + 모델 크기 ¹ | 50 GB 이상 SSD |
| OS | macOS 12+, Ubuntu 22.04+, Windows 10 64‑bit |  |
| ¹ 예) 7B GGUF‑Q4 약 4‑5 GB, 13B는 8‑10 GB. |  |  |

## 3 | 설치

### macOS

```
# 스크립트 설치
curl -fsSL https://ollama.com/install.sh | sh
# 또는 Homebrew
brew install ollama
```

### Linux (Ubuntu 예시)

```
curl -fsSL https://ollama.com/install.sh | sh
```

서비스 등록(선택):

```
sudo systemctl enable --now ollama
```

### Windows

1. <https://ollama.com/download> 에서 설치 파일(.exe) 다운로드
2. 설치 후 **Ollama Desktop** 실행 또는 터미널에서 `ollama serve` 실행

## 4 | 기본 CLI

```
# 모델 내려받기
ollama pull llama3:8b
# 로드된 모델 확인
ollama ps
# 대화형 실행
ollama run llama3:8b
# 실행 중지
ollama stop llama3:8b
```

## 5 | API 서버 설정

- `ollama serve` → `http://127.0.0.1:11434`에 바인딩
- 원격 노출 예시

```
# 모든 인터페이스 + 기본 포트
OLLAMA_HOST=0.0.0.0 ollama serve
# 호스트+포트 동시 지정
OLLAMA_HOST=0.0.0.0:8000 ollama serve
```

### systemd 샘플

```
[Unit]
Description=Ollama Service
After=network.target

[Service]
Type=simple
User=ollama
Environment="OLLAMA_HOST=0.0.0.0"
ExecStart=/usr/local/bin/ollama serve
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## 6 | REST API 빠른 예시

```
# 응답 생성
curl http://localhost:11434/api/generate \
     -d '{"model":"llama3:8b","prompt":"기계학습이란?"}'
# 채팅
curl http://localhost:11434/api/chat \
     -d '{"model":"llama3:8b","messages":[{"role":"user","content":"AI란?"}]}'
# 로컬 모델 목록
curl http://localhost:11434/api/tags
# 모델 다운로드
curl -X POST http://localhost:11434/api/pull -d '{"name":"phi3:mini"}'
```

## 7 | Python 통합

```
pip install ollama          # PyPI 공식
```

```
import ollama
resp = ollama.generate(model="llama3:8b", prompt="AI란?")
print(resp["response"])
```

스트리밍:

```
for chunk in ollama.generate(model="llama3:8b", prompt="시를 써줘", stream=True):
    print(chunk["response"], end="", flush=True)
```

## 8 | 성능 팁

- **모델 크기** : 하드웨어 제약 시 7B → 3B 계열 선택
- **양자화** : `llama3:8b-q4_K_M` 등 낮은 정밀도로 VRAM 절감
- **컨텍스트 길이**
- `ollama run llama3:8b --parameters num_ctx=2048`
- **온도·배치**
- `ollama run llama3:8b --parameters temperature=0.1,num_batch=128`

## 9 | 보안 가이드

- 로컬 전용이 기본. 원격 노출 시 **TLS 리버스 프록시 + Basic Auth** 고려
- 방화벽로 11434 차단
- 신뢰할 수 없는 GGUF/Modelfile은 검증 후 사용

## 10 | 문제 해결 FAQ

| 증상 | 해결책 |
| --- | --- |
| 404 또는 연결 실패 | `ollama serve` 실행 여부·방화벽 확인 |
| GPU 미사용 | 드라이버 & CUDA 버전 확인 |
| 메모리 부족 | 더 작은/양자화 모델 또는 num\_ctx 축소 |
| 모델 다운로드 경로 변경 | export OLLAMA\_MODELS=/path 후 재시작 |

---

## 11 | 참고 링크

- GitHub README & API Docs: <https://github.com/ollama/ollama>
- Python 패키지: <https://pypi.org/project/ollama/>
- FAQ (ENV 설정): <https://github.com/ollama/ollama/blob/main/docs/faq.md>
