---
layout: single  
title:  "np.concatenate(axis)"
categories: Python
tag: [API]
# toc: true
# toc_sticky: true
author_profile: false
search: true
use_math: true
---

### np.concatenate의 axis=-1(default), 0, 1
<br/>

(1) axis = -1 : Line up <br/>


```python
a = np.array([1,2])
b = np.array([[1, 2], [3, 4]])
c = np.array([5,6])

np.concatenate((a,c), axis=-1)
# array([1, 2, 5, 6])

np.concatenate((b,c), axis=-1)
# ValueError: all the input array dimensions for the concatenation axis must match exactly
```
<br/>

(2) axis = 0 : (when same dimension) Line up  or (when different dimensions) Add as rows <br/>


```python
np.concatenate((a,c), axis=0)
# array([1, 2, 5, 6])

np.concatenate((b,c), axis=0)
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
```

<br/>

(3) axis = 1 : Add as columns <br/>


```python
np.concatenate((a,b.T), axis=1)

# [[1, 2, 5],
#  [3, 4, 6]]
```
