---
title: "Integrating Keycloak SSO with JavaScript"
date: 2025-02-09T00:47:36+09:00
slug: "441-Keycloak-SSO를-JavaScript로-연동하기"
original_url: "https://memoryhub.tistory.com/441"
tistory_id: 441
draft: false
categories: ["Dev Ops"]
tags: ["SSO"]
---

Today, let's explore how to integrate **Keycloak** with **SSO (Single Sign-On)** in JavaScript applications. Keycloak is an open-source authentication and authorization server that can be used to quickly build SSO functionality based on OAuth 2.0 and OpenID Connect standards.

---

## **1. What is Keycloak SSO?**

Keycloak SSO allows multiple applications to share user authentication information through a single authentication system (Keycloak). Once a user logs in once, that information can be reused by other applications.

- **Concept Summary**: Keycloak server acts as a central authentication hub, allowing users to access multiple services or apps without logging in repeatedly.
- **Real-life Example**: Similar to using a Google account to seamlessly log into YouTube, Gmail, Drive, and other services with the same account.
- **Problem It Solves**: Instead of each app implementing its own login logic, Keycloak handles authentication centrally, greatly improving **security, maintainability, and consistency**.

---

## **2. How Does It Work?**

By using the **Keycloak JavaScript Adapter (keycloak.js)** provided by Keycloak, even SPAs (Single Page Applications) or regular web applications can relatively easily integrate SSO. The process generally involves the following steps:

### 1) Keycloak Server Setup

1. **Create a Realm**
   Create a `Realm` in the Keycloak Admin console. A Realm is a logical partition where authentication and authorization information is collected.
2. **Create a Client**

   - Navigate to the **Clients** menu within the Realm to create a new Client.
   - Set the **Client Protocol** to **OpenID Connect**.
   - Set **Access Type** to Public, Confidential, or Bearer-only as needed. For **SPAs**, typically use **Public**.
   - Specify the exact domain or URL that can be redirected to in **Valid Redirect URIs**. (Example: `http://localhost:3000/*`)
3. **Verify Meta Information**

   - Click on the created Client to verify **Client ID**, **Secret (required if Confidential)**, **Redirect URIs**, etc.

### 2) JavaScript Adapter (keycloak.js) Basic Concepts

Through the Keycloak JS Adapter, the application can automate the following process:

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
    onLoad: 'login-required',    // Automatically show login screen when app loads
    checkLoginIframe: false      // Whether to use iframe for token status checking
  })
  .then(function(authenticated) {
    if (!authenticated) {
      console.log('Not authenticated!');
    } else {
      console.log('Authenticated!');
      // From here, you can manage user info, tokens, etc. using the keycloak object
    }
  })
  .catch(function() {
    console.log('Failed to initialize Keycloak');
  });
</script>
```

The **onLoad** option can be divided into two main types:

- `login-required`: Forcibly show the login screen when the application loads, then load after login is complete.
- `check-sso`: If the user is already logged in elsewhere, retrieve that information. If not logged in, ignore it.

### 3) Actual Operation Flow

1. **User Request**: User accesses the app via browser.
2. **Keycloak JS Adapter Initialization**: When `keycloak.init()` is called, the client communicates with the Keycloak server to check if the user is already logged in.
3. **Login Redirect**: If the user is not logged in, the browser is redirected to the Keycloak login page.
4. **Authentication Callback**: Once login is complete, the browser returns to the configured **Redirect URI**. At this time, user information and access token are stored in the Keycloak JS Adapter.
5. **Token Transmission on API Calls**: When the app makes backend API calls, it can automatically include the token in the header (Authorization) or customly send it.

---

## **3. Key Advantages**

1. **Enhanced Security**:
   Since Keycloak is based on OAuth 2.0 / OpenID Connect, token-based authentication significantly reduces security risks like **session hijacking, CSRF, and XSS**.
2. **Centralized Management**:
   You can centrally manage users, groups, and authorization policies in one place. Password changes, 2FA, account locking, and other centralized policies can be easily applied.
3. **Extensibility**:
   Various custom features (social login, LDAP integration, SAML support, etc.) can be plugged in like add-ons, making it suitable for both enterprise environments and personal projects.

---

## **4. Important Considerations ⚠️**

1. **Redirect URI Configuration**:
   Keycloak only allows redirection to URLs that exactly match those specified in `Valid Redirect URIs`. When using wildcards (`http://localhost:3000/*`), be careful about security implications.
2. **Token Expiration Management**:
   Access tokens have an expiration period, so you must automatically refresh them using **refresh tokens** before they expire. Consider logic to refresh login status in `check-sso` mode.
3. **CORS Configuration**:
   If your SPA and API server are on different domains, CORS settings must be properly configured on both Keycloak and the API server.
4. **Security Mode (HTTPS)**:
   In production environments, use **HTTPS** to ensure tokens are transmitted securely.

---

## **5. Real Usage Examples**

The following is an example of integrating Keycloak in a vanilla JavaScript SPA environment without using React or similar frameworks. (In frameworks like React and Vue, the principle is similar; you just load and initialize the Adapter.)

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>Keycloak SSO Example</title>
</head>
<body>
  <h1>Keycloak SSO Integration Demo</h1>
  <button id="loginBtn">Log In</button>
  <button id="logoutBtn">Log Out</button>

  <!-- Load Keycloak JS library -->
  <script src="https://<Keycloak Server Address>/auth/js/keycloak.js"></script>

  <script>
    // 1. Configure Keycloak
    const keycloakConfig = {
      url: 'https://<Keycloak Server Address>/auth',
      realm: 'example-realm',
      clientId: 'example-client'
    };

    // 2. Create Keycloak object
    const keycloak = new Keycloak(keycloakConfig);

    // 3. Initialize
    keycloak.init({
      onLoad: 'check-sso',       // Reuse existing session if user is already logged in
      checkLoginIframe: false
    })
    .then(authenticated => {
      if (authenticated) {
        console.log('User token: ', keycloak.token);
        console.log('User info: ', keycloak.tokenParsed);
      } else {
        console.log('Not logged in');
      }
    })
    .catch(e => {
      console.error('Keycloak initialization failed', e);
    });

    // 4. Login button
    document.getElementById('loginBtn').onclick = () => {
      keycloak.login();
    };

    // 5. Logout button
    document.getElementById('logoutBtn').onclick = () => {
      keycloak.logout();
    };
  </script>
</body>
</html>
```

- **keycloak.init()**

  - Since we're in `check-sso` mode, if there's an existing login session, it reuses it.
  - If there's no session, it doesn't redirect to the login screen (you must click the login button to proceed).
- **Login / Logout Buttons**

  - Calling `login()` redirects to the Keycloak login page.
  - Calling `logout()` redirects to the Keycloak logout page.

---

## **6. Conclusion**

By using the Keycloak JS Adapter, you can easily build SSO that conforms to **OAuth 2.0 / OpenID Connect** standards without implementing complex authentication logic yourself. This is particularly beneficial in enterprise environments where you want to integrate multiple internal systems with unified authentication.

**With this technology**, you can centrally manage user permissions and implement a **convenient and secure SSO** solution that allows various applications to be accessed with a single login!

---

### **References and Sources**

- [Keycloak Official Documentation](https://www.keycloak.org/documentation)
- [Keycloak JavaScript Adapter Guide](https://www.keycloak.org/docs/latest/securing_apps/index.html#_javascript_adapter)
- [OAuth 2.0 and OpenID Connect Concept Guide](https://oauth.net/2/)

Through the above documents, you can find more in-depth configurations and advanced features (social login, LDAP integration, 2FA, etc.). I hope this guide helps you learn the basic Keycloak SSO integration process!
