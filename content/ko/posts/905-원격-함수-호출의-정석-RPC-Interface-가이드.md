---
title: "원격 함수 호출의 정석, RPC Interface 가이드"
date: 2025-11-11T05:49:21+09:00
slug: "905-원격-함수-호출의-정석-RPC-Interface-가이드"
original_url: "https://memoryhub.tistory.com/905"
tistory_id: 905
draft: false
---

```
    ┌──────────────────────────────┐
    │   Client Application         │
    │  ┌────────────┐              │
    │  │   Stub     │              │
    │  └─────┬──────┘              │
    └────────┼───────────────────────┘
             │ Network
    ┌────────┼───────────────────────┐
    │  ┌─────┴──────┐              │
    │  │   Stub     │              │
    │  └────────────┘              │
    │   Server Application         │
    └──────────────────────────────┘
         RPC 통신 구조
```

로컬 함수처럼 원격 서버의 함수를 호출할 수 있다면? 마이크로서비스 아키텍처를 구축하면서 이 질문에 답해야 했습니다. REST API는 너무 느렸고, WebSocket은 복잡했죠. 그때 만난 것이 RPC였습니다. 이 글에서는 RPC Interface의 개념부터 gRPC 같은 최신 구현체, 그리고 실무 적용 노하우까지 모두 담았습니다.

RPC를 이해하면 분산 시스템 통신을 로컬 함수 호출처럼 간단하게 만들 수 있습니다.

## 배경

### RPC가 등장한 이유

1970년대 후반, 컴퓨터들이 네트워크로 연결되면서 새로운 문제가 생겼습니다. 서로 다른 컴퓨터에 있는 프로그램들이 데이터를 주고받으려면 복잡한 네트워크 프로그래밍이 필요했죠. 소켓 통신을 직접 다뤄야 했고, 데이터 포맷을 맞추고, 에러를 처리하는 모든 과정이 개발자의 몫이었습니다.

RPC는 이런 복잡함을 해결하기 위해 탄생했습니다. 원격에 있는 함수를 마치 내 컴퓨터의 함수처럼 호출할 수 있다면 얼마나 편할까요? 네트워크 통신의 복잡한 세부사항은 프레임워크가 처리하고, 개발자는 비즈니스 로직에만 집중할 수 있습니다.

### 주요 용어 정의

| 용어 | 의미 | 비고 |
| --- | --- | --- |
| RPC | Remote Procedure Call, 원격 프로시저 호출 | 분산 시스템 통신의 핵심 패러다임 |
| Stub | 클라이언트/서버 측 프록시 코드 | 네트워크 통신을 추상화하는 계층 |
| IDL | Interface Definition Language | 인터페이스 정의 언어, .proto나 .idl 파일 |
| Marshalling | 데이터를 전송 가능한 형태로 변환 | Serialization과 유사한 개념 |
| XDR | External Data Representation | 데이터 표준 형식 정의 |

## 핵심

> RPC는 원격 프로시저를 로컬 함수처럼 호출할 수 있게 해주는 프로세스 간 통신 기술입니다.

RPC Interface는 클라이언트와 서버가 합의한 통신 규약입니다. 이 인터페이스를 통해 서로 다른 언어로 작성된 프로그램, 서로 다른 운영체제에서 실행되는 애플리케이션이 마치 하나의 프로그램처럼 함수를 주고받을 수 있습니다.

### 작동 원리

1. 클라이언트가 로컬 함수를 호출하듯 Stub 함수를 호출합니다
2. Client Stub이 매개변수를 네트워크 전송 형식으로 변환합니다
3. RPC 런타임이 네트워크를 통해 서버에 요청을 전송합니다
4. Server Stub이 요청을 받아 원래 형식으로 복원합니다
5. 실제 서버 함수가 실행되어 결과를 생성합니다
6. 역순으로 결과가 클라이언트에 전달됩니다

### 2025년 현재의 RPC

전통적인 RPC는 CORBA, ONC RPC 같은 구현체로 시작했지만, 구현의 어려움과 제한된 기능으로 REST에 자리를 내주었습니다. 하지만 2015년 Google이 gRPC를 공개하면서 상황이 바뀌었습니다.

gRPC는 HTTP/2와 Protocol Buffers를 사용하여 REST 대비 3~10배 빠른 성능을 보여줍니다. 2025년 현재, Netflix, Uber, Square 같은 기업들이 내부 마이크로서비스 통신에 gRPC를 적극 활용하고 있습니다.

### REST vs gRPC 성능 비교

최신 벤치마크 결과를 보면 차이가 명확합니다. 동일한 데이터를 전송할 때, JSON 기반 REST API는 약 250바이트의 페이로드를 사용하지만, gRPC의 Protocol Buffers는 약 80바이트로 3배 이상 작습니다. 직렬화 속도도 gRPC가 월등히 빠릅니다.

HTTP/2의 멀티플렉싱 덕분에 gRPC는 단일 연결로 여러 요청을 병렬 처리할 수 있습니다. REST는 HTTP/1.1 기반으로 각 요청마다 새로운 연결을 맺어야 하므로 네트워크 오버헤드가 큽니다.

## 실습

### 1단계 - 개발 환경 준비

Python으로 gRPC를 구현해보겠습니다. Python 3.8 이상이 필요합니다.

```
pip install grpcio grpcio-tools --break-system-packages
```

### 2단계 - 인터페이스 정의

calculator.proto 파일을 생성합니다. 이것이 RPC Interface의 핵심입니다.

```
syntax = "proto3";

service Calculator {
  rpc Add(CalculateRequest) returns (CalculateResponse) {}
  rpc Multiply(CalculateRequest) returns (CalculateResponse) {}
}

message CalculateRequest {
  int32 a = 1;
  int32 b = 2;
}

message CalculateResponse {
  int32 result = 1;
}
```

### 3단계 - Stub 코드 생성

Proto 파일로부터 클라이언트와 서버 코드를 자동 생성합니다.

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

이 명령어는 calculator\_pb2.py와 calculator\_pb2\_grpc.py 두 파일을 생성합니다. 이것들이 바로 Stub 코드입니다.

### 4단계 - 서버 구현

```
import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return calculator_pb2.CalculateResponse(result=result)

    def Multiply(self, request, context):
        result = request.a * request.b
        return calculator_pb2.CalculateResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorService(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
```

### 5단계 - 클라이언트 구현

```
import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        # Add 함수 호출 - 로컬 함수처럼!
        response = stub.Add(calculator_pb2.CalculateRequest(a=10, b=20))
        print(f"10 + 20 = {response.result}")

        # Multiply 함수 호출
        response = stub.Multiply(calculator_pb2.CalculateRequest(a=5, b=7))
        print(f"5 * 7 = {response.result}")

if __name__ == '__main__':
    run()
```

### 6단계 - 실행 및 테스트

터미널 1에서 서버를 실행합니다.

```
python server.py
```

터미널 2에서 클라이언트를 실행합니다.

```
python client.py
```

결과가 즉시 출력됩니다. 네트워크 통신이지만 로컬 함수를 호출하는 것처럼 간단합니다.

## 모범사례

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| 내부 마이크로서비스용 gRPC | HTTP/2로 3~10배 빠른 성능, 양방향 스트리밍 지원 | 브라우저 직접 호출 불가, gRPC-Web 게이트웨이 필요 |
| 공개 API용 REST | 범용 브라우저 지원, 친숙한 개발 경험 | 성능은 gRPC보다 낮음, 텍스트 기반으로 용량 큼 |
| 하이브리드 접근 | 외부는 REST, 내부는 gRPC로 장점 결합 | 두 시스템 관리 필요, API Gateway 설정 복잡도 증가 |
| IDL 기반 설계 | 타입 안정성 보장, 자동 코드 생성 | .proto 파일 버전 관리 필수, 하위 호환성 고려 필요 |
| 에러 처리 명시 | 네트워크 장애 시 재시도 로직 구현 | 무한 재시도 방지, Timeout 설정 필수 |

## 마치며

RPC Interface는 분산 시스템에서 로컬 함수 호출처럼 간단한 통신을 가능하게 합니다. gRPC 같은 현대적 구현체는 REST를 능가하는 성능을 제공하면서도 개발 생산성을 높여줍니다. 다만 REST가 여전히 공개 API의 표준인 만큼, 상황에 맞게 선택하는 지혜가 필요합니다.

KT Cloud 같은 국내 기업도 내부 모듈 간 통신에 gRPC를 도입하여 2배 이상의 성능 향상을 달성했습니다. 외부 접점은 REST로 유지하면서 내부는 gRPC로 최적화하는 하이브리드 전략이 효과적입니다.

## 참고자료

- Microsoft RPC 공식 문서 (<https://learn.microsoft.com/ko-kr/windows/win32/rpc/rpc-start-page>)
- AWS gRPC와 REST 비교 (<https://aws.amazon.com/ko/compare/the-difference-between-grpc-and-rest/>)
- 네이버 클라우드 gRPC 깊게 파고들기 ([https://medium.com/naver-cloud-platform/nbp-기술-경험-시대의-흐름-grpc-깊게-파고들기-1-39e97cb3460](https://medium.com/naver-cloud-platform/nbp-%EA%B8%B0%EC%88%A0-%EA%B2%BD%ED%97%98-%EC%8B%9C%EB%8C%80%EC%9D%98-%ED%9D%90%EB%A6%84-grpc-%EA%B9%8A%EA%B2%8C-%ED%8C%8C%EA%B3%A0%EB%93%A4%EA%B8%B0-1-39e97cb3460))
- KT Cloud REST에서 gRPC로 도입기 ([https://tech.ktcloud.com/entry/REST에서-gRPC로-차세대-API-통신-방식-도입기](https://tech.ktcloud.com/entry/REST%EC%97%90%EC%84%9C-gRPC%EB%A1%9C-%EC%B0%A8%EC%84%B8%EB%8C%80-API-%ED%86%B5%EC%8B%A0-%EB%B0%A9%EC%8B%9D-%EB%8F%84%EC%9E%85%EA%B8%B0))
- gRPC vs REST 2025 벤치마크 (<https://markaicode.com/grpc-vs-rest-benchmarks-2025/>)
- 원격 프로시저 호출 위키백과 ([https://ko.wikipedia.org/wiki/원격\_프로시저\_호출](https://ko.wikipedia.org/wiki/%EC%9B%90%EA%B2%A9_%ED%94%84%EB%A1%9C%EC%8B%9C%EC%A0%80_%ED%98%B8%EC%B6%9C))
