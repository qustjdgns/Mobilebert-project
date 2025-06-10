#  Spotify 리뷰 감성 분석 프로젝트 (MobileBERT 기반)

## 1. 개요
사용자리뷰는 가장 전형적이고 객관적인 통계데이터 중 하나로, 사용자 만족도나 개선점에 가장 영향력있는 통계데이터 중 하나이다. 이 사용자리뷰를 이용하여 기업은  앞으로의 사업방향성 이나 정책을 정하기도한다. 

이번 프로젝트에서는 전세계에서 가장 많이 사용하는 음악어플인 스포티파이에 대한 리뷰를 분석하고자 한다. 

다양한 국적의 가수들과 사용자들이 이용하는 스포티파이는 현재 전세계 1등 음악 스트리밍 서비스 업체이다.

2024년 총296억달러의 수익을 기록하였는데 사용자 리뷰를 확인하였을때 통계가 무색할 정도로 모든 사용자가 스포티파이에 만족하는 것은 아니였다. 

또한 특정 과거 시점(2024년 Q2까지)의 리뷰 데이터는 현재 구글 플레이 스토어에 표시되는 평점과 비교하면 의미를 알 수 없다. 

이유는 구글플레이어의 최근 평점 표시 방식은 최근의 사용자 피드백을 좀 더 강력하게 반영하는 가중 평균 방식으로 계산이 되기 때문에 경험이 개선되거나 긍정적인 업데이트가 있는 경우 평점이 크게 달라질 수 있기때문에 우리가 인사이트 도출을 통한 피드백은 이미 적용이 되있을 확율이 매우 높다. 

이번 프로젝트는 스포티파이 리뷰 데이터를 이용하여 MobileBERT 모델 기반의 감정분석 모델 구축, 리뷰의 긍정과 부정 예측 , 토픽 모델링의 결과를 도출하고, 우리가 도출한 개선점이 개선 되어있는지 확인까지 할 예정이다.  [1][참고자료](https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd) [2][데이터불일치](https://github.com/user-attachments/files/20676258/_.pdf)



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

**training loss 그래프**



**training accuracy & validation accuracy (x축 epoch)**





**문장 분류 예측 결과**
  




## 5. 인사이트 도출

**분기별 평점 유형별 비율 추이**


![분기별](https://github.com/user-attachments/assets/9a4d922c-75e2-43a1-b49e-4b843e2ab7ab)

<br>

- 특정 기간 동안 부정 리뷰가 60%를 넘는 상황이 지속되었음을 확인 
- 급증 또는 감소 하는 구간을 찾아본 결과, 가장 눈에 띄는 두 시기는 다음과 같음
- (2018년 3분기 ~ 2019년 2분기): 이 구간에는 부정 리뷰가 60% 이상으로 급증하는 현상이 나타남 
- (2024년 1분기 ~ 2024년 2분기): 이 구간에는 부정 리뷰가 60% 이하로 대폭 감소하는 긍정적인 변화를 보였음
- 두 구간에 업데이트된 버전을 이용하여 토픽모델링을 한다면,부정 리뷰가 급증하는 현상 또는 부정 리뷰가 60% 감소하는 현상의 원인을 알 수 있음




<br>

**토픽 모델링**

**특정 과거 시점(2024년 Q2까지)의 리뷰 데이터는 현재 구글 플레이 스토어에 표시되는 평점과 비교하면 의미를 알 수 없다. 그 이유는 구글플레이어의 최근 평점 표시 방식은 최근의 사용자 피드백을 좀 더 강력하게 반영하는 가중 평균 방식으로 계산이 되기 때문에 경험이 개선되거나 긍정적인 업데이트가 있는 경우 평점이 크게 달라질 수 있기때문에 우리가 인사이트 도출을 통한 피드백은 이미 적용이 되있을 확율이 매우 높다. 우리는 토픽 모델링의 결과를 도출하고, 우리가 도출한 개선점이 개선 되어있는지 확인까지 할 예정이다**

<br>

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

특정 과거 시점(2024년 Q2까지)의 리뷰 데이터는 현재 구글 플레이 스토어에 표시되는 평점과 비교하면 의미를 알 수 가없다. 그 이유는 구글플레이어의 최근 평점 표시 방식은 최근의 사용자 피드백을 좀 더 강력하게 반영하는 가중 평균 방식으로 계산이 되기 때문에 경험이 개선되거나 긍정적인 업데이트가 있는 경우 평점이 크게 달라질 수 있기때문에 우리가 인사이트 도출을 통한 피드백은 이미 적용이 되있을 확율이 매우 높다.


## 사용 기술
<img src="https://img.shields.io/badge/pycharm-%23000000.svg?&style=for-the-badge&logo=pycharm&logoColor=white" />
<img src="https://img.shields.io/badge/spotify-%231ED760.svg?&style=for-the-badge&logo=spotify&logoColor=white" />
<img src="https://img.shields.io/badge/kaggle-%2320BEFF.svg?&style=for-the-badge&logo=kaggle&logoColor=white" />







##  출처



 [참고자료](참고자료)(https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd)

[원본데이터](원본데이터)(https://www.kaggle.com/datasets/ashishkumarak/spotify-reviews-playstore-daily-update?resource=download)

[논문](논문)(https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11229727)

[분석](데이터불일치)(https://github.com/user-attachments/files/20676258/_.pdf)



