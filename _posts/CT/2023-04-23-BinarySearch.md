---
layout: single  
title:  "(14) BinarySearch"
categories: Coding_Test
tag: [Binary Search]
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

이분탐색의 시간복잡도는 O(logN)입니다.   

### middle을 업데이트하면서 target값 찾기

<img src="/assets/images/2023-04-23-BinarySearch/1.png" alt="1" style="zoom:50%;" />

mid값이 아니므로, left와 rigth는 mid의 +-1로 업데이트합니다. 

<img src="/assets/images/2023-04-23-BinarySearch/2.png" alt="2" style="zoom:50%;" />

<img src="/assets/images/2023-04-23-BinarySearch/3.png" alt="3" style="zoom:50%;" />


### 코테 문제 

#### 🍓 [1. Binary Search](https://leetcode.com/problems/binary-search/)

- 문제 상황 : 오름차순으로 정렬된 배열에서 target값을 찾아야 합니다.   

- 제한 사항 : 알고리즘은 반드시 O(logn) 이어야 합니다.  

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        # 예외처리
        if len(nums) ==1:
            if nums[0] == target:
                return 0
            else:
                return -1        
        
        while (left <= right):
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
```
