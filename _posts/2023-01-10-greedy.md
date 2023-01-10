---
layout: single  
title:  "Greedy Algorithm"
categories: Algorithm
tag: [Queu]
# toc: true
# toc_sticky: true
author_profile: false
search: true
use_math: true
---
<br/>

**부분적인 최적해가 전체적인 최적해가 되는 경우**

<br/>

## 1. 두 큐 합 같게 하기 (카카오_2020_level2)
큐와 포인터 2개

```python
def solution(queue1, queue2):
    queue_sum = (sum(queue1) + sum(queue2))
    
    if queue_sum%2 == 1:
        return -1
    
    target = queue_sum/2
    cur = sum(queue1)
    
    que3 = queue1 + queue2
    end = len(queue1)-1
    start = 0
    
    answer = 0
    
    while cur != target:
        if cur < target:
            end += 1
            
            if end == len(que3):
                return -1
            
            cur += que3[end]
            
        else:
            cur -= que3[start]
            start += 1
        answer += 1
    return answer
```
<br/>

## 2. 조이스틱 최소작동 (프로그래머스_level2)
A가 아닌 글자간의 최소 거리 (각 인덱스 마다)

시작점이 0 인덱스이므로, idx는 거리를 의미하게 된다.

```python
def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(chr):
        num_char = [i for i in range(14)] + [j for j in range(12,0,-1)]
        return num_char[ord(chr)-ord('A')]
    
    for ch in name:
        answer += alphabet_to_num(ch)   # letter_cost

    move = n-1
    for idx in range(n):
        next_id = idx + 1
        while (next_id < n) and (name[next_idx]=='A'):
            next_id += 1
        distance = min(idx, n-next_idx)         # 왼쪽 오른쪽 중 더 짧은 거리
        each = idx + (n-next_idx) + distance    # 각 idx마다 움직인 총 거리
        move = min(move, each)          # move_cost

    answer += move
    return answer
```
