---
title: "Fundamental Mathematics Used in Machine Learning"
date: 2020-11-25T09:31:22+09:00
slug: "43-Machine-Learning-에서-사용하는-기초-수학"
original_url: "https://memoryhub.tistory.com/43"
tistory_id: 43
draft: false
categories: ["Dev Library"]
tags: ["Machine Learning"]
---

ML: Teaching computers to learn by studying data and statistics. (Analyzing data to predict results) [Python Machine Learning (w3schools.com)](https://www.w3schools.com/python/python_ml_getting_started.asp)

[Python Machine Learning

Machine Learning Machine Learning is making the computer learn from studying data and statistics. Machine Learning is a step into the direction of artificial intelligence (AI). Machine Learning is a program that analyses data and learns to predict the outc

www.w3schools.com](https://www.w3schools.com/python/python_ml_getting_started.asp)

Types of Data:

- **Numerical**
- **Categorical**
- **Ordinal**

**Numerical** data: numbers

- Discrete Data
  - numbers that are limited to integers. Example: The number of cars passing by.
- Continuous Data
  - numbers that are of infinite value. Example: The price of an item, or the size of an item

**Categorical** data: non-comparable data. Values that cannot be measured up against each other. Example: a color value, or any yes/no values.

**Ordinal** data: relatively comparable data. Like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.

Knowing the data type allows us to understand how to analyze it.

---

- **Mean** - The average value
- **Median** - The mid point value
- **Mode** - The most common value

Example:

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

Results:

89.76923076923077

87.0

ModeResult(mode=array([86]), count=array([3]))

9.258292301032677

---

**Standard Deviation**

Definition: Determining how spread apart each value is from one another (based on the mean value)

Example is shown above
