---
layout: single  
title:  "RuntimeError 정리"
categories: Python
tag: [Error]
# toc: true
# toc_sticky: true
author_profile: false
search: true
use_math: true
---

## 1. RuntimeError: dictionary changed size during iteration

반목문안에서 dic이나 list 사이즈가 바뀌면 발생하는 에러이다.

**<span style="color:dodgerblue">다만, del dic[key] 다음에 break 하는 경우는 발생하지 않는다.</span>**

```python
number = "4177252841"
k = 3

n = len(number)- k
answer = ''
limit = 0
dic = {}
for i, j in enumerate(number):
    dic[i] = int(j)

dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))

while n != 0:
    for key, value in dic.items():
        if key < limit:
            del dic[key]     # 에러 발생
            continue
        
        if (len(number)-key >= n):
            answer += str(value)
            limit = key
            
            n -= 1
            del dic[key]    # 에러 발생하지 않음
            break
                    
print(answer)
```