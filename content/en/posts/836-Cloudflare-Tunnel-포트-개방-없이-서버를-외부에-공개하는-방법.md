---
title: "Cloudflare Tunnel: Expose Your Server Without Opening Ports"
date: 2025-10-06T15:20:22+09:00
slug: "836-Cloudflare-Tunnel-포트-개방-없이-서버를-외부에-공개하는-방법"
original_url: "https://memoryhub.tistory.com/836"
tistory_id: 836
draft: false
---

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     🔒 CLOUDFLARE TUNNEL                                ║
    ║                                                           ║
    ║     ┌─────────┐                      ┌─────────────┐     ║
    ║     │  Your   │ ◄──── Outbound ────► │ Cloudflare  │     ║
    ║     │ Server  │      Connection      │   Network   │     ║
    ║     └─────────┘                      └─────────────┘     ║
    ║         │                                   ▲            ║
    ║         │ No Open Ports                     │            ║
    ║         │ No Public IP                      │ HTTPS      ║
    ║         ▼                                   │            ║
    ║     🔥 Firewall                      👤 Users          ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
```

# 

Ever wanted to access your home server from outside but dreaded router port forwarding or security concerns? Or shared a local app in development with teammates using ngrok, but got frustrated with constantly changing URLs?

**Cloudflare Tunnel is reverse tunneling technology that lets you safely access your server externally without opening any ports.** This article explains the principle and advantages clearly.

**One-liner:** Cloudflare Tunnel is a free tunneling service using "outbound-only" reverse proxying—your server initiates the connection to Cloudflare. It safely exposes web servers, SSH, remote desktop, etc. without opening firewall ports.

## Background

Traditionally, accessing internal servers from outside relied on two methods. Port forwarding opens specific router ports to forward external requests to internal servers. VPN connects to an internal network via virtual private network.

The problem: both methods **expose the server's IP address externally**. This makes servers targets for DDoS attacks, port scanning, brute-force attacks. Also, home internet usually uses dynamic IPs, requiring DDNS setup.

> Cloudflare Tunnel is reverse proxy technology where the server 'calls first' to Cloudflare to establish communication paths.

Think of it like a post office. The old way is "publish your home address and let anyone find you." Cloudflare Tunnel is "register a PO box and let the post office deliver instead." You hide your home address (server IP) and communicate only through the post office (Cloudflare).

## Core Concept

Cloudflare Tunnel's operating principle condenses to one sentence: "outbound-only connection."

Normal web servers await inbound connections. They open ports 80 and 443 to receive client requests. Cloudflare Tunnel does the opposite. A lightweight daemon called `cloudflared` installed on your server **creates an outbound connection first** to Cloudflare's global network.

Most firewalls permit outbound traffic by default. `cloudflared` leverages this. Once the server's outbound connection to Cloudflare succeeds, bidirectional communication becomes possible via this tunnel. External user requests reach the internal server through Cloudflare.

The specific workflow is:

**First**, install and run `cloudflared` daemon on your server.

**Second**, `cloudflared` performs TLS handshake with Cloudflare edge servers, creating encrypted WebSocket connection.

**Third**, register the tunnel-connected domain in Cloudflare DNS.

**Fourth**, users accessing that domain have their requests delivered through the tunnel to your internal server via Cloudflare.

The core security advantage: **block all inbound traffic in your server's firewall**. Allowing only `cloudflared`'s outbound connection makes direct attacks impossible, bypassing Cloudflare entirely.

## Tutorial

Here are step-by-step instructions for simplest Cloudflare Tunnel setup.

### ① Install cloudflared

Installation commands vary by OS.

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

Verify successful installation with `cloudflared --version`.

### ② Quick Test (TryCloudflare)

Create temporary tunnels instantly without an account. If your dev server runs on port 3000 locally:

```
cloudflared tunnel --url http://localhost:3000
```

Running this generates a temp URL like `https://random-words.trycloudflare.com`. You can access your local server externally via this URL. Useful for testing and demos, but URLs change each time, unsuitable for permanent use.

### ③ Create Permanent Tunnel (Dashboard Method)

To create permanent tunnel with fixed domain, you need a Cloudflare account and that domain.

Go to Cloudflare dashboard and navigate to Zero Trust menu. Select Tunnels under Networks and click Create a tunnel. Specifying a tunnel name provides installation commands and tokens. Run those commands on your server to create the tunnel. Next, on the Public Hostnames tab, map your desired subdomain to your local service address.

For example, map `app.mydomain.com` to `http://localhost:3000` and `api.mydomain.com` to `http://localhost:8000` respectively. DNS records are created automatically.

## Best Practices/Pattern Comparison

| Aspect | Cloudflare Tunnel | ngrok | Port Forwarding |
| --- | --- | --- | --- |
| Cost | Free (unlimited bandwidth) | Limited free tier, custom domain paid | Free |
| Custom domain | Free support | Requires paid plan | DDNS setup needed |
| Setup complexity | Medium (account/domain needed) | Low (instant) | High (router config) |
| Security | Very high (no IP exposure, DDoS protection) | High | Low (IP exposed) |
| Protocols | HTTP, HTTPS, SSH, RDP, TCP | HTTP, TCP | All protocols |
| Stability | High (global edge network) | Medium | Medium |

ngrok suits quick testing; Cloudflare Tunnel shines for production stability and free custom domains. Port forwarding supports all protocols without special dependencies but has security gaps.

## Closing

- Cloudflare Tunnel uses "outbound-first" approach where servers initiate external connections, exposing services without inbound ports.
- Free tier includes custom domains, unlimited bandwidth, DDoS protection, SSL certificates.
- Practical tip: Try `cloudflared tunnel --url http://localhost:port` today to expose your local server externally.

## References

- Cloudflare Tunnel official docs (<https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>)
- Zero Trust Dashboard guide (<https://blog.cloudflare.com/ridiculously-easy-to-use-tunnels/>)
- cloudflared GitHub repo (<https://github.com/cloudflare/cloudflared>)
