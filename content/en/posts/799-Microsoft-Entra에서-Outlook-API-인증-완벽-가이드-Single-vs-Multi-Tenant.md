---
title: "Complete Guide to Outlook API Authentication in Microsoft Entra: Single vs Multi-Tenant"
date: 2025-09-29T09:46:54+09:00
slug: "799-Microsoft-Entra에서-Outlook-API-인증-완벽-가이드-Single-vs-Multi-Tenant"
original_url: "https://memoryhub.tistory.com/799"
tistory_id: 799
draft: false
categories: ["Dev Util"]
tags: ["Agents"]
---

```
     ┌─────────────────────────────────┐
     │  🔐 Microsoft Entra ID          │
     │                                 │
     │   ┌─────┐      ┌─────┐         │
     │   │ APP │──────│ KEY │         │
     │   └─────┘      └─────┘         │
     │     │            │              │
     │     └────────────┘              │
     │         │                       │
     │         ▼                       │
     │    📧 Outlook API               │
     │                                 │
     │  Single ←→ Multi-Tenant         │
     └─────────────────────────────────┘
```

# 

## 

**To change an Azure App to Multi-tenant**, change the App registration's **Supported account types** to "**Accounts in any organizational directory and personal Microsoft accounts**", clean up **Redirect URI/permissions/verification (Publisher verification)**, and align the OAuth endpoint to /common (or /organizations, /consumers as needed).

---

Have you ever started a Microsoft 365 Outlook API automation project only to get stuck at the first step—getting authentication keys? With entra.microsoft.com's UI differing from the old Azure Portal, many people confuse Client ID and Secret ID, or don't know where to copy values. Multi-tenant conversion is even more complex. This article provides a **step-by-step guide to registering apps for Outlook API in Microsoft Entra, generating client credentials, and configuring Single/Multi-tenant settings** without mistakes.

---

## 1. Background: Single vs Multi-Tenant, Why It Matters

Microsoft Entra ID organizes users and apps into groups called tenants. Single-tenant apps only work in the registered tenant (home tenant), while Multi-tenant apps work for both home tenant and other tenant users.

### Core Concepts Explained

Term Meaning Usage

|  |  |  |
| --- | --- | --- |
| **Single-Tenant** | Only one organization (tenant) can access | Internal apps, enhanced security |
| **Multi-Tenant** | Users from multiple organizations can access | SaaS products, public services |
| **Application (Client) ID** | Unique GUID identifying the app | Required for all API calls |
| **Client Secret** | App's password | Used for token issuance authentication |
| **Secret ID** | Identifier for the Secret | ⚠️ Not used for authentication |
| **signInAudience** | Supported account types setting | AzureADMyOrg, AzureADMultipleOrgs, etc. |

### Endpoint Differences

The issuer part of the OAuth authentication URL controls who can sign in.

Endpoint Target Use Case

|  |  |  |
| --- | --- | --- |
| /common | Work/school accounts + personal Microsoft accounts | Multi-tenant apps (all users) |
| /organizations | Work/school accounts only | Organization-only Multi-tenant |
| /consumers | Personal Microsoft accounts only | Personal user-targeted apps |
| /{tenant-id} | Specific tenant only | Single-tenant apps |

---

## 2. Core Concept

> **In Microsoft Entra, when you register an app and create a Client Secret, the Value shown is displayed only once—you must save it immediately. The Value, not Secret ID, is the actual authentication key. When converting to Multi-tenant, change both Supported account types and the endpoint together.**

---

## 3. Practice

### ① App Registration (Single-Tenant by Default)

1. **Access Microsoft Entra Admin Center**
   - Log in to <https://entra.microsoft.com> (Application Developer permission minimum required)
   - Select **Identity > Applications > App registrations** from left menu
2. **Click New registration**
   - **Name**: Enter app name (e.g., OutlookMailAPI)
   - **Supported account types**:
     - **Accounts in this organizational directory only**: Single-tenant (default recommended)
     - **Accounts in any organizational directory**: Multi-tenant (organizations only)
     - **Accounts in any organizational directory and personal Microsoft accounts**: Multi-tenant (all users)
   - **Redirect URI**: Optional (leave empty if not a web app)
   - Click **Register**
3. **Verify Client ID**
   - Copy **Application (client) ID** from Overview tab (⚠️ Not Object ID or Directory ID)
   - Also copy **Directory (tenant) ID** (needed for Single-tenant endpoint)

### ② Generate Client Secret

1. **Navigate to Certificates & secrets menu**
   - Select **Certificates & secrets** from left menu
2. **Click New client secret**
   - **Description**: Enter Secret purpose (e.g., OutlookAPI-Production)
   - **Expires**: Select 6 months or custom period (recommended)
   - Click **Add**
3. **⚠️ Important: Copy Value Immediately**
   - The **Value** shown under the Value column is your actual Client Secret
   - Secret ID is not used for authentication, and this page cannot be revisited to see the Value again
   - Save securely in a password manager

### ③ Set Up Outlook API Permissions

1. **Navigate to API permissions menu**
   - Select **API permissions** from left menu
2. **Add Microsoft Graph permissions**
   - Click **Add a permission > Microsoft Graph**
   - Select based on your scenario:**Delegated permissions**: Act on behalf of user
   - Mail.Read: Read user mail
   - Mail.ReadWrite: Read/write mail
   - Mail.Send: Send mail
   - offline\_access: Issue refresh token**Application permissions**: For background services
   - Mail.Read: Read all mailboxes
   - Mail.ReadWrite: Write all mailboxes
   - Mail.Send: Send as all users
3. **Grant Admin Consent**
   - Application permissions require clicking **Grant admin consent** button

---

## 4. Single-Tenant → Multi-Tenant Conversion Method

### Step 1: Switch App Basic Settings

1. **Azure Portal → Microsoft Entra ID → App registrations → (Your app)**
2. **Authentication tab → Choose option from Supported account types**
   - ✅ **Accounts in any organizational directory and personal Microsoft accounts** (broadest scope)
   - Or **Accounts in any organizational directory** (organizations only)
3. Click **Save**

### Step 2: Clean Up Redirect URIs

1. In same **Authentication** screen, register **Web** item's **Redirect URI**
   - n8n example: https://<YOUR\_N8N\_HOST>/rest/oauth2-credential/callback
   - Protocol (https), slash must match exactly
2. Disable **Implicit grant** (not recommended)
   - **Authorization code + PKCE** recommended

### Step 3: Change Authentication Endpoint

The issuer value in the endpoint controls who can sign in.

**Single-tenant endpoint** (existing):

```
https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize
https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token
```

**Multi-tenant endpoint** (after change):

```
https://login.microsoftonline.com/common/oauth2/v2.0/authorize
https://login.microsoftonline.com/common/oauth2/v2.0/token
```

**Organization accounts only** (optional):

```
Use /organizations
```

**Personal accounts only** (optional):

```
Use /consumers
```

### Step 4: Permissions and Consent Flow

For Multi-tenant apps, other tenant users need user or admin consent on first login.

- Run **Grant admin consent** in home tenant (applies to your organization only)
- Other tenants require their organization's admin approval

### Step 5: Enhance Security/Trust (Strongly Recommended)

Multi-tenant app development can face difficulties due to various IT admin policies.

1. **Branding & properties**: Set app name/icon/homepage URL
2. **Publisher verification(Verified publisher)**:
   - Connect verified domain (e.g., yourcompany.com)
   - After verification, provide clean consent screen without "Unverified" warning
3. **Least privilege principle**: Request only permissions your app actually needs

---

## 5. Practical Setup in n8n

### OAuth Credential Settings

1. **Create Credentials → Microsoft OAuth2**
2. **Grant Type**: Authorization Code
3. **Authorization URL**: <https://login.microsoftonline.com/common/oauth2/v2.0/authorize>
4. **Token URL**: <https://login.microsoftonline.com/common/oauth2/v2.0/token>
5. **Scope** (space-separated):

   ```
   openid profile email offline_access User.Read Mail.Read
   ```
6. **Client ID**: Enter Application (client) ID
7. **Client Secret**: Enter Secret Value
8. **Redirect URI**: Enter exactly as in Azure

### Test

**Test with HTTP Request node:**

```
GET https://graph.microsoft.com/v1.0/me/messages?$top=5
```

---

## 6. Quick Conversion with Azure CLI

```
# Change to Multi-tenant (organizations + personal accounts)
az ad app update \
  --id <APPLICATION_CLIENT_ID> \
  --set signInAudience=AzureADandPersonalMicrosoftAccount

# Organization-only Multi-tenant
az ad app update \
  --id <APPLICATION_CLIENT_ID> \
  --set signInAudience=AzureADMultipleOrgs

# Add Redirect URI
az ad app update \
  --id <APPLICATION_CLIENT_ID> \
  --web-redirect-uris https://<YOUR_N8N_HOST>/rest/oauth2-credential/callback
```

**signInAudience value options**: AzureADMyOrg(Single-tenant) / AzureADMultipleOrgs(organization-only Multi-tenant) / AzureADandPersonalMicrosoftAccount(organizations+personal)

---

## 7. Best Practices

Item Recommended Approach Cautions

|  |  |  |
| --- | --- | --- |
| **Secret Storage** | Use Azure Key Vault | Never hardcode in source code |
| **Expiration Management** | Renew every 6 months with alert | No default alert—requires script automation |
| **Permission Design** | Apply least privilege principle | Avoid requesting unnecessary permissions |
| **Authentication Method** | Use Managed Identity if possible | No secret management needed in Azure environment |
| **Multi-tenant Security** | Complete Publisher Verification | Build user trust |
| **Endpoint Selection** | Choose /common or /organizations per purpose | Use /organizations if need to block personal accounts |

---

## 8. Quick Diagnosis When Issues Occur

Symptom Cause Solution

|  |  |  |
| --- | --- | --- |
| AADSTS50194 error | Single-tenant but using /common | Switch /common → /{tenant-id} or convert to Multi-tenant |
| Consent failure | Other tenant needs admin consent | Request approval from that organization's admin |
| Redirect URI mismatch | Azure and app URIs don't match exactly | Verify 100% match including protocol/slash |
| Permission mismatch | Graph permission added but consent not refreshed | Re-run Grant admin consent |

---

## 9. Conclusion

While Microsoft Entra's UI improvements make it easy to confuse Secret ID with Client Secret Value, remember this article's core: **The Value column's value is the actual password**, and to convert from Single-tenant to Multi-tenant, change both Supported account types and the endpoint together.

**3 Real-World Tips:**

1. Automate Secret expiration alerts with PowerShell
2. Increase trust with Publisher Verification when deploying Multi-tenant
3. When using Mail.Send with Application permissions, restricting specific mailboxes through Application Access Policy is essential for security

Now you can safely start various projects like mail automation and calendar sync with Outlook API.

---

### References

- Microsoft Learn: App Registration Guide - <https://learn.microsoft.com/entra/identity-platform/quickstart-register-app>
- Single vs Multi-tenant Apps - <https://learn.microsoft.com/entra/identity-platform/single-and-multi-tenant-apps>
- Converting Single-tenant to Multi-tenant - <https://learn.microsoft.com/entra/identity-platform/howto-convert-app-to-be-multi-tenant>
- OAuth 2.0 and OpenID Connect Protocols - <https://learn.microsoft.com/entra/identity-platform/v2-protocols>
- Outlook Mail API Overview - <https://learn.microsoft.com/graph/api/resources/mail-api-overview>
- Microsoft Graph Permissions Reference - <https://learn.microsoft.com/graph/permissions-reference>
