---
title: "? Cloudflare Tunnel, 포트 개방 없이 서버를 외부에 공개하는 방법"
date: 2025-10-06T15:20:22+09:00
slug: "836-Cloudflare-Tunnel-포트-개방-없이-서버를-외부에-공개하는-방법"
original_url: "https://memoryhub.tistory.com/836"
tistory_id: 836
draft: false
---

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     ? CLOUDFLARE TUNNEL                                 ║
    ║                                                           ║
    ║     ┌─────────┐                      ┌─────────────┐     ║
    ║     │  Your   │ ◄──── Outbound ────► │ Cloudflare  │     ║
    ║     │ Server  │      Connection      │   Network   │     ║
    ║     └─────────┘                      └─────────────┘     ║
    ║         │                                   ▲            ║
    ║         │ No Open Ports                     │            ║
    ║         │ No Public IP                      │ HTTPS      ║
    ║         ▼                                   │            ║
    ║     ? Firewall                        ? Users         ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
```

# 

집에서 운영하는 홈서버를 외부에서 접속하고 싶지만, 공유기 포트포워딩이 귀찮거나 보안이 걱정된 적 있으신가요? 아니면 개발 중인 로컬 앱을 팀원에게 보여주려고 ngrok을 켰는데, URL이 계속 바뀌어서 불편했던 경험은요?

**Cloudflare Tunnel은 서버의 포트를 전혀 열지 않고도 외부에서 안전하게 접근할 수 있게 해주는 역방향 터널링 기술입니다.** 이 글에서 그 원리와 장점을 명확하게 정리해 드리겠습니다.

**한줄요약:** 결론부터 말하면, Cloudflare Tunnel은 서버가 먼저 Cloudflare에 연결을 요청하는 "아웃바운드 전용" 방식으로, 방화벽 포트를 열지 않고도 웹서버, SSH, 원격 데스크톱 등을 안전하게 외부에 노출할 수 있는 무료 터널링 서비스입니다.

## 배경

전통적으로 외부에서 내부 서버에 접근하려면 두 가지 방법이 일반적이었습니다. 포트포워딩은 공유기에서 특정 포트를 열어 외부 요청을 내부 서버로 전달하는 방식이고, VPN은 가상 사설망을 통해 내부 네트워크에 접속하는 방식입니다.

문제는 두 방식 모두 **서버의 IP 주소가 외부에 노출**된다는 점입니다. 이는 DDoS 공격, 포트 스캐닝, 무차별 대입 공격의 표적이 될 수 있습니다. 또한 가정용 인터넷은 대부분 동적 IP를 사용하므로 DDNS 설정도 필요합니다.

> Cloudflare Tunnel은 서버가 Cloudflare에 "먼저 연결을 걸어" 통신 경로를 만드는 역방향 프록시 기술입니다.

이 개념을 우체국에 비유해 보겠습니다. 기존 방식이 "집 주소를 공개하고 누구나 찾아오게 하는 것"이라면, Cloudflare Tunnel은 "내가 우체국 사서함을 등록하고, 우체국이 대신 배달해주는 것"과 같습니다. 집 주소(서버 IP)는 숨기면서, 우체국(Cloudflare)을 통해서만 소통하는 방식입니다.

## 핵심 개념

Cloudflare Tunnel의 작동 원리는 "아웃바운드 전용 연결"이라는 한 문장으로 요약됩니다.

일반적인 웹 서버는 외부에서 들어오는 인바운드 연결을 기다립니다. 80번, 443번 포트를 열어두고 클라이언트의 요청을 수신합니다. 반면 Cloudflare Tunnel은 정반대입니다. 서버 측에서 설치한 `cloudflared`라는 경량 데몬이 Cloudflare의 글로벌 네트워크로 **먼저 아웃바운드 연결을 생성**합니다.

대부분의 방화벽은 아웃바운드 트래픽을 기본적으로 허용합니다. `cloudflared`는 이 특성을 활용합니다. 서버에서 Cloudflare로 나가는 연결이 성공하면, 이 터널을 통해 양방향 통신이 가능해집니다. 외부 사용자의 요청은 Cloudflare를 거쳐 이 터널을 통해 내부 서버로 전달됩니다.

구체적인 동작 흐름은 다음과 같습니다.

**첫째**, 서버에 `cloudflared` 데몬을 설치하고 실행합니다.

**둘째**, `cloudflared`가 Cloudflare 엣지 서버와 TLS 핸드셰이크를 수행하여 암호화된 WebSocket 연결을 생성합니다.

**셋째**, Cloudflare DNS에 터널과 연결된 도메인을 등록합니다.

**넷째**, 사용자가 해당 도메인으로 접속하면, 요청이 Cloudflare 네트워크를 거쳐 터널을 통해 내부 서버로 전달됩니다.

이 방식의 핵심 보안 이점은 **서버의 방화벽에서 모든 인바운드 트래픽을 차단**해도 된다는 것입니다. 오직 `cloudflared`의 아웃바운드 연결만 허용하면, Cloudflare를 우회한 직접 공격은 원천적으로 불가능해집니다.

## 실습

Cloudflare Tunnel을 설정하는 가장 간단한 방법을 단계별로 정리합니다.

### ① cloudflared 설치

운영체제별 설치 명령이 다릅니다.

```
# macOS (Homebrew)
brew install cloudflare/cloudflare/cloudflared

# Ubuntu/Debian
curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg > /dev/null
echo 'deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared $(lsb_release -cs) main' | sudo tee /etc/apt/sources.list.d/cloudflared.list
sudo apt update && sudo apt install cloudflared

# Docker
docker run cloudflare/cloudflared:latest tunnel --no-autoupdate run --token <YOUR_TOKEN>
```

설치 후 `cloudflared --version`으로 정상 설치를 확인합니다.

### ② 빠른 테스트 (TryCloudflare)

계정 없이도 임시 터널을 즉시 생성할 수 있습니다. 로컬에서 3000번 포트로 개발 서버가 실행 중이라면 다음과 같이 입력합니다.

```
cloudflared tunnel --url http://localhost:3000
```

실행하면 `https://random-words.trycloudflare.com` 형태의 임시 URL이 생성됩니다. 이 URL로 외부에서 로컬 서버에 접속할 수 있습니다. 테스트나 데모 용도로 유용하지만, URL이 매번 바뀌므로 영구적 사용에는 적합하지 않습니다.

### ③ 영구 터널 생성 (대시보드 방식)

고정 도메인으로 영구 터널을 만들려면 Cloudflare 계정과 해당 도메인이 필요합니다.

Cloudflare 대시보드에서 Zero Trust 메뉴로 이동합니다. Networks 하위의 Tunnels를 선택하고 Create a tunnel을 클릭합니다. 터널 이름을 지정하면 설치 명령어와 토큰이 제공됩니다. 해당 명령어를 서버에서 실행하면 터널이 생성됩니다. 이후 Public Hostnames 탭에서 원하는 서브도메인과 로컬 서비스 주소를 매핑합니다.

예를 들어 `app.mydomain.com`을 `http://localhost:3000`으로, `api.mydomain.com`을 `http://localhost:8000`으로 각각 연결할 수 있습니다. DNS 레코드는 자동으로 생성됩니다.

## 모범사례/패턴 비교

| 구분 | Cloudflare Tunnel | ngrok | 포트포워딩 |
| --- | --- | --- | --- |
| 비용 | 무료 (무제한 대역폭) | 무료 티어 제한적, 커스텀 도메인 유료 | 무료 |
| 커스텀 도메인 | 무료 지원 | 유료 플랜 필요 | DDNS 별도 설정 필요 |
| 설정 복잡도 | 중간 (계정/도메인 필요) | 낮음 (즉시 사용 가능) | 높음 (라우터 설정 필요) |
| 보안 | 매우 높음 (IP 미노출, DDoS 보호) | 높음 | 낮음 (IP 노출) |
| 프로토콜 | HTTP, HTTPS, SSH, RDP, TCP | HTTP, TCP | 모든 프로토콜 |
| 안정성 | 높음 (글로벌 엣지 네트워크) | 중간 | 중간 |

ngrok은 빠른 테스트에 적합하고, Cloudflare Tunnel은 프로덕션 수준의 안정성과 무료 커스텀 도메인이 필요할 때 강점을 보입니다. 포트포워딩은 특별한 의존성 없이 모든 프로토콜을 지원하지만 보안 취약점이 존재합니다.

## 마치며

- Cloudflare Tunnel은 서버가 먼저 외부로 연결하는 "아웃바운드 전용" 방식으로, 인바운드 포트 없이 서비스를 외부에 공개합니다.
- 무료 티어에서도 커스텀 도메인, 무제한 대역폭, DDoS 보호, SSL 인증서가 포함됩니다.
- 실전 팁: 오늘 당장 `cloudflared tunnel --url http://localhost:포트번호` 명령어로 로컬 서버를 외부에 공개해보세요.

## 참고자료

- Cloudflare Tunnel 공식 문서 (<https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>)
- Zero Trust Dashboard 가이드 (<https://blog.cloudflare.com/ridiculously-easy-to-use-tunnels/>)
- cloudflared GitHub 저장소 (<https://github.com/cloudflare/cloudflared>)
