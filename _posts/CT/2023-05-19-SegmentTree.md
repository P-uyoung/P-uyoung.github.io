---
layout: single  
title:  "(15) Segment Tree"
categories: 코테
tag: [Segment Tree, 구분합]
toc: true
toc_sticky: true
author_profile: false
search: true
use_math: true
header:
#   overlay_image: /assets/images/teaser/CT.webp
#   overlay_filter: 0.5
  teaser: /assets/images/teaser/CT.webp
---

구분합/곱, 최솟값과 최댓값 구하기 문제에서 사용할 수 있는 알고리즘입니다.

세그먼트 트리는 특정 범위에 대한 연산 결과를 빠르게 찾을 수 있도록 도와주는 자료구조(알고리즘)입니다.  

<u>범위 밖의 값은 연산에 포함되지 않습니다.</u>

세그먼트 트리는 주어진 범위 내에서 여러 번의 쿼리를 처리할 때 효율적입니다. 시간 복잡도는 Tree의 높이인 O(logN)입니다.

따라서 시간제약이 10^6이 되면? 이진탐색과 함께 고려해봐야 합니다!


### 코테 문제 

#### 🍓 [1. BOJ 2042 구분합](https://www.acmicpc.net/problem/2042)

인덱스는 1에서부터 시작!

1. query

특정범위에 연산결과를 빠르게 찾는 함수 부분

<img src="/assets/images/2023-05-19-SegmentTree/query.png" alt="쿼리"/> <br/>
[참고 블로그](https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%84%B8%EA%B7%B8%EB%A8%BC%ED%8A%B8-%ED%8A%B8%EB%A6%AC-Segment-Tree)


2. update

세그먼트 트리 update 함수 부분

```python
import sys
# sys.setrecursionlimit(10**7)

## 0. 입력받기
N, M, K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

# 완전이진트리 높이 : lb(N)
# 완전이진트리의 노드, 개수 : 2^(lb(N)+1)-1
# 세그먼트트리 높이 : ceil(lb(N))   (2의 거듭제곱이 아닌 경우도 고려해야 함.)
# 세그먼트트리의 노드 개수 : 2^(ceil(lb(N))+1)-1
tree = [0]*(N*4)

## 1. 트리 Setting
# start, end :  arr의 인덱스
# idx : tree의 인덱스
def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start-1]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    return tree[idx]

## 2. 쿼리 수행
def query(start, end, idx, left, right):
    # 범위 밖일 때,
    if start > right or end < left:
        return 0
    # 찾으려는 범위 left와 right가 segment tree 노드안에 구현되어 있을 때,
    if start >= left and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return query(start, mid, idx*2, left, right) + query(mid+1, end, idx*2+1, left, right)

# what : 수정할 인덱스, value : 수정할 값
def update(start, end, idx, what, value):
    if what < start or what > end:
        return
    tree[idx] += value
    if start == end:
        return
    mid = (start + end) //2
    update(start, mid, idx*2, what, value)
    update(mid+1, end, idx*2+1, what, value)

init(1, N, 1)

for _ in range(M+K):
    a,b,c = map(int, sys.stdin.readline().split())
    if a == 1:
        diff = c - arr[b-1]
        update(1, N, 1, b, diff)
        arr[b-1] = c
    elif a == 2:
        print(query(1, N, 1, b, c))
```