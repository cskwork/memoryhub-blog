---
title: "SWE-bench와 Claude 3.5 Sonnet의 소프트웨어 엔지니어링 벤치마크 분석 ?"
date: 2024-12-21T20:16:22+09:00
slug: "422-SWE-bench와-Claude-3-5-Sonnet의-소프트웨어-엔지니어링-벤치마크-분석"
original_url: "https://memoryhub.tistory.com/422"
tistory_id: 422
draft: false
---

안녕하세요! 오늘은 인공지능의 코딩 능력을 평가하는 SWE-bench와 Claude 3.5 Sonnet의 놀라운 성과에 대해 자세히 알아보겠습니다.

## SWE-bench란? ?

SWE-bench는 AI 모델의 실제 소프트웨어 엔지니어링 능력을 평가하는 벤치마크입니다. 마치 실제 개발자처럼 GitHub 이슈를 해결할 수 있는지 테스트하죠!

### 주요 특징:

- 실제 오픈소스 Python 프로젝트의 이슈들을 활용
- AI가 코드를 이해하고, 수정하고, 테스트하는 전 과정 평가
- 실제 PR(Pull Request)의 단위 테스트로 검증
- "에이전트" 시스템 전체를 평가 (AI 모델 + 소프트웨어 스캐폴딩)

## Claude 3.5 Sonnet의 혁신적 성과 ?

### 성능 비교

```
모델                          점수
Claude 3.5 Sonnet (신규)     49%
이전 최고 성능               45%
Claude 3.5 Sonnet (구버전)   33%
Claude 3 Opus               22%
```

## 어떻게 이런 성과를 달성했나? ?

### 1. Tool Using Agent 설계 철학

- AI 모델에 최대한의 자율성 부여
- 최소한의 스캐폴딩 유지
- 두 가지 핵심 도구 제공:
  - Bash Tool: 명령어 실행
  - Edit Tool: 파일 조작

### 2. 프롬프트 최적화

```
주요 단계:
1. 저장소 구조 탐색
2. 에러 재현 스크립트 작성
3. 소스코드 수정
4. 재실행으로 검증
5. 엣지케이스 처리
```

### 3. 도구 설계의 섬세함

- 명확한 도구 설명
- 에러 방지 메커니즘
- 상태 유지 관리
- 파일 경로 처리 최적화

## 실제 작동 예시 ?

1. **초기 탐색**
   - 저장소 구조 분석
   - 문제 상황 파악
2. **에러 재현**
3. `# 테스트 데이터 생성 n = 100 x = np.random.randn(n, 30) y = np.random.normal(size = n)`
4. **코드 수정**
   - 정확한 위치 파악
   - 최소한의 변경으로 해결

## 도전 과제들 ?

1. **자원 소비**
   - 긴 실행 시간
   - 높은 토큰 비용
   - 수백 번의 상호작용 필요
2. **평가의 어려움**
   - 환경 설정 이슈
   - 숨겨진 테스트 케이스
   - 추상화 수준 불일치
3. **멀티모달 한계**
   - 파일 시각화 제한
   - URL 참조 어려움
   - 디버깅 복잡성

## 미래 전망 ?

Claude 3.5 Sonnet의 성과는 AI 코딩 능력의 새로운 지평을 열었습니다. 특히:

- 더 높은 정확도
- 자가 수정 능력 향상
- 다양한 해결 방법 시도
- 지속적인 개선 가능성

## 참고자료 ?

1. SWE-bench 공식 사이트: <https://www.swebench.com/>
2. Anthropic Blog: Claude 3.5 Sonnet 업데이트 발표
3. SWE-Agent 프레임워크 문서

---

# Claude 3.5 Sonnet과 함께하는 실용적인 소프트웨어 엔지니어링 가이드 ?️

Claude 3.5 Sonnet이 실제로 어떻게 코딩 문제를 해결하는지, 구체적인 예제와 함께 살펴보겠습니다.

## 1. 실제 버그 수정 사례: RidgeClassifierCV 파라미터 문제 ?

### 문제 상황

```
# 에러가 발생하는 코드
from sklearn import linear_model as lm
import numpy as np

n = 100
x = np.random.randn(n, 30)
y = np.random.normal(size = n)

rr = lm.RidgeClassifierCV(
    alphas = np.arange(0.1, 1000, 0.1), 
    normalize = True,
    store_cv_values = True
).fit(x, y)
```

### 발생한 에러

```
TypeError: __init__() got an unexpected keyword argument 'store_cv_values'
```

### Claude의 분석 과정

1. **코드 탐색**

   ```
   # ridge.py 파일 내부
   class RidgeClassifierCV:
    def __init__(self, alphas=(0.1, 1.0, 10.0), 
                 fit_intercept=True,
                 normalize=False, 
                 scoring=None, 
                 cv=None, 
                 class_weight=None):
        # store_cv_values 파라미터가 없음!
   ```
2. **해결 방안 도출**

   ```
   # 수정된 코드
   def __init__(self, alphas=(0.1, 1.0, 10.0),
             fit_intercept=True,
             normalize=False,
             scoring=None,
             cv=None,
             class_weight=None,
             store_cv_values=False):  # 파라미터 추가
    super(RidgeClassifierCV, self).__init__(
        alphas=alphas,
        fit_intercept=fit_intercept,
        normalize=normalize,
        scoring=scoring,
        cv=cv,
        store_cv_values=store_cv_values  # 상위 클래스에 전달
    )
   ```

## 2. 실제 기능 구현 예시: 파일 처리 시스템 ?️

### 요구사항

- 디렉토리 탐색
- 파일 내용 수정
- 변경 사항 검증

### Claude의 구현 과정

1. **디렉토리 탐색**

   ```
   def explore_directory(path):
    """
    디렉토리 구조를 탐색하는 함수
    """
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')
   ```
2. **파일 수정**

   ```
   def modify_file(file_path, old_str, new_str):
    """
    파일 내용을 안전하게 수정하는 함수
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # 정확한 매칭 확인
    if content.count(old_str) != 1:
        raise ValueError("고유한 매칭이 필요합니다")

    # 백업 생성
    backup_path = f"{file_path}.bak"
    shutil.copy2(file_path, backup_path)

    # 내용 수정
    new_content = content.replace(old_str, new_str)

    with open(file_path, 'w') as file:
        file.write(new_content)
   ```
3. **변경 검증**

   ```
   def verify_changes(file_path, test_function):
    """
    변경 사항을 검증하는 함수
    """
    try:
        result = test_function()
        print(f"검증 성공: {file_path}")
        return True
    except Exception as e:
        print(f"검증 실패: {str(e)}")
        # 백업에서 복구
        if os.path.exists(f"{file_path}.bak"):
            shutil.copy2(f"{file_path}.bak", file_path)
        return False
   ```

## 3. 실제 사용 시나리오 ?

### 시나리오 1: 설정 파일 업데이트

```
# 설정 파일 수정 예제
def update_config():
    file_path = "/repo/config.py"
    old_config = """
    DEBUG = False
    MAX_RETRIES = 3
    """
    new_config = """
    DEBUG = True
    MAX_RETRIES = 5
    """

    modify_file(file_path, old_config, new_config)
    verify_changes(file_path, run_tests)
```

### 시나리오 2: API 엔드포인트 수정

```
# API 라우트 업데이트 예제
def update_api_route():
    file_path = "/repo/api/routes.py"
    old_route = """
    @app.route('/users', methods=['GET'])
    def get_users():
        return jsonify(users)
    """
    new_route = """
    @app.route('/users', methods=['GET'])
    def get_users():
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        return jsonify(paginate_users(users, page, per_page))
    """

    modify_file(file_path, old_route, new_route)
    verify_changes(file_path, test_api)
```

## 마치며 ?

Claude 3.5 Sonnet의 실제 사용 사례를 통해 우리는 다음과 같은 점들을 배웠습니다:

1. **체계적인 접근**

   - 문제 분석
   - 해결책 설계
   - 구현 및 검증
2. **안전한 코드 수정**

   - 백업 생성
   - 변경 검증
   - 롤백 메커니즘
3. **효율적인 디버깅**

   - 명확한 에러 메시지
   - 단계별 검증
   - 자동화된 테스트

## 참고 자료 ?

1. Anthropic Technical Blog
2. sklearn Documentation
3. Python Software Engineering Best Practices
