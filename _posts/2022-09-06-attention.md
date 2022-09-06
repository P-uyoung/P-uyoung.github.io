---
layout: single  # single, 댓글기능을 달기 위해...
title:  "어텐션 메커니즘 (Attention Mechanism)"
categories: DL
tag: [basic]
toc: true
toc_sticky: false
author_profile: false
search: true
use_math: true
---
<br/>

### CONCLUSION
**RNN 기반으로 한 Seq2Seq는 시퀀스가 길어질 때, 전체 문맥을 제대로 고려하지 못하므로, Attnetion을 사용하여 현재 아웃풋 아이템이 주목해야 하는 인풋 시퀀스 파트들을 직접 연결해준다..**
<br/>

### RNN vs Seq2Seq
(1) RNN <br/> 
문맥이 있는 sequence data (음성인식, 자연어) 를 다룰 때 사용한다. <br/>
이전의 결과가 다음 결과에 영향을 미칠 수 있게 하여, 맥락을 이해하고 처리할 수 있도록 하는 것이다. <br/>

![RNN_loop](/assets/images/2022-09-06-attention/RNN_loop-16624468482883.png)

**A의 결과가 다시 A로 돌아가는 루프를 통해, x값을 통해 y를 계산할 때 이전 상태(state, NN)를 고려하게 된다.**
<br/>

자세한 설명은 다음 블로그 참고. <br/>
<https://medium.com/humanscape-tech/rnn-recurrent-neural-network-%EC%88%9C%ED%99%98%EC%8B%A0%EA%B2%BD%EB%A7%9D-%EC%9D%84-%EC%9D%B4%ED%95%B4%ED%95%B4%EB%B3%B4%EC%9E%90-1697a5472af2>
<br/>

(2) Seq2Seq <br/>
RNN은 출력이 바로 이전 입력까지만 고려하므로 전체 입력 문장을 고려하지 못한다. 이로 인해 정확도가 떨어지게 되는데, 이를 보완한 것이 Seq2Seq 모델이다. <br/>

**Seq2Seq Network (혹은 Encoder Decoder Network) 은 두 개의 RNN 으로 구성된 모델이다.**

<span style="color:lightseagreen">*시퀀스 (sequence) 란, 몇 개의 관련된 장면을 모아서 이루는 구성단위로도 쓰이고, NLP에서는 단어들이 2개 이상 묶여있는 것을 말한다. [i, am, a, girl]</span>
<br/>

- 인코더 : 입력된 정보를 어떻게 처리해서 **저장(취함)할** 것인가 <br/>

- 디코더 : 인코더로부터 압축된 정보를 어떻게 풀어서 **출력/반환할** 것인가 <br/>

<img src="/assets/images/2022-09-06-attention/s2s_1.png" alt="s2s_1" style="zoom:40%;" />

<img src="/assets/images/2022-09-06-attention/s2s_2.png" alt="s2s_2" style="zoom:80%;" />
<br/>

<span style="color:lightseagreen">*인코더는 Input Sequence 를 > Context Vactor 로, <br/>
디코더는 Input Sequence 를 > item by item 으로 Output Sequence로 생성한다 (구현 시, 하나씩 리스트의 append) </span>
<br/>

**하지만, RNN을 기반으로 한 Seq2Seq 에서 시퀀스가 길어지면 (Long Sequence) 앞의 내용보다 뒷부분의 내용이 훨씬 더 많은 영향을 미치는 단점이 있다. 이러한 문제를 해결하기 위해 Attention 을 사용한다.**

<br/>

### Attention 
(정리하겠음) <br/>
<https://acdongpgm.tistory.com/216> <br/>
<https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ckdgus1433&logNo=221608376139>

<br/>

### REFERENCE
[1] <https://glee1228.tistory.com/3> <br/>
[2] <https://acdongpgm.tistory.com/216>

