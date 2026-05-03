---
title: "Keycloak SSO를 JavaScript로 연동하기"
date: 2025-02-09T00:47:36+09:00
slug: "441-Keycloak-SSO를-JavaScript로-연동하기"
original_url: "https://memoryhub.tistory.com/441"
tistory_id: 441
draft: false
---

오늘은 **Keycloak**을 활용하여 **SSO(Single Sign-On)**를 JavaScript 애플리케이션과 연동하는 방법에 대해 알아보겠습니다. Keycloak은 오픈소스로 제공되는 인증·인가 서버로, OAuth 2.0과 OpenID Connect 표준을 기반으로 쉽고 빠르게 SSO 기능을 구축할 수 있습니다.

---

## **1. Keycloak SSO란? ?**

Keycloak SSO는 말 그대로 하나의 인증 시스템(Keycloak)을 통해 여러 애플리케이션이 사용자 인증 정보를 공유하는 방식입니다. 사용자는 한 번 로그인하면, 그 정보를 다른 애플리케이션이 재활용할 수 있게 됩니다.

- ? **개념 요약**: Keycloak 서버가 중앙 인증 역할을 맡아, 사용자가 여러 서비스나 앱을 이용할 때 매번 로그인할 필요 없도록 해줍니다.
- ? **실생활 예시**: 구글 계정으로 유튜브, 지메일, 드라이브 등 다양한 서비스에 동일 계정으로 무중단 로그인을 하는 것과 유사합니다.
- ? **해결되는 문제**: 여러 앱이 각자 로그인 로직을 구현하는 대신, Keycloak을 통해 공통적으로 인증을 처리하므로 **보안, 유지보수, 일관성**이 크게 향상됩니다.

---

## **2. 어떻게 동작하나요? ?**

Keycloak에서 제공하는 **Keycloak JavaScript Adapter(keycloak.js)**를 사용하면, SPA(Single Page Application)이나 일반 웹 애플리케이션에서도 비교적 쉽게 SSO를 연동할 수 있습니다. 크게 다음 과정을 거칩니다:

### 1) Keycloak 서버 설정

1. **Realm 생성**  
   Keycloak Admin 콘솔에서 `Realm`을 만듭니다. Realm은 인증·인가 정보가 모이는 논리적 구분 단위입니다.
2. **Client 생성**

   - Realm 내에서 **Clients** 메뉴로 이동해 새 Client를 만듭니다.
   - **Client Protocol**은 **OpenID Connect**로 설정합니다.
   - **Access Type**은 Public, Confidential, Bearer-only 등 상황에 따라 설정하되, **SPA**라면 대체로 **Public**을 사용합니다.
   - **Valid Redirect URIs**에 리다이렉트될 수 있는 도메인·URL을 정확히 지정합니다. (예: `http://localhost:3000/*`)
3. **메타 정보 확인**

   - 생성된 Client를 클릭하여 **Client ID**, **Secret(Confidential이면 필요)**, **Redirect URIs** 등을 확인합니다.

### 2) JavaScript Adapter(keycloak.js) 기본 개념

Keycloak JS Adapter를 통해 애플리케이션은 다음 과정을 자동화할 수 있습니다.

```
<script src="https://<Keycloak Server URL>/js/keycloak.js"></script>
<script>
  const keycloakConfig = {
    url: 'https://<Keycloak Server URL>/auth',
    realm: 'my-realm',
    clientId: 'my-client-id'
  };

  const keycloak = new Keycloak(keycloakConfig);

  keycloak.init({ 
    onLoad: 'login-required',    // 앱 로드시 자동으로 로그인 화면 노출
    checkLoginIframe: false      // 토큰 상태 체크를 위한 iframe 사용 여부
  })
  .then(function(authenticated) {
    if (!authenticated) {
      console.log('Not authenticated!');
    } else {
      console.log('Authenticated!');
      // 여기서부터는 keycloak 객체를 활용하여 사용자 정보, 토큰 등을 관리 가능
    }
  })
  .catch(function() {
    console.log('Failed to initialize Keycloak');
  });
</script>
```

**onLoad** 옵션은 크게 두 가지로 나눌 수 있습니다:

- `login-required`: 애플리케이션 로드시 로그인 화면을 강제로 보여주고, 로그인 완료 후 로드합니다.
- `check-sso`: 사용자가 이미 다른 곳에 로그인해 있으면 그 정보를 가져오고, 로그인 안 되어 있으면 무시합니다.

### 3) 실제 동작 원리

1. **사용자 요청**: 사용자가 브라우저로 앱에 접근.
2. **Keycloak JS Adapter 초기화**: `keycloak.init()` 호출 시, 클라이언트가 Keycloak 서버와 통신해 사용자가 이미 로그인했는지 확인합니다.
3. **로그인 Redirect**: 사용자가 로그인되지 않았다면 Keycloak 로그인 페이지로 리다이렉트됩니다.
4. **인증 후 Callback**: 로그인 완료 시 브라우저가 설정된 **Redirect URI**로 돌아옵니다. 이때 사용자 정보와 액세스 토큰이 Keycloak JS Adapter에 저장됩니다.
5. **API 호출 시 토큰 전송**: 앱에서 백엔드 API 호출 시 토큰을 자동으로 헤더(Authorization)에 포함(또는 커스텀)시켜 보낼 수 있습니다.

---

## **3. 주요 장점 ?**

1. **보안 강화**:  
   Keycloak은 OAuth 2.0 / OpenID Connect 기반이므로, 토큰 기반 인증으로 **세션 하이재킹, CSRF, XSS** 등의 보안 위험을 크게 줄여줍니다.
2. **중앙 관리**:  
   한 곳에서 사용자, 그룹, 권한 정책을 통합 관리할 수 있습니다. 비밀번호 변경, 2FA, 계정 잠금 등 중앙화된 정책을 쉽게 적용할 수 있습니다.
3. **확장성**:  
   다양한 커스텀 기능(소셜 로그인, LDAP 연동, SAML 지원 등)을 플러그인처럼 붙일 수 있어, 기업 환경부터 개인 프로젝트까지 폭넓게 사용 가능합니다.

---

## **4. 주의할 점 ⚠️**

1. **Redirect URI 설정**:  
   Keycloak에서는 `Valid Redirect URIs`에 정확히 일치하는 주소로만 리다이렉트를 허용합니다. 와일드카드를 사용하는 경우(`http://localhost:3000/*`) 보안상 주의를 기울여야 합니다.
2. **토큰 만료 관리**:  
   액세스 토큰은 유효기간이 있으므로, 토큰이 만료되기 전에 자동으로 **refresh token**을 사용해 갱신해야 합니다. `check-sso` 모드에서 로그인 상태를 갱신하는 로직도 고려해야 합니다.
3. **CORS 설정**:  
   SPA가 API 서버와 다른 도메인에 있을 경우, Keycloak과 API 서버 양측에 CORS 설정이 올바르게 되어 있어야 합니다.
4. **보안 모드(HTTPS)**:  
   실제 운영 환경에서는 **HTTPS**를 사용해야 토큰이 안전하게 전송됩니다.

---

## **5. 실제 사용 예시 ?**

다음은 React 등을 사용하지 않는 순수 JavaScript SPA 환경에서 Keycloak을 연동하는 예시입니다. (React, Vue 등의 프레임워크에서도 원리는 비슷하며, Adapter를 불러와 초기화 과정을 거치면 됩니다.)

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>Keycloak SSO Example</title>
</head>
<body>
  <h1>Keycloak SSO 연동 데모</h1>
  <button id="loginBtn">로그인</button>
  <button id="logoutBtn">로그아웃</button>

  <!-- Keycloak JS 라이브러리 로드 -->
  <script src="https://<키클록 서버 주소>/auth/js/keycloak.js"></script>

  <script>
    // 1. 키클록 구성 설정
    const keycloakConfig = {
      url: 'https://<키클록 서버 주소>/auth',
      realm: 'example-realm',
      clientId: 'example-client'
    };

    // 2. 키클록 객체 생성
    const keycloak = new Keycloak(keycloakConfig);

    // 3. 초기화
    keycloak.init({
      onLoad: 'check-sso',       // 이미 로그인되어 있다면 세션을 재활용
      checkLoginIframe: false
    })
    .then(authenticated => {
      if (authenticated) {
        console.log('사용자 토큰: ', keycloak.token);
        console.log('사용자 정보: ', keycloak.tokenParsed);
      } else {
        console.log('로그인되지 않음');
      }
    })
    .catch(e => {
      console.error('Keycloak 초기화 실패', e);
    });

    // 4. 로그인 버튼
    document.getElementById('loginBtn').onclick = () => {
      keycloak.login();
    };

    // 5. 로그아웃 버튼
    document.getElementById('logoutBtn').onclick = () => {
      keycloak.logout();
    };
  </script>
</body>
</html>
```

- **keycloak.init()**

  - `onLoad: 'check-sso'` 모드이므로, **이미 로그인** 세션이 있다면 그대로 사용합니다.
  - 세션이 없다면 로그인 창으로 넘어가지 않습니다(로그인 버튼을 눌러야 이동).
- **로그인 / 로그아웃 버튼**

  - `login()`을 호출하면 Keycloak 로그인 페이지로 이동
  - `logout()`을 호출하면 Keycloak 로그아웃 페이지로 이동

---

## **6. 마치며 ?**

이렇게 Keycloak JS Adapter를 사용하면, 번거로운 인증 로직을 직접 구현하지 않고도 **OAuth 2.0 / OpenID Connect** 표준에 맞춰 손쉽게 SSO를 구축할 수 있습니다. 특히 기업 환경에서 여러 내부 시스템을 한 번에 통합 인증하고 싶을 때 큰 이점을 얻을 수 있습니다.

**이 기술을 사용하면** 중앙에서 사용자 권한을 관리하고, 한 번의 로그인으로 다양한 애플리케이션에 접근할 수 있는 **편리하고 안전한 SSO** 솔루션을 구현할 수 있습니다!

---

### **참고 자료 및 출처**

- [Keycloak 공식 문서](https://www.keycloak.org/documentation)
- [Keycloak JavaScript Adapter 가이드](https://www.keycloak.org/docs/latest/securing_apps/index.html#_javascript_adapter)
- [OAuth 2.0 및 OpenID Connect 개념 정리](https://oauth.net/2/)

위 문서들을 통해 더 심도 있는 설정과 고급 기능(소셜 로그인, LDAP 연동, 2FA 등)을 확인할 수 있습니다.  
해당 가이드를 통해 기본적인 Keycloak SSO 연동 과정을 익히셨기를 바랍니다!
