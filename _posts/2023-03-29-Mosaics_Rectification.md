---
layout: single  
title:  "(5) Mosaics and Rectification"
categories: Computer_Vision
tag: [Image Processing]
toc: true
toc_sticky: true
author_profile: false
search: true
use_math: true
---

### 각 veiw point의 이미지를 합쳐서 한 장의 파노라마 사진을 만들려면 어떻게 어떻게 해야할까요? <span style='background-color:#F7DDBE'>Mosaic</span>을 하면 됩니다.
#### 두 이미지간의 매칭되는 <span style="color:#ff0000">특징점(keypoint)</span>으로 <span style="color:#ff0000">homography matrix</span>을 구한 후, 이를 통해 <span style="color:#ff0000">warping</span> 한 후 이미지를 이어붙이면 됩니다.     

### 또한, 이미지 속 물체가 정면을 보도록 warping 하는 것을 <span style='background-color:#F7DDBE'>Rectification</span> 이라고 합니다.    

### 1. Keypoint 와 homography matrix

이미지의 특징이 되는 점을 특징점(keypoint)이라고 합니다. **<u>특징점은 보통 물체의 모서리나 코너</u>**입니다. 

따라서 대부분의 특징점 검출 알고리즘은 코너 검출을 바탕으로 합니다. 대표적으로 해리스 코너 검출(Harris Corner Detection), 이에 affine 변화까지 고려한 시-토마시 검출(Shi & Tomasi Detection), 그리고 DoG를 통해 스케일까지 고려한 SIFT-DoG 등이 있습니다.  

(1) 우선 여기서는 특징점을 직접 지정해보겠습니다. 
<img src="/assets/images/2023-03-29-warping/keypoint.png" alt="이미지 특징점"/>

(2) 이미지를 warping하기 위해서는 3차원 변환행렬인 Homography 행렬이 필요합니다.  

두 이미지의 대응되는 특징점의 좌표를 가지고
$$\begin{bmatrix}-5.53723803e-01&-7.57213921e-02&2.86499527e+02\\  
1.85636315e-01&-2.44602262e-01&4.63977743e+01\\ 
-4.78748251e-04&1.53204801e-03&3.74904029e-01\\ \end{bmatrix}$$

<!-- <img src="/assets/images/2023-03-29-Mosaics_Rectification/keypoint.png" alt="이미지 특징점" style="zoom:100%;" /> <br/> -->
<!-- https://staff.fnwi.uva.nl/r.vandenboomgaard/IPCV20162017/20162017/LabExercises/Lab_ImageMosaic.html -->

<!-- https://hygenie-studynote.tistory.com/52 -->


## 2. 투시변환행렬 반환
<!-- https://deep-learning-study.tistory.com/200 -->