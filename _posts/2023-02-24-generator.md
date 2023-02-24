---
layout: single  
title:  "yield 키워드와 generator"
categories: Python
tag: []
# toc: true
# toc_sticky: true
author_profile: false
search: true
use_math: true
---
<br/>

## ***Generator is called as 'lazy iterator'***

**yield 키워드를 사용하며, 여러 개의 데이터를 미리 만들어 놓지 않고 필요할 때마다 하나씩 만들어낼 수 있는 객체**

**메모리에 한 번에 올리기 부담스러운 대용량 파일을 읽거나, 스트림 데이터를 처리할 때 유용**

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