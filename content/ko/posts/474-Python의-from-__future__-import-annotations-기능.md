---
title: "Python의 from __future__ import annotations 기능"
date: 2025-03-15T16:54:17+09:00
slug: "474-Python의-from-__future__-import-annotations-기능"
original_url: "https://memoryhub.tistory.com/474"
tistory_id: 474
draft: false
---

## 1. 개요

`from __future__ import annotations`는 Python에서 **타입 힌트를 문자열로 처리하도록 하는 기능**입니다. 이를 통해 **클래스를 선언하기 전에 참조할 수 있고, 불필요한 의존성 문제를 해결하며, 성능을 향상**시킬 수 있습니다.

Python 3.11부터는 기본적으로 활성화되어 있지만, 이전 버전(3.7~3.10)에서는 직접 사용해야 합니다.

---

## 2. 왜 필요할까?

### ? 문제: 클래스 내부에서 자기 자신을 참조할 때 오류 발생

다음과 같이 클래스 내부에서 자기 자신을 타입 힌트로 사용하면 오류가 발생합니다.

```
class Person:
    def friend(self, other: Person) -> Person:
        return other
```

? **오류 발생!**

> `NameError: name 'Person' is not defined`

Python은 코드를 **위에서 아래로 해석**하기 때문에 `Person` 클래스가 완전히 정의되기 전에 타입 힌트에서 `Person`을 사용하면 오류가 발생합니다.

---

## 3. 해결 방법: `from __future__ import annotations` 사용하기

위 문제는 다음과 같이 `from __future__ import annotations`를 사용하면 해결할 수 있습니다.

```
from __future__ import annotations

class Person:
    def friend(self, other: Person) -> Person:  # ✅ 정상 작동
        return other
```

이제 `Person`을 **문자열(`"Person"`)로 처리**하여 Python이 타입 힌트를 즉시 평가하지 않도록 만듭니다. 이렇게 하면 **클래스가 정의되기 전에도 참조할 수 있습니다!** ?

---

## 4. 추가적인 이점

### ✅ **순환 참조 문제 해결**

다음과 같이 두 개의 파일이 서로를 참조하는 경우 **순환 참조(Circular Import)** 오류가 발생할 수 있습니다.

#### ❌ 오류 발생 코드 (`module_a.py`와 `module_b.py`가 서로 import)

**module\_a.py**

```
from module_b import B

class A:
    def method(self, obj: B) -> A:
        return self
```

**module\_b.py**

```
from module_a import A

class B:
    def method(self, obj: A) -> B:
        return self
```

? **실행하면 오류 발생!**

> ImportError: cannot import name 'A'

✅ `from __future__ import annotations`를 사용하면 Python이 타입 힌트를 나중에 평가하기 때문에, 이러한 **순환 참조 문제를 방지**할 수 있습니다.

---

## 5. Python 3.11 이상에서는 필요 없음

Python 3.11부터는 `from __future__ import annotations` 없이도 동일한 동작을 합니다. 즉, **Python 3.11 이상에서는 자동으로 타입 힌트를 문자열처럼 처리**하므로 추가할 필요가 없습니다.

하지만 **Python 3.7~3.10을 사용하는 경우 반드시 추가해야** 합니다!

---

## 6. 정리 ?

✔ `from __future__ import annotations`는 **타입 힌트를 문자열로 처리**하여 코드 실행 시점을 늦춥니다.  
✔ **클래스를 정의하기 전에 참조할 수 있도록 도와줍니다.**  
✔ **순환 참조(Circular Import) 문제를 해결**할 수 있습니다.  
✔ **Python 3.11 이상에서는 기본적으로 활성화**되므로 필요 없습니다.

✅ **Python 3.7~3.10을 사용한다면 꼭 추가하세요!**
