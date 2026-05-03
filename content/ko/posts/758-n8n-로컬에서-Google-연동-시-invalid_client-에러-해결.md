---
title: "n8n 로컬에서 Google 연동 시 invalid_client 에러 해결"
date: 2025-08-23T07:59:35+09:00
slug: "758-n8n-로컬에서-Google-연동-시-invalid_client-에러-해결"
original_url: "https://memoryhub.tistory.com/758"
tistory_id: 758
draft: false
---

로컬에서 **n8n ↔ Google(Drive/Docs/Sheets)** 연동을 시도하면, 콜백까지는 잘 돌아오는데 토큰 교환 단계에서 아래처럼 실패하는 경우가 많습니다.

```
Error: Client authentication failed (e.g., unknown client, no client authentication included, or unsupported authentication method)
{"error":"invalid_client","error_description":"Unauthorized"}
```

이 글은 위 오류를 **빠르게 진단하고 바로 해결**하는 실전 매뉴얼입니다. (n8n npx/Docker 모두 동일)

---

## 요약 (TL;DR)

- **문제 원인**: 구글 토큰 엔드포인트가 **클라이언트 인증**을 못 알아들어서 실패함.
- **정답 3가지**
  1. OAuth 클라이언트 **유형을 “웹 애플리케이션(Web application)”** 으로 만들기
  2. **Redirect URI** 를 n8n 콜백과 **완전히 동일**하게 등록: http://localhost:5678/rest/oauth2-credential/callback
  3. n8n 크리덴셜의 **Client authentication method = “Send in body”** (a.k.a. client\_secret\_post)

> code가 n8n으로 돌아왔다면 **리다이렉트 설정은 이미 성공**입니다. 그 뒤 **토큰 교환**에서 터진 것이므로 클라이언트 유형/시크릿/인증 방식부터 확인하세요.

---

## 증상 → 원인 빠른 매칭표

화면/로그에서 보이는 것 의미 조치

|  |  |  |
| --- | --- | --- |
| 콜백 URL에 ?code=...&scope=...가 붙어서 n8n으로 **돌아옴** | Redirect URI/client\_id는 정상 | 다음 단계(토큰 교환) 점검 |
| {"error":"invalid\_client","error\_description":"Unauthorized"} | 구글이 **클라이언트 인증**을 실패로 판정 | **웹 앱 클라이언트인지**, **시크릿 최신인지**, n8n에서 **Send in body** 사용했는지 확인 |
| 예전엔 되던 게 갑자기 invalid\_client | **클라이언트 시크릿 회전/변경** 후 n8n에 **미반영** | 새 시크릿을 n8n에 다시 저장 |
| redirect\_uri\_mismatch | 리다이렉트 URI 철자/포트/경로 불일치 | GCP와 n8n의 문자열을 **완전 동일**하게 맞춤 |

---

## 준비물

- Google Cloud 프로젝트 (APIs & Services 사용 가능)
- 활성화할 API: **Google Drive API**, (필요 시) **Google Docs API / Sheets API**
- 로컬 n8n (예: npx n8n 또는 Docker로 http://localhost:5678 실행)

---

## 1) Google Cloud에서 **웹 애플리케이션** 클라이언트 만들기

1. Google Cloud Console → **APIs & Services → Credentials**
2. **Create Credentials → OAuth client ID**
3. **Application type = Web application** 선택
4. **Authorized redirect URIs**에 아래 **정확히** 추가
5. http://localhost:5678/rest/oauth2-credential/callback
6. 생성 후 **Client ID / Client Secret** 복사

> **주의**: Consent Screen의 **Authorized domains**에는 localhost(포트 포함) 등록이 **안 됩니다.** 로컬 테스트는 **앱을 Testing 상태**로 두고, **Test users**에 본인 구글 계정을 추가하면 충분합니다.

---

## 2) n8n에서 크리덴셜 설정

n8n 에디터 → **Credentials**에서 다음 중 하나를 씁니다.

- **Google Drive/Docs/Sheets** 전용 크리덴셜, 또는
- **OAuth2 API**(Generic) 크리덴셜

### 공통 입력값

- **Auth URL**: <https://accounts.google.com/o/oauth2/v2/auth>
- **Token URL**: <https://oauth2.googleapis.com/token>
- **Client ID / Client Secret**: (방금 GCP에서 생성한 값)
- **Scope**(필요한 것만 공백 구분)
  - Drive 파일 전체: <https://www.googleapis.com/auth/drive>
  - n8n이 만든 파일만: <https://www.googleapis.com/auth/drive.file>
  - Docs: <https://www.googleapis.com/auth/documents>
- **Client Authentication**: **Send in body** (a.k.a. client\_secret\_post)
- **Callback URL**(n8n가 표시하는 값): http://localhost:5678/rest/oauth2-credential/callback

> 포인트: 구글 토큰 엔드포인트는 client\_secret\_basic(헤더) 방식보다 **바디 전송**이 호환성이 좋습니다. n8n에서 “Send in body”로 두세요.

---

## 3) 동작 확인 절차

1. **Connect**를 눌러 구글 로그인 → 동의하면 n8n으로 돌아옵니다.
2. 실패하면 **n8n 로그**와 **브라우저 주소창**을 확인:
   - 주소창에 ?code=...가 있으면 **리다이렉트 OK**
   - 이후 invalid\_client면 **ID/Secret/인증방식**을 재점검

### (선택) 수동 토큰 교환 테스트

아래 curl로 바로 토큰 교환을 시도해 **자격 증명 자체를 검증**합니다.

```
curl -X POST https://oauth2.googleapis.com/token \
  -d code=PASTE_CODE_HERE \
  -d client_id=PASTE_CLIENT_ID \
  -d client_secret=PASTE_CLIENT_SECRET \
  -d redirect_uri=http://localhost:5678/rest/oauth2-credential/callback \
  -d grant_type=authorization_code
```

- 여기서도 invalid\_client면 **클라이언트 유형(웹 앱)** 또는 **시크릿** 문제가 거의 확실합니다.

---

## 4) 흔한 실수 체크리스트

- OAuth 클라이언트를 **Desktop**으로 만들었다 → **Web application**으로 다시 생성
- **Client secret**을 회전했는데 n8n에 **예전 값**이 남아있다 → 새 시크릿 반영
- **Redirect URI 글자 하나라도 다름** → 전체 문자열을 복붙하여 정확히 일치시킴
- **Test users**에 내 구글 계정을 안 넣음(Testing 모드) → 추가
- 필요한 **API(Drive/Docs/Sheets)** 를 활성화 안 함 → 활성화
- n8n **Client authentication**이 “Send in body”가 아님 → “Send in body”로 변경

---

## 5) 환경별 팁 (npx vs Docker)

- **npx n8n**: 별도 설정 없이 기본 콜백 http://localhost:5678/... 사용 가능
- **Docker**: 컨테이너 내부 포트는 같아도, 브라우저가 접근하는 **호스트 기준 URL**이 콜백으로 등록되어야 합니다.
  - 로컬 단일 PC에서 브라우저로 접속 중이라면 그대로 http://localhost:5678/rest/oauth2-credential/callback 사용
  - 원격 서버에서 접속한다면 **그 서버의 외부 도메인/프로토콜**로 콜백을 바꿔야 함 (예: https://your-domain/rest/oauth2-credential/callback)
  - 배포 시에는 N8N\_HOST, N8N\_PORT, N8N\_PROTOCOL 환경 변수로 **n8n의 외부 URL**을 정확히 지정하면 OAuth/웹훅에 유리

---

## 6) “Authorized domains” 경고 이해하기

- **Authorized domains**에는 **검증 가능한 실도메인만** 들어갑니다(포트 X, localhost X).
- 로컬 테스트에는 **필수 아님**. 앱을 **Testing**으로 두고 **Test users**만 추가하면 충분합니다.

---

## 7) 대안/우회 2가지 (필요 시)

1. **공개 URL로 노출(권장)**

- **Cloudflare Tunnel / Ngrok**으로 로컬 n8n을 임시 도메인에 노출하고, 그 **도메인**을 리다이렉트 URI로 등록
- 실제 배포 환경을 미리 시뮬레이션 가능

1. **n8n Cloud 또는 고정 도메인 배포**

- 고정 **HTTPS 도메인**을 확보하면 OAuth, 웹훅, 외부 콜백 모두 안정적

> 서비스 계정은 개인 Google Drive/Docs 액세스에 적합하지 않습니다(별도 공유/도메인 위임 필요). 사용자 로그인 기반 플로우에는 **OAuth 클라이언트**가 정석입니다.

---

## 8) 자주 묻는 질문 (FAQ)

**Q1. code는 오는데 왜 계속 invalid\_client인가요?**  
A. 리다이렉트는 정상입니다. **웹 앱 클라이언트인지**, **Client Secret 최신값인지**, n8n의 **Client Authentication=Send in body**인지 순서대로 점검하세요.

**Q2. Authorized domains에 localhost를 넣으라던데요?**  
A. 아닙니다. localhost는 **승인 도메인에 넣지 않습니다**. 로컬 테스트엔 **Test users**만 추가하세요.

**Q3. 도커에서만 안 됩니다.**  
A. 브라우저가 접속하는 **외부 URL** 기준으로 리다이렉트 URI를 등록해야 합니다. 원격 서버면 https://서버도메인/rest/oauth2-credential/callback처럼 맞추세요.

**Q4. PKCE를 써야 하나요?**  
A. 필수는 아닙니다. n8n 기본 방식(client\_secret\_post)만으로 충분합니다. 배포 시에는 HTTPS, 최소 권한 스코프, 시크릿 주기적 회전을 권장합니다.

---

## 보안 메모

- 스코프는 **최소 권한 원칙**으로 선택(예: drive.file 우선 고려)
- 시크릿은 팀 채팅/이슈에 **평문으로 공유 금지**
- 배포 환경에서는 **HTTPS 강제**, n8n 사용자 계정에 **2FA** 활성화

---

## 체크리스트

```
[ ] Web application OAuth 클라이언트 생성
[ ] Redirect URI = http://localhost:5678/rest/oauth2-credential/callback
[ ] Client ID/Secret 최신값 n8n에 입력
[ ] Client authentication = Send in body
[ ] 필요한 스코프만 입력 (drive / drive.file / documents / sheets)
[ ] Test users에 내 구글 계정 추가
[ ] Drive/Docs/Sheets API 활성화
```

---

## 마무리

\*\*핵심은 ‘웹 앱 클라이언트 + 정확한 리다이렉트 URI + Send in body’\*\*입니다. 이 3가지만 맞추면 invalid\_client는 대부분 사라집니다.

> 한 줄 결론: **웹 앱 클라이언트·정확한 콜백·바디 인증이면 invalid\_client는 끝!**
