---
title: "[☁️] AWS CloudFormation, 클릭 대신 코드로 인프라 찍어내기?"
date: 2024-05-28T12:36:46+09:00
slug: "115-AWS-CloudFormation-클릭-대신-코드로-인프라-찍어내기"
original_url: "https://memoryhub.tistory.com/115"
tistory_id: 115
draft: false
---

```
      .--.
    .----' ,-.
    '-.  `'   `
      .'        `.
     /      ☁️     \
    |   { IaC }   |
     \    ➡️     /
      `.   AWS  .'
        `'---'`
```

서버 한 대 구성하는데 AWS 콘솔에서 EC2, VPC, 보안 그룹, IAM 역할... 클릭하다 날 새본 경험, 다들 있으시죠? 배포 환경마다 이 작업을 반복해야 하고, 동료가 어떤 설정을 바꿨는지 추적하기도 어렵습니다. 실수로 설정 하나 잘못 바꾸면 서비스 전체가 흔들리는 아찔한 상황이 발생할 수도 있습니다. 이 모든 과정을 자동화하고, 실수 없이, 언제든 똑같이 재현할 수는 없을까요?

⚡ **TL;DR:**

- AWS CloudFormation은 인프라를 코드로 관리(IaC)하는 AWS의 대표적인 서비스입니다[2][6].
- 템플릿 파일 하나로 EC2, S3 같은 AWS 자원을 선언하고, CloudFormation이 자동으로 생성 및 관리해줍니다[1][4].

## 목차

1. 배경: 왜 CloudFormation을 써야 할까?
2. 핵심 개념: 템플릿과 스택
3. 실습: 코드로 S3 버킷 만들기
4. 베스트 프랙티스
5. 마치며 & 참고자료

---

## 1. 배경: 왜 CloudFormation을 써야 할까?

과거에는 개발자가 AWS 콘솔에 직접 접속해 필요한 리소스(EC2 인스턴스, 데이터베이스 등)를 하나하나 생성하고 설정했습니다[1]. 이 방식은 직관적이지만 몇 가지 치명적인 문제가 있습니다.

- **느린 속도와 반복 작업:** 확장 가능한 웹 애플리케이션을 위해 Auto Scaling 그룹, 로드 밸런서, 데이터베이스를 구성하는 일은 복잡하고 시간이 많이 소요됩니다[1][4].
- **휴먼 에러:** 수동 작업은 설정 누락이나 실수로 이어지기 쉽습니다.
- **일관성 부재:** 개발, 스테이징, 운영 환경의 인프라를 동일하게 구성하기 어렵습니다.
- **변경 이력 추적 불가:** 누가, 언제, 왜 인프라를 변경했는지 파악하기 힘듭니다.

AWS CloudFormation은 이러한 문제들을 **IaC(Infrastructure as Code)** 접근 방식으로 해결합니다. 인프라 구성을 코드(템플릿)로 작성하여 관리함으로써, 인프라 관리를 간소화하고, 신속하게 복제하며, 변경 사항을 쉽게 제어하고 추적할 수 있게 됩니다[1][6].

✅ **관련 용어 정리**

- **IaC(Infrastructure as Code):** 코드를 사용해 인프라를 관리하고 프로비저닝하는 방법론입니다. CloudFormation은 AWS의 대표적인 IaC 서비스입니다[2][6].
- **템플릿(Template):** 생성할 모든 AWS 리소스와 그 속성을 정의하는 설계도 파일입니다. JSON 또는 YAML 형식으로 작성할 수 있습니다[1][5][6].
- **스택(Stack):** 템플릿을 통해 생성되고 관리되는 AWS 리소스들의 묶음입니다. 스택은 하나의 단위로 생성, 업데이트, 삭제됩니다[1][5][6].

## 2. 핵심 개념: 템플릿과 스택

> **AWS CloudFormation은 템플릿이라는 설계도를 통해 AWS 인프라를 예측 가능하고 반복 가능한 방식으로 자동으로 생성하고 관리하는 서비스입니다[1][2][7].**

개발자는 필요한 모든 리소스를 **템플릿**에 정의하기만 하면 됩니다[4]. 그러면 CloudFormation이 템플릿을 읽어 리소스 간의 의존성을 파악하고 순서에 맞게 프로비저닝하여 **스택**을 생성합니다[1].

간단한 S3 버킷을 생성하는 YAML 형식의 템플릿 예제입니다.

```
# 템플릿 파일 규격 버전
AWSTemplateFormatVersion: '2010-09-09'
Description: S3 버킷 생성을 위한 간단한 CloudFormation 템플릿

# 스택 생성 시 외부에서 입력받을 값 (파라미터)
Parameters:
  BucketName:
    Description: 생성할 S3 버킷의 이름
    Type: String

# 실제로 생성될 AWS 리소스 정의
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket' # 리소스 타입: S3 버킷
    Properties:
      BucketName: !Ref BucketName # 파라미터로 받은 BucketName을 버킷 이름으로 사용

# 스택 생성 후 출력할 값
Outputs:
  BucketARN:
    Description: 생성된 S3 버킷의 ARN
    Value: !GetAtt S3Bucket.Arn
```

이 템플릿은 `Parameters`, `Resources`, `Outputs` 라는 주요 섹션으로 구성되어 있습니다[5]. `Resources` 섹션이 가장 중요하며, 실제로 생성할 AWS 리소스를 정의하는 부분입니다[5].

## 3. 실습: 코드로 S3 버킷 만들기

위에서 작성한 템플릿을 사용해 실제로 스택을 생성해보겠습니다.

**① 템플릿 파일 준비**

- 위 YAML 코드를 `s3-bucket-template.yaml`과 같은 이름으로 저장합니다.

**② 스택 생성하기 (AWS 콘솔)**

- AWS 관리 콘솔에 로그인하여 CloudFormation 서비스로 이동합니다[8].
- **'스택 생성'**을 클릭하고 '새 리소스 사용(표준)'을 선택합니다[8].
- '템플릿 준비' 단계에서 '템플릿 파일 업로드'를 선택하고, 방금 저장한 `s3-bucket-template.yaml` 파일을 업로드합니다.
- '스택 이름'을 입력하고, `Parameters` 섹션에 원하는 `BucketName`을 입력합니다.
- 나머지 옵션은 기본값으로 두고 끝까지 진행하여 **'스택 생성'** 버튼을 누릅니다.

**③ 생성 결과 확인 및 삭제**

- 잠시 후 스택 상태가 `CREATE_COMPLETE`로 바뀌면 성공적으로 리소스가 생성된 것입니다. EC2나 S3 콘솔에 가보면 실제로 버킷이 만들어진 것을 확인할 수 있습니다[1].
- 스택을 삭제하면 해당 스택에 속한 모든 리소스가 한 번에 깔끔하게 삭제되어 리소스 관리가 매우 편리합니다[1][4].

## 4. 모범 사례

CloudFormation을 더 효과적으로 사용하기 위한 몇 가지 모범 사례입니다.

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **템플릿 모듈화 (네스티드 스택)** | 복잡한 인프라를 네트워크, 애플리케이션 등 작은 단위로 나눠 재사용성을 높이고 관리를 용이하게 합니다[5]. | 스택 간 의존성이 생겨 관리가 복잡해질 수 있으므로, 명확한 설계가 필요합니다. |
| **파라미터(Parameters)와 매핑(Mappings) 활용** | 환경(개발/운영)에 따라 다른 인스턴스 타입이나 AMI ID를 적용하는 등, 템플릿 수정 없이 유연하게 재사용할 수 있습니다[5]. | 파라미터가 너무 많아지면 템플릿 사용이 오히려 복잡해질 수 있습니다. |
| **변경 세트(Change Sets) 사용** | 스택을 업데이트하기 전, 어떤 리소스가 어떻게 변경될지 미리 확인할 수 있어 의도치 않은 리소스 변경이나 삭제를 방지합니다. | 변경 사항을 적용하기 전 검토하는 추가 단계가 필요합니다. |
| **드리프트 탐지(Drift Detection)** | 템플릿에 정의된 구성과 실제 리소스 구성 간의 차이(드리프트)를 감지하여 인프라 일관성을 유지하는 데 도움을 줍니다[5]. | 정기적으로 드리프트를 확인하고 조치하는 운영 노력이 필요합니다. |

## 5. 마치며

오늘은 코드를 통해 AWS 인프라를 자동으로 프로비저닝하고 관리하는 CloudFormation에 대해 알아보았습니다.

- 인프라를 코드로 관리하면 수동 작업의 실수를 줄이고 생산성을 극대화할 수 있습니다[1][6].
- 템플릿을 통해 복잡한 아키텍처도 표준화하고, 어떤 환경에서든 신속하게 복제할 수 있습니다[6].
- 스택 단위 관리는 리소스의 생성부터 삭제까지 전체 생명주기를 명확하고 안전하게 관리해줍니다[1].

**실제 프로젝트 적용 팁:** 작성한 CloudFormation 템플릿을 Git으로 버전 관리하고, Jenkins나 AWS CodePipeline 같은 CI/CD 도구와 연동하여 인프라 변경을 자동화해보세요. DevOps 파이프라인의 핵심적인 부분이 될 수 있습니다[2][7].

오늘 내용이 유익했다면 ❤️와 댓글 부탁드립니다! 여러분의 작은 관심이 더 좋은 글을 쓰는 데 큰 힘이 됩니다.

---

**참고자료**

- [AWS CloudFormation 공식 사용자 가이드](https://docs.aws.amazon.com/ko_kr/AWSCloudFormation/latest/UserGuide/Welcome.html)[1]
- [AWS CloudFormation 제품 페이지](https://aws.amazon.com/ko/cloudformation/)[2]
- [AWS CloudFormation - Wikipedia](https://en.wikipedia.org/wiki/AWS_CloudFormation)[5]
- [[AWS] AWS CloudFormation 의 개념 - 티스토리 블로그](https://nearhome.tistory.com/117)[3]

[1] <https://docs.aws.amazon.com/ko_kr/AWSCloudFormation/latest/UserGuide/Welcome.html>  
[2] <https://aws.amazon.com/ko/cloudformation/>  
[3] <https://nearhome.tistory.com/117>  
[4] <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html>  
[5] <https://en.wikipedia.org/wiki/AWS_CloudFormation>  
[6] <https://yoo11052.tistory.com/188>  
[7] <https://aws.amazon.com/cloudformation/>  
[8] <https://www.youtube.com/watch?v=2gT1dvbppg8>  
[9] <https://aws.amazon.com/ko/cloudformation/features/>
