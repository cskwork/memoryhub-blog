---
title: "Python's from __future__ import annotations Feature"
date: 2025-03-15T16:54:17+09:00
slug: "474-Python의-from-__future__-import-annotations-기능"
original_url: "https://memoryhub.tistory.com/474"
tistory_id: 474
draft: false
---

## 1. Overview

`from __future__ import annotations` is a **feature in Python that treats type hints as strings**. Through this, you can **reference classes before declaring them, solve unnecessary dependency issues, and improve performance**.

It's enabled by default starting from Python 3.11, but you need to use it directly in earlier versions (3.7-3.10).

---

## 2. Why Is It Needed?

### ? Problem: Error When Referencing Itself Inside a Class

If you use a class inside itself as a type hint like this, an error occurs:

```
class Person:
    def friend(self, other: Person) -> Person:
        return other
```

? **Error Occurs!**

> `NameError: name 'Person' is not defined`

Python interprets code **from top to bottom**, so if you use `Person` in a type hint before the `Person` class is completely defined, an error occurs.

---

## 3. Solution: Using `from __future__ import annotations`

The above problem can be solved by using `from __future__ import annotations`:

```
from __future__ import annotations

class Person:
    def friend(self, other: Person) -> Person:  # ✅ Works correctly
        return other
```

Now `Person` is **treated as a string (`"Person"`)** so Python doesn't evaluate type hints immediately. This way, you can **reference the class before it's even defined!** ?

---

## 4. Additional Benefits

### ✅ **Solve Circular Reference Problems**

If you have two files that reference each other like this, **circular import errors** can occur:

#### ❌ Error Code (`module_a.py` and `module_b.py` import each other)

**module_a.py**

```
from module_b import B

class A:
    def method(self, obj: B) -> A:
        return self
```

**module_b.py**

```
from module_a import A

class B:
    def method(self, obj: A) -> B:
        return self
```

? **Running it causes an error!**

> ImportError: cannot import name 'A'

✅ Using `from __future__ import annotations` allows Python to evaluate type hints later, so you can **avoid such circular reference problems**.

---

## 5. Not Needed in Python 3.11+

Starting from Python 3.11, it behaves the same way without `from __future__ import annotations`. In other words, **Python 3.11+ automatically treats type hints like strings** so you don't need to add it.

However, **if you use Python 3.7-3.10, you must add it!**

---

## 6. Summary ?

✔ `from __future__ import annotations` **treats type hints as strings** and delays code execution timing.  
✔ **Helps you reference classes before defining them.**  
✔ **Can solve circular import problems.**  
✔ **Enabled by default in Python 3.11+** so it's not needed.

✅ **If you use Python 3.7-3.10, definitely add it!**
