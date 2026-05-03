---
title: "쿠버네티스(Kubernetes) Helm - 복잡한 애플리케이션 배포의 구세주! ?"
date: 2025-04-12T10:35:57+09:00
slug: "546-쿠버네티스-Kubernetes-Helm-복잡한-애플리케이션-배포의-구세주"
original_url: "https://memoryhub.tistory.com/546"
tistory_id: 546
draft: false
categories: ["데브 옵스"]
tags: ["Kubernetes"]
---

쿠버네티스, 정말 강력하고 멋진 도구죠! ? 그런데 여러 개의 리소스를 배포하고 관리하려면 YAML 파일들이 너무 많아져서 머리가 아파오지 않나요? ? 마치 수많은 레고 조각을 설명서 없이 조립하려는 느낌이랄까요? 이럴 때 필요한 것이 바로 **Helm(헬름)**입니다! Helm이 여러분의 쿠버네티스 여정을 훨씬 쉽고 즐겁게 만들어 줄 거예요. 자, Helm의 세계로 함께 떠나볼까요?

## 등장 배경: YAML 지옥에서 벗어나자! ?

쿠버네티스를 사용하다 보면 Deployment, Service, ConfigMap, Secret 등 수많은 종류의 리소스들을 정의해야 합니다. 애플리케이션 하나를 배포하기 위해 여러 개의 YAML 파일을 작성하고, 환경별로 설정을 다르게 관리하고, 버전 업데이트라도 하려면… 생각만 해도 복잡하죠? ?

초기에는 `kubectl apply -f <디렉토리명>` 같은 명령어로 여러 YAML 파일을 한 번에 적용하곤 했지만, 다음과 같은 문제들이 여전히 남아있었습니다.

- **버전 관리의 어려움:** 어떤 버전의 애플리케이션이 배포되었는지 추적하기 어렵고, 이전 버전으로 되돌리기가 까다로웠어요.
- **애플리케이션 단위 관리 부재:** 여러 리소스가 모여 하나의 애플리케이션을 구성하는데, 이를 묶어서 관리할 표준적인 방법이 없었습니다.
- **설정의 중복 및 재사용 어려움:** 비슷한 애플리케이션을 배포할 때마다 YAML 파일을 복사-붙여넣기 하고 수정하는 비효율적인 작업이 반복되었죠.
- **의존성 관리:** 내 애플리케이션이 특정 데이터베이스나 메시지 큐에 의존할 때, 이를 함께 설치하고 관리하기가 번거로웠습니다.

이런 문제들을 해결하기 위해 등장한 것이 바로 **Helm**, 쿠버네티스 패키지 매니저입니다! 마치 리눅스에서 `apt`나 `yum`, Node.js에서 `npm`이나 `yarn`처럼 쿠버네티스 애플리케이션을 쉽게 설치하고 관리할 수 있게 도와줍니다.

Helm이 해결하는 문제 (특징/용도):

1. **복잡한 애플리케이션 관리 ⚙️:** 여러 쿠버네티스 리소스를 '차트(Chart)'라는 하나의 패키지로 묶어 관리합니다. 덕분에 애플리케이션 전체를 하나의 단위로 설치, 업그레이드, 삭제할 수 있습니다.
2. **쉬운 재사용과 공유 ?:** 잘 만들어진 차트는 다른 사람들과 쉽게 공유하고 재사용할 수 있습니다. Helm Hub와 같은 공개/비공개 저장소를 통해 다양한 오픈 소스 애플리케이션 차트를 찾아 바로 사용할 수도 있습니다.
3. **간편한 버전 관리 및 롤백 ⏮️:** 배포된 애플리케이션(릴리스, Release)의 버전을 관리하고, 문제가 발생했을 때 이전 버전으로 쉽게 되돌릴 수 있습니다.
4. **템플릿 기반 설정 관리 ?:** Go 템플릿 언어를 사용하여 쿠버네티스 매니페스트 파일을 동적으로 생성합니다. `values.yaml` 파일에 환경별 설정 값을 정의하고 템플릿에 주입하여 유연하게 설정을 관리할 수 있습니다.
5. **의존성 관리 ?:** 차트 간의 의존성을 정의하여, 특정 애플리케이션 설치 시 필요한 다른 애플리케이션(예: 데이터베이스)을 함께 설치할 수 있습니다.

## 핵심 원리: 차트, 릴리스, 리포지토리 ?️

Helm은 크게 세 가지 핵심 개념으로 동작합니다.

### 1. 차트 (Chart) ?

차트는 쿠버네티스 애플리케이션을 배포하는 데 필요한 모든 리소스 정의, 설정값, 메타데이터 등을 모아놓은 **패키지**입니다. 특정 디렉토리 구조를 가지며, 주요 파일들은 다음과 같습니다.

- `Chart.yaml`: 차트의 이름, 버전, 설명 등 메타데이터를 담고 있는 파일입니다.
- `values.yaml`: 차트의 기본 설정값(변수)을 정의하는 파일입니다. 여기서 정의된 값들은 템플릿 파일 내에서 사용됩니다. 사용자는 이 파일을 수정하거나 `--set` 옵션을 통해 값을 오버라이드하여 차트를 커스터마이징할 수 있습니다.
- `templates/`: 쿠버네티스 리소스 매니페스트(YAML) 파일들의 **템플릿**이 들어있는 디렉토리입니다. Go 템플릿 문법을 사용하여 `values.yaml`의 값들을 참조해 동적으로 최종 YAML 파일을 생성합니다. 예를 들어, 레플리카 수나 이미지 태그 등을 변수로 처리할 수 있습니다.
- `charts/`: 이 차트가 의존하는 다른 차트들(서브차트)이 위치하는 디렉토리입니다. (의존성 관리)

**예시: `values.yaml`과 템플릿 (`templates/deployment.yaml`)**

```
# values.yaml
replicaCount: 1
image:
  repository: nginx
  tag: stable
  pullPolicy: IfNotPresent
service:
  type: ClusterIP
  port: 80
```

```
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}-nginx
spec:
  replicas: {{ .Values.replicaCount }}  # values.yaml의 replicaCount 값을 사용
  selector:
    matchLabels:
      app: {{ .Release.Name }}-nginx
  template:
    metadata:
      labels:
        app: {{ .Release.Name }}-nginx
    spec:
      containers:
        - name: nginx
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}" # values.yaml의 이미지 정보 사용
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - containerPort: {{ .Values.service.port }} # values.yaml의 포트 정보 사용
```

### 2. 릴리스 (Release) ?

릴리스는 **클러스터에 배포된 차트의 실행 인스턴스**입니다. 동일한 차트를 사용하더라도 다른 설정값(`values.yaml` 오버라이드)이나 다른 이름으로 여러 번 배포할 수 있으며, 각각은 고유한 릴리스가 됩니다. Helm은 이 릴리스 단위로 애플리케이션의 설치, 업그레이드, 롤백, 삭제를 관리합니다.

**예시: Nginx 차트를 'my-nginx'라는 이름으로 배포**

```
# helm install <릴리스_이름> <차트_경로_또는_이름>
helm install my-nginx ./nginx-chart  # 로컬 차트 설치

# 또는 저장소의 차트 설치 (예: bitnami 저장소의 nginx)
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-nginx bitnami/nginx --set replicaCount=3 # replicaCount를 3으로 오버라이드하여 설치
```

### 3. 리포지토리 (Repository) ?

리포지토리는 **차트를 저장하고 공유하는 공간**입니다. 로컬 디렉토리일 수도 있고, HTTP 서버일 수도 있습니다. Helm 클라이언트는 리포지토리를 추가하고, 해당 리포지토리에서 차트를 검색하고 다운로드할 수 있습니다. `bitnami`, `stable`(deprecated) 등 유명한 공개 리포지토리들이 많으며, 회사 내부용 비공개 리포지토리를 구축하여 사용할 수도 있습니다.

**예시: 리포지토리 추가 및 차트 검색**

```
# 리포지토리 추가
helm repo add bitnami https://charts.bitnami.com/bitnami

# 로컬 리포지토리 캐시 업데이트
helm repo update

# 'mysql' 키워드가 포함된 차트 검색
helm search repo mysql
```

## 사례 소개: WordPress 블로그 쉽게 배포하기 뚝딱! ?

Bitnami에서 제공하는 WordPress Helm 차트를 사용하면 데이터베이스(MariaDB) 의존성까지 포함된 WordPress 블로그를 단 몇 개의 명령어로 쿠버네티스 클러스터에 배포할 수 있습니다.

```
# 1. Bitnami 리포지토리 추가 (이미 추가했다면 생략)
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# 2. WordPress 차트 설치 (기본 설정 사용)
# 'my-blog'라는 이름으로 릴리스 생성
helm install my-blog bitnami/wordpress
```

잠시 기다리면 WordPress와 MariaDB에 필요한 모든 쿠버네티스 리소스(Deployment, Service, PersistentVolumeClaim 등)가 생성되고 연동됩니다. `kubectl get svc` 명령어로 WordPress 서비스의 외부 IP를 확인하고 접속하면 바로 WordPress 설정 화면을 만날 수 있습니다! ✨

**Helm 주요 명령어 요약**

| 명령어 | 설명 | 예시 |
| --- | --- | --- |
| `helm create <이름>` | 새로운 차트의 기본 구조를 생성합니다. | `helm create my-chart` |
| `helm install <릴리스> <차트>` | 차트를 클러스터에 배포하여 릴리스를 생성합니다. | `helm install my-release ./my-chart` |
| `helm upgrade <릴리스> <차트>` | 기존 릴리스를 새로운 버전의 차트나 설정으로 업그레이드합니다. | `helm upgrade my-release ./my-chart --set image.tag=1.2.0` |
| `helm rollback <릴리스> [버전]` | 릴리스를 이전 버전으로 되돌립니다. | `helm rollback my-release 1` |
| `helm uninstall <릴리스>` | 릴리스와 관련된 모든 리소스를 클러스터에서 삭제합니다. | `helm uninstall my-release` |
| `helm list` / `helm ls` | 현재 클러스터에 배포된 릴리스 목록을 보여줍니다. | `helm list` |
| `helm status <릴리스>` | 특정 릴리스의 상태 및 리소스 정보를 확인합니다. | `helm status my-release` |
| `helm repo add <이름> <URL>` | 새로운 차트 리포지토리를 추가합니다. | `helm repo add bitnami https://charts.bitnami.com/bitnami` |
| `helm repo update` | 로컬 리포지토리 캐시를 최신 상태로 업데이트합니다. | `helm repo update` |
| `helm search repo <키워드>` | 추가된 리포지토리에서 차트를 검색합니다. | `helm search repo nginx` |
| `helm template <릴리스> <차트>` | 차트를 실제로 배포하지 않고, 렌더링된 쿠버네티스 YAML을 출력합니다. | `helm template my-release ./my-chart` |
| `helm lint <차트경로>` | 차트의 문법이나 구조에 오류가 없는지 검사합니다. | `helm lint ./my-chart` |

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **Tiller 제거 (Helm 3+)**: Helm 2 버전에는 Tiller라는 서버 측 컴포넌트가 필요했고, 이는 보안 및 권한 관리 측면에서 문제가 있었습니다. Helm 3부터는 Tiller가 완전히 제거되어 클라이언트 측에서 모든 작업을 처리하므로 훨씬 안전하고 간편해졌습니다. **반드시 Helm 3 이상 버전을 사용하세요!**
2. **`values.yaml` 관리**: 프로덕션 환경에서는 `values.yaml` 파일에 민감한 정보(비밀번호, API 키 등)를 직접 넣지 마세요. 쿠버네티스 Secret을 활용하거나, 외부 Vault 연동, 또는 GitOps 도구(Argo CD, Flux)와 함께 사용하여 안전하게 관리하는 것이 좋습니다.
3. **차트 의존성**: 차트 의존성은 편리하지만, 너무 복잡해지면 관리하기 어려울 수 있습니다. 의존성 버전 충돌 등에 주의하고, 꼭 필요한 경우에만 사용하는 것이 좋습니다.

? **꿀팁**

- **`helm template` 활용**: `helm install`이나 `helm upgrade`를 실행하기 전에 `helm template` 명령어를 사용하면 실제로 어떤 쿠버네티스 리소스들이 생성/변경될지 미리 YAML 형태로 확인할 수 있습니다. 배포 전 검토에 매우 유용합니다! ?
- **버전 관리 시스템 (Git) 사용**: 차트 파일과 `values.yaml` 파일들은 Git과 같은 버전 관리 시스템으로 철저히 관리하세요. 변경 이력을 추적하고 협업하기 훨씬 수월해집니다.
- **Helmfile 또는 GitOps 도구**: 여러 Helm 차트를 조합하여 복잡한 환경을 구성해야 한다면, Helmfile, Argo CD, Flux 같은 도구를 검토해보세요. 선언적으로 Helm 릴리스를 관리하고 GitOps 워크플로우를 구축하는 데 도움을 줍니다.

## 마치며

지금까지 쿠버네티스의 패키지 매니저, Helm에 대해 알아보았습니다. Helm을 사용하면 복잡한 쿠버네티스 애플리케이션 배포와 관리가 훨씬 간편해지는 것을 느끼셨을 거예요. 처음에는 차트 구조나 템플릿 문법이 조금 낯설 수 있지만, 몇 번 사용해보면 금방 익숙해지실 겁니다! ?

Helm은 쿠버네티스 생태계에서 사실상 표준처럼 사용되고 있으니, 꼭 한번 직접 사용해보시길 바랍니다. 여러분의 쿠버네티스 운영이 한결 편안해질 거예요! 궁금한 점이 있다면 언제든지 댓글로 남겨주세요! ?‍♀️

## 참고 자료 ?

- **Helm 공식 문서:** <https://helm.sh/docs/> (영문이지만 가장 정확하고 방대한 정보를 얻을 수 있습니다.)
- **Helm GitHub 리포지토리:** <https://github.com/helm/helm>
- **Artifact Hub (Helm 차트 검색):** <https://artifacthub.io/> (다양한 공개 Helm 차트를 찾아볼 수 있습니다.)

---

#Helm #Kubernetes #쿠버네티스 #헬름 #패키지매니저 #DevOps #클라우드네이티브
