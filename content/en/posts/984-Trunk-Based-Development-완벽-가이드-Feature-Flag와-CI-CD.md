---
title: "Trunk-Based Development Complete Guide, Feature Flags and CI/CD"
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

If you're a developer who fears code merges, pay attention. You're trying to merge a feature branch you worked on for two weeks, but there are 200 conflicts, and the reviewer sighs seeing 500 lines of changes. If this nightmare repeats, it's time to reconsider your branching strategy itself.

**Trunk-Based Development (TBD) is a philosophy of "small, frequent, safe" merging, and**

**Feature Flags and CI/CD pipelines make it possible.**

Through this article, you can learn how TBD works and how to implement it.

**In short, TBD is characterized by short branch lifespans (under a day), automated CI/CD pipelines,**

**and deployment-release separation through Feature Flags. With these three in place, you can escape "merge hell."**

## Background

One of the biggest bottlenecks in software development is code integration. The longer multiple developers work on separate branches, the bigger the problems when merging. This is called "Integration Hell" or "Merge Hell."

According to research by Google's DORA (DevOps Research and Assessment) team conducted for 10+ years, **high-performing teams (Elite Performers) share the trait of high deployment frequency and short change lead times.**

They deploy to production multiple times a day and aim to get from code commit to deployment within 1 hour. TBD is exactly a systematization of how high-performing teams work.

> Trunk-Based Development is a version control strategy where all developers frequently integrate small changes into one main branch (trunk). Even when creating feature branches, the rule is to merge within hours to a maximum of 1-2 days.

The core idea is simple: **the longer a branch lives, the greater the risk.** Code separated for two weeks grows further from main,

and eventually becomes a "big bang integration" when merged. In contrast, merging small changes daily means conflicts are narrow in scope and easier to resolve.

## Core Principles of TBD

To successfully adopt TBD, you must understand three core principles.

First, **short branch lifespan**. Feature branches must merge to main within hours to at most a day. Even if work isn't complete, you merge. Incomplete features are hidden with Feature Flags.

Second, **small batch sizes**. Instead of changing hundreds of lines at once, commit frequently in 10-50 line units. Ideally sized for reviewers to check in 10 minutes. Small changes are easier to debug, and rollback is simple if problems occur.

Third, **separation of deployment and release**. Deploying code to production and exposing features to users are separate. Using Feature Flags, you can deploy incomplete code while keeping it invisible to users. This is the key mechanism making TBD safe.

## Feature Flags: TBD's Safety Net

Feature Flags (or Feature Toggles) are techniques for controlling feature activation at the code level. Simply put, it's turning specific features on or off with if-else statements. The key is controlling features at runtime without redeployment.

### Types of Feature Flags

According to Martin Fowler's classification, Feature Flags come in four types.

**Release Toggle** hides incomplete features. The most important type in TBD. Merge code under development to main while keeping it invisible to users. When complete, toggle on; when stable, remove the toggle code itself.

**Experiment Toggle** is used for A/B testing. Expose new features to some users and measure reaction. Used for experiments like "would changing the button color to blue increase click-through rate?"

**Ops Toggle** is used for operational purposes. Temporarily disable specific features when system load is high, or activate alternate logic when external services fail. Combined with Circuit Breaker pattern to enhance system stability.

**Permission Toggle** controls features based on user permissions. Provide features only to premium users or expose features first to beta tester groups.

### Feature Flag Implementation Methods

Feature Flags can be implemented directly or using specialized platforms like LaunchDarkly, Unleash, or Flagsmith. Below are examples of both approaches.

**Direct Implementation (TypeScript example)**

```typescript
// featureFlags.ts
interface FeatureFlags {
  newCheckoutFlow: boolean;
  darkMode: boolean;
  experimentalSearch: boolean;
}

// Load from environment variables or config file
const flags: FeatureFlags = {
  newCheckoutFlow: process.env.FF_NEW_CHECKOUT === 'true',
  darkMode: process.env.FF_DARK_MODE === 'true',
  experimentalSearch: false, // Default off
};

export function isFeatureEnabled(flagName: keyof FeatureFlags): boolean {
  return flags[flagName] ?? false;
}

// Usage example
if (isFeatureEnabled('newCheckoutFlow')) {
  renderNewCheckout();
} else {
  renderLegacyCheckout();
}
```

Direct implementation's advantage is no external dependencies. However, runtime changes are difficult and user-specific targeting is complex.

**Using LaunchDarkly SDK (Node.js example)**

```typescript
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

// Usage example - Express middleware
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

The advantage of specialized platforms is you can change flags without redeployment and enable gradual rollout by user segment. First expose to 1% of users, then expand to 10%, 50%, 100% if no issues.

### Feature Flag Best Practices

Flag management can become technical debt. Follow these principles:

**Keep lifespan short.** Release Toggles should be removed within 2-4 weeks after feature stabilization. Old flags increase code complexity and exponentially expand test combinations.

**Establish naming conventions.** Use names that clarify behavior like `show-header`, `enable-new-search`, `use-v2-api`. camelCase is recommended; consistency within the team is important.

**Avoid flag dependencies.** A structure where Flag B only matters if Flag A is on explodes complexity. Each flag should operate independently.

**Test all flag combinations.** The CI pipeline should run tests for key flag combinations. With 3 flags, 8 combinations exist. Select important combinations for your test matrix.

## CI/CD Pipeline: TBD's Heart

TBD requires a strong CI/CD pipeline to function. Developers merge to main multiple times daily; you can't manually test and deploy each time. **Automated tests ensure quality, automated deployment ensures speed.**

### TBD CI/CD Pipeline Structure

A typical TBD CI/CD pipeline consists of these stages:

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
      └──── Hide features with Feature Flag
```

### Implementing CI/CD with GitHub Actions

Below is a GitHub Actions workflow optimized for TBD.

```yaml
# .github/workflows/ci-cd.yml
name: TBD CI/CD Pipeline

on:
  push:
    branches: [main]  # Run only on main branch push
  pull_request:
    branches: [main]  # PR also validated by same pipeline

env:
  NODE_VERSION: '20'

jobs:
  # Stage 1: Code quality checks
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

  # Stage 2: Tests
  test:
    runs-on: ubuntu-latest
    needs: lint-and-format
    strategy:
      matrix:
        # Test by Feature Flag combinations
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

  # Stage 3: Security scan
  security:
    runs-on: ubuntu-latest
    needs: lint-and-format
    steps:
      - uses: actions/checkout@v4

      - name: Run Snyk security scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  # Stage 4: Build and image creation
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

  # Stage 5: Deployment (Canary approach)
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

### Pipeline Design Key Points

**Fast feedback** matters most. The entire pipeline should complete within 10 minutes. Lint and unit tests target 2 minutes, integration tests 5 minutes. Slow tests make developers lose context waiting for feedback.

**Use parallel execution.** In the example above, test and security jobs run simultaneously. Process independent tasks in parallel to reduce overall time.

**Include Feature Flag combination testing.** Use matrix strategy to test key flag combinations. If testing all combinations is difficult, select the most risky ones.

**Implement gradual deployment.** Use strategies like canary deployment, blue-green deployment, or rolling updates to distribute risk. First expose new version to 10% traffic, then expand gradually if no issues.

**Prepare auto-rollback.** Include logic for automatic rollback to previous version if smoke tests fail. Fast rollback minimizes downtime.

## Practical Exercise: Complete TBD Workflow

Let's follow TBD workflow through an actual development scenario.

### Step 1: Start Work

Assume developing a new payment feature. First, create a Feature Flag.

```
# Create flag using LaunchDarkly CLI or dashboard
# Flag Key: new-payment-gateway
# Variations: true (new payment), false (legacy payment)
# Default: false (off)
```

### Step 2: Create Short Branch and Develop

```bash
# Create branch from main
git checkout main
git pull origin main
git checkout -b feat/payment-gateway-init

# Write initial code wrapped in Feature Flag
```

```typescript
// payment.service.ts
import { isFeatureEnabled } from './featureFlags';

export async function processPayment(order: Order): Promise<PaymentResult> {
  const useNewGateway = await isFeatureEnabled('new-payment-gateway', {
    kind: 'user',
    key: order.userId
  });

  if (useNewGateway) {
    return newPaymentGateway.process(order);  // Still incomplete
  }
  return legacyPaymentGateway.process(order);  // Legacy logic
}
```

### Step 3: Merge to Main Same Day

Work incomplete but Feature Flag deactivates it, so safe to merge.

```bash
git add .
git commit -m "feat: add new payment gateway behind feature flag (WIP)"
git push origin feat/payment-gateway-init

# Create PR → Code review → Verify CI passes → Merge
```

### Step 4: Continue Development Next Day

```bash
git checkout main
git pull origin main
git checkout -b feat/payment-gateway-validation

# Add payment validation logic
# ... work ...

git commit -m "feat: add payment validation for new gateway"
git push origin feat/payment-gateway-validation
# PR → review → merge
```

Repeat this process, integrating small changes to main daily.

### Step 5: Gradual Rollout After Feature Completion

Gradually activate the Feature Flag after completion.

```
Day 1: Enable for internal QA team only (1%)
Day 3: Enable for beta users (5%)
Day 7: Enable for 25% of all users
Day 14: Enable for 100% if no issues
Day 21: Remove Feature Flag code
```

### Step 6: Clean Up Flag (Prevent Technical Debt)

Remove the flag once feature stabilizes.

```typescript
// Before: Flag exists
if (useNewGateway) {
  return newPaymentGateway.process(order);
}
return legacyPaymentGateway.process(order);

// After: Remove flag, keep only new logic
return newPaymentGateway.process(order);
```

## Best Practices/Pattern Comparison

| Situation | Recommended Approach | Cautions |
| --- | --- | --- |
| Small team (2-5) | Commit directly to main | Strong automated tests required |
| Medium team (5-20) | PR-based + same-day merge | Keep branch lifespan under 24 hours |
| Large team (20+) | PR + Merge Queue | Use tools like Graphite, Mergify |
| Incomplete feature deployment | Use Release Toggle | Keep flag lifespan under 2-4 weeks |
| A/B testing | Use Experiment Toggle | Ensure statistical significance before conclusion |
| Emergency rollback needed | Ops Toggle + auto-rollback | Build monitoring alert system |

## Conclusion

- TBD minimizes merge conflicts and integration risk through short branches, small batches, and frequent integration.
- Feature Flags separate deployment and release, enabling safe merging of incomplete code to main. However, flags can become technical debt, so keep their lifespan short.
- CI/CD pipeline is TBD's heart. Fast feedback within 10 minutes, Feature Flag combination testing, and gradual deployment strategy are key.
- Practical tip: Find the longest-lived branch this week and analyze "why has it lived so long?" Solving that reason is your first step toward TBD.

## References

- Trunk-Based Development Official Site (<https://trunkbaseddevelopment.com/>)
- Feature Flags - Trunk Based Development (<https://trunkbaseddevelopment.com/feature-flags/>)
- Continuous Integration - Trunk Based Development (<https://trunkbaseddevelopment.com/continuous-integration/>)
- Feature Toggles (aka Feature Flags) - Martin Fowler (<https://martinfowler.com/articles/feature-toggles.html>)
- Trunk-Based Development - Atlassian (<https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development>)
- DORA Research (<https://dora.dev/research/>)
- Implement trunk-based development using feature flags - Unleash (<https://docs.getunleash.io/feature-flag-tutorials/use-cases/trunk-based-development>)
- Build CI/CD Pipeline with GitHub Actions - GitHub Blog (<https://github.blog/enterprise-software/ci-cd/build-ci-cd-pipeline-github-actions-four-steps/>)
- LaunchDarkly JavaScript SDK Documentation (<https://docs.launchdarkly.com/sdk/client-side/javascript>)
