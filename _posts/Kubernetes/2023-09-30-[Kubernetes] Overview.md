---
layout: single  
categories: MLOps
toc: true
toc_sticky: true
author_profile: false
search: true
header:
  teaser: /assets/images/teaser/Kubernetes.webp
---

## 쿠버네티스의 필요성

대규모 서비스를 운영할 때, 서버자원을 효율적으로 사용하기 위해  **<span style="color:#ff0000">가상화 기술</span>** 이 필요함.

### 1) 가상화 기술

<img src="/assets/images/2023-09-30-Kubernetes/overview.png" /><br/>

| 가상화 기술 | 특 징 | 단 점 |
|------|-------------|--------|
| 리눅스의 자원격리기술 | 프로세스(서비스)간 자원을 독립적으로 | 사용성이 떨어짐 (어려움) |
| VM 가상화기술 | 자동화 가능 | 시스템 효율이 떨어짐 (무거운 OS를 띄어야 함) |
| Container 가상화기술 | 서비스간 자원격리에 별도의 OS 필요없음 (빠르고 효율적임) | 개별의 서비스에 컨테이너로 가상화시켜 배포함. 따라서, 여러 서비스를 운영할 때 **<span style="color:#ff0000">컨테이너 오케스트레이터</span>** 필요 |
| Container 오케스트레이터 | 쿠버네티스가 끝판왕 (여러 기업의 협업) |  |
| Kubernetes 클라우드서비스 | 쿠버네티스 환경이 설치되어 있는 인프라를 서비스 함<br>(쿠버네티스 설치할 필요없음)<br>(쿠버네티스 설치해서 자신의 운영환경에 맞게 최적화할 수 있음)| |

<br/>

### 2) 쿠버네티스 (Admin / User)

사용자입장에서 쿠버네티스 기능은 다음과 같이 구분할 수 있다.

<img src="/assets/images/2023-09-30-Kubernetes/kubernetes.png" /><br/>


*해당 게시글은 [대세는 쿠버네티스 초중급편](https://www.inflearn.com/course/%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EA%B8%B0%EC%B4%88?gad=1&gclid=CjwKCAjwvfmoBhAwEiwAG2tqzAD7E333fVc-gkDWnwIGPKATXtXbd3yC2CaV8GF4w-Ha70ouUlGIlRoCBlAQAvD_BwE) 를 바탕으로 작성하였습니다.*