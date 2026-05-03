---
title: "⚙️ kubectl 명령어, 실무에서 이것만 알면 90% 해결됩니다"
date: 2025-10-28T22:07:29+09:00
slug: "886-kubectl-명령어-실무에서-이것만-알면-90-해결됩니다"
original_url: "https://memoryhub.tistory.com/886"
tistory_id: 886
draft: false
categories: ["데브 옵스"]
tags: ["Kubernetes"]
---

```
    ⎈ Kubernetes CLI
   _______________
  |  $ kubectl   |
  |   get pods   |
  |______________|
        ||
    [컨테이너 클러스터]
```

쿠버네티스 클러스터를 처음 마주했을 때 가장 막막했던 순간은 무엇이었나요? 수백 개의 명령어와 옵션 앞에서 어디서부터 시작해야 할지 몰라 헤맸던 경험, 저도 있습니다. 분명 공식 문서엔 다 나와 있지만, 정작 실무에서 자주 쓰는 건 따로 있더라고요. 이 글에서는 현업에서 반복적으로 사용하는 핵심 명령어와 옵션을 카테고리별로 정리해드립니다.

**kubectl 기본 조회부터 디버깅까지, 실무에서 매일 쓰는 핵심 명령어와 효율적인 사용 패턴을 단계별로 정리합니다.**

## 배경

### kubectl이란?

kubectl은 쿠버네티스 클러스터를 제어하기 위한 CLI 도구입니다. 클러스터의 상태를 확인하고 리소스를 생성, 수정, 삭제하는 모든 작업이 이 명령줄 도구를 통해 이루어집니다.

### 왜 kubectl을 익혀야 하나?

| 이유 | 설명 |
| --- | --- |
| 클러스터 제어의 핵심 | GUI 대시보드도 있지만 모든 작업은 결국 kubectl로 수행됩니다 |
| 자동화 필수 | CI/CD 파이프라인에서 쿠버네티스 배포를 자동화하려면 kubectl 명령어 숙지가 필수입니다 |
| 트러블슈팅 | 파드가 시작되지 않거나 서비스가 응답하지 않을 때 로그 확인과 상태 점검은 kubectl로 진행됩니다 |

### 주요 용어 정의

- **파드(Pod)**: 쿠버네티스에서 배포 가능한 가장 작은 컴퓨팅 단위로, 하나 이상의 컨테이너를 포함합니다
- **네임스페이스(Namespace)**: 클러스터 내 리소스를 논리적으로 구분하는 가상 공간입니다
- **디플로이먼트(Deployment)**: 파드와 레플리카셋을 관리하는 상위 추상화 객체입니다
- **서비스(Service)**: 파드에 대한 네트워크 접근을 제공하는 추상화 계층입니다

## 핵심

> kubectl [COMMAND] [TYPE] [NAME] [FLAGS] 형태로 명령어를 구성하며, 리소스 조회·생성·수정·삭제와 디버깅 작업을 수행합니다

kubectl 명령어는 크게 다섯 가지 카테고리로 나뉩니다.

**1. 리소스 조회 명령어**

- `get`: 리소스 목록을 간단히 확인
- `describe`: 리소스의 상세 정보 및 이벤트 확인
- `explain`: 특정 리소스 타입의 스펙 설명 확인

**2. 리소스 생성 및 적용**

- `apply`: YAML 파일로 리소스 생성 또는 업데이트
- `create`: 새로운 리소스 생성
- `delete`: 리소스 삭제

**3. 디버깅 명령어**

- `logs`: 파드의 로그 확인
- `exec`: 컨테이너 내부에서 명령어 실행
- `port-forward`: 로컬에서 클러스터 서비스에 접근

**4. 클러스터 정보**

- `cluster-info`: 클러스터 기본 정보 확인
- `top`: 노드와 파드의 리소스 사용량 확인

**5. 고급 작업**

- `rollout`: 디플로이먼트 롤아웃 관리
- `scale`: 레플리카 수 조정
- `edit`: 리소스를 에디터로 직접 수정

## 실습

### ① 기본 조회 명령어

가장 먼저 익혀야 할 명령어는 리소스 조회입니다.

```
# 모든 파드 조회 (현재 네임스페이스)
kubectl get pods

# 모든 네임스페이스의 파드 조회
kubectl get pods --all-namespaces
# 또는 줄여서
kubectl get pods -A

# 더 자세한 정보로 조회 (노드, IP 포함)
kubectl get pods -o wide

# YAML 형식으로 조회
kubectl get pod my-pod -o yaml

# 특정 레이블을 가진 파드만 조회
kubectl get pods -l app=nginx

# 여러 리소스 타입 동시 조회
kubectl get pods,services,deployments
```

**리소스 타입 줄임말**

- `po` → pods
- `svc` → services
- `deploy` → deployments
- `rs` → replicasets
- `ns` → namespaces

### ② 상세 정보 확인

```
# 파드의 상세 정보 확인 (이벤트, 상태 포함)
kubectl describe pod my-pod

# 노드 정보 확인
kubectl describe node worker-node-1

# 특정 네임스페이스의 서비스 상세 정보
kubectl describe svc my-service -n production
```

### ③ 리소스 생성 및 적용

```
# YAML 파일로 리소스 생성
kubectl apply -f deployment.yaml

# URL로 직접 적용 가능
kubectl apply -f https://example.com/manifest.yaml

# 여러 파일 한번에 적용
kubectl apply -f ./manifests/

# Dry-run으로 실제 생성 없이 검증
kubectl apply -f deployment.yaml --dry-run=client

# 명령형으로 디플로이먼트 생성
kubectl create deployment nginx --image=nginx:1.21

# ConfigMap 생성
kubectl create configmap app-config --from-file=config.properties
```

### ④ 디버깅 명령어

문제 발생 시 가장 많이 사용하는 명령어입니다.

```
# 파드 로그 확인
kubectl logs my-pod

# 실시간 로그 확인 (-f는 follow)
kubectl logs -f my-pod

# 특정 컨테이너의 로그 확인 (멀티 컨테이너 파드)
kubectl logs my-pod -c nginx-container

# 이전에 종료된 컨테이너 로그 확인
kubectl logs my-pod --previous

# 파드 내부 접속 (bash shell)
kubectl exec -it my-pod -- bash

# 파드 내부에서 단일 명령어 실행
kubectl exec my-pod -- ls /app

# 로컬 포트를 파드로 포워딩
kubectl port-forward pod/my-pod 8080:80

# 서비스로 포트 포워딩
kubectl port-forward svc/my-service 8080:80
```

### ⑤ 리소스 수정 및 삭제

```
# 리소스 삭제
kubectl delete pod my-pod

# YAML 파일로 생성한 리소스 삭제
kubectl delete -f deployment.yaml

# 레이블로 여러 리소스 삭제
kubectl delete pods -l app=old-version

# 네임스페이스 내 모든 파드 삭제
kubectl delete pods --all

# 리소스 즉시 삭제 (기본 30초 대기 없이)
kubectl delete pod my-pod --grace-period=0 --force

# 리소스 직접 편집 (vim 에디터 실행)
kubectl edit deployment my-deployment
```

### ⑥ 고급 활용 명령어

```
# 디플로이먼트 스케일 조정
kubectl scale deployment my-deployment --replicas=5

# 이미지 업데이트 (롤링 업데이트)
kubectl set image deployment/my-deployment nginx=nginx:1.22

# 롤아웃 상태 확인
kubectl rollout status deployment/my-deployment

# 롤아웃 히스토리 확인
kubectl rollout history deployment/my-deployment

# 이전 버전으로 롤백
kubectl rollout undo deployment/my-deployment

# 특정 리비전으로 롤백
kubectl rollout undo deployment/my-deployment --to-revision=2

# 리소스 사용량 확인 (metrics-server 필요)
kubectl top nodes
kubectl top pods

# 이벤트 확인 (타임스탬프 순)
kubectl get events --sort-by=.metadata.creationTimestamp

# 컨텍스트 확인 및 변경
kubectl config get-contexts
kubectl config use-context production-cluster
```

### ⑦ 실무 팁 명령어

```
# alias 설정으로 타이핑 절약
alias k='kubectl'
alias kg='kubectl get'
alias kd='kubectl describe'

# JSON 경로로 특정 필드만 추출
kubectl get pods -o jsonpath='{.items[*].metadata.name}'

# 여러 파드에 동시 명령 실행
for pod in $(kubectl get po -o jsonpath='{.items[*].metadata.name}'); do
  echo $pod && kubectl exec -it $pod -- env
done

# 컨피그맵 내용 확인
kubectl get configmap my-config -o yaml

# 시크릿 디코드
kubectl get secret my-secret -o jsonpath='{.data.password}' | base64 --decode
```

## 모범사례/패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **선언적 방식 (`apply`)** | YAML 파일로 관리하여 버전 관리와 재현성 확보, GitOps 워크플로우에 적합 | 초기 학습 곡선이 있고 YAML 문법 숙지 필요 |
| **명령형 방식 (`create`, `delete`)** | 빠른 테스트와 실험에 유용, 즉각적인 결과 확인 가능 | 재사용성 낮고 히스토리 추적 어려움, 프로덕션 환경에 부적합 |
| **하이브리드 방식** | 개발 환경에서는 명령형으로 빠르게 테스트, 운영 환경에서는 선언적 방식 사용 | 일관성 유지를 위한 팀 컨벤션 필요 |

## 마치며

kubectl의 핵심 명령어를 살펴봤습니다. 처음에는 복잡해 보이지만 실제로는 get, describe, logs, exec 정도만 익숙해져도 일상 업무의 대부분을 처리할 수 있습니다. 나머지 명령어들은 필요할 때마다 찾아서 사용하면 됩니다.

실전에서는 alias 설정부터 시작하세요. `alias k=kubectl`만으로도 타이핑이 절반으로 줄어듭니다. 그리고 YAML 파일을 Git으로 관리하는 습관을 들이면 팀원들과 협업할 때 훨씬 효율적입니다.

**미팅에서 써먹을 한마디**: "실무에서는 apply로 배포하고, describe로 상태 확인하며, logs로 디버깅합니다. 이 세 가지만 마스터해도 절반은 갑니다."

## 참고자료

- kubectl 치트 시트 (<https://kubernetes.io/ko/docs/reference/kubectl/cheatsheet/>)
- 쿠버네티스 안내서 - 기본 명령어 (<https://subicura.com/k8s/guide/kubectl.html>)
- Kubernetes 공식 문서 - 명령줄 도구 (<https://kubernetes.io/ko/docs/reference/kubectl/>)
- Kubernetes v1.34 릴리스 노트 (<https://kubernetes.io/ko/blog/2025/08/27/kubernetes-v1-34-release/>)
