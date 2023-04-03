---
layout: single  
title:  "[CV] 6. optical flow (LKtracking)"
categories: CV
tag: [Image Processing]
toc: true
toc_sticky: false
author_profile: false
search: true
use_math: true
---

## 결론
<br/>

밝기(intensity)변화는 `optical flow` 를 의미하고, `3-D velocity vector (u,v)`, optical flow는 물체의 움직임으로 가정할 수 있다.   
(물론, `motion field` 가 곧 optical field는 아니다. 구체 회전과 광원 이동의 경우 다르다.) (이때, motion field는 모션 벡터로 얻어낸 2차원 motion map을 의미한다.)

Optical flow는 (1) color constancy, (2) small motion 조건하에 (u,v) 일차식을 얻을 수 있다. (즉, 하나의 해는 얻을 수 없다.) 이때, (3) Area-based method (지역적 연산) 조건을 추가하여 Lukas Kanade 기법으로 각 픽셀 당 단 하나의 `(u,v)` 를 구할 수 있다.
<br/>

## 1. Optical flow

## 2. Lukas kanade (LK) method

