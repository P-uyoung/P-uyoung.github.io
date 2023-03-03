---
layout: single  
title:  "[Python] RuntimeError"
categories: Python
# tag: [Error]
# toc: true
# toc_sticky: true
author_profile: false
search: true
use_math: true
---

## 1. RuntimeError: dictionary changed size during iteration

반목문안에서 dic이나 list 사이즈가 바뀌면 발생하는 에러이다.

**<span style="color:dodgerblue">다만, break 하여 for문에서 나갈 경우는 발생하지 않는다.</span>**

```python
def solution(number, k):
    n = len(number)- k
    answer = ''
    limit = -1
    dic = {}
    for i, j in enumerate(number):
        dic[i] = int(j)

    dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))

    while n != 0:
        for key, value in dic.items():
            if key < limit:
                del dic[key]        # 에러 발생
                continue
                
            if (len(number)-key >= n):
                answer += str(value)
                limit = key
                n -= 1
                
                del dic[key]        # 에러 발생하지 않음
                break
                
    return answer
```