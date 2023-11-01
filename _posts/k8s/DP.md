<!-- ---
layout: single  
categories: k8s
title: "[K8S] 오브젝트 기초 - Namespace"
toc: true
toc_sticky: true
tag: [k8s]
author_profile: false
search: true
header:
  teaser: /assets/images/teaser/kubernetes.png
--- -->

Namespace, ResourceQuota, LimitRange

<img src="/assets/images/2023-10-12-k8s/summary.jpg" /><br/>

<br/>

## 필요성

쿠버네티스 클러스터에서 사용할 수 있는 자원인 메모리와 CPU가 한정이 되어있다.

클러스터 안에는 여러 namespace를 만들 수 있고, 그 안에 여러 pod들을 만들 수 있다. 

각 pod는 필요한 자원을 클러스터의 자원을 공유해서 사용하는데 이때 특정 네임 스페이스나 pod에서 클러스터의 자원은 모두 사용해버리면 다른 pod 들은 자원을 사용하지 못하는 문제가 발생한다.

이러한 문제를 해결하기 위해서 ResourceQuota, LimitRange가 존재한다.

먼저, ResourceQuota는 nameSpace의 최대한계를 설정하여 pod가 사용하는 자원이 이 한계를 넘을 수 없다.    
Pod 입장에서는 자원이 부족해서 문제가 될지언정 다른 nameSpace안의 pode들에게는 영향을 끼치지 않는다.

또한, 한 pod가 nameSpace의 최대한계를 다 써버리면 다른 pod들이 해당 nameSpace에 더 이상 들어올 수 없게 된다. 

LimitRange는 이를 막기 위해 limitRange lense를 둬서 nameSpace에 들어오는 pod의 크기를 제한한다.

**<u> </u>**   

#### <span style="color:#ff0000"> </span>

---

## [1] 

<img src="/assets/images/2023-10-13-k8s/img1.jpg" /><br/>
-

### 실습

-

```yaml

```


```yaml

```


```yaml

```



---

## [2] 

<img src="/assets/images/2023-10-13-k8s/img2.jpg" /><br/>

-

### 실습

-

```yaml

```


```yaml

```


```yaml

```



---

## [3] 

<img src="/assets/images/2023-10-13-k8s/img3.jpg" /><br/>

-

### 실습

-

```yaml

```


```yaml

```


```yaml

```

<br/>

*해당 게시글은 '[대세는 쿠버네티스 초중급편](https://www.inflearn.com/course/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EA%B8%B0%EC%B4%88?gad=1&gclid=CjwKCAjwvfmoBhAwEiwAG2tqzAD7E333fVc-gkDWnwIGPKATXtXbd3yC2CaV8GF4w-Ha70ouUlGIlRoCBlAQAvD_BwE)' 강의와 '컨테이너 인프라 환경 구축을 위한 쿠버네티스.도커_조훈' 도서를 바탕으로 작성하였습니다.*