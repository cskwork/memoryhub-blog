---
title: "? Microsoft Entra에서 Outlook API 인증 완벽 가이드: Single vs Multi-Tenant"
date: 2025-09-29T09:46:54+09:00
slug: "799-Microsoft-Entra에서-Outlook-API-인증-완벽-가이드-Single-vs-Multi-Tenant"
original_url: "https://memoryhub.tistory.com/799"
tistory_id: 799
draft: false
---

```
     ┌─────────────────────────────────┐
     │  ? Microsoft Entra ID          │
     │                                 │
     │   ┌─────┐      ┌─────┐         │
     │   │ APP │──────│ KEY │         │
     │   └─────┘      └─────┘         │
     │     │            │              │
     │     └────────────┘              │
     │         │                       │
     │         ▼                       │
     │    ? Outlook API               │
     │                                 │
     │  Single ←→ Multi-Tenant         │
     └─────────────────────────────────┘
```

# 

## 

**Azure App을 Multi-tenant로 바꾸려면** App 등록의 **Supported account types**를 "**Accounts in any organizational directory and personal Microsoft accounts**"로 변경하고, \*\*Redirect URI/권한/검증(Publisher verification)\*\*을 정리한 뒤 OAuth 엔드포인트를 /common(또는 필요 시 /organizations, /consumers)으로 맞추면 됩니다.

---

Microsoft 365 Outlook API를 활용한 메일 자동화 프로젝트를 시작했지만, 첫 단계인 인증 키 발급부터 막힌 경험 있으신가요? entra.microsoft.com의 UI가 예전 Azure Portal과 달라지면서, Client ID와 Secret ID를 혼동하거나 어디서 값을 복사해야 할지 헷갈리는 경우가 많습니다. 특히 Single-tenant로 설정했다가 Multi-tenant로 전환해야 하는 상황에서는 더욱 복잡해집니다. 이 글에서는 **Microsoft Entra에서 Outlook API용 앱 등록부터 클라이언트 인증 정보 생성, 그리고 Single/Multi-tenant 설정까지** 실수 없이 완료하는 방법을 단계별로 정리했습니다.

---

## 1. 배경: Single vs Multi-Tenant, 왜 중요한가?

Microsoft Entra ID는 사용자와 앱을 테넌트(tenant)라는 그룹으로 조직화합니다. Single-tenant 앱은 등록된 테넌트(홈 테넌트)에서만 사용 가능하며, Multi-tenant 앱은 홈 테넌트와 다른 테넌트의 사용자 모두가 사용할 수 있습니다.

### 핵심 개념 정리

용어 의미 용도

|  |  |  |
| --- | --- | --- |
| **Single-Tenant** | 하나의 조직(테넌트)만 접근 가능 | 사내 전용 앱, 보안 강화 |
| **Multi-Tenant** | 여러 조직의 사용자가 접근 가능 | SaaS 제품, 공개 서비스 |
| **Application (Client) ID** | 앱을 식별하는 고유 GUID | 모든 API 호출에 필요 |
| **Client Secret** | 앱의 비밀번호 역할 | 토큰 발급 시 인증 사용 |
| **Secret ID** | Secret의 식별자 | ⚠️ 인증에 사용되지 않음 |
| **signInAudience** | 지원 계정 유형 설정 | AzureADMyOrg, AzureADMultipleOrgs 등 |

### 엔드포인트 차이

OAuth 인증 URL의 issuer 부분은 누가 로그인할 수 있는지를 제어합니다.

엔드포인트 대상 사용 사례

|  |  |  |
| --- | --- | --- |
| /common | 회사/학교 계정 + 개인 Microsoft 계정 | Multi-tenant 앱 (모든 사용자) |
| /organizations | 회사/학교 계정만 | 조직 전용 Multi-tenant |
| /consumers | 개인 Microsoft 계정만 | 개인 사용자 대상 앱 |
| /{tenant-id} | 특정 테넌트만 | Single-tenant 앱 |

---

## 2. 핵심

> **Microsoft Entra에서 앱을 등록하고 Client Secret을 생성하면, 단 한 번만 표시되는 Value 값을 반드시 즉시 저장해야 합니다. Secret ID가 아닌 Value가 실제 인증 키입니다. Multi-tenant로 전환 시 Supported account types와 엔드포인트를 함께 변경해야 합니다.**

---

## 3. 실습

### ① 앱 등록 (Single-Tenant 기본)

1. **Microsoft Entra 관리 센터 접속**
   - <https://entra.microsoft.com> 에 로그인 (최소 Application Developer 권한 필요)
   - 왼쪽 메뉴에서 **Identity > Applications > App registrations** 선택
2. **New registration 클릭**
   - **Name**: 앱 이름 입력 (예: OutlookMailAPI)
   - **Supported account types**:
     - **Accounts in this organizational directory only**: Single-tenant (기본 권장)
     - **Accounts in any organizational directory**: Multi-tenant (조직만)
     - **Accounts in any organizational directory and personal Microsoft accounts**: Multi-tenant (모든 사용자)
   - **Redirect URI**: 선택 사항 (웹앱이 아니면 비워두기)
   - **Register** 클릭
3. **Client ID 확인**
   - Overview 탭에서 **Application (client) ID** 복사 (⚠️ Object ID나 Directory ID가 아님)
   - **Directory (tenant) ID**도 함께 복사 (Single-tenant 엔드포인트에 필요)

### ② Client Secret 생성

1. **Certificates & secrets 메뉴 이동**
   - 왼쪽 메뉴에서 **Certificates & secrets** 선택
2. **New client secret 클릭**
   - **Description**: Secret 용도 입력 (예: OutlookAPI-Production)
   - **Expires**: 권장 6개월 또는 사용자 정의 기간 선택
   - **Add** 클릭
3. **⚠️ 중요: Value 즉시 복사**
   - 생성 직후 **Value** 열에 표시되는 값이 실제 Client Secret입니다
   - Secret ID는 인증에 사용되지 않으며, 이 페이지를 나가면 Value는 다시 볼 수 없습니다
   - 비밀번호 관리 도구에 안전하게 저장

### ③ Outlook API 권한 설정

1. **API permissions 메뉴 이동**
   - 왼쪽 메뉴에서 **API permissions** 선택
2. **Microsoft Graph 권한 추가**
   - **Add a permission > Microsoft Graph** 선택
   - 사용 시나리오에 따라 선택:**위임 권한 (Delegated permissions)**: 사용자 대신 작동
   - Mail.Read: 사용자 메일 읽기
   - Mail.ReadWrite: 메일 읽기/쓰기
   - Mail.Send: 메일 발송
   - offline\_access: 리프레시 토큰 발급**애플리케이션 권한 (Application permissions)**: 백그라운드 서비스용
   - Mail.Read: 모든 사서함 읽기
   - Mail.ReadWrite: 모든 사서함 쓰기
   - Mail.Send: 모든 사용자 이름으로 발송
3. **관리자 동의 부여**
   - 애플리케이션 권한은 반드시 **Grant admin consent** 버튼 클릭 필요

---

## 4. Single-Tenant → Multi-Tenant 전환 방법

### 단계 1: App 기본 설정 전환

1. **Azure Portal → Microsoft Entra ID → App registrations → (당신의 앱)**
2. **Authentication** 탭 → **Supported account types**에서 원하는 옵션 선택
   - ✅ **Accounts in any organizational directory and personal Microsoft accounts** (가장 넓은 범위)
   - 또는 **Accounts in any organizational directory** (조직만)
3. **Save** 클릭

### 단계 2: Redirect URI 정리

1. 같은 **Authentication** 화면에서 **Web** 항목의 **Redirect URI** 등록
   - n8n 예시: https://<YOUR\_N8N\_HOST>/rest/oauth2-credential/callback
   - 프로토콜(https), 슬래시까지 정확히 일치 필수
2. **Implicit grant**는 비활성화 (권장하지 않음)
   - **Authorization code + PKCE** 권장

### 단계 3: 인증 엔드포인트 변경

엔드포인트의 issuer 값으로 로그인 가능한 사용자를 제어합니다.

**Single-tenant 엔드포인트** (기존):

```
https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize
https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token
```

**Multi-tenant 엔드포인트** (변경 후):

```
https://login.microsoftonline.com/common/oauth2/v2.0/authorize
https://login.microsoftonline.com/common/oauth2/v2.0/token
```

**조직 계정만 허용** (선택):

```
/organizations 사용
```

**개인 계정만 허용** (선택):

```
/consumers 사용
```

### 단계 4: 권한 및 동의 흐름

Multi-tenant 앱의 경우, 다른 테넌트 사용자가 처음 로그인할 때 사용자 동의 또는 해당 테넌트 관리자 동의가 필요합니다.

- 홈 테넌트에서 **Grant admin consent** 실행 (자신의 조직만 적용)
- 다른 테넌트는 해당 조직의 관리자가 승인해야 함

### 단계 5: 보안/신뢰도 강화 (강력 권장)

Multi-tenant 앱 개발 시 다양한 IT 관리자의 정책 때문에 어려움이 있을 수 있습니다.

1. **Branding & properties**: 앱 이름/아이콘/홈페이지 URL 설정
2. **Publisher verification(검증된 게시자)**:
   - 검증된 도메인 연결 (예: yourcompany.com)
   - 검증 후 "Unverified" 경고 없이 깔끔한 동의 화면 제공
3. **최소 권한 원칙**: 앱이 실제로 필요한 권한만 요청하도록 하세요

---

## 5. n8n에서의 실전 설정

### OAuth Credential 설정

1. **Credentials → Microsoft OAuth2** 생성
2. **Grant Type**: Authorization Code
3. **Authorization URL**: <https://login.microsoftonline.com/common/oauth2/v2.0/authorize>
4. **Token URL**: <https://login.microsoftonline.com/common/oauth2/v2.0/token>
5. **Scope** (공백으로 구분):

   ```
   openid profile email offline_access User.Read Mail.Read
   ```
6. **Client ID**: Application (client) ID 입력
7. **Client Secret**: Secret Value 입력
8. **Redirect URI**: Azure와 정확히 동일하게 입력

### 테스트

**HTTP Request 노드**로 테스트:

```
GET https://graph.microsoft.com/v1.0/me/messages?$top=5
```

---

## 6. Azure CLI로 빠르게 전환하기

```
# Multi-tenant로 변경 (조직 + 개인 계정)
az ad app update \
  --id <APPLICATION_CLIENT_ID> \
  --set signInAudience=AzureADandPersonalMicrosoftAccount

# 조직 전용 Multi-tenant
az ad app update \
  --id <APPLICATION_CLIENT_ID> \
  --set signInAudience=AzureADMultipleOrgs

# Redirect URI 추가
az ad app update \
  --id <APPLICATION_CLIENT_ID> \
  --web-redirect-uris https://<YOUR_N8N_HOST>/rest/oauth2-credential/callback
```

**signInAudience** 값 옵션: AzureADMyOrg(Single-tenant) / AzureADMultipleOrgs(조직 전용 Multi-tenant) / AzureADandPersonalMicrosoftAccount(조직+개인)

---

## 7. 모범 사례

항목 권장 방식 주의점

|  |  |  |
| --- | --- | --- |
| **Secret 저장** | Azure Key Vault 사용 | 코드에 하드코딩 금지 |
| **만료 관리** | 6개월 주기 갱신 알림 | 기본 알림 없음 - 스크립트 자동화 필요 |
| **권한 설계** | 최소 권한 원칙 적용 | 불필요한 권한 요청 금지 |
| **인증 방식** | 가능하면 Managed Identity 사용 | Azure 환경에서 Secret 관리 불필요 |
| **Multi-tenant 보안** | Publisher Verification 완료 | 사용자 신뢰 확보 |
| **엔드포인트 선택** | 목적에 맞게 /common 또는 /organizations | 개인 계정 차단 필요 시 /organizations |

---

## 8. 문제 발생 시 빠른 진단

증상 원인 해결 방법

|  |  |  |
| --- | --- | --- |
| AADSTS50194 에러 | Single-tenant인데 /common 사용 | /common → /{tenant-id} 또는 Multi-tenant로 전환 |
| 동의 실패 | 다른 테넌트에서 관리자 동의 필요 | 해당 조직 관리자에게 승인 요청 |
| Redirect URI 불일치 | Azure와 앱의 URI가 정확히 일치하지 않음 | 프로토콜/슬래시까지 100% 일치 확인 |
| 권한 미스매치 | Graph 권한 추가 후 동의 안 함 | Grant admin consent 재실행 |

---

## 9. 마치며

Microsoft Entra의 UI가 개선되면서 Secret ID와 Client Secret Value를 혼동하기 쉬워졌지만, 이 글의 핵심만 기억하세요: **Value 열의 값이 진짜 비밀번호**이며, Single-tenant에서 Multi-tenant로 전환하려면 Supported account types와 엔드포인트를 함께 변경해야 합니다.

**실무 팁 3가지:**

1. Secret 만료 전 갱신 알림을 PowerShell로 자동화하세요
2. Multi-tenant 배포 시 Publisher Verification으로 신뢰도를 높이세요
3. 애플리케이션 권한으로 Mail.Send를 사용할 경우, Application Access Policy를 통해 특정 사서함만 제한하는 것이 보안상 필수입니다

이제 Outlook API로 메일 자동화, 일정 동기화 등 다양한 프로젝트를 안전하게 시작할 수 있습니다.

---

### 참고자료

- Microsoft Learn: 앱 등록 가이드 - <https://learn.microsoft.com/entra/identity-platform/quickstart-register-app>
- Single vs Multi-tenant 앱 - <https://learn.microsoft.com/entra/identity-platform/single-and-multi-tenant-apps>
- Single-tenant을 Multi-tenant로 전환 - <https://learn.microsoft.com/entra/identity-platform/howto-convert-app-to-be-multi-tenant>
- OAuth 2.0 및 OpenID Connect 프로토콜 - <https://learn.microsoft.com/entra/identity-platform/v2-protocols>
- Outlook Mail API 개요 - <https://learn.microsoft.com/graph/api/resources/mail-api-overview>
- Microsoft Graph 권한 레퍼런스 - <https://learn.microsoft.com/graph/permissions-reference>
