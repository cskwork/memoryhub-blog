---
title: "Google OAuth 2.0 Refresh Token Complete Guide 2024 - Latest UI Updates Reflected"
date: 2025-03-21T14:25:53+09:00
slug: "493-Google-OAuth-2-0-리프레시-토큰-획득-완벽-가이드-2024-최신-UI-업데이트-반영"
original_url: "https://memoryhub.tistory.com/493"
tistory_id: 493
draft: false
categories: ["Dev Util"]
tags: ["Google Integration"]
---

Hello everyone! Today, let's explore refresh tokens—essential for long-term stable use of Google APIs. Especially, I'll explain based on the 2024 updated Google Cloud Console's latest UI.

Imagine checking into a hotel:

- Regular guests get a 'daily keycard' (access token) for short stays
- Long-term guests get a 'master keycard' (refresh token) allowing them to exchange expired daily keycards for new ones anytime
- Google API refresh tokens work the same way!

## Why is it Needed?

Problems that Google OAuth 2.0 refresh tokens solve:

1. **Authentication expiration issue**: Access tokens typically expire after 1 hour, requiring users to log in again—inconvenient.
2. **Balance security and convenience**: Maintain security with short-lived access tokens while enabling new access token issuance through refresh tokens without user re-authentication.
3. **Server-side automation**: Essential for services requiring periodic background Google API access (e.g., calendar sync, email automation).

## Basic Principle

Let's explore core principles of Google OAuth 2.0.

### Understanding Token System

OAuth 2.0 uses two main tokens:

- **Access Token**: Short-term credentials authenticating API requests (valid ~1 hour)
- **Refresh Token**: Long-term credentials for obtaining new access tokens

### Authentication Flow

1. User grants app permission
2. App receives access token and refresh token
3. Use access token for API requests
4. When access token expires, get new one with refresh token
5. Repeat steps 3-4

## Practical Example: 2024 Latest Google Cloud Console Setup

Now let's detail the process of acquiring refresh tokens in 2024's latest Google Cloud Console UI.

### 1. Create Google Cloud Project and Enable APIs

1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project or select existing one
3. Navigate to "APIs & Services" > "Library" from left menu
4. Search needed API (e.g., Google Calendar API) and enable it

### 2. OAuth Consent Screen Setup (2024 UI Changes ⚠️)

1. Navigate to "**Google Auth platform > Branding**" from left menu
   - This corresponds to previous UI's "APIs & Services > OAuth consent screen"
2. Select user type (internal or external)
3. Input app information:
   - App name
   - User support email
   - Developer contact information
4. Add required scopes in "Scopes" or "Data Access" section:
   - Example: `https://www.googleapis.com/auth/calendar` for Calendar API
5. Add test users if needed
6. **Important 2024 Update**: Set publishing status to "Production"
   - Leaving as "Test" causes refresh tokens to expire after 7 days! 
   - Must set to "Production" for refresh tokens to remain valid long-term

### 3. OAuth Client ID and Redirect URI Setup (2024 UI Changes ⚠️)

1. Navigate to "**Google Auth platform > Clients**" from left menu
   - This corresponds to previous UI's "APIs & Services > Credentials"
2. Click "Create client" button
3. Select application type:
   - **Important**: Select "**Web Application**" specifically! 
   - Selecting other types (Desktop App, Android, iOS, etc.) won't show redirect URI input field
4. Enter client name
5. Add following to "**Authorized redirect URIs**" section:
   - For OAuth Playground: `https://developers.google.com/oauthplayground`
   - For your own app: Your application callback URL
6. Click "Create" button to generate client ID and client secret
7. Securely save generated `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`

### 4. Get Refresh Token in OAuth 2.0 Playground

1. Visit [Google OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)
2. Click settings icon (⚙️) upper right
3. **Important**: Check "Use your own OAuth credentials" option
   - Without this, tokens generated with Playground's default credentials auto-cancel within 24 hours! ⚠️
4. Input OAuth client ID and secret created earlier
5. Select needed API and scope from left panel:
   - Example: Select `https://www.googleapis.com/auth/calendar` from "Calendar API v3"
6. Click "Authorize APIs" button and complete OAuth authentication
7. Click "Exchange authorization code for tokens" button
8. Copy "Refresh token"—this is your `GOOGLE_REFRESH_TOKEN`
9. Securely save this refresh token—you must repeat entire process to get another

### 5. Refresh Token Usage Example

Here's the process of acquiring new access tokens using refresh tokens:

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

# Acquire new access token
new_access_token = get_new_access_token(
    'YOUR_CLIENT_ID', 
    'YOUR_CLIENT_SECRET', 
    'YOUR_REFRESH_TOKEN'
)

# Call API with acquired access token
headers = {'Authorization': f'Bearer {new_access_token}'}
response = requests.get('https://www.googleapis.com/calendar/v3/calendars/primary/events', headers=headers)
```

## Precautions and Tips

⚠️ **Watch Out For These!**

1. **Verify paths according to UI changes**

   - Google Cloud Console UI continuously updates, so menu paths may differ slightly
   - Currently (2024), OAuth settings moved to "Google Auth platform" section
2. **Select web application type**

   - Must select "Web Application" type to set redirect URIs
   - Other types (Desktop App, Android, iOS, etc.) don't display redirect URI field
3. **Refresh token expiration issue**

   - Refresh tokens expire after 7 days if OAuth consent screen is in "Test" state
   - Must set publishing status to "Production" for production environments
   - Verification process may be required, subject to Google policy changes
4. **Refresh token limit**

   - Google enforces maximum 100 refresh tokens per account per OAuth 2.0 client ID
   - Reaching limit automatically invalidates oldest token when creating new one
   - Easy to hit this limit during testing—be careful

5. **Token security**

   - Refresh tokens are more powerful credentials than access tokens, so handle with extra care
   - Store in environment variables or secure secret management systems
   - Never include in source code or version control systems

💡 **Helpful Tips**

- OAuth setup consists of two separate parts:
  1. **Consent Screen Setup** (Google Auth platform > Branding): Permission request screen users see
  2. **Client ID/Redirect Setup** (Google Auth platform > Clients): Technical settings for actual authentication flow
- Redirect URIs must match exactly—case, slashes, http/https scheme all identical
- Consider implementing your own OAuth flow instead of OAuth 2.0 Playground in actual production
- Start with limited scopes during testing, expand as needed
- Implement retry logic to handle access token expiration errors

## Conclusion

So far, we've explored how to acquire OAuth 2.0 refresh tokens in 2024's latest Google Cloud Console UI. Most important changes are UI path changes, selecting web application type when setting redirect URIs, and "Production" status setting to solve refresh token 7-day expiration issue.

Hope this guide helped your Google API integration work!

Any questions or want to know more? Please comment.

## References

- [Google Developer Documentation: Access Google APIs using OAuth 2.0](https://developers.google.com/identity/protocols/oauth2)
- [Google Cloud Console Help: Configure OAuth Consent Screen](https://support.google.com/cloud/answer/10311615?hl=en-GB)
- [Google OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)
- [Google Cloud Platform Console Help: Manage OAuth Clients](https://support.google.com/cloud/answer/15549257?hl=en)

---

#GoogleAPI #OAuth2 #RefreshToken #AuthenticationSystem #GoogleCloud #2024Update
