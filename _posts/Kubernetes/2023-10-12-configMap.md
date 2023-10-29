---
layout: single  
categories: Kubernetes
title: "[K8S] 오브젝트 기초 - ConfigMap, Secret"
toc: true
toc_sticky: true
tag: [Kubernetes]
author_profile: false
search: true
header:
  teaser: /assets/images/teaser/kubernetes.png
---

Env(Literal, File), Mount(File)
<img src="/assets/images/2023-10-12-k8s/summary.jpg" /><br/>

## ConfigMap과 Secret 의 필요성

개발환경에서 일반접근을 하다가, 상용환경으로 배포한다면 보안접속으로 설정을 하고 user와 key값도 변해야한다.

user와 key값은 컨테이너 이미지에 들어있는 값이기 때문에 이 부분을 변경한다는 것은,    
**<u>개발환경과 상용환경의 컨테이너 이미지를 각각 관리하겠다는</u>** 의미이다.

이 값 몇 개 때문에 큰 용량의 이미지를 별도로 관리하는 것은 효율적이지 못하다.

<img src="/assets/images/2023-10-12-k8s/필요성.png" /><br/>

이때, **<u><span style="color:#ff0000">환경에 따라 변하는 값들을 외부에서 결정할 수 있게 도와주는 오브젝트가</span> ConfigMap, Seceret이다.</u>**

이를 이용해서 이미지를 하나 만들어 놓으면, 개발환경과 상용환경에 사용할 수 있다.

configMap은 일반적인 설정 정보를, secret은 민감한 정보를 관리하는 데 사용한다. key-value 쌍으로 구성된다.

Pod 생성 시, 이 두 오브젝트를 연결할 수 있다.    
연결하면, container의 환경변수에 해당 데이터가 들어가게 된다.   
<br/>

## ConfigMap과 Secret 처리방식 비교

secret이 configMap과 다른 점은, **<u>value를 넣을 때 Base64 인코딩</u>**을 해서 만들어야한다.
pod의 환경변수로 연결될 때는 자동으로 decoding이 돼서 원래의 값으로 보여진다.


또한, **<u>secret은 민감한 정보가 디스크에 기록되지 않도록 memory에 저장</u>**된다.   
1. 생성 : Kubernetes 클러스터에서 configMap, secret 오브젝트를 생성    
2. 저장 : 이 오브젝트들을 kubernets DB(etcd)에 저장
3. 파일로 매핑 : 쿠버네티스는 configMap 또는 secret 오브젝트의 데이터를 파일로 매핑. 
이 매핑은 작업 노드의 파일 시스템에 일시적으로 저장된다. **<u><span style="color:#ff0000">Secret의 경우 인메모리 파일 시스템(tmpfs)에 저장</span></u>**될 수 있어 디스크에 민감한 데이터가 기록되지 않도록 보호된다.
4. Pod에 mount : 파일로 매핑된 데이터는 Pod의 볼륨으로 마운트되고, 애플리케이션 코드는 이 볼륨을 통해 데이터에 접근할 수 있다.

**<u>따라서, secret은 memory에 저장하기 때문에 너무 많이 만들게 되면 시스템 자원에 영향을 끼치므로 주의해야한다.</u>**   

---

### <span style="color:#ff0000">Tips: 쿠버네티스 아키텍처</span>

쿠버네티스 아키텍처는 크게 Master Node와 Worker Node로 구분되며, 이 두 부분이 합쳐져서 컨테이너화된 애플리케이션의 배포, 확장, 및 관리를 수행한다.

<img src="/assets/images/2023-10-12-k8s/architecture.png" width="450"/><br/>

- **Master Node (Control Plane)**: 
    - <u>API Server (kube-apiserver)</u>: 모든 쿠버네티스 클러스터의 통신 중심으로 사용자와 클러스터 간의 모든 상호 작용은 API 서버를 통해 처리한다.
    - <u>Controller Manager (kube-controller-manager)</u>: 클러스터의 상태를 관리하고, 예상된 상태와 현재 상태를 일치시키는 여러 컨트롤러를 실행한다.   
    - <u>Scheduler (kube-scheduler)</u>: Pod를 적절한 Worker Node에 배치하는 역할을 한다. 스케줄러는 리소스 가용성, 제약 조건, affinity, anti-affinity 등을 고려하여 결정한다.
    - <u>etcd</u>: 쿠버네티스의 중앙데이터베이스로 클러스터의 모든 구성 데이터를 저장하는 분산 키-값 저장소이다.    

- **Worker Node (컴퓨팅 작업을 수행하는 노드)**:
  - <u>Kubelet</u>: 각 Worker Node에서 실행되는 에이전트로, 해당 노드에서 실행되는 Pod의 상태를 모니터링하고 관리한다.   
  - <u>Kube Proxy (kube-proxy)</u>: 네트워크 프록시 및 로드 밸런싱을 제공하여 Pod 간의 네트워크 통신을 가능하게 한다.  
  - <u>Container Runtime</u>: 컨테이너를 실행하는 데 필요한 런타임으로, Docker, containerd, rkt 등이 있다.    
  - <u>Pods</u>: Pod는 하나 이상의 컨테이너와 그 컨테이너의 저장소 및 네트워크 리소스를 캡슐화합니다.    

  kubectl : Kubernetes CLI

---

**<u><span style="color:#ff0000">configMap과 Secret을 만들 때 데이터로 [상수, 파일]을 넣을 수 있다.<br>파일을 넣을 때는 환경변수로 세팅하는 것이 아닌 volume을 mount해서 사용할 수 있다.</span></u>**   


## [1] Env (Literal)

<img src="/assets/images/2023-10-12-k8s/literal.jpg" /><br/>

이는 key-value를 상수로 정의하고 환경변수에 넣는 방법이다.

### 실습

ConfigMap, Secret, Pod를 각각 만든다.

- **ConfigMap**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cm-dev
data:
  SSH: 'false'
  User: dev
```

- **Secret**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: sec-dev
data:
  Key: MTIzNA==
```
*Key: MTIzNA==* value에 Base64 인코딩이 들어가지 않으면 에러 발생한다.

- **Pod**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-1
spec:
  containers:
  - name: container
    image: kubetm/init
    envFrom:
    - configMapRef:
        name: cm-dev
    - secretRef:
        name: sec-dev
```

pod의 container에서 환경변수를 출력해보면 key-value값을 확인할 수 있다.   
이때, pod에서는 인코딩된 value값이 디코딩된 것도 확인할 수 있다.    

<img src="/assets/images/2023-10-12-k8s/dash1.png" /><br/>

---

## [2] Env (File)

<img src="/assets/images/2023-10-12-k8s/file_env.jpg" /><br/>

이는 파일을 환경변수에 넣는 방법이다.

file.txt 파일을 통으로 ConfigMap에 담을 수 있다. 파일명이 key이고, 파일내용이 value가 된다.


해당 명령은 텍스트 내용을 Base64 인코딩을 하기 때문에, 이미 텍스트 내용이 Base64인코딩이 되어있다면 두 번 인코딩 되는 경우를 유의해야 한다.

### 실습

대쉬보드에서 파일로 configMap을 만드는 것을 지원하지 않기 때문에 직접 master의 kubectl을 이용해서 두 오브젝트를 만들어보자.

- **ConfigMap**
```s
echo "Content" >> file-c.txt
kubectl create configmap cm-file --from-file=./file-c.txt
```

- **Secret**
```s
echo "Content" >> file-s.txt
kubectl create secret generic sec-file --from-file=./file-s.txt
```

- **Pod**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-file
spec:
  containers:
  - name: container
    image: kubetm/init
    env:
    - name: file-c
      valueFrom:
        configMapKeyRef:
          name: cm-file
          key: file-c.txt
    - name: file-s
      valueFrom:
        secretKeyRef:
          name: sec-file
          key: file-s.txt
```

pod의 container에 들어가서 환경변수에 configMap과 secret의 key-value가 들어있는 것을 확인할 수 있다.

<img src="/assets/images/2023-10-12-k8s/dash2.png" /><br/>


추가로, 대시보드에서 secret 데이터를 볼 수 있으므로 실제 업무에서는 보안상의 문제로 대시보드 안쓴다.

<img src="/assets/images/2023-10-12-k8s/dash3.png" width="350" /><br/>

---

## [3] Volume Mount (File)

<img src="/assets/images/2023-10-12-k8s/file_mount.jpg" /><br/>

파일을 ConfigMap에 담는 것까지 동일하고, pod를 만들 때 container 안에 mount path를 정의한다.

**<u><span style="color:#ff0000">환경변수 방식은 configMap의 데이터가 변해도 반영이 안된다.<br>파일 마운트는, 마운트라는 게 원본과 연결시켜준다는 개념이므로, configMap의 데이터가 변경되면 pod에 마운팅된 내용도 변한다.</span></u>**  


### 실습

앞에서 만든 파일 *file-c.txt, file-s.txt* 을 volume으로 mount 해보자.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-mount
spec:
  containers:
  - name: container
    image: kubetm/init
    volumeMounts:
    - name: file-volume
      mountPath: /mount
  volumes:
  - name: file-volume
    configMap:
      name: cm-file
```

container에서 mount path에 이동하여 확인해보니 volume으로 mount가 잘 되었다.

<img src="/assets/images/2023-10-12-k8s/dash4.png" /><br/>


**<u><span style="color:#ff0000">이때, configMap 파일의 내용이 변경되면 잘 변경이되는지도 확인하였다.</span></u>**  

<br/>

#### Tips

volumes는 기본적으로 configMap이건 secret건 하나의 아이템만 설정할 수 있다.    
함께 주입하고 싶으면  projected라는 속성을 사용해야한다.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-mount
spec:
  containers:
  - name: container
    image: kubetm/init
    volumeMounts:
    - name: file-volume
      mountPath: /mount
  volumes:
  - name: file-volume
    projected:
      sources:
      - configMap:
          name: cm-file
      - secret:
          name: sec-file
```
<br/>

*해당 게시글은 '[대세는 쿠버네티스 초중급편](https://www.inflearn.com/course/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EA%B8%B0%EC%B4%88?gad=1&gclid=CjwKCAjwvfmoBhAwEiwAG2tqzAD7E333fVc-gkDWnwIGPKATXtXbd3yC2CaV8GF4w-Ha70ouUlGIlRoCBlAQAvD_BwE)' 강의와 '컨테이너 인프라 환경 구축을 위한 쿠버네티스.도커_조훈' 도서를 바탕으로 작성하였습니다.*