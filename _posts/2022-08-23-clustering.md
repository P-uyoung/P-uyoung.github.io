---
layout: single  # single, 댓글기능을 달기 위해...
title:  "PCA 와 K-means Clustering 의 관계"
categories: ML
tag: [python, jekyll]
toc: true
author_profile: false
search: true
---



보통, k-means clustering 전에 노이즈 감소를 위해 PCA (principal component analysis)를 적용한다. 

 **So k-means can be seen as a super-sparse PCA.**



## (1) Projection (투영) / PCA

#### -개념



<img src="../images/2022-08-23-clustering/projection.jpg" alt="projection" style="zoom: 50%;" />
$$
\vec{e}^*=arg max_\vec{e}Var(M\vec{e})
$$
Projection 시, **데이터set인 M**을 가장 잘 설명하는 (데이터가 골고루 분산되도록 하는)  **vector(axis) e** 를 찾고자 한다.

왜냐하면 데이터의 차원 축소 시 정보 손실을 최소화 하기 위해서이다.

다시 말해, *Var(Me)* 분산식 을 최대로 하는 *eigen vector e* 를 찾고자 한다. 



**분산식은 *공분산 행렬 $\sum$*  로 나타낼 수 있으며, 분산식은 곧 *eigen value $\lambda$* 를 의미한다.**
$$
Var(M\vec{e})=\vec{e}^T \Sigma  \vec{e}=\lambda
$$
이는 다음과 같은 풀이과정으로 도출된다.
$$
Var(M\vec{e})={\operatorname{1}\over\operatorname{N}}\sum_{i=1}^N(M\vec{e}-E(M\vec{e}))^2\\
Var(M\vec{e})={\operatorname{1}\over\operatorname{N}}\sum_{i=1}^N(M\vec{e})^2 \quad   s.t. E(M\vec{e})=0\\
Var(M\vec{e})={\operatorname{1}\over\operatorname{N}}\sum_{i=1}^N(M\vec{e})(M\vec{e})={\operatorname{1}\over\operatorname{N}}\sum_{i=1}^N(M\vec{e})(M\vec{e})  \quad  (Bassel's correction)\\
Var(M\vec{e})={\operatorname{1}\over\operatorname{N}}\vec{e}^TM^TM\vec{e}
=\vec{e}^T{\operatorname{M^TM}\over\operatorname{N}}\vec{e}=\vec{e}^T\sum\vec{e}=\vec{e}^T\lambda\vec{e}=\lambda
$$

**Principal projection vector (axis) 는 eigenvector e 이다. 이때의 분산이 eigen-value $ \lambda\ $이며, 이는 데이터가 얼마나 spread 되어있는지를 의미한다.**





#### -코드

코드로 보면 다음과 같다.

```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

x= np.random.normal(scale=8, size=200)
y= x+np.random.normal(scale=3, size=200)

x= x-np.mean(x)
y= y-np.mean(y)
data= np.array([x,y])

plt.figure()
plt.scatter(x,y)
plt.show()
```

![image-20220823174936356](../images/2022-08-23-clustering/image-20220823174936356.png)

```python
from sklearn.decomposition import PCA
pca = PCA()
pca.fit(data.T)
print(pca.components_.T)

#[[ 0.69246889  0.72144774]
#[ 0.72144774 -0.69246889]]
```

pca.components는 feature space 상에서, principal vectors를 의미한다. 

이는 <u>데이터의 분산이 최대</u>가 되도록 하는 방향을 의미한다. (이 경우는, $ \lambda$ 11.11)

해당 component는 explain_variance에 의한 순서이다.

<span style="color:green">음수에 대해서는 조금 더 생각해보기</span>

```python
np.sqrt(pca.explained_variance_)

#array([11.11412819,  2.05445079])
```

```python
any_num = 3     # 대각선 길이
sigma3_evalue= any_num*np.sqrt(pca.explained_variance_[0])
sigma3_evalue_arr= np.array([[-sigma3_evalue, sigma3_evalue]])
eigenvector = np.array([pca.components_[0]]).T
evector_x, evector_y = np.dot(eigenvector, sigma3_evalue_arr)

plt.figure()
plt.scatter(x,y)
plt.plot(evector_x, evector_y)
plt.show()
```

![image-20220823175153357](../images/2022-08-23-clustering/image-20220823175153357.png)







## (2) K-means clustering

## (3) Relation between PCA and K-means

+50



It is true that K-means clustering and PCA appear to have very different goals and at first sight do not seem to be related. However, as explained in the Ding & He 2004 paper [K-means Clustering via Principal Component Analysis](http://ranger.uta.edu/~chqding/papers/KmeansPCA1.pdf), there is a deep connection between them.

The intuition is that PCA seeks to represent all nn data vectors as linear combinations of a small number of eigenvectors, and does it to minimize the mean-squared reconstruction error. In contrast, K-means seeks to represent all nn data vectors via small number of cluster centroids, i.e. to represent them as linear combinations of a small number of cluster centroid vectors where linear combination weights must be all zero except for the single 11. This is also done to minimize the mean-squared reconstruction error.







참조

<https://stats.stackexchange.com/questions/183236/what-is-the-relation-between-k-means-clustering-and-pca>

[]