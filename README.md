#  Spotify 리뷰 감성 분석 프로젝트 (MobileBERT 기반)

## 1. 개요
사용자리뷰는 가장 전형적이고 객관적인 통계데이터 중 하나로, 사용자 만족도나 개선점에 가장 영향력있는 통계데이터 중 하나이다.

이 사용자리뷰를 이용하여 기업은  앞으로의 사업방향성 이나 정책을 정하기도한다. 

이번 프로젝트에서는 전세계에서 가장 많이 사용하는 음악어플인 스포티파이에 대한 리뷰를 분석하고자 한다. 

다양한 국적의 가수들과 사용자들이 이용하는 스포티파이는 현재 전세계 1등 음악 스트리밍 서비스 업체이다.

2024년 총296억달러의 수익을 기록하였는데 사용자 리뷰를 확인하였을때 통계가 무색할 정도로 모든 사용자가 스포티파이에 만족하는 것은 아니였다. 

이번 프로젝트는 스포티파이 리뷰 데이터를 이용하여 MobileBERT 모델 기반의 감정분석 모델 구축, 리뷰의 긍정과 부정 예측 , 토픽 모델링의 결과를 도출하고, 

우리가 도출한 문제점이 개선 되어있는지 확인까지 할 예정이다.  [1][참고자료](https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd) 



## 2. 데이터

**수집된 데이터 활용**

[2][원본데이터](https://www.kaggle.com/datasets/ashishkumarak/spotify-reviews-playstore-daily-update?resource=download)

- **사용 데이터**: Spotify 앱 리뷰 
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
- 학습 데이터 14,434건을 (학습 : 검증 = 8 : 2)로 나누어 검증 데이터를 추출
- 긍/부정 비율: 부정 67%, 긍정 33%  
  
  ![원그래프](https://github.com/user-attachments/assets/6b817043-11a7-4643-b333-a62c10519908)


## 4. MobileBERT Finetuning 결과

**training loss & Train Accuracy 그래프**

![fhtm로스이제안하나다](https://github.com/user-attachments/assets/103ac869-e5df-4916-a936-b108e4be5cbc)


- 학습 손실율이 계속 감소한 사실을 보아, 모델이 정상 작동함을 확인
- 학습 정확도 또한 하락 없이 상승 추세를 유지하고 있음

**training accuracy & validation accuracy (x축 epoch)**

![Figure_9999](https://github.com/user-attachments/assets/082c2587-4bb1-49a2-8f71-63f3ac5721e0)


- 검증 정확도 또한 0.9이상의 높은 정확도를 보이고 있음

**문장 분류 예측 결과**

- 예측 정확도 : 0.917
  
  <br>
![Figure_18888888](https://github.com/user-attachments/assets/d0d2430b-2a3b-4288-89f7-40ff58e6e86d)




## 5. 인사이트 도출

**분기별 평점 유형별 비율 추이**


![분기별](https://github.com/user-attachments/assets/9a4d922c-75e2-43a1-b49e-4b843e2ab7ab)

<br>

- 특정 기간 동안 부정 리뷰가 60%를 넘는 상황이 지속되었음을 확인 
- 급증 또는 감소 하는 구간을 찾아본 결과, 가장 눈에 띄는 두 시기는 다음과 같음
- (2018년 3분기 ~ 2019년 2분기): 이 구간에는 부정 리뷰가 60% 이상으로 급증하는 현상이 나타남 
- (2024년 1분기 ~ 2024년 2분기): 이 구간에는 부정 리뷰가 60% 이하로 대폭 감소하는 긍정적인 변화를 보였음
- 두 구간 기간을 기준을 토픽모델링을 한다면,부정 리뷰가 급증하는 현상 또는 부정 리뷰가 감소하는 현상의 원인을 알 수 있음




<br>

**토픽 모델링**

**(2018년 3분기 ~ 2019년 2분기)**

<br>

![image](https://github.com/user-attachments/assets/3e81aa90-2b48-4a8e-95b3-30792751008e)


**부정적인 리뷰가 급증한 이유**

premium, ad, paying: 유료 사용자 경험 불만

Spotify, app, update, version: 앱 및 서비스 자체 문제

song, play, playlist, shuffle: 음악 재생 기능 문제

screen, phone, time: 디바이스 및 사용 경험 문제

<br>

**사용자가 불만인 이유**



<br>

**(2024년 1분기 ~ 2024년 2분기)**

<br>

![image](https://github.com/user-attachments/assets/3c3ca461-92f1-4d64-96b6-12d7f68ecbf6)

**긍정적인 리뷰가 급증한 이유**

music, app, Spotify, sound, streaming : 서비스에 대한 전반적인 만족

premium, ad, free, pay, version, skip : 유료 서비스에 대한 긍정적 평가 또는 개선 기대


song, playlist, play, shuffle, add, artist : 음악 기능의 유용성과 즐거움

listen, like, love, hear, experience : 감성적 만족과 애정 표현


good, best, great, excellent, awesome, quality : 전반적인 품질과 서비스에 대한 긍정 평가

use, easy, update, feature, platform : 사용 편의성과 기능적 장점


**현재 개선된 부분**





## 6. 마무리

이번 프로젝트를 통해 사용자 리뷰 데이터를 기반으로 실제 사용자 경험을 통계적으로 분석할 수 있었고, 이를 통해 서비스 개선 방향을 도출할 수 있었다. 단순히 모델의 정확도를 높이는 것보다, 어떤 요소들이 사용자 불만으로 이어지고 있는지를 토픽 모델링으로 분석하면서 데이터 기반 의사결정의 중요성을 다시 한번 느낀다.

또한, MobileBERT와 같은 경량화된 모델을 활용해도 충분히 높은 성능을 낼 수 있다는 점에서, 모델 선택과 전처리, 라벨링의 중요성을 체감한다.

특정 과거 시점(2024년 Q2까지)의 리뷰 데이터는 현재 구글 플레이 스토어에 표시되는 평점과 비교하면 의미를 알 수 없다. 그 이유는 구글플레이어의 최근 평점 표시 방식은 최근의 사용자 피드백을 좀 더 강력하게 반영하는 가중 평균 방식으로 계산이 되기 때문에 경험이 개선되거나 긍정적인 업데이트가 있는 경우 평점이 크게 달라질 수 있기때문에 우리가 인사이트 도출을 통한 피드백은 이미 적용이 되있을 확율이 매우 높다. 물


## 사용 기술
<img src="https://img.shields.io/badge/pycharm-%23000000.svg?&style=for-the-badge&logo=pycharm&logoColor=white" />
<img src="https://img.shields.io/badge/spotify-%231ED760.svg?&style=for-the-badge&logo=spotify&logoColor=white" />
<img src="https://img.shields.io/badge/kaggle-%2320BEFF.svg?&style=for-the-badge&logo=kaggle&logoColor=white" />







##  출처



 [참고자료](참고자료)(https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd)

[원본데이터](원본데이터)(https://www.kaggle.com/datasets/ashishkumarak/spotify-reviews-playstore-daily-update?resource=download)

[논문](논문)(https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11229727)

[분석](데이터불일치)(https://github.com/user-attachments/files/20676258/_.pdf)



