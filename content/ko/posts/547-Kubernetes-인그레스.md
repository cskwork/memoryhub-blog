---
title: "Kubernetes 인그레스"
date: 2025-04-13T11:57:40+09:00
slug: "547-Kubernetes-인그레스"
original_url: "https://memoryhub.tistory.com/547"
tistory_id: 547
draft: false
---

안녕하세요! 쿠버네티스(Kubernetes) 세상에 오신 것을 환영합니다! ? 서비스를 여러 개 만들었는데, 이걸 어떻게 외부 사용자들이 쉽게 접근하게 할 수 있을지 고민해보신 적 있으신가요? 마치 여러 상점이 모인 큰 쇼핑몰 입구에서 원하는 가게로 안내해주는 안내 데스크처럼, 쿠버네티스 클러스터 외부의 요청을 내부의 여러 서비스로 똑똑하게 연결해주는 문지기 역할이 필요한데요, 바로 **인그레스(Ingress)**가 그 역할을 해준답니다! 오늘은 인그레스가 무엇이고 왜 필요한지 쉽고 재미있게 알아볼게요! ?

## 등장 배경

예전에는 쿠버네티스 클러스터 안의 서비스를 외부로 노출시키려면 주로 `Service`의 `NodePort`나 `LoadBalancer` 타입을 사용했어요.

- **NodePort**: 모든 워커 노드(Worker Node)의 특정 포트를 열어서 외부에서 접근하게 하는 방식이에요. 하지만 노드의 IP가 변경될 수 있고, 80(HTTP)이나 443(HTTPS) 같은 표준 포트를 사용하기 어렵다는 단점이 있었죠. ?
- **LoadBalancer**: 클라우드 환경(AWS, GCP, Azure 등)에서 주로 사용되며, 서비스마다 클라우드 제공업체의 로드밸런서를 생성해서 외부 IP를 할당받는 방식이에요. 편리하긴 하지만, 서비스마다 로드밸런서가 생성되어 비용 부담이 커질 수 있다는 단점이 있었어요. ?

특히, 여러 서비스를 하나의 도메인 이름이나 IP 주소 아래에서 경로별로 나누어 관리하고 싶을 때, 위 방식들로는 설정이 복잡하거나 비효율적이었습니다. 이때, 더 스마트한 방법이 필요했고, 그래서 인그레스가 등장하게 되었답니다! ?

## 인그레스(Ingress)의 특징/용도 - 인그레스가 해결하는 문제들

인그레스는 클러스터 외부에서 들어오는 HTTP/HTTPS 요청을 내부 서비스로 연결해주는 \*\*API 객체(규칙 모음)\*\*입니다. 인그레스는 다음과 같은 문제들을 멋지게 해결해줘요!

1. **외부 트래픽의 단일 진입점 관리**: 여러 서비스가 있더라도, 외부에서는 주로 인그레스 컨트롤러에 할당된 **하나의 IP 주소**로만 접근하면 됩니다. 마치 쇼핑몰의 정문처럼요! 이렇게 하면 DNS 설정이나 방화벽 관리가 훨씬 수월해져요. ?
2. **L7 라우팅 (호스트/경로 기반)**: OSI 7계층 중 애플리케이션 계층(L7)에서 작동하기 때문에, 요청 URL의 **호스트 이름**(`service1.example.com`, `service2.example.com`)이나 **경로**(`/api`, `/web`)를 보고 어떤 서비스로 보낼지 결정할 수 있어요. 마치 안내 데스크에서 "A 매장은 왼쪽, B 매장은 오른쪽으로 가세요"라고 안내하는 것과 같아요. ?
3. **SSL/TLS 종료 (Termination)**: HTTPS 통신을 위한 복잡한 SSL/TLS 인증서 관리와 암호화/복호화 과정을 인그레스 컨트롤러에서 **대신 처리**해줄 수 있어요. 개별 서비스는 암호화 부담 없이 내부 통신에만 집중할 수 있게 되죠. 보안 설정도 한 곳에서 관리하니 편리해요! ?
4. **이름 기반 가상 호스팅**: 하나의 IP 주소를 사용하면서도 여러 개의 도메인 이름(예: `blog.example.com`, `shop.example.com`)으로 서비스를 구분하여 운영할 수 있게 해줘요. 효율적인 IP 사용이 가능해집니다. ?

## 핵심 원리

인그레스가 실제로 동작하려면 두 가지 핵심 요소가 필요해요. 바로 '인그레스 리소스'와 '인그레스 컨트롤러'입니다.

### 1. 인그레스 리소스 (Ingress Resource)

"어떤 요청이 오면(규칙), 어떤 서비스로 보내라(목적지)"는 **라우팅 규칙**을 정의하는 쿠버네티스 오브젝트(객체)예요. YAML 파일 형태로 작성하며, 이것만 생성한다고 해서 바로 트래픽이 처리되는 것은 아니에요. 어디까지나 '설계도'나 '규칙 설명서' 같은 역할이죠. ?

```
# 예시: 라우팅 규칙 정의 (ingress-rules.yaml)
apiVersion: networking.k8s.io/v1
kind: Ingress # 종류는 Ingress
metadata:
  name: my-ingress-rules # 이 인그레스 규칙의 이름
  annotations:
    # 특정 Ingress Controller를 위한 추가 설정 (예: Nginx)
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx-custom # 사용할 Ingress Controller 지정 (권장)
  rules: # 여기에 규칙들을 정의해요
  - host: myapp.example.com # 만약 'myapp.example.com'으로 요청이 오면
    http:
      paths:
      - path: /login # 경로가 '/login'으로 시작하면
        pathType: Prefix # Prefix: '/login', '/login/v2' 등 모두 해당
        backend:
          service:
            name: login-service # 'login-service'라는 이름의 서비스로 보낸다
            port:
              number: 8080 # 그 서비스의 8080 포트로
      - path: /user # 경로가 '/user'로 시작하면
        pathType: Prefix
        backend:
          service:
            name: user-service # 'user-service'로 보낸다
            port:
              number: 80 # 그 서비스의 80 포트로
  # 기본 규칙 (위 규칙에 해당하지 않는 모든 요청)
  defaultBackend:
    service:
      name: default-service # 'default-service'로 보낸다
      port:
        number: 80
```

### 2. 인그레스 컨트롤러 (Ingress Controller)

인그레스 리소스에 정의된 **규칙(설계도)을 실제로 읽어서 실행하는** 똑똑한 로드밸런서 또는 프록시 서버예요. ?‍♀️ 외부로부터 들어오는 트래픽을 감시하고 있다가, 인그레스 규칙에 맞춰 적절한 내부 서비스로 연결(라우팅)해주는 실질적인 '행동 대장'이죠.

쿠버네티스 자체에서 기본으로 제공하는 컨트롤러는 없기 때문에, **반드시 클러스터에 별도로 설치하고 실행해야** 인그레스가 작동합니다! 대표적인 인그레스 컨트롤러로는 다음과 같은 것들이 있어요.

- **Nginx Ingress Controller**: 가장 널리 사용되는 컨트롤러 중 하나예요. (쿠버네티스 공식 지원)
- **Traefik**: 설정이 비교적 간편하고 동적인 환경에 잘 맞는 컨트롤러예요.
- **HAProxy Ingress**: 고성능 프록시인 HAProxy 기반의 컨트롤러예요.
- **클라우드 제공사 컨트롤러**: AWS (ALB Ingress Controller), GCP (GCE Ingress Controller), Azure (Application Gateway Ingress Controller) 등 클라우드 환경에 최적화된 컨트롤러도 있어요.

인그레스 컨트롤러는 보통 클러스터 내부에 파드(Pod) 형태로 배포되고, 외부에서 이 컨트롤러에 접근할 수 있도록 `LoadBalancer`나 `NodePort` 타입의 서비스를 이용해 노출시켜줍니다.

```
# Nginx Ingress Controller 설치 예시 (Helm 패키지 매니저 사용)

# 1. Helm 리포지토리 추가
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

# 2. 네임스페이스 생성 및 설치 (LoadBalancer 타입 서비스로 노출)
helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --create-namespace \
  --set controller.service.type=LoadBalancer # 클라우드 환경 등에서 외부 IP 자동 할당
```

## 사례 소개

인그레스는 정말 다양한 상황에서 유용하게 쓰여요.

- **마이크로서비스 아키텍처 (MSA)**: 여러 개의 작은 서비스(로그인, 상품, 주문 등)를 개발했을 때, 외부에는 `api.example.com`이라는 단일 주소로 노출하고, `/login`, `/products`, `/orders` 같은 경로에 따라 각 마이크로서비스로 라우팅할 수 있어요. 관리가 정말 편해지겠죠? ?
- **Blue/Green 배포**: 새로운 버전의 애플리케이션(Green)을 배포한 뒤, 인그레스 규칙만 살짝 변경해서 트래픽을 점진적으로 새 버전으로 옮기거나, 문제가 생겼을 때 즉시 이전 버전(Blue)으로 되돌릴 수 있어요. ?
- **A/B 테스팅**: 특정 사용자 그룹이나 특정 비율의 트래픽만 새로운 기능이 있는 서비스로 보내서 테스트해볼 수 있어요. 인그레스 컨트롤러의 고급 기능을 활용하면 가능해요. ?

**정리하면 이런 흐름이에요:**

![](/images/547-Kubernetes-인그레스/Editor _ Mermaid Chart-2025-04-13-030202.png)

**표로 비교 정리:**

| 특징 | NodePort | LoadBalancer (Service Type) | Ingress |
| --- | --- | --- | --- |
| **OSI 계층** | L4 (Transport) | L4 (Transport) | L7 (Application) |
| **진입점** | 모든 노드 IP + 지정 포트 | 서비스별 외부 IP (클라우드 LB) | 단일 외부 IP (Ingress Controller의 LB) |
| **라우팅 단위** | 서비스 | 서비스 | 서비스 (Host/Path 기반) |
| **대상 서비스 수** | 1 | 1 | 다수 (규칙에 따라) |
| **주요 기능** | 기본적인 외부 노출 | 외부 로드밸런서 자동 생성 | 경로/호스트 라우팅, SSL 종료, 가상 호스팅 |
| **필수 요소** | - | 클라우드 환경 지원 | **Ingress Controller 설치 필요** |

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **Ingress Controller 설치는 필수!**: 다시 한번 강조하지만, Ingress 리소스(규칙)만 만들면 아무 일도 일어나지 않아요. ?‍♀️ Nginx, Traefik 같은 **Ingress Controller를 꼭 설치하고 실행**해야 규칙이 실제로 적용됩니다!
   - **상세 설명**: 컨트롤러가 없다면, 외부 요청이 들어와도 어디로 가야 할지 알려주는 실행 주체가 없는 셈이에요.
   - **해결 방법**: 사용하는 환경(클라우드, 온프레미스 등)과 요구사항에 맞는 Ingress Controller를 선택하고, 공식 문서를 따라 설치해주세요. (Helm, kubectl apply 등)
2. **Ingress Controller 노출 확인**: 설치된 Ingress Controller 자체도 외부에서 접근 가능해야 해요. 보통 Controller 설치 시 `LoadBalancer`나 `NodePort` 타입의 서비스가 함께 생성되는데, 이 서비스의 외부 IP나 포트로 접근해야 합니다.
   - **상세 설명**: 사용자는 Ingress Controller의 외부 주소로 요청을 보내고, Controller가 내부 서비스로 연결해주는 구조입니다.
   - **해결 방법**: `kubectl get svc -n <ingress-controller-namespace>` 명령어로 Controller 서비스의 `EXTERNAL-IP` 또는 `PORT`를 확인하세요.

? **꿀팁**

- **어노테이션(Annotations) 적극 활용**: Ingress 리소스의 `metadata.annotations` 필드를 통해 컨트롤러별 부가 기능을 설정할 수 있어요. 예를 들어 Nginx Controller에서는 경로 재작성(`rewrite-target`), 인증, 속도 제한 등을 어노테이션으로 제어할 수 있답니다. 컨트롤러 문서를 꼭 확인해보세요! ⚙️
- **IngressClass 사용**: 클러스터에 여러 종류의 Ingress Controller를 사용하거나, 특정 Controller를 명시적으로 지정하고 싶을 때 `spec.ingressClassName` 필드를 사용하면 좋아요. 혼란을 줄이고 명확하게 관리할 수 있어요.
- **TLS 인증서 관리 자동화**: `cert-manager`와 같은 도구를 Ingress Controller와 함께 사용하면 Let's Encrypt 같은 무료 인증 기관에서 SSL/TLS 인증서를 자동으로 발급받고 갱신할 수 있어서 HTTPS 설정이 정말 편해져요! ✨

## 마치며

지금까지 쿠버네티스의 똑똑한 문지기, 인그레스(Ingress)에 대해 알아보았습니다. 처음에는 인그레스 리소스와 컨트롤러 개념이 조금 헷갈릴 수 있지만, 클러스터 외부 트래픽을 효율적이고 유연하게 관리하는 데 정말 강력한 도구랍니다! 이 글이 여러분의 쿠버네티스 여정에 작은 도움이 되었기를 바랍니다! ?

혹시 더 궁금한 점이나 공유하고 싶은 경험이 있다면 언제든지 댓글로 남겨주세요! ?‍♀️

## 참고 자료 ?

- [쿠버네티스 공식 문서 - 인그레스(Ingress)](https://kubernetes.io/ko/docs/concepts/services-networking/ingress/)
- [쿠버네티스 공식 문서 - 인그레스 컨트롤러](https://kubernetes.io/ko/docs/concepts/services-networking/ingress-controllers/)
- [[Kubernetes] k8s Ingress란? (feat. 도메인 없이 테스트하기) - 티스토리](https://nayoungs.tistory.com/entry/Kubernetes-k8s-Ingress%EB%9E%80)
- [Ingress vs. Load Balancer in Kubernetes | Baeldung on Ops (영문)](https://www.baeldung.com/ops/kubernetes-ingress-vs-load-balancer)
