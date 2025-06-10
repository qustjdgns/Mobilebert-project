#  Spotify 리뷰 감성 분석 프로젝트 (MobileBERT 기반)

## 1. 개요
사용자리뷰는 가장 전형적이고 객관적인 통계데이터 중 하나로, 사용자 만족도나 개선점에 가장 영향력있는 통계데이터 중 하나이다. 이 사용자리뷰를 이용하여 기업은  앞으로의 사업방향성 이나 정책을 정하기도한다. 

이번 프로젝트에서는 전세계에서 가장 많이 사용하는 음악어플인 스포티파이에 대한 리뷰를 분석하고자 한다. 다양한 국적의 가수들과 사용자들이 이용하는 스포티파이는 현재 전세계 1등 음악 스트리밍 서비스 업체이다. 2024년 총296억달러의 수익을 기록하였는데 사용자 리뷰를 확인하였을때 통계가 무색할 정도로 모든 사용자가 스포티파이에 만족하는 것은 아니였다. 이번 프로젝트는 스포티파이 리뷰 데이터를 이용하여 MobileBERT 모델 기반의 감정분석 모델 구축, 리뷰의 긍정과 부정 예측 , 서비스 개선점에 대해 분석 및 도출해 보고자 한다. [1][참고자료](https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd)



## 2. 데이터

**수집된 데이터 활용**

- **사용 데이터**: Spotify 앱 리뷰 - [2][원본데이터](https://www.kaggle.com/datasets/ashishkumarak/spotify-reviews-playstore-daily-update?resource=download)
- **총 데이터 수**: 83,829건
  
**데이터 컬럼 요약 설명**

| 컬럼명                   | 설명 요약 |
|------------------------|-----------|
| **content**             | 사용자가 작성한 실제 리뷰 텍스트 |
| **score**               | 리뷰 평점 (1~5점) |
| **reviewCreatedVersion**| 리뷰 작성 당시 사용자의 Spotify 앱 버전. |
| **at**                  | 리뷰가 작성된 날  |


 
 **점수 분포**
 
![점수 분포 그래프](https://github.com/user-attachments/assets/febc97d0-f45d-48e9-899f-2cc4d8538921)
- 1점을 받은 리뷰가 제일 많다. 그 뒤로 2점, 5점, 3점, 4점 순으로 많음을 보이고 있다.
  
**문장 길이 분포**

![문장 길이 분포](https://github.com/user-attachments/assets/51091394-527f-4d96-a5c8-2c64578b8257)
- 주로 문장 길이의 분포는 200전반보다 200후반의 길이가 더많은 것으로 보이며, 짧은 문장길이의 리뷰를 확인하였을때 무의미한 리뷰는 보이지 않았다.

  

**라벨링**

| 평점 구간 | 레이블 | 설명     |
| --------- | ------ | -------- |
| 1~2점     | 0      | 부정 리뷰 |
| 3점       | 제외   | 중립 리뷰 |
| 4~5점     | 1      | 긍정 리뷰 |


- 라벨링 전 데이터 : 83,829건
- 라벨링 후 데이터: 72,146건
  
## 3. 학습 데이터 구성

- 학습 데이터: 약 20%인 14,434건 추출
- 학습 데이터 14,434건을 8:2로 나누어 검증 데이터를 추출
- 긍/부정 비율: 부정 67%, 긍정 33%  
  
  ![원그래프](https://github.com/user-attachments/assets/6b817043-11a7-4643-b333-a62c10519908)


## 4. MobileBERT Finetuning 결과

**training loss 그래프**

![Training Loss](https://github.com/user-attachments/assets/155e0aef-09b3-4ca8-88ef-d8b4f226691a)

**training accuracy & validation accuracy (x축 epoch)**

![Training Accuracy & Validation Accuracy](https://github.com/user-attachments/assets/b0026eb5-158e-44cd-892d-5265449c2f4e)
그래프 소수잘보이게 수정, 그래프 로스랑 validation 합치기

![Validation Accuracy](https://github.com/user-attachments/assets/b736a623-e1d0-44cc-917f-c3061a5fa4cc)

- 그래프를 보았을 때 각각의 EPOCH 별 training loss는 감소하고,training accuracy & validation accuracy 수치는 점점 증가함을 보인다. 
- 이는 모델이 해당 데이터를 잘 학습했다는 증거이며,학습 후 비교데이터(약 57,718건)을을 이용한 문장 분류 예측 결과의 정확도 또한 높을 것으로 예상한다.

**문장 분류 예측 결과**
  
![Inference 결과](https://github.com/user-attachments/assets/b0b63121-9188-4b68-b29d-4061ab658709)

-  데이터를 이용한 문장 분류 예측 결과는 정확도 약 91% 매우 높은 수치를 보이며, 모델의 문장 분류 예측 성능이 우수하다.
-  검증데이터의 긍정 예측 비율 또한 전체 데이터의 긍정 부정 분포와 유사한 비율을 보이고 있다.



## 5. 인사이트 도출



**검증 데이터 예측 결과 부정의 비율이 압도적으로 많았다. 그 원인을 데이터 분석을 통해 알아보고 인사이트를 도출해보자.**

**2024년 4월 이후 평점 급감 확인**
   
![2024년 4월 이후 평점 급감](https://github.com/user-attachments/assets/5cfbed12-ff41-4b97-bde2-b97a70da748a)


2024년 4월 이후 평균 평점이 급격히 하락. 이는 특정 업데이트 이후 사용자 불만이 증가했음을 시사 
-> 2024년 4월 이후 평점이 눈에 띄게 하락했으며, 해당 시점의 업데이트가 부정적 영향을 미쳤을 가능성이 높음.


**특정 버전 리뷰 급증 확인**

![특정 버전 리뷰 급증 확인](https://github.com/user-attachments/assets/f077cdf6-9696-4176-a86c-13735a873745)


8.9.36.616 버전에서 리뷰 수가 폭발적으로 증가, 해당 버전에서 기능 이슈나 불편 사항이 다수 제기된 것으로 추정
->버전 8.9.36.616은 리뷰 수가 급증한 이례적인 현상이 나타났으며, 사용자 불만이 집중된 버전으로 분석됨.

**최근 버전별 긍/부정 비율 (누적 막대그래프)**

![최근 버전별 긍/부정 비율](https://github.com/user-attachments/assets/a1482b89-8002-4e75-b063-b2a2e57ee180)


최신 버전들 중 일부는 부정 리뷰 비율이 60% 이상. 단순 리뷰 수가 아니라 사용자 만족도가 크게 하락한 버전이 확인됨
-> 최근 버전 중 일부는 부정 리뷰가 전체의 60% 이상을 차지하고 있어, 단순한 리뷰 수보다 사용자 만족도 저하가 더 문제로 드러남.


**토픽 모델링**

![zmffkdnem](https://github.com/user-attachments/assets/ad4779b3-0aee-40ca-a2e7-dafe6c036519)

| 분류           | 주요 이슈 키워드                                         | 사용자 불만 요약                                 |
|----------------|----------------------------------------------------------|--------------------------------------------------|
| 음악 재생       | play, playlist, shuffle, skip, listen                    | 원하는 방식으로 음악을 재생하지 못함            |
| 앱 오류         | stop, fix, bug, update                                   | 앱이 멈추거나 오류가 잦음                        |
| 광고            | ad, free, pay, service                                   | 광고가 너무 많거나 프리미엄 유도 강함           |
| 오프라인 문제    | offline, downloaded, internet, connection               | 오프라인에서도 음악이 제대로 재생되지 않음      |
| 업데이트/기능   | premium, update, cant, even, without                    | 기능 제한, 업데이트로 인한 혼란                 |
| 계정 문제       | account, login, password, cancel, support               | 로그인, 비밀번호, 계정 관리 문제                |

**토픽 모델링을 통해 알아낸 서비스에 대한 불만을 개선하기 위해 실현 가능한 개선점을 마련.** 전문가의 의견 달기

**개선 방안**

음악 재생 유연성 강화  
- 무료 사용자도 최소한의 트랙 선택 및 순서 재생 허용  
- 사용자 맞춤형 플레이리스트 추천 및 순서 제어 기능 추가

앱 안정성 향상  
- 긴급 패치 주기 단축  
- OS 호환성 테스트 강화  
- 사용자 피드백 기반 QA 자동화

광고 정책 개선  
- 광고 간격 조절 (예: 3곡당 1광고)  
- 스킵 가능한 광고 도입  
- 개인화 광고 적용



## 6. 마무리

이번 프로젝트를 통해 사용자 리뷰 데이터를 기반으로 실제 사용자 경험을 통계적으로 분석할 수 있었고, 이를 통해 서비스 개선 방향을 도출할 수 있었다. 단순히 모델의 정확도를 높이는 것보다, 어떤 요소들이 사용자 불만으로 이어지고 있는지를 토픽 모델링으로 분석하면서 데이터 기반 의사결정의 중요성을 다시 한번 느낀다.

또한, MobileBERT와 같은 경량화된 모델을 활용해도 충분히 높은 성능을 낼 수 있다는 점에서, 모델 선택과 전처리, 라벨링의 중요성을 체감한다.

무엇보다도 단순한 리뷰 수치 이상의 인사이트를 확보하여, 서비스 운영자 입장에서 사용자의 목소리를 어떻게 반영해야 할지를 고민해볼 수 있었던 값진 경험이었다. 


## 사용 기술
<img src="https://img.shields.io/badge/pycharm-%23000000.svg?&style=for-the-badge&logo=pycharm&logoColor=white" />
<img src="https://img.shields.io/badge/spotify-%231ED760.svg?&style=for-the-badge&logo=spotify&logoColor=white" />
<img src="https://img.shields.io/badge/kaggle-%2320BEFF.svg?&style=for-the-badge&logo=kaggle&logoColor=white" />







##  출처



 [참고자료](참고자료)(https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd)

[원본데이터](원본데이터)(https://www.kaggle.com/datasets/ashishkumarak/spotify-reviews-playstore-daily-update?resource=download)




