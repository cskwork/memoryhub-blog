---
title: "Comprehensive Ollama Configuration Guide for API Hosting in Local Environments"
date: 2025-03-02T22:41:12+09:00
slug: "460-로컬-환경에서-API-호스팅을-위한-Ollama-설정-종합-가이드"
original_url: "https://memoryhub.tistory.com/460"
tistory_id: 460
draft: false
---

## 1 | What is Ollama?

- **Offline LLM**: Run large language models on your personal PC without internet
- **Simple CLI**: Intuitive commands like `ollama pull·run·ps·stop`
- **REST API**: Default port 11434, provides endpoints like `/api/generate·chat`
- **Automatic CPU·GPU Acceleration**: Supports NVIDIA CUDA·Apple Silicon Metal
- **Model Lifecycle Management**: Built-in download·run·stop·delete

## 2 | System Requirements

| Category | Minimum | Recommended |
| --- | --- | --- |
| RAM | **8 GB** (7B model) | **16 GB+** (13B model) |
| GPU | Optional | NVIDIA CUDA ≥ 11 or Apple Silicon GPU |
| Storage | 4 GB (binary) + model size ¹ | 50 GB+ SSD |
| OS | macOS 12+, Ubuntu 22.04+, Windows 10 64-bit |  |
| ¹ Example) 7B GGUF-Q4 ~4-5 GB, 13B is 8-10 GB. |  |  |

## 3 | Installation

### macOS

```
# Script installation
curl -fsSL https://ollama.com/install.sh | sh
# Or Homebrew
brew install ollama
```

### Linux (Ubuntu Example)

```
curl -fsSL https://ollama.com/install.sh | sh
```

Service registration (optional):

```
sudo systemctl enable --now ollama
```

### Windows

1. Download installer file (.exe) from <https://ollama.com/download>
2. After installation, run **Ollama Desktop** or run `ollama serve` in terminal

## 4 | Basic CLI

```
# Download model
ollama pull llama3:8b
# Check loaded model
ollama ps
# Interactive run
ollama run llama3:8b
# Stop execution
ollama stop llama3:8b
```

## 5 | API Server Configuration

- `ollama serve` → Binds to `http://127.0.0.1:11434`
- Remote exposure example

```
# All interfaces + default port
OLLAMA_HOST=0.0.0.0 ollama serve
# Specify host + port simultaneously
OLLAMA_HOST=0.0.0.0:8000 ollama serve
```

### systemd Sample

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

## 6 | Quick REST API Examples

```
# Generate response
curl http://localhost:11434/api/generate \
     -d '{"model":"llama3:8b","prompt":"What is machine learning?"}'
# Chat
curl http://localhost:11434/api/chat \
     -d '{"model":"llama3:8b","messages":[{"role":"user","content":"What is AI?"}]}'
# List local models
curl http://localhost:11434/api/tags
# Download model
curl -X POST http://localhost:11434/api/pull -d '{"name":"phi3:mini"}'
```

## 7 | Python Integration

```
pip install ollama          # Official PyPI
```

```
import ollama
resp = ollama.generate(model="llama3:8b", prompt="What is AI?")
print(resp["response"])
```

Streaming:

```
for chunk in ollama.generate(model="llama3:8b", prompt="Write a poem", stream=True):
    print(chunk["response"], end="", flush=True)
```

## 8 | Performance Tips

- **Model Size**: For hardware constraints, choose 7B → 3B series
- **Quantization**: Save VRAM with lower precision like `llama3:8b-q4_K_M`
- **Context Length**
- `ollama run llama3:8b --parameters num_ctx=2048`
- **Temperature·Batch**
- `ollama run llama3:8b --parameters temperature=0.1,num_batch=128`

## 9 | Security Guide

- Local-only by default. For remote exposure, consider **TLS reverse proxy + Basic Auth**
- Block port 11434 with firewall
- Verify untrusted GGUF/Modelfile before use

## 10 | Troubleshooting FAQ

| Symptom | Solution |
| --- | --- |
| 404 or connection failure | Check if `ollama serve` is running·firewall |
| GPU not used | Check driver & CUDA version |
| Out of memory | Use smaller/quantized model or reduce num_ctx |
| Change model download path | `export OLLAMA_MODELS=/path` then restart |

---

## 11 | Reference Links

- GitHub README & API Docs: <https://github.com/ollama/ollama>
- Python Package: <https://pypi.org/project/ollama/>
- FAQ (ENV Configuration): <https://github.com/ollama/ollama/blob/main/docs/faq.md>
