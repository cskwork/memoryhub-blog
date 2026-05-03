---
title: "Resolving n8n Local Google Integration invalid_client Error"
date: 2025-08-23T07:59:35+09:00
slug: "758-n8n-로컬에서-Google-연동-시-invalid_client-에러-해결"
original_url: "https://memoryhub.tistory.com/758"
tistory_id: 758
draft: false
categories: ["Dev Util"]
tags: ["Agents"]
---

When trying to integrate **n8n ↔ Google (Drive/Docs/Sheets)** locally, the callback usually comes back fine but fails at the token exchange step with an error like:

```
Error: Client authentication failed (e.g., unknown client, no client authentication included, or unsupported authentication method)
{"error":"invalid_client","error_description":"Unauthorized"}
```

This article is a practical manual to **quickly diagnose and resolve** the above error. (Same for n8n npx/Docker)

---

## Summary (TL;DR)

- **Problem**: The Google token endpoint can't recognize **client authentication**, causing failure.
- **Three solutions**
  1. Make the OAuth client **type "Web application"**
  2. Register **Redirect URI** **exactly matching** n8n callback: http://localhost:5678/rest/oauth2-credential/callback
  3. Set n8n credential's **Client authentication method = "Send in body"** (a.k.a. client_secret_post)

> If code arrived back at n8n, **redirect setup is already successful**. If it fails at token exchange, check client type/secret/auth method.

---

## Quick Symptom → Cause Matching Table

| What You See in UI/Logs | Meaning | Action |
| --- | --- | --- |
| Callback URL gets ?code=...&scope=... and **returns to n8n** | Redirect URI/client_id OK | Check next step (token exchange) |
| {"error":"invalid_client","error_description":"Unauthorized"} | Google fails **client authentication** | Check if **web app client**, **secret current**, n8n uses **Send in body** |
| Used to work, suddenly invalid_client | **Client secret rotated/changed** after n8n creation | Re-save new secret in n8n |
| redirect_uri_mismatch | Redirect URI spelling/port/path mismatch | Match GCP and n8n strings **exactly** |

---

## Prerequisites

- Google Cloud project (APIs & Services enabled)
- APIs to enable: **Google Drive API**, (if needed) **Google Docs API / Sheets API**
- Local n8n (e.g., npx n8n or Docker running http://localhost:5678)

---

## 1) Create **Web Application** Client in Google Cloud

1. Google Cloud Console → **APIs & Services → Credentials**
2. **Create Credentials → OAuth client ID**
3. Select **Application type = Web application**
4. Add to **Authorized redirect URIs** **exactly** this:
5. http://localhost:5678/rest/oauth2-credential/callback
6. After creation, copy **Client ID / Client Secret**

> **Note**: **Authorized domains** only accepts verified real domains (no ports, no localhost). For local testing, keep the app in **Testing** status and just add your Google account to **Test users**.

---

## 2) Configure Credentials in n8n

In n8n editor → **Credentials**, use one of:

- **Google Drive/Docs/Sheets**-specific credential, or
- **OAuth2 API** (Generic) credential

### Common Input Values

- **Auth URL**: https://accounts.google.com/o/oauth2/v2/auth
- **Token URL**: https://oauth2.googleapis.com/token
- **Client ID / Client Secret**: (values just created in GCP)
- **Scope** (space-separated, what you need)
  - All Drive files: https://www.googleapis.com/auth/drive
  - Only n8n-created files: https://www.googleapis.com/auth/drive.file
  - Docs: https://www.googleapis.com/auth/documents
- **Client Authentication**: **Send in body** (a.k.a. client_secret_post)
- **Callback URL** (shown by n8n): http://localhost:5678/rest/oauth2-credential/callback

> Key point: Google's token endpoint has better compatibility with **body transmission** than client_secret_basic (header). Use "Send in body" in n8n.

---

## 3) Verification Procedure

1. Click **Connect** to Google login → after consent, you return to n8n.
2. If it fails, check **n8n logs** and **browser address bar**:
   - If address bar shows ?code=..., **redirect OK**
   - If invalid_client after, re-check **ID/Secret/auth method**

### (Optional) Manual Token Exchange Test

Try token exchange directly with curl to **validate credentials themselves**:

```
curl -X POST https://oauth2.googleapis.com/token \
  -d code=PASTE_CODE_HERE \
  -d client_id=PASTE_CLIENT_ID \
  -d client_secret=PASTE_CLIENT_SECRET \
  -d redirect_uri=http://localhost:5678/rest/oauth2-credential/callback \
  -d grant_type=authorization_code
```

- If invalid_client here too, it's almost certainly a **client type (web app)** or **secret** issue.

---

## 4) Common Mistakes Checklist

- Created OAuth client as **Desktop** → recreate as **Web application**
- Rotated **Client secret** but n8n has **old value** → reflect new secret
- **Redirect URI doesn't match** even one character → copy-paste entire string exactly
- Didn't add my Google account to **Test users** (Testing mode) → add it
- Didn't enable required **APIs (Drive/Docs/Sheets)** → enable them
- n8n **Client authentication** not "Send in body" → change to "Send in body"

---

## 5) Tips by Environment (npx vs Docker)

- **npx n8n**: Can use default callback http://localhost:5678/... without extra config
- **Docker**: Even if container port is same, the **host-based URL** that browser accesses must be registered as callback.
  - If accessing locally from browser on same PC, use http://localhost:5678/rest/oauth2-credential/callback as-is
  - If accessing from remote server, **change callback to that server's external domain/protocol** (e.g., https://your-domain/rest/oauth2-credential/callback)
  - On deployment, use **N8N_HOST, N8N_PORT, N8N_PROTOCOL** environment variables to specify n8n's **external URL** precisely—helps OAuth/webhooks

---

## 6) Understanding "Authorized domains" Warning

- **Authorized domains** only accept **verifiable real domains** (no ports, no localhost).
- **Not required** for local testing. Keeping the app in **Testing** and just adding **Test users** is sufficient.

---

## 7) Two Alternatives/Workarounds (if needed)

1. **Expose via Public URL (Recommended)**

- Expose local n8n to a temporary domain via **Cloudflare Tunnel / Ngrok**, register that **domain** as redirect URI
- Can pre-simulate actual deployment environment

2. **n8n Cloud or Fixed Domain Deployment**

- With fixed **HTTPS domain**, OAuth, webhooks, external callbacks all work reliably

> Service accounts aren't suitable for personal Google Drive/Docs access (requires separate sharing/domain delegation). For user-login-based flows, **OAuth client** is standard.

---

## 8) Frequently Asked Questions (FAQ)

**Q1. Code arrives but why always invalid_client?**  
A. Redirect is fine. Check in order: **is it web app client?**, **is secret current?**, **is n8n's Client Authentication=Send in body?**

**Q2. I heard to put localhost in Authorized domains?**  
A. No. Don't put localhost in **authorized domains**. For local testing, just add **Test users**.

**Q3. Doesn't work only in Docker.**  
A. You must register redirect URI based on **external URL** the browser accesses. If remote server, match like https://your-domain/rest/oauth2-credential/callback.

**Q4. Do I need PKCE?**  
A. Not required. n8n's default approach (client_secret_post) is enough. On deployment, recommend HTTPS, least-privilege scopes, periodic secret rotation.

---

## Security Notes

- Choose scopes by **least privilege principle** (prefer drive.file)
- Never share secrets **plaintext** in team chat/issues
- In production, **enforce HTTPS**, enable **2FA** on n8n user accounts

---

## Checklist

```
[ ] Create Web application OAuth client
[ ] Redirect URI = http://localhost:5678/rest/oauth2-credential/callback
[ ] Latest Client ID/Secret in n8n
[ ] Client authentication = Send in body
[ ] Input only needed scopes (drive / drive.file / documents / sheets)
[ ] Add my Google account to Test users
[ ] Enable Drive/Docs/Sheets APIs
```

---

## Wrap-up

**The essence is 'web app client + exact redirect URI + Send in body'**. Get these three right and invalid_client mostly disappears.

> One-line conclusion: **Web app client, exact callback, body auth = invalid_client solved!**
