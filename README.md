#  Spotify 리뷰 감성 분석 프로젝트 (MobileBERT 기반)

## 1. 개요
사용자리뷰는 가장 전형적이고 객관적인 통계데이터 중 하나로, 사용자 만족도나 개선점에 가장 영향력있는 통계데이터 중 하나이다.

이 사용자리뷰를 이용하여 기업은  앞으로의 사업방향성 이나 정책을 정하기도한다. 

이번 프로젝트에서는 전세계에서 가장 많이 사용하는 음악어플인 스포티파이에 대한 리뷰를 분석하고자 한다. 

다양한 국적의 가수들과 사용자들이 이용하는 스포티파이는 현재 전세계 1등 음악 스트리밍 서비스 업체이다.

2024년 총296억달러의 수익을 기록하였는데 사용자 리뷰를 확인하였을때 통계가 무색할 정도로 모든 사용자가 스포티파이에 만족하는 것은 아니였다. 

이번 프로젝트는 스포티파이 리뷰 데이터를 이용하여 MobileBERT 모델 기반의 감정분석 모델 구축, 리뷰의 긍정과 부정 예측 , 토픽 모델링의 결과를 통해 인사이트를 도출 할 예정이다.  [1][참고자료](https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd) 



## 2. 데이터 설명 및 학습데이터 구성성

**수집된 데이터 활용**

- **사용 데이터**: Spotify 앱 리뷰 
- **총 데이터 수**: 83,829건

[2][원본데이터](https://www.kaggle.com/datasets/ashishkumarak/spotify-reviews-playstore-daily-update?resource=download)

<br>

**데이터 컬럼 요약 설명**

| 컬럼명                   | 설명 요약 |
|------------------------|-----------|
| **content**             | 사용자가 작성한 실제 리뷰 텍스트 |
| **score**               | 리뷰 평점 (1~5점) |
| **reviewCreatedVersion**| 리뷰 작성 당시 사용자의 Spotify 앱 버전. |
| **at**                  | 리뷰가 작성된 날  |


**문장 길이 통계**

| 항목                   | 개수 |
|------------------------|-----------|
| 총 리뷰 수  | 72,146 개 |
| 평균 길이   | 310 자   |
| 최대 길이   | 2,399 자 |


 **점수 설명 및 레이블 라벨링**

| 점수 | 리뷰 수   | 레이블 | 설명       |
|------|----------|--------|------------|
| 1    | 35,060 개 | 0      | 부정 리뷰   |
| 2    | 13,846 개 | 0      | 부정 리뷰   |
| 3    | 12,019 개 | 제외   | 중립 리뷰   |
| 4    | 9,672 개  | 1      | 긍정 리뷰   |
| 5    | 13,568 개 | 1      | 긍정 리뷰   |

- 라벨링 전 데이터 : 83,829건
- 라벨링 후 데이터: 72,146건  
  
**학습 데이터 구성**

- 학습 데이터: 전체 데이터 약 20%인 14,434건 추출
- 14,434건의 데이터 (학습 : 검증 = 8 : 2) 구성
- 부정 67%, 긍정 33%
  
  




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

- 특정 기간 동안 부정 리뷰가 60%를 초과하는 상황이 지속됨
- 급격한 변화 구간

   **2018년 3분기 ~ 2019년 2분기**  
     - 부정 리뷰 비율이 **60% 이상으로 급증**
  
   **2024년 1분기 ~ 2024년 2분기**  
     - 부정 리뷰 비율이 **60% 이하로 급감**, **긍정적인 변화** 발생

- 두 기간의 부정 리뷰의 급증 원인 또는 감소 요인을 파악




<br>

## 토픽 모델링

## (2018년 3분기 ~ 2019년 2분기)

<br>

![image](https://github.com/user-attachments/assets/3e81aa90-2b48-4a8e-95b3-30792751008e)


**부정적인 리뷰가 급증한 이유**

| 문제/논란             | 설명                                                      | 사용자에게 미친 영향                                |
|--------------------|---------------------------------------------------------|-------------------------------------------------|
| 2019년 4월 서비스 중단  | 전 세계적 대규모 서비스 중단, 2만 명 이상 영향                     | 음악 스트리밍·다운로드 불가, 불만 폭주, 신뢰 저하          |
| "스콜피온 SZN" 프로모션  | 드레이크 앨범 홍보 위해 관련 없는 플레이리스트까지 이미지 도배          | 광고 없는 프리미엄 경험 침해, 환불 요청, 브랜드 신뢰 훼손      |
| "가짜 아티스트" 의혹      | 스톡 음악 기반 가짜 아티스트 홍보 의혹으로 로열티 절감 시도             | 아티스트 보상 문제, 플랫폼 신뢰 하락, 음악 발견 방해          |
| "페이-포-플레이" 관행     | 레이블이 인기 플레이리스트 배치를 위해 스포티파이에 금전 지불 의혹         | 음악 발견 공정성 및 아티스트 보상에 대한 우려               |
| 2018년 5월 앱 업데이트    | 기존 기능 대거 제거 및 복잡한 UI 도입으로 사용자 불만 증폭                | 사용자 경험 저하, 소셜 기능 상실, 플랫폼 이탈 고려           |
| 팟캐스트 통합 불만        | 팟캐스트가 음악 피드에 강제 통합되고 관리 기능 축소                       | 음악 청취 방해, 앱 복잡화 불만, 팟캐스트 관리 어려움          |




- [Criticism of Spotify - Wikipedia](https://en.wikipedia.org/wiki/Criticism_of_Spotify)
- [Drake promotion on Spotify goes too far, users demand refunds - Karen Civil](https://karencivil.com/2018/07/03/spotify-subscribers-are-demanding-refunds-over-too-much-drake-promotion)
- [Users Demand Refund From Spotify After Heavy-Handed Drake Promotion - Okayplayer](https://okayplayer.com/music/drake-scorpion-spotify-takeover.html)
- [Controversy over fake artists on Spotify - Wikipedia](https://en.wikipedia.org/wiki/Controversy_over_fake_artists_on_Spotify)

<br>

## (2024년 1분기 ~ 2024년 2분기)

<br>

![image](https://github.com/user-attachments/assets/3c3ca461-92f1-4d64-96b6-12d7f68ecbf6)

**긍정적인 리뷰가 급증한 이유**

| 핵심 기능                       | 요약 설명                                 |
|------------------------------|----------------------------------------|
| AI 플레이리스트                | 사용자 맞춤 음악 발견 및 큐레이션 강화       |
| DJ                           | 청취 습관 기반 개인화 라디오 및 음악 추천   |
| 대기열 업그레이드 & 30일 스누즈 | 재생 제어 개선과 추천 신선도 유지            |
| 모바일 플레이리스트 관리 & 만들기 버튼 | 편리한 큐레이션과 소셜 기능                  |
| 오디오북 통합                  | 프리미엄 오디오북 제공으로 콘텐츠 다양성 확대 |
| 광고 익스체인지 & AI 광고 도구    | 광고 효율성과 확장성 증대                   |



- [Spotify Q1'25 Preview: Resilient Business Model Amid Tariff and Economic Turmoil - Inderes](https://inderes.dk/en/analyst-comments/spotify-q125-preview-resilient-business-model-amid-tariff-and-economic-turmoil)
- [Q2 2024 Earnings Call Prepared Remarks (PDF)](https://s29.q4cdn.com/175625835/files/doc_financials/2024/q2/Q2-24-Earnings-Call-Prepared-Remarks.pdf)
- [Culture Next 2024: The Major Gen Z Trends That Are Shaping Audio Streaming - Spotify Newsroom](https://newsroom.spotify.com/2024-11-04/culture-ne)
- [Experience a New Dimension of Music Discovery With More Controls and Enhanced Tools - Spotify Newsroom](https://newsroom.spotify.com/2025-05-07/experience-a-new-dimension-of-music-discovery-with-more-controls-and-enhanced-tools)
- [Spotify Admits It Made Mistakes With Your Wrapped 2024 – Here's What Could Change This Year | TechRadar](https://techradar.com/audio/spotify/spotify)

## 6. 마무리

2018-2019년의 부정적인 서비스 기간은 주로 제품 관리의 내부적인 실수(열악한 UI, 강제적인 팟캐스트 통합), 논란이 된 마케팅(드레이크 인수), 그리고 윤리적 문제(가짜 아티스트, 페이-포-플레이)에 기인했으며, 이는 핵심 서비스 안정성 문제와 경쟁 환경에서의 ARPU 감소로 더욱 심화되었습니다. 이러한 문제들은 사용자 신뢰와 만족도에 직접적인 영향을 미쳤습니다.

대조적으로, 2024년의 긍정적인 서비스 기간은 스포티파이가 보다 성숙한 비즈니스 모델로 성공적으로 전환했음을 반영합니다. 여기에는 효과적인 수익화 전략(낮은 이탈률과 함께 가격 인상), AI 기반 개인화에 대한 상당한 투자, 그리고 다양한 오디오 콘텐츠(팟캐스트, 오디오북)로의 전략적 확장이 포함됩니다. 



## 사용 기술
<img src="https://img.shields.io/badge/pycharm-%23000000.svg?&style=for-the-badge&logo=pycharm&logoColor=white" />
<img src="https://img.shields.io/badge/spotify-%231ED760.svg?&style=for-the-badge&logo=spotify&logoColor=white" />
<img src="https://img.shields.io/badge/kaggle-%2320BEFF.svg?&style=for-the-badge&logo=kaggle&logoColor=white" />







##  출처



 [참고자료](참고자료)(https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd)

[원본데이터](원본데이터)(https://www.kaggle.com/datasets/ashishkumarak/spotify-reviews-playstore-daily-update?resource=download)







