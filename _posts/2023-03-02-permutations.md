---
layout: single  
title:  "순열 및 조합"
categories: Python
tag: [Permutation, Combination, 타겟 넘버]
toc: true
toc_sticky: true
author_profile: false
search: true
use_math: true
---
<br/>

## 순열, 조합

```python
from itertools import permutations, combinations, product, combinations_with_replacement

# (1) 순열(permutations)
a = list(permutations(['A', 'B', 'C'], 2))
print(a)    # nPr, [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# (2) 조합(combinations)
a = list(combinations(['A','B','C'], 2))
print(a)    # nCr, [('A', 'B'), ('A', 'C'), ('B', 'C')]

# (3) 중복순열(product)
a = list(product(['A','B','C'], repeat=4))
print(a)    # nPr

# (4) 중복조합(combinations_with_replacement)
a = list(combinations_with_replacement(['A','B','C'], 2))
print(a)    # nHr
```


## 코테 문제

### [1. 타겟 넘버 (프로그래머스_level2)](https://school.programmers.co.kr/learn/courses/30/lessons/43165)

**(1) 중복순열**

```python
import copy
from itertools import product

def solution(numbers, target):
    arr = list(product([1,-1], repeat=len(numbers)))
    result = []
    for i in range(len(arr)):
        result.append(sum([x*y for x,y in zip(numbers, arr[i])]))

    return result.count(target)
```
<br/>

