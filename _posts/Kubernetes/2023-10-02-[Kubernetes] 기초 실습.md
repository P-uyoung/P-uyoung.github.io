---
layout: single  
categories: MLOps
toc: true
toc_sticky: true
tag: [Kubernetes]
author_profile: false
search: true
header:
  teaser: /assets/images/teaser/Kubernetes.webp
---

## [1] Kubernetes Cluster 설치

<img src="/assets/images/2023-10-02-Kubernetes/installation_process.png" /><br/>

### 네트워크 구성

인터넷과 연결된 **<span style="color:#ff0000">공유기</span>** 에서 IP (192.168.0.20) 를 Physical Server가 할당받음. **<span style="color:#ff0000">(physical port)</span>**

vm(node)의 가상 네트워크가 physical port를 통해서 공유기에서 직접 IP를 할당받을 수 있음.

내 PC에서 master나 노드에 연결을 시도하면, 해당 트래픽은 공유기를 거쳐 다시 PC의 브릿지 연결을 통해 **<span style="color:#ff0000">vm의 IP</span>** 로 연결이 됨.

<img src="/assets/images/2023-10-02-Kubernetes/network.jpg" /><br/>

### vagrant 명령어

- vagrant up : 가상머신 기동 (최초에는 스크립트가 실행, 그 다음에는 vm만 기동)

- vagrant halt : 가상머신 Shutdown (vm 모두 내려감)

- vagrant ssh : 가상머신 접속 (직접 원격접속툴의 역할을 함) (ex. vargrant ssh k8s-master)

- vagrant destroy : 가상머신 삭제 (virtualBox로 설치된 모든 vm 삭제)
<br/>
<br/>

### Xshell

#### 1. master노드와 worker노드 등록

master 호스트 : 192.168.56.30

worker1 호스트 : 192.168.56.31

worker2 호스트 : 192.168.56.32

#### 2. Worker Node 연결

1. VM의 쿠버네티스 master로 접속

2. cat ~/join.sh 명령으로 자신의 master 접근 token 확인 및 복사

    ```s
    [root@k8s-master ~]# cat ~/join.sh
    ```

3. worker node 1, 2 각각에 접속 후 토큰 붙여넣기

#### 3. Kubernetes Cluster 설치완료 확인

```s
[root@k8s-master ~]# kubectl get pod -A
[root@k8s-master ~]# kubectl get nodes
```
모두 running으로 뜨고, 세 개의 노드가 보임.

<img src="/assets/images/2023-10-02-Kubernetes/Xshell.png" /><br/>


#### 4. 대시보드 접근 가능

<link>http://192.168.56.30:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/workloads?namespace=default</link>

단, Master Node 재기동 시 Dashboard에 접속하기 위해선 아래 명령어를 실행해서 Proxy 오픈하기

```s
[root@k8s-master ~]# nohup kubectl proxy --port=8001 --address=192.168.56.30 --accept-hosts='^*$' >/dev/null 2>&1 &
```

<br/>

*해당 게시글은 [대세는 쿠버네티스 초중급편](https://www.inflearn.com/course/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EA%B8%B0%EC%B4%88?gad=1&gclid=CjwKCAjwvfmoBhAwEiwAG2tqzAD7E333fVc-gkDWnwIGPKATXtXbd3yC2CaV8GF4w-Ha70ouUlGIlRoCBlAQAvD_BwE) 를 바탕으로 작성하였습니다.*