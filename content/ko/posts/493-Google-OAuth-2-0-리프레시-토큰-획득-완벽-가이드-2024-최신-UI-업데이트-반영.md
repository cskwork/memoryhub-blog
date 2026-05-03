---
title: "Google OAuth 2.0 리프레시 토큰 획득 완벽 가이드 2024 - 최신 UI 업데이트 반영"
date: 2025-03-21T14:25:53+09:00
slug: "493-Google-OAuth-2-0-리프레시-토큰-획득-완벽-가이드-2024-최신-UI-업데이트-반영"
original_url: "https://memoryhub.tistory.com/493"
tistory_id: 493
draft: false
categories: ["데브 유틸"]
tags: ["구글 연동"]
---

안녕하세요, 여러분! 오늘은 Google API를 장기간 안정적으로 사용하기 위해 꼭 필요한 리프레시 토큰에 대해 알아보겠습니다. 특히 2024년에 변경된 Google Cloud Console의 최신 UI를 기준으로 설명해드리겠습니다. ?

여러분이 호텔에 체크인하는 상황을 생각해보세요.

- 일반 투숙객은 단기 체류를 위한 '일일 키카드'(액세스 토큰)를 받습니다
- 장기 투숙객은 '마스터 키카드'(리프레시 토큰)를 추가로 받아 만료된 일일 키카드를 언제든 새것으로 교체할 수 있죠
- Google API의 리프레시 토큰도 이와 같은 역할을 합니다!

## 왜 필요한가?

Google OAuth 2.0 리프레시 토큰이 해결하는 문제들은 다음과 같습니다:

1. **인증 만료 문제**: 액세스 토큰은 보통 1시간 후 만료되어 사용자가 다시 로그인해야 하는 불편함이 있습니다
2. **보안과 편의성 균형**: 짧은 수명의 액세스 토큰으로 보안을 유지하면서, 리프레시 토큰으로 사용자 재인증 없이 새 액세스 토큰을 발급받을 수 있습니다
3. **서버 측 자동화**: 백그라운드에서 주기적으로 Google API에 접근해야 하는 서비스에 필수적입니다 (예: 캘린더 동기화, 이메일 자동화 등)

## 기본 원리

Google OAuth 2.0의 핵심 원리를 알아볼까요?

### 토큰 시스템의 이해

OAuth 2.0은 두 가지 주요 토큰을 사용합니다:

- **액세스 토큰**: API 요청을 인증하는 단기 자격 증명 (약 1시간 유효)
- **리프레시 토큰**: 새 액세스 토큰을 얻기 위한 장기 자격 증명

### 인증 흐름

1. 사용자가 애플리케이션에 권한 부여
2. 애플리케이션이 액세스 토큰과 리프레시 토큰을 받음
3. 액세스 토큰으로 API 요청
4. 액세스 토큰 만료 시 리프레시 토큰으로 새 액세스 토큰 획득
5. 3~4 반복

## 실제 예제: 2024년 최신 Google Cloud Console 설정

이제 2024년 기준 최신 Google Cloud Console UI에서 리프레시 토큰을 획득하는 과정을 상세히 알아보겠습니다.

### 1. Google Cloud 프로젝트 생성 및 API 활성화

1. [Google Cloud Console](https://console.cloud.google.com/)에 접속합니다
2. 새 프로젝트를 생성하거나 기존 프로젝트를 선택합니다
3. 왼쪽 메뉴에서 "APIs & Services" > "Library"로 이동합니다
4. 필요한 API(예: Google Calendar API)를 검색하고 활성화합니다

### 2. OAuth 동의 화면 설정 (2024년 UI 변경 ⚠️)

1. 왼쪽 메뉴에서 "**Google Auth platform > Branding**"으로 이동합니다
   - 이는 이전 UI의 "APIs & Services > OAuth consent screen"에 해당합니다
2. 사용자 유형(내부 또는 외부)을 선택합니다
3. 앱 정보 입력:
   - 앱 이름
   - 사용자 지원 이메일
   - 개발자 연락처 정보
4. "Scopes" 또는 "Data Access" 섹션에서 필요한 범위를 추가합니다:
   - 예: Calendar API를 위한 `https://www.googleapis.com/auth/calendar`
5. 필요에 따라 테스트 사용자를 추가합니다
6. **중요 2024년 업데이트**: 게시 상태를 "프로덕션"으로 설정합니다
   - "테스트" 상태로 두면 리프레시 토큰이 7일 후 만료됩니다! ?
   - "프로덕션" 상태로 설정해야 리프레시 토큰이 장기간 유효합니다

### 3. OAuth 클라이언트 ID 및 리디렉션 URI 설정 (2024년 UI 변경 ⚠️)

1. 왼쪽 메뉴에서 "**Google Auth platform > Clients**"로 이동합니다
   - 이는 이전 UI의 "APIs & Services > Credentials"에 해당합니다
2. "Create client" 버튼을 클릭합니다
3. 애플리케이션 유형 선택:
   - **중요**: 반드시 "**Web Application**"을 선택하세요! ?
   - 다른 유형(Desktop App, Android, iOS 등)을 선택하면 리디렉션 URI 입력 필드가 나타나지 않습니다
4. 클라이언트 이름을 입력합니다
5. "**Authorized redirect URIs**" 섹션에 다음을 추가합니다:
   - OAuth Playground용: `https://developers.google.com/oauthplayground`
   - 자체 애플리케이션 용: 귀하의 애플리케이션 콜백 URL
6. "Create" 버튼을 클릭하여 클라이언트 ID와 클라이언트 시크릿을 생성합니다
7. 생성된 `GOOGLE_CLIENT_ID`와 `GOOGLE_CLIENT_SECRET`을 안전하게 저장합니다

### 4. OAuth 2.0 Playground에서 리프레시 토큰 획득

1. [Google OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)에 접속합니다
2. 오른쪽 상단 설정 아이콘(⚙️)을 클릭합니다
3. **중요**: "Use your own OAuth credentials" 옵션을 체크합니다
   - 이 옵션을 체크하지 않으면 Playground의 기본 자격 증명으로 생성된 토큰은 24시간 내에 자동 취소됩니다! ⚠️
4. 앞서 생성한 OAuth 클라이언트 ID와 시크릿을 입력합니다
5. 왼쪽 패널에서 필요한 API와 스코프를 선택합니다:
   - 예: "Calendar API v3"에서 `https://www.googleapis.com/auth/calendar` 선택
6. "Authorize APIs" 버튼을 클릭하고 OAuth 인증 과정을 완료합니다
7. "Exchange authorization code for tokens" 버튼을 클릭합니다
8. "Refresh token"을 복사합니다 - 이것이 바로 `GOOGLE_REFRESH_TOKEN`입니다
9. 이 리프레시 토큰을 안전하게 저장하세요 - 다시 획득하기 위해서는 전체 과정을 반복해야 합니다

### 5. 리프레시 토큰 사용 예시

리프레시 토큰을 사용하여 새 액세스 토큰을 획득하는 과정은 다음과 같습니다:

```
import requests

def get_new_access_token(client_id, client_secret, refresh_token):
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }

    response = requests.post('https://oauth2.googleapis.com/token', data=params)
    return response.json()['access_token']

# 새 액세스 토큰 획득
new_access_token = get_new_access_token(
    'YOUR_CLIENT_ID', 
    'YOUR_CLIENT_SECRET', 
    'YOUR_REFRESH_TOKEN'
)

# 획득한 액세스 토큰으로 API 호출
headers = {'Authorization': f'Bearer {new_access_token}'}
response = requests.get('https://www.googleapis.com/calendar/v3/calendars/primary/events', headers=headers)
```

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **UI 변경에 따른 경로 확인**

   - Google Cloud Console UI는 계속 업데이트되므로, 메뉴 경로가 약간 다를 수 있습니다
   - 현재(2024년) 기준으로 OAuth 설정은 "Google Auth platform" 섹션으로 이동했습니다
2. **웹 애플리케이션 유형 선택**

   - 리디렉션 URI를 설정하려면 반드시 "Web Application" 유형을 선택해야 합니다
   - Desktop App, Android, iOS 등 다른 유형에서는 리디렉션 URI 필드가 표시되지 않습니다
3. **리프레시 토큰 만료 이슈**

   - OAuth 동의 화면이 "테스트" 상태인 경우 리프레시 토큰은 7일 후 만료됩니다
   - 프로덕션 환경에서는 반드시 게시 상태를 "프로덕션"으로 변경하세요
   - 검증 과정이 필요할 수 있으며, 이는 Google의 정책에 따라 변경될 수 있습니다
4. **리프레시 토큰 제한**

   - Google 계정당 OAuth 2.0 클라이언트 ID당 최대 100개의 리프레시 토큰 제한이 있습니다
   - 제한에 도달하면 새 리프레시 토큰을 생성할 때 가장 오래된 토큰이 자동으로 무효화됩니다
   - 테스트 중에는 이 제한에 쉽게 도달할 수 있으니 주의하세요
5. **토큰 보안**

   - 리프레시 토큰은 액세스 토큰보다 더 강력한 자격 증명이므로 보안에 각별히 신경 써야 합니다
   - 환경 변수나 안전한 비밀 관리 시스템에 저장하세요
   - 소스 코드나 버전 관리 시스템에 절대 포함시키지 마세요

? **꿀팁**

- OAuth 설정은 두 개의 별도 부분으로 구성됩니다:
  1. **동의 화면 설정** (Google Auth platform > Branding): 사용자가 보게 될 권한 요청 화면
  2. **클라이언트 ID/리디렉션 설정** (Google Auth platform > Clients): 실제 인증 흐름에 필요한 기술적 설정
- 리디렉션 URI는 정확히 일치해야 합니다 - 대소문자, 슬래시, http/https 스키마까지 모두 동일해야 합니다
- 실제 프로덕션 환경에서는 OAuth 2.0 Playground 대신 자체 OAuth 흐름 구현을 고려하세요
- 테스트 단계에서는 제한된 스코프로 시작하여 필요에 따라 확장하세요
- 액세스 토큰 만료 오류를 처리하는 재시도 로직을 구현하세요

## 마치며

지금까지 2024년 최신 Google Cloud Console UI에서 OAuth 2.0 리프레시 토큰을 획득하는 방법에 대해 알아보았습니다. 가장 중요한 변경사항은 UI 경로 변경, 웹 애플리케이션 유형 선택 시 리디렉션 URI 설정, 그리고 리프레시 토큰의 7일 만료 문제를 해결하기 위한 "프로덕션" 상태 설정입니다.

이 가이드가 여러분의 Google API 통합 작업에 도움이 되었기를 바랍니다! ?

혹시 궁금한 점이 있으시거나, 더 알고 싶은 내용이 있으시면 댓글로 남겨주세요.

## 참고 자료 ?

- [Google 개발자 문서: OAuth 2.0을 사용하여 Google API 액세스](https://developers.google.com/identity/protocols/oauth2)
- [Google Cloud Console 도움말: OAuth 동의 화면 설정](https://support.google.com/cloud/answer/10311615?hl=en-GB)
- [Google OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)
- [Google Cloud Platform 콘솔 도움말: OAuth 클라이언트 관리](https://support.google.com/cloud/answer/15549257?hl=en)

---

#GoogleAPI #OAuth2 #RefreshToken #인증시스템 #GoogleCloud #2024업데이트
