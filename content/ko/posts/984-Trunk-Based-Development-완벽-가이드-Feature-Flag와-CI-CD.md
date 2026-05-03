---
title: "Trunk-Based Development 완벽 가이드, Feature Flag와 CI/CD"
date: 2026-01-21T22:16:00+09:00
slug: "984-Trunk-Based-Development-완벽-가이드-Feature-Flag와-CI-CD"
original_url: "https://memoryhub.tistory.com/984"
tistory_id: 984
draft: false
---

```
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║     ┌─────────────────────────────────────────────────────────┐   ║
║     │  main ──●──●──●──●──●──●──●──●──●──●──●──●──●──●──●──►  │   ║
║     │          ╲╱    ╲╱    ╲╱    ╲╱    ╲╱    ╲╱    ╲╱         │   ║
║     │         feat  feat  feat  feat  feat  feat  feat        │   ║
║     │        (2hrs) (4hrs)(1hr) (3hrs)(2hrs)(1hr) (4hrs)      │   ║
║     └─────────────────────────────────────────────────────────┘   ║
║                                                                   ║
║     ┌─────────────────────────────────────────────────────────┐   ║
║     │  [Push] ──► [CI Test] ──► [Build] ──► [Deploy] ──► [✓]  │   ║
║     │    │           │            │           │               │   ║
║     │    └───────────┴────────────┴───────────┘               │   ║
║     │              Feature Flag Control                       │   ║
║     └─────────────────────────────────────────────────────────┘   ║
║                                                                   ║
║              TRUNK-BASED DEVELOPMENT + CI/CD                      ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

"코드 머지가 무섭다"는 개발자라면 주목해야 합니다. 2주간 작업한 feature 브랜치를 머지하려는데 충돌이 200개, 리뷰어는 500줄 변경 사항을 보며 한숨을 쉽니다. 이 악몽 같은 상황이 반복된다면, 브랜칭 전략 자체를 다시 생각해볼 때입니다.

**Trunk-Based Development(TBD)는 "작게, 자주, 안전하게" 머지하는 철학이며,**

**Feature Flag와 CI/CD 파이프라인이 이를 가능하게 합니다.**

이 글을 통해 TBD의 작동 원리부터 실제 구현 방법까지 모두 익힐 수 있습니다.

**결론부터 말하면, TBD는 하루 이내의 짧은 브랜치 수명, 자동화된 CI/CD 파이프라인,**

**그리고 Feature Flag를 통한 배포-릴리스 분리가 핵심이며, 이 세 가지가 갖춰지면 "머지 지옥"에서 벗어날 수 있습니다.**

## 배경

소프트웨어 개발에서 가장 큰 병목 중 하나는 코드 통합입니다. 여러 개발자가 각자의 브랜치에서 오래 작업할수록, 나중에 합칠 때 문제가 커집니다. 이를 "Integration Hell" 또는 "Merge Hell"이라 부릅니다.

Google의 DORA(DevOps Research and Assessment) 연구팀이 10년 이상 진행한 조사에 따르면, **고성과 팀(Elite Performers)의 공통점은 배포 빈도가 높고, 변경 리드 타임이 짧다**는 것입니다.

이들은 하루에도 여러 번 프로덕션에 배포하며, 코드 커밋부터 배포까지 1시간 이내를 목표로 합니다. TBD는 바로 이런 고성과 팀의 작업 방식을 체계화한 것입니다.

> Trunk-Based Development란, 모든 개발자가 하나의 main 브랜치(trunk)에 자주, 작은 변경을 통합하는 버전 관리 전략입니다. Feature 브랜치를 만들더라도 수 시간에서 최대 1~2일 이내에 머지하는 것이 원칙입니다.

핵심 아이디어는 간단합니다. **브랜치가 오래 살아있을수록 위험이 커진다**는 것입니다. 2주간 분리된 코드는 main과 점점 멀어지고,

결국 머지할 때 "빅뱅 통합"이 됩니다. 반면 매일 작은 변경을 머지하면, 충돌이 발생해도 범위가 좁아 해결이 쉽습니다.

## TBD의 핵심 원칙

TBD를 성공적으로 도입하려면 세 가지 핵심 원칙을 이해해야 합니다.

첫째, **짧은 브랜치 수명**입니다. Feature 브랜치는 몇 시간에서 최대 하루 이내에 main으로 머지되어야 합니다. 작업이 완료되지 않았더라도 머지합니다. 완료되지 않은 기능은 Feature Flag로 숨기면 됩니다.

둘째, **작은 배치 크기**입니다. 한 번에 수백 줄을 변경하는 대신, 10~50줄 단위의 작은 커밋을 자주 합니다. 리뷰어가 10분 안에 검토할 수 있는 크기가 이상적입니다. 작은 변경은 버그를 찾기 쉽고, 문제가 생겨도 롤백이 간단합니다.

셋째, **배포와 릴리스의 분리**입니다. 코드를 프로덕션에 배포하는 것과 사용자에게 기능을 노출하는 것은 별개입니다. Feature Flag를 사용하면 미완성 코드를 배포하되, 사용자에게는 보이지 않게 할 수 있습니다. 이것이 TBD를 안전하게 만드는 핵심 메커니즘입니다.

## Feature Flag: TBD의 안전망

Feature Flag(또는 Feature Toggle)는 코드 수준에서 기능의 활성화 여부를 제어하는 기법입니다. 간단히 말해, if-else 조건문으로 특정 기능을 켜거나 끄는 것입니다. 재배포 없이 런타임에 기능을 제어할 수 있다는 점이 핵심입니다.

### Feature Flag의 유형

Martin Fowler의 분류에 따르면 Feature Flag는 네 가지 유형으로 나뉩니다.

**Release Toggle**은 미완성 기능을 숨기는 데 사용합니다. TBD에서 가장 중요한 유형입니다. 개발 중인 코드를 main에 머지하되, 사용자에게는 보이지 않게 합니다. 기능이 완성되면 Toggle을 켜고, 안정화되면 Toggle 코드 자체를 제거합니다.

**Experiment Toggle**은 A/B 테스트에 사용합니다. 사용자의 일부에게만 새 기능을 노출하고 반응을 측정합니다. "버튼 색상을 파란색으로 바꾸면 클릭률이 올라갈까?" 같은 실험에 활용합니다.

**Ops Toggle**은 운영 목적으로 사용합니다. 시스템 부하가 높을 때 특정 기능을 일시적으로 끄거나, 외부 서비스 장애 시 대체 로직을 활성화하는 데 씁니다. Circuit Breaker 패턴과 결합하여 시스템 안정성을 높입니다.

**Permission Toggle**은 사용자 권한에 따라 기능을 제어합니다. 프리미엄 사용자에게만 특정 기능을 제공하거나, 베타 테스터 그룹에게 먼저 기능을 공개할 때 사용합니다.

### Feature Flag 구현 방법

Feature Flag는 직접 구현하거나, LaunchDarkly, Unleash, Flagsmith 같은 전문 플랫폼을 사용할 수 있습니다. 아래는 두 가지 방식의 예시입니다.

**직접 구현 (TypeScript 예시)**

```
// featureFlags.ts
interface FeatureFlags {
  newCheckoutFlow: boolean;
  darkMode: boolean;
  experimentalSearch: boolean;
}

// 환경변수 또는 설정 파일에서 로드
const flags: FeatureFlags = {
  newCheckoutFlow: process.env.FF_NEW_CHECKOUT === 'true',
  darkMode: process.env.FF_DARK_MODE === 'true',
  experimentalSearch: false, // 기본값 off
};

export function isFeatureEnabled(flagName: keyof FeatureFlags): boolean {
  return flags[flagName] ?? false;
}

// 사용 예시
if (isFeatureEnabled('newCheckoutFlow')) {
  renderNewCheckout();
} else {
  renderLegacyCheckout();
}
```

직접 구현의 장점은 외부 의존성이 없다는 것입니다. 하지만 런타임 변경이 어렵고, 사용자별 타겟팅이 복잡합니다.

**LaunchDarkly SDK 사용 (Node.js 예시)**

```
// launchDarklyClient.ts
import * as LaunchDarkly from 'launchdarkly-node-server-sdk';

const client = LaunchDarkly.init(process.env.LAUNCHDARKLY_SDK_KEY);

export async function isFeatureEnabled(
  flagKey: string, 
  userContext: LaunchDarkly.LDContext
): Promise<boolean> {
  await client.waitForInitialization();
  return client.variation(flagKey, userContext, false);
}

// 사용 예시 - Express 미들웨어
async function checkoutMiddleware(req, res, next) {
  const userContext = {
    kind: 'user',
    key: req.user.id,
    email: req.user.email,
    custom: { plan: req.user.subscriptionPlan }
  };

  const useNewCheckout = await isFeatureEnabled('new-checkout-flow', userContext);

  if (useNewCheckout) {
    return newCheckoutHandler(req, res, next);
  }
  return legacyCheckoutHandler(req, res, next);
}
```

전문 플랫폼의 장점은 재배포 없이 플래그를 변경할 수 있고, 사용자 세그먼트별 점진적 롤아웃이 가능하다는 것입니다. 1%의 사용자에게 먼저 노출하고, 문제가 없으면 10%, 50%, 100%로 확대하는 식입니다.

### Feature Flag 모범 사례

Flag 관리는 기술 부채가 될 수 있습니다. 다음 원칙을 지켜야 합니다.

**수명을 짧게 유지합니다.** Release Toggle은 기능 안정화 후 2~4주 내에 제거해야 합니다. 오래된 Flag는 코드 복잡도를 높이고, 테스트 조합을 기하급수적으로 늘립니다.

**명명 규칙을 정합니다.** `show-header`, `enable-new-search`, `use-v2-api`처럼 동작을 명확히 드러내는 이름을 사용합니다. camelCase를 권장하며, 팀 내 일관성이 중요합니다.

**Flag 간 의존성을 피합니다.** Flag A가 켜져야 Flag B가 의미 있는 구조는 복잡도를 폭발시킵니다. 각 Flag는 독립적으로 작동해야 합니다.

**모든 Flag 조합을 테스트합니다.** CI 파이프라인에서 주요 Flag 조합에 대해 테스트를 실행해야 합니다. Flag가 3개면 8가지 조합이 생깁니다. 중요한 조합을 선별하여 테스트 매트릭스를 구성합니다.

## CI/CD 파이프라인: TBD의 심장

TBD가 작동하려면 강력한 CI/CD 파이프라인이 필수입니다. 개발자가 하루에 여러 번 main에 머지하는데, 매번 수동으로 테스트하고 배포할 수는 없기 때문입니다. **자동화된 테스트가 품질을 보장하고, 자동화된 배포가 속도를 보장합니다.**

### TBD를 위한 CI/CD 파이프라인 구조

일반적인 TBD CI/CD 파이프라인은 다음 단계로 구성됩니다.

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Commit    │───►│  CI Build   │───►│   Deploy    │───►│  Monitor    │
│   & Push    │    │   & Test    │    │   to Prod   │    │  & Verify   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                   │                  │                  │
      │              ┌────┴────┐        ┌────┴────┐        ┌────┴────┐
      │              │ Lint    │        │ Canary  │        │ Metrics │
      │              │ Unit    │        │ Blue/   │        │ Alerts  │
      │              │ Integ   │        │ Green   │        │ Rollback│
      │              │ Security│        │         │        │         │
      │              └─────────┘        └─────────┘        └─────────┘
      │
      └──── Feature Flag로 기능 숨김
```

### GitHub Actions를 활용한 CI/CD 파이프라인 구현

아래는 TBD에 최적화된 GitHub Actions 워크플로우 예시입니다.

```
# .github/workflows/ci-cd.yml
name: TBD CI/CD Pipeline

on:
  push:
    branches: [main]  # main 브랜치에 푸시될 때만 실행
  pull_request:
    branches: [main]  # PR도 같은 파이프라인으로 검증

env:
  NODE_VERSION: '20'

jobs:
  # 1단계: 코드 품질 검사
  lint-and-format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run ESLint
        run: npm run lint

      - name: Check formatting (Prettier)
        run: npm run format:check

  # 2단계: 테스트
  test:
    runs-on: ubuntu-latest
    needs: lint-and-format
    strategy:
      matrix:
        # Feature Flag 조합별 테스트
        feature-flags: 
          - 'FF_NEW_CHECKOUT=false'
          - 'FF_NEW_CHECKOUT=true'
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run unit tests
        run: npm run test:unit
        env:
          ${{ matrix.feature-flags }}

      - name: Run integration tests
        run: npm run test:integration
        env:
          ${{ matrix.feature-flags }}

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          fail_ci_if_error: true

  # 3단계: 보안 스캔
  security:
    runs-on: ubuntu-latest
    needs: lint-and-format
    steps:
      - uses: actions/checkout@v4

      - name: Run Snyk security scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  # 4단계: 빌드 및 이미지 생성
  build:
    runs-on: ubuntu-latest
    needs: [test, security]
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    outputs:
      image-tag: ${{ steps.meta.outputs.tags }}
    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=sha,prefix=
            type=raw,value=latest

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  # 5단계: 배포 (Canary 방식)
  deploy:
    runs-on: ubuntu-latest
    needs: build
    environment: production
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to Kubernetes (10% canary)
        run: |
          kubectl set image deployment/app \
            app=ghcr.io/${{ github.repository }}:${{ github.sha }} \
            --record
          kubectl rollout status deployment/app --timeout=5m
        env:
          KUBECONFIG: ${{ secrets.KUBECONFIG }}

      - name: Run smoke tests
        run: npm run test:smoke
        env:
          API_URL: ${{ secrets.PRODUCTION_URL }}

      - name: Promote to 100% (if smoke tests pass)
        if: success()
        run: |
          kubectl scale deployment/app --replicas=10
```

### 파이프라인 설계 핵심 포인트

**빠른 피드백**이 가장 중요합니다. 전체 파이프라인은 10분 이내에 완료되어야 합니다. Lint와 단위 테스트는 2분 이내, 통합 테스트는 5분 이내를 목표로 합니다. 느린 테스트는 개발자가 피드백을 기다리다 맥락을 잃게 만듭니다.

**병렬 실행**을 활용합니다. 위 예시에서 test와 security 작업은 동시에 실행됩니다. 독립적인 작업은 병렬로 처리하여 전체 시간을 단축합니다.

**Feature Flag 조합 테스트**를 포함합니다. matrix 전략을 사용하여 주요 Flag 조합에 대해 테스트를 실행합니다. 모든 조합을 테스트하기 어렵다면, 가장 위험한 조합을 선별합니다.

**점진적 배포**를 구현합니다. Canary 배포, Blue-Green 배포, Rolling Update 등의 전략으로 위험을 분산합니다. 먼저 10%의 트래픽에만 새 버전을 노출하고, 문제가 없으면 점진적으로 확대합니다.

**자동 롤백**을 준비합니다. Smoke Test 실패 시 자동으로 이전 버전으로 롤백하는 로직을 포함해야 합니다. 빠른 롤백은 장애 시간을 최소화합니다.

## 실습: TBD 워크플로우 전체 흐름

실제 개발 시나리오로 TBD 워크플로우를 따라가 봅시다.

### 1단계: 작업 시작

새로운 결제 기능을 개발한다고 가정합니다. 먼저 Feature Flag를 생성합니다.

```
# LaunchDarkly CLI 또는 대시보드에서 Flag 생성
# Flag Key: new-payment-gateway
# Variations: true (새 결제), false (기존 결제)
# Default: false (off)
```

### 2단계: 짧은 브랜치 생성 및 개발

```
# main에서 브랜치 생성
git checkout main
git pull origin main
git checkout -b feat/payment-gateway-init

# Feature Flag로 감싼 초기 코드 작성
```

```
// payment.service.ts
import { isFeatureEnabled } from './featureFlags';

export async function processPayment(order: Order): Promise<PaymentResult> {
  const useNewGateway = await isFeatureEnabled('new-payment-gateway', {
    kind: 'user',
    key: order.userId
  });

  if (useNewGateway) {
    return newPaymentGateway.process(order);  // 아직 미완성
  }
  return legacyPaymentGateway.process(order);  // 기존 로직
}
```

### 3단계: 같은 날 main에 머지

작업이 완료되지 않았지만, Feature Flag로 비활성화되어 있으므로 안전하게 머지합니다.

```
git add .
git commit -m "feat: add new payment gateway behind feature flag (WIP)"
git push origin feat/payment-gateway-init

# PR 생성 → 코드 리뷰 → CI 통과 확인 → 머지
```

### 4단계: 다음 날 계속 개발

```
git checkout main
git pull origin main
git checkout -b feat/payment-gateway-validation

# 결제 검증 로직 추가
# ... 작업 ...

git commit -m "feat: add payment validation for new gateway"
git push origin feat/payment-gateway-validation
# PR → 리뷰 → 머지
```

이 과정을 반복하며, 매일 작은 변경을 main에 통합합니다.

### 5단계: 기능 완성 후 점진적 롤아웃

기능이 완성되면 Feature Flag 플랫폼에서 점진적으로 활성화합니다.

```
1일차: 내부 QA 팀에게만 활성화 (1%)
3일차: 베타 사용자에게 활성화 (5%)
7일차: 전체 사용자의 25%에게 활성화
14일차: 문제 없으면 100% 활성화
21일차: Feature Flag 코드 제거
```

### 6단계: Flag 정리 (기술 부채 방지)

기능이 안정화되면 Flag를 제거합니다.

```
// Before: Flag 있음
if (useNewGateway) {
  return newPaymentGateway.process(order);
}
return legacyPaymentGateway.process(order);

// After: Flag 제거, 새 로직만 유지
return newPaymentGateway.process(order);
```

## 모범사례/패턴 비교

| 상황 | 권장 접근법 | 주의점 |
| --- | --- | --- |
| 소규모 팀 (2~5명) | main에 직접 커밋 | 강력한 자동화 테스트 필수 |
| 중규모 팀 (5~20명) | PR 기반 + 당일 머지 | 브랜치 수명 24시간 이내 유지 |
| 대규모 팀 (20명+) | PR + Merge Queue | Graphite, Mergify 같은 도구 활용 |
| 미완성 기능 배포 | Release Toggle 사용 | Flag 수명 2~4주 이내 |
| A/B 테스트 | Experiment Toggle 사용 | 통계적 유의성 확보 후 결론 |
| 긴급 롤백 필요 | Ops Toggle + 자동 롤백 | 모니터링 알림 체계 구축 |

## 마치며

- TBD는 짧은 브랜치, 작은 배치, 빈번한 통합을 통해 머지 충돌과 통합 위험을 최소화하는 전략입니다.
- Feature Flag는 배포와 릴리스를 분리하여 미완성 코드를 안전하게 main에 머지할 수 있게 합니다. 단, Flag는 기술 부채가 될 수 있으므로 수명을 짧게 유지해야 합니다.
- CI/CD 파이프라인은 TBD의 심장입니다. 10분 이내의 빠른 피드백, Feature Flag 조합 테스트, 점진적 배포 전략이 핵심입니다.
- 실전 팁: 이번 주에 가장 오래 살아있는 브랜치를 찾아 "왜 이렇게 오래 됐는지" 분석해보세요. 그 이유를 해결하면 TBD로 가는 첫 걸음이 됩니다.

## 참고자료

- Trunk-Based Development 공식 사이트 (<https://trunkbaseddevelopment.com/>)
- Feature Flags - Trunk Based Development (<https://trunkbaseddevelopment.com/feature-flags/>)
- Continuous Integration - Trunk Based Development (<https://trunkbaseddevelopment.com/continuous-integration/>)
- Feature Toggles (aka Feature Flags) - Martin Fowler (<https://martinfowler.com/articles/feature-toggles.html>)
- Trunk-Based Development - Atlassian (<https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development>)
- DORA Research (<https://dora.dev/research/>)
- Implement trunk-based development using feature flags - Unleash (<https://docs.getunleash.io/feature-flag-tutorials/use-cases/trunk-based-development>)
- Build CI/CD Pipeline with GitHub Actions - GitHub Blog (<https://github.blog/enterprise-software/ci-cd/build-ci-cd-pipeline-github-actions-four-steps/>)
- LaunchDarkly JavaScript SDK Documentation (<https://docs.launchdarkly.com/sdk/client-side/javascript>)
