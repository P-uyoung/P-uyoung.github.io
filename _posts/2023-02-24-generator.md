---
layout: single  
title:  "제너레이터 (43163 단어 변환)"
categories: Coding_Test
# tag: [단어 변환]
toc: true
toc_sticky: true
author_profile: false
search: true
use_math: true
---
## ***Generator is called as 'lazy iterator'***

**yield 키워드를 사용하며, 여러 개의 데이터를 미리 만들어 놓지 않고 필요할 때마다 하나씩 만들어낼 수 있는 객체**

**메모리에 한 번에 올리기 부담스러운 대용량 파일을 읽거나, 스트림 데이터를 처리할 때 유용**

<span style="color:blue">**-리스트 return이랑 같아보이지만, 아래와 같은 차이가 있다.**</span>

```python
import time 

def return_abc():
    abc = []
    for c in 'abc':
        time.sleep(1)
        abc.append(c)
    return abc

def yield_abc():
    for c in 'abc':
        time.sleep(1)
        yeild c
```

```python
for r in return_abc():
  print(r) 

# after 3 minutes
# a
# b
# c

for r in yield_abc():
  print(r)

# after 1 minute
# a
# after 1 minute
# b
# after 1 minute
# c
```

**- Generator Comprehension**

list comprehension과 같은데, 단지 '대괄호'가 아니라 '소괄호'를 사용한다는 점이 다르다.

```python
abc = (c for i in 'abc')

print(abc) # <generator object <genexpr> at 0x7f2dab21ff90>
```
<br/>


## 코테 문제

### [1. 단어 변환 (level3)](https://school.programmers.co.kr/learn/courses/30/lessons/43163)

**-자료구조 : Generator, Dictionary**

**-zip() 함수를 사용하여, 두 문자열 비교**

**visited가 아닌, dist 개념으로 풂**

```python
def get_next(cur, words):
    for nxt in words:
        count = 0
        for c, n in zip(cur, nxt):
            if c != n:
                count += 1
            if count > 1:
                break
        if count == 1:
            yield nxt

def solution(begin, target, words):
    dist = {begin:0}
    q = []
    q.append(begin)

    while q:
        cur = q.pop(0)

        for nxt in get_next(cur, words):
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist.get(target, 0)
```
<br/>