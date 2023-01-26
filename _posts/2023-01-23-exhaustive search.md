---
layout: single  
title:  "완전탐색"
categories: Algorithm
tag: [set, map, 에라토스테네스체, join]
# toc: true
# toc_sticky: true
author_profile: false
search: true
use_math: true
---
<br/>

**가능한 모든 상황 조사**

<br/>

## 1. 소수(prime number) 찾기

(1) 나의 풀이

소수 특성 : 제곱근 이하의 숫자들을 나누었을 때 0으로 떨어지는 경우가 없을 때, 소수이다.

```python
from itertools import permutations
import math

def solution(numbers):
    answer = 0
    cand = set()
    root = 0
    n = len(numbers)

    temp = ''
    for i in range(n):
        temp += '0'
    if temp == numbers:
        return 0

    # 일의 자리
    prime = [2,3,5,7]
    one = set(numbers)
    for i in one:
        if int(i) in prime:
            answer += 1

    # 2이상
    for k in range(2,n+1):
        permu = list(permutations(numbers, k))
        for i in range(len(permu)):
            temp = ''
            for j in range(k):
                if permu[i][0] == '0':
                    break
                temp += permu[i][j]
            if temp != '':
                cand.add(int(temp))

    for num in cand:
        root = math.sqrt(num)
        check = 'true'
        for j in range(2, math.floor(root)+1):
            if num % j == 0:
                check = 'fail'
                break
        if check == 'true':
            answer += 1

    return answer
```
<br/>

(2) 모범답안 : 에라토스테네스 체

- map 함수 : map(함수, 적용할 자료형)

- join 함수 : 매개변수 리스트 요소를 합쳐서 하나의 문자열로 반환

```python
from itertools import permutations
def solution(numbers):
    a = set()
    # 에라토스테네스체 채우기
    for k in range(len(numbers)):
        a |= map(int, map("".join, permutations(numbers, k+1)))
    a -= set(range(0,2))

    # 에라토스테네스체 빼기
    for i in range(2, int(max(a)**0.5)+1):
        a -= set(range(i*2, max(a)+1, i))
    
    return len(a)
```