---
title: "Remote Procedure Call Best Practices: RPC Interface Guide"
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
         RPC Communication Structure
```

What if you could call functions on a remote server just like local functions? While building microservices architecture, I had to answer this question. REST APIs were too slow, and WebSocket was too complex. That's when I met RPC. This article covers everything from RPC Interface concepts to modern implementations like gRPC, and practical application know-how.

Understanding RPC can make distributed system communication as simple as calling local functions.

## Background

### Why RPC Emerged

In the late 1970s, as computers became networked, new problems arose. Programs on different computers needed complex network programming to exchange data. Developers had to handle socket communication directly, match data formats, and handle all error processing themselves.

RPC was born to solve this complexity. How convenient would it be if you could call remote functions just like functions on your local computer? The framework handles the complex details of network communication, and developers can focus only on business logic.

### Key Term Definitions

| Term | Meaning | Notes |
| --- | --- | --- |
| RPC | Remote Procedure Call | Core paradigm of distributed system communication |
| Stub | Client/server-side proxy code | Layer abstracting network communication |
| IDL | Interface Definition Language | .proto or .idl files |
| Marshalling | Convert data to transmittable format | Similar to serialization |
| XDR | External Data Representation | Standard format for data definition |

## Core Points

> RPC is inter-process communication technology enabling remote procedures to be called like local functions.

RPC Interface is a communication protocol agreed upon by client and server. Through this interface, programs written in different languages and applications running on different operating systems can exchange functions as if they were one program.

### How It Works

1. Client calls Stub function just like calling local function
2. Client Stub converts parameters to network transmission format
3. RPC runtime sends request to server over network
4. Server Stub receives request and restores to original format
5. Actual server function executes and produces result
6. Result is passed back to client in reverse order

### RPC in 2025

Traditional RPC started with implementations like CORBA and ONC RPC, but lost ground to REST due to implementation difficulties and limited functionality. However, the situation changed when Google released gRPC in 2015.

gRPC uses HTTP/2 and Protocol Buffers to show 3~10x faster performance compared to REST. As of 2025, companies like Netflix, Uber, and Square actively leverage gRPC for internal microservice communication.

### REST vs gRPC Performance Comparison

Recent benchmark results show clear differences. When transmitting identical data, JSON-based REST APIs use approximately 250 bytes of payload, while gRPC's Protocol Buffers use approximately 80 bytes—more than 3x smaller. Serialization speed is also significantly faster with gRPC.

Thanks to HTTP/2 multiplexing, gRPC can parallelly process multiple requests over a single connection. REST is HTTP/1.1 based, requiring new connections for each request, resulting in high network overhead.

## Practice

### Step 1 - Prepare Development Environment

We'll implement gRPC with Python. Python 3.8 or higher is required.

```
pip install grpcio grpcio-tools --break-system-packages
```

### Step 2 - Define Interface

Create calculator.proto file. This is the core of RPC Interface.

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

### Step 3 - Generate Stub Code

Auto-generate client and server code from proto file.

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

This command generates two files: calculator_pb2.py and calculator_pb2_grpc.py. These are the Stub code.

### Step 4 - Implement Server

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

### Step 5 - Implement Client

```
import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        # Call Add function - like local function!
        response = stub.Add(calculator_pb2.CalculateRequest(a=10, b=20))
        print(f"10 + 20 = {response.result}")

        # Call Multiply function
        response = stub.Multiply(calculator_pb2.CalculateRequest(a=5, b=7))
        print(f"5 * 7 = {response.result}")

if __name__ == '__main__':
    run()
```

### Step 6 - Execute and Test

Run server in Terminal 1.

```
python server.py
```

Run client in Terminal 2.

```
python client.py
```

Results are displayed immediately. It's network communication but as simple as calling a local function.

## Best Practices

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| gRPC for internal microservices | HTTP/2 provides 3~10x faster performance, bidirectional streaming support | Can't call directly from browser, needs gRPC-Web gateway |
| REST for public APIs | Universal browser support, familiar development experience | Lower performance than gRPC, larger payload due to text format |
| Hybrid approach | Combine advantages with REST externally, gRPC internally | Requires managing two systems, increased API Gateway complexity |
| IDL-based design | Guarantees type safety, auto code generation | Proto file version control required, backward compatibility consideration needed |
| Explicit error handling | Implement retry logic for network failures | Prevent infinite retries, Timeout settings required |

## Conclusion

RPC Interface enables simple communication like local function calls in distributed systems. Modern implementations like gRPC provide performance exceeding REST while improving development productivity. However, since REST remains the standard for public APIs, wisdom in choosing based on situation is necessary.

Domestic companies like KT Cloud have also adopted gRPC for inter-module communication and achieved performance improvements of more than 2x. A hybrid strategy maintaining REST on external interfaces while optimizing internal systems with gRPC is effective.

## References

- Microsoft RPC Official Documentation (<https://learn.microsoft.com/ko-kr/windows/win32/rpc/rpc-start-page>)
- AWS gRPC vs REST Comparison (<https://aws.amazon.com/ko/compare/the-difference-between-grpc-and-rest/>)
- Naver Cloud Deep Dive into gRPC ([https://medium.com/naver-cloud-platform/nbp-기술-경험-시대의-흐름-grpc-깊게-파고들기-1-39e97cb3460](https://medium.com/naver-cloud-platform/nbp-%EA%B8%B0%EC%88%A0-%EA%B2%BD%ED%97%98-%EC%8B%9C%EB%8C%80%EC%9D%98-%ED%9D%90%EB%A6%84-grpc-%EA%B9%8A%EA%B2%8C-%ED%8C%8C%EA%B3%A0%EB%93%A4%EA%B8%B0-1-39e97cb3460))
- KT Cloud Transition from REST to gRPC ([https://tech.ktcloud.com/entry/REST에서-gRPC로-차세대-API-통신-방식-도입기](https://tech.ktcloud.com/entry/REST%EC%97%90%EC%84%9C-gRPC%EB%A1%9C-%EC%B0%A8%EC%84%B8%EB%8C%80-API-%ED%86%B5%EC%8B%A0-%EB%B0%A9%EC%8B%9D-%EB%8F%84%EC%9E%85%EA%B8%B0))
- gRPC vs REST 2025 Benchmarks (<https://markaicode.com/grpc-vs-rest-benchmarks-2025/>)
- Remote Procedure Call Wikipedia ([https://ko.wikipedia.org/wiki/원격\_프로시저\_호출](https://ko.wikipedia.org/wiki/%EC%9B%90%EA%B2%A9_%ED%94%84%EB%A1%9C%EC%8B%9C%EC%A0%80_%ED%98%B8%EC%B6%9C))
