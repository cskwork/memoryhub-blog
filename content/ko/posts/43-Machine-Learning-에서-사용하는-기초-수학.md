---
title: "Machine Learning 에서 사용하는 기초 수학"
date: 2020-11-25T09:31:22+09:00
slug: "43-Machine-Learning-에서-사용하는-기초-수학"
original_url: "https://memoryhub.tistory.com/43"
tistory_id: 43
draft: false
---

ML: 데이터와 통계로 컴퓨터를 학습시킴. (데이터를 분석해서 결과를 예측함) [Python Machine Learning (w3schools.com)](https://www.w3schools.com/python/python_ml_getting_started.asp)

[Python Machine Learning

Machine Learning Machine Learning is making the computer learn from studying data and statistics. Machine Learning is a step into the direction of artificial intelligence (AI). Machine Learning is a program that analyses data and learns to predict the outc

www.w3schools.com](https://www.w3schools.com/python/python_ml_getting_started.asp)

데이터의 종류:

- **Numerical**
- **Categorical**
- **Ordinal**

**Numerical** data :숫자 

- Discrete Data  
  - numbers that are limited to integers. Example: The number of cars passing by.
- Continuous Data  
  - numbers that are of infinite value. Example: The price of an item, or the size of an item

**Categorical** data : 비교 불가 데이터. values that cannot be measured up against each other. Example: a color value, or any yes/no values.

**Ordinal** data : 상대적으로 비교 가능한 데이터. like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.

데이터 타입을 알아야 어떻게 분석할지 알 수 있다.

---

- **Mean** - The average value
- **Median** - The mid point value
- **Mode** - The most common value

예제:

```
import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)
median = numpy.median(speed)
mode = stats.mode(speed)
standard_deviation = numpy.std(speed)

print(mean)
print()
print(median)
print()
print(mode)
print()
print(standard_deviation)

#The mode() method returns a ModeResult object that contains the mode number (86), and count (how many times the mode number appeared (3)).
```

결과:

89.76923076923077

87.0

ModeResult(mode=array([86]), count=array([3]))

9.258292301032677

---

**Standard Deviation**

정의: 각 값이 서로 얼마나 퍼져있는지 확인. (mean value를 기준으로)

예제는 상단에 있음
