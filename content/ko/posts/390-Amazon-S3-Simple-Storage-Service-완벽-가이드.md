---
title: "Amazon S3(Simple Storage Service) 완벽 가이드 ?"
date: 2024-11-17T09:12:57+09:00
slug: "390-Amazon-S3-Simple-Storage-Service-완벽-가이드"
original_url: "https://memoryhub.tistory.com/390"
tistory_id: 390
draft: false
categories: ["Dev AWS"]
tags: ["S3"]
---

오늘은 **Amazon S3(Simple Storage Service)**에 대해 알아보겠습니다! Amazon Web Services(AWS)에서 제공하는 객체 스토리지 서비스인 S3는 확장성과 안정성을 동시에 제공하여, 기업 규모와 상관없이 다양한 용도로 사용되고 있습니다. 지금부터 Amazon S3의 핵심 개념과 동작 방식, 장점, 주의사항, 그리고 실제 사용 예시를 살펴보겠습니다.

---

## **1. Amazon S3란? ?**

Amazon S3(Simple Storage Service)는 인터넷을 통해 데이터를 저장하고 불러올 수 있는 **객체 스토리지(Object Storage) 서비스**입니다. 여기서 '객체'란 파일 그 자체와 해당 파일을 설명하는 메타데이터를 포함하는 단위를 말합니다.

- **? 개념 요약**:

  - S3는 데이터를 ‘버킷(Bucket)’이라는 큰 컨테이너에 저장하고, 각 데이터를 객체(Object)로 취급합니다.
  - 객체는 파일 + 메타데이터로 구성됩니다.
  - URL, API 또는 SDK를 통해 객체를 업로드 및 다운로드할 수 있습니다.
- **? 실생활 예시**:

  - 사진 공유 웹사이트에서 사용자들이 업로드하는 이미지 파일을 저장.
  - 동영상 스트리밍 서비스에서 미디어 파일(영상, 음악)을 보관.
  - 모바일 앱에서 사용자 프로필이나 로그 데이터를 S3에 적재 후 분석.
- **? 어떤 문제를 해결하는지?**

  1. **확장성**: 스토리지 용량이 자동으로 확장되어, 용량 걱정 없이 데이터를 저장할 수 있습니다.
  2. **가용성**: 여러 지역(Region)에 걸쳐 안정적으로 호스팅되어, 높은 내구성과 가용성을 보장합니다.
  3. **관리 편의성**: 서버를 직접 구축하거나 운영할 필요 없이, AWS 콘솔 또는 API를 통해 간편하게 관리할 수 있습니다.

---

## **2. 어떻게 동작하나요? ?**

### 1) 기본 개념

Amazon S3의 핵심 동작은 크게 다음과 같습니다.

- **버킷(Bucket) 생성**: S3에 데이터를 저장하기 위해서는 먼저 버킷(저장 공간)을 만들어야 합니다. 버킷 이름은 전 세계에서 유일(unique)해야 하며, AWS 리전(Region)을 설정할 수 있습니다.
- **객체(Object) 업로드**: 버킷이 준비되면 데이터를 업로드합니다. 객체를 업로드할 때는 권한과 메타데이터를 설정할 수 있으며, 해당 객체에 접근하기 위한 URL도 자동으로 생성됩니다.
- **버전 관리(Versioning)**: 버킷에 버전 관리를 활성화하면, 같은 이름의 파일을 여러 번 업로드해도 각각의 버전으로 저장됩니다. 이로써 의도치 않은 삭제나 변경에 안전하게 대비할 수 있습니다.
- **객체 수명 주기(Lifecycle)**: S3에 저장된 데이터를 특정 시점 이후에 자동으로 Glacier나 다른 스토리지 클래스로 옮길 수 있는 라이프사이클 관리 기능을 제공합니다. 이를 통해 비용을 절감할 수 있습니다.

아래는 AWS CLI를 이용해 버킷을 생성하고 객체를 업로드하는 간단한 예시입니다.

```
# AWS CLI를 사용해 버킷 생성
aws s3 mb s3://my-example-bucket --region ap-northeast-2

# 로컬 파일을 S3 버킷에 업로드
aws s3 cp ./testfile.txt s3://my-example-bucket
```

### 2) 실제 적용 예시 (Java 코드 예시)

AWS SDK for Java를 이용하여 S3에 객체를 업로드하는 간단한 코드입니다.

```
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import java.nio.file.Paths;

public class S3UploadExample {
    public static void main(String[] args) {
        // 1. S3 Client 생성
        S3Client s3 = S3Client.builder()
                .region(Region.AP_NORTHEAST_2)
                .credentialsProvider(ProfileCredentialsProvider.create())
                .build();

        // 2. PutObjectRequest 생성
        PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                .bucket("my-example-bucket")
                .key("uploaded-file.txt")
                .build();

        // 3. S3에 업로드
        s3.putObject(putObjectRequest, Paths.get("local-file.txt"));

        System.out.println("파일 업로드가 완료되었습니다!");
    }
}
```

#### ? 동작 원리

1. **버킷 생성**: 전 세계에서 유일한 이름으로 버킷을 생성합니다. 예: `my-example-bucket`
2. **S3Client 설정**: AWS SDK를 사용하여 S3와 통신하기 위한 자격 증명과 리전을 지정합니다.
3. **객체 업로드/다운로드**: PutObject, GetObject 등의 메서드를 이용해 데이터를 업로드/다운로드합니다.
4. **권한 관리**: AWS IAM 정책 또는 S3 버킷 정책을 통해, 누가 어떤 방식으로 객체에 접근할 수 있는지를 제어합니다.

---

## **3. 주요 장점 ?**

1. **높은 확장성**

   - S3는 자동으로 확장되어, 요구 사항이 갑작스럽게 증가해도 문제없이 수용할 수 있습니다. 이를 통해 트래픽이 급증하는 이벤트나 프로모션 시점에도 안정적으로 서비스를 운영할 수 있습니다.
2. **높은 내구성 & 가용성**

   - S3 표준 스토리지(Standard Storage)의 경우 99.999999999%(일명 11 Nine) 내구성을 보장합니다. 또한, 가용성이 높아 데이터 손실이나 서비스 중단 위험을 크게 줄여줍니다.
3. **보안 기능**

   - AWS IAM(Identity and Access Management)과 연동하여 세분화된 접근 제어가 가능합니다. 버킷 정책, 객체 수준의 ACL(Access Control List)도 지원해 객체 단위의 세부 권한을 설정할 수 있습니다.
   - **서버 사이드 암호화(Server-Side Encryption)**와 **클라이언트 사이드 암호화(Client-Side Encryption)** 기능을 활용하여 추가적인 보안 계층을 쌓을 수 있습니다.
4. **비용 효율성**

   - 사용한 만큼만 지불(Pay-as-you-go)하는 모델이어서, 초기 투자 비용이 거의 없습니다.
   - 스토리지 클래스(예: Standard, Infrequent Access, Glacier 등)를 상황에 맞게 조합하면 저장 비용을 최소화할 수 있습니다.

---

## **4. 주의할 점 ⚠️**

1. **이름 충돌**

   - 버킷 이름은 전 세계에서 유일해야 하므로, 일반적인 이름을 사용하면 충돌 위험이 있습니다. 버킷 이름을 지을 때 회사나 프로젝트 고유 식별자를 포함시키면 좋습니다.
2. **버전 관리 활성화 시 비용 증가**

   - 버전을 켜두면 같은 파일을 여러 번 저장하므로, 그만큼 스토리지 비용이 증가할 수 있습니다. 버전 정리 정책을 잘 설정해야 합니다.
3. **권한 설정 실수로 인한 공개 노출**

   - S3 버킷 및 객체에 퍼블릭 접근 권한을 잘못 열어두면 의도치 않게 데이터를 전 세계에 노출할 수 있습니다. 버킷 정책과 접근 제어 리스트(ACL)를 신중히 설정해야 합니다.
4. **리전 선택**

   - 버킷 생성 시 리전을 올바르게 선택해야, 트래픽 지연(Latency)과 전송 비용을 최소화할 수 있습니다. 사용자가 주로 이용하는 지역과 가까운 리전에 버킷을 생성하는 것이 좋습니다.

---

## **5. 실제 사용 예시 ?**

여기서는 AWS CLI와 간단한 라이프사이클 정책(Lifecycle Policy) 설정 예시를 살펴보겠습니다.

```
# 1. 버킷 생성
aws s3 mb s3://my-lifecycle-bucket --region ap-northeast-2

# 2. 라이프사이클 정책 파일(JSON) 작성 (lifecycle.json)
cat <<EOL > lifecycle.json
{
   "Rules": [
      {
         "ID": "TransitionToIA",
         "Prefix": "",
         "Status": "Enabled",
         "Transitions": [
            {
               "Days": 30,
               "StorageClass": "STANDARD_IA"
            }
         ]
      }
   ]
}
EOL

# 3. 라이프사이클 정책 설정
aws s3api put-bucket-lifecycle-configuration --bucket my-lifecycle-bucket --lifecycle-configuration file://lifecycle.json

# 4. 라이프사이클 정책 확인
aws s3api get-bucket-lifecycle-configuration --bucket my-lifecycle-bucket
```

1. `my-lifecycle-bucket` 버킷을 생성합니다.
2. 30일 후 `STANDARD_IA`(가끔 접근하는 데이터용 스토리지 클래스)로 객체가 자동 전환되도록 라이프사이클 정책을 작성합니다.
3. 작성한 JSON 파일을 S3 버킷 설정에 반영합니다.
4. 정책이 적용되었는지 확인합니다.

이를 통해 사용 빈도가 적어진 객체를 자동으로 저렴한 스토리지 클래스로 전환하여 비용을 절감할 수 있습니다.

---

## **6. 마치며 ?**

Amazon S3는 **고가용성, 고내구성, 무한 확장성**을 갖춘 강력한 객체 스토리지 서비스입니다. 간단한 버킷 생성부터 시작해서, 버전 관리, 라이프사이클, 암호화 등의 기능을 전략적으로 활용하면 **안정적인 데이터 관리와 비용 최적화**를 모두 달성할 수 있습니다.  
S3를 적절히 활용하면 파일 호스팅, 백업 및 복구, 로그 아카이빙, 정적 웹 사이트 호스팅, 빅데이터 분석 스테이징 등 다양한 문제를 유연하게 해결할 수 있습니다!

---

### **참고 자료 및 출처**

- [AWS 공식 문서: Amazon S3](https://docs.aws.amazon.com/ko_kr/s3/index.html)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/s3/)
- [AWS SDK for Java Developer Guide](https://docs.aws.amazon.com/sdk-for-java/index.html)

Amazon S3를 통해 쉽고 간편하게 대용량 데이터를 저장하고 관리해보세요! 어떤 프로젝트든 빠르게 확장 가능한 백엔드 스토리지를 갖추게 될 것입니다.
