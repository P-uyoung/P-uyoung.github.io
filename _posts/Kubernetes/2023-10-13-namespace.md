---
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
---

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
LimitRanges는 클러스터에도 설정할 수 있다.

<!-- **<u> </u>**   

#### <span style="color:#ff0000"> </span> -->

---

각 오브젝트의 기능을  살펴보자.
<br/>

## [1] NameSpace

Cluster 안에 Node, Node안에 Pod 이렇게 공부했는데 NameSpace는 어떤 것들의 집합일까? 

<img src="/assets/images/2023-10-13-k8s/namespace.png" /><br/>

쿠버네티스에서, nameSpace 는 단일 클러스터 내에서의 리소스 그룹 격리 메커니즘을 제공한다. 

(1) 리소스의 이름은 nameSpace 내에서 유일해야 하며, nameSpace 간에서 유일할 필요는 없다. 

(2) nameSpace 기반 스코핑은 nameSpace 기반 오브젝트 (예: 디플로이먼트, 서비스 등) 에만 적용 가능하며 클러스터 범위의 오브젝트 (예: 스토리지클래스, 노드, 퍼시스턴트볼륨 등) 에는 적용 불가능하다.


### 특징 (1): 같은 타입의 오브젝트명은 유일해야 한다.

한 nameSpace 안에는 같은 type의 오브젝트들은 이름이 중복될 수 없다.   
오브젝트마다 별도의 UUID가 존재하지만, 한 nameSpace 안에서는 같은 종류의 오브젝트라면 이름 또한 UUID 같이 유일한 키 역할을 할 수 있는 셈이다.

### 특징 (2): 다른 nameSpace간에는 pod와 service 연결이 불가능하다.

Pod와 Service와 연결할 때, pod에는 label을 달고 service에는 selector를 달아서 연결한다.

하지만, 다른 nameSpace간에는 이러한 연결이 불가능하다.    
(물론 node나 persistence volume과 같이 모든 nameSpace에서 공용으로 사용되는 오브젝트도 있긴하다.)


### 추가 특징

Pod마다 IP를 가지고 있는데, **pod에서 다른 pod의 IP로 접근한다면 어떻게 될까?** 기본적으로 이러한 연결을 허용하지 않지만 이는 **network policy 오브젝트** 를 통해서 허용될 수 있다.

**또한, nameSpace를 지우게 되면 그 안에 있는 자원들도 모두 지워지므로 이를 유의해야한다.**    

<br/>

NameSpace의 특징을 정리한 그림은 아래와 같다.

<img src="/assets/images/2023-10-13-k8s/img1.png" /><br/>

### 실습

nameSpace1에 pod와 service를 만든다.

- nameSpace1
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: nm-1
```

- pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-1
  namespace: nm-1
  labels:
    app: pod
spec:
  containers:
  - name: container
    image: kubetm/app
    ports:
    - containerPort: 8080
```

- service 

```yaml
apiVersion: v1
kind: Service
metadata:
  name: svc-1
  namespace: nm-1
spec:
  selector:
    app: pod
  ports:
  - port: 9000
    targetPort: 8080
```

nameSpace2에 pod와 service를 만든다.

- nameSpace
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: nm-2
```
- pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-1
  namespace: nm-2
  labels:
    app: pod
spec:
  containers:
  - name: container
    image: kubetm/init
    ports:
    - containerPort: 8080
```


---

## [2] ResourceQuota

ResourceQuota는 nameSpace에 제한하고 싶은 자원을 명시하는 오브젝트이다.

주의해야할 점이 있다.

ResourceQuota가 지정되어 있는 nameSpace에 pod를 만들때 pod는 해당 스펙을 명시해야한다.

또한, 현재 남은 request 자원보다 높은 request 자원을 원하는 pod를 만들 수 없다.

<img src="/assets/images/2023-10-13-k8s/img2.jpg" /><br/>

CPU와 메모리 이외에도 제한할 수 있는 자원은 아래의 표와 같다.

|자원|종류|
|-----|----------|
|**Computer ReSource**| CPU, memory, storage|
|**Object Count**|pod, service, configMap, PVC,...|

<small>쿠버네티스 버전이 업데이트되면서 제한할 수 있는 오브젝트 숫자가 늘어나고 있다. 따라서, 오브젝트를 제한할 때는 사용하는 쿠버네티스 버전에서는 어느 오브젝트까지 제한하는지 확인해봐야한다.</small>

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

## [3] LimitRange

LimitRange는 각각의 pod마다 nameSapce에 들어올 수 있는지 자원을 체크해준다.

체크하는 항목은 min, max, maxLimitRequestRatio 값이 있다.

추가로 defaultReqeust, default 항목이 있다.   
앞서 말했듯, nameSpace에 pod를 만들 때 pod에 해당 스펙을 명시하지 않으면 안되었는데,   
두 항목을 설정해 놓으면 pod에 자동으로 request와 limits 값이 명시된 값으로 할당된다.

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

---

**Tips**  

Pod의 requests와 limits는 쿠버네티스에서 리소스 관리를 위해 사용되는 설정이다.

- **Request 메모리** : pod가 실행되기 위해 필요한 최소 메모리 양을 지정

- **Limits 메모리** : pod가 사용할 수 있는 최대 메모리 양을 지정
---

**REF.**

- [대세는 쿠버네티스 초중급편 강의](https://www.inflearn.com/course/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EA%B8%B0%EC%B4%88?gad=1&gclid=CjwKCAjwvfmoBhAwEiwAG2tqzAD7E333fVc-gkDWnwIGPKATXtXbd3yC2CaV8GF4w-Ha70ouUlGIlRoCBlAQAvD_BwE)

- [쿠버네티스 Documents](https://kubernetes.io/ko/docs/concepts/overview/working-with-objects/namespaces/)
