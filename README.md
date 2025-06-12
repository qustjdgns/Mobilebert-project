#  Spotify 리뷰 감성 분석 프로젝트 (MobileBERT 기반)

## 1. 개요
사용자리뷰는 가장 전형적이고 객관적인 통계데이터 중 하나로, 사용자 만족도나 개선점에 가장 영향력있는 통계데이터 중 하나이다.

이 사용자리뷰를 이용하여 기업은  앞으로의 사업방향성 이나 정책을 정하기도한다. 

이번 프로젝트에서는 전세계에서 가장 많이 사용하는 음악어플인 스포티파이에 대한 리뷰를 분석하고자 한다. 

다양한 국적의 가수들과 사용자들이 이용하는 스포티파이는 현재 전세계 1등 음악 스트리밍 서비스 업체이다.

2024년 총296억달러의 수익을 기록하였는데 사용자 리뷰를 확인하였을때 통계가 무색할 정도로 모든 사용자가 스포티파이에 만족하는 것은 아니였다. 

이번 프로젝트는 스포티파이 리뷰 데이터를 이용하여 MobileBERT 모델 기반의 감정분석 모델 구축, 리뷰의 긍정과 부정 예측 , 토픽 모델링의 결과를 도출, 

우리가 도출한 문제점이 개선 되어있는지 확인까지 할 예정이다.  [1][참고자료](https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd) 



## 2. 데이터

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


 
 **점수 분포**
 
| 점수 | 리뷰 수  |
|------|---------|
| 1    | 35,060 개 |
| 2    | 13,846 개 |
| 3    | 12,019 개 |
| 4    | 9,672 개  |
| 5    | 13,568 개 |
  


**문장 길이 통계**

| 항목                   | 개수 |
|------------------------|-----------|
| 총 리뷰 수  | 72,146 개 |
| 평균 길이   | 310 자   |
| 최대 길이   | 2,399 자 |



  

**라벨링**

| 평점 구간 | 레이블 | 설명     |
| --------- | ------ | -------- |
| 1~2점     | 0      | 부정 리뷰 |
| 3점       | 제외   | 중립 리뷰 |
| 4~5점     | 1      | 긍정 리뷰 |

- 라벨링 전 데이터 : 83,829건
- 라벨링 후 데이터: 72,146건
  
## 3. 학습 데이터 구성

- 학습 데이터: 전체에서 약 20%인 14,434건 추출
- 14,434건의 데이터 (학습 : 검증 = 8 : 2)로 구성
- 긍/부정 비율: 부정 67%, 긍정 33%  
  



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
- 급격한 변화 구간은 다음과 같음:

   **2018년 3분기 ~ 2019년 2분기**  
     - 부정 리뷰 비율이 **60% 이상으로 급증**
  
   **2024년 1분기 ~ 2024년 2분기**  
     - 부정 리뷰 비율이 **60% 이하로 급감**, **긍정적인 변화** 발생

- 위 두 기간을 기준으로 토픽모델링을 수행 할 경우:  
  → 부정 리뷰의 급증 원인 또는 감소 요인을 파악할 수 있음




<br>

## 토픽 모델링

## (2018년 3분기 ~ 2019년 2분기)

<br>

![image](https://github.com/user-attachments/assets/3e81aa90-2b48-4a8e-95b3-30792751008e)


**부정적인 리뷰가 급증한 이유**

| 문제/논란 | 설명 | 사용자에게 미친 영향 | 
|------------|------|------------------------|
| **2019년 4월 서비스 중단** | 전 세계적인 대규모 서비스 중단으로 2만 명 이상 사용자에게 영향. | 음악 스트리밍 및 다운로드 불가, 소셜 미디어에서 불만 폭주, 사용자 신뢰 저하, 플랫폼 전환 고려. | 
| **"스콜피온 SZN" 프로모션** | 드레이크 앨범 홍보를 위해 관련 없는 플레이리스트 커버까지 드레이크 이미지로 도배. | 프리미엄 사용자의 광고 없는 경험 침해에 대한 불만, 일부 사용자 환불 요청, 브랜드 신뢰 훼손. | 
| **"가짜 아티스트" 의혹** | 스포티파이가 로열티 절감을 위해 자체 큐레이션 플레이리스트에 스톡 음악 기반의 "가짜 아티스트"를 홍보했다는 의혹. | 아티스트 보상 및 플랫폼 무결성 훼손에 대한 우려, 사용자 신뢰 저하, 진정한 음악 발견 방해. | 
| **"페이-포-플레이" 관행** | 레이블이 특정 곡을 인기 플레이리스트에 배치하기 위해 스포티파이에 돈을 지불했다는 의혹. | 음악 발견의 공정성 및 아티스트 보상에 대한 우려. | 
| **2018년 5월 앱 업데이트** | 아티스트 스토리, 유사 아티스트 페이지, 친구 활동 확인, 장르/라디오 탐색 등 기존 기능 제거. 새로운 UI는 "끔찍하고 복잡하다"는 평가. | 사용자 경험 저하, 앱이 "껍데기" 같다는 불만, 소셜 기능 상실, 다른 플랫폼으로의 전환 고려. | 
| **팟캐스트 통합 불만** | 팟캐스트가 음악 피드에 강제로 통합되고, 전용 "새 에피소드" 폴더가 제거됨. | 음악 청취 경험 방해, 앱이 "복잡한 하이브리드"가 된다는 불만, 팟캐스트 관리 어려움. | 
| **개인 정보 보호 정책 우려** | 데이터 수집 범위, 제3자 공유, 추적 방식에 대한 사용자들의 지속적인 우려. | 개인 정보 침해에 대한 불안감, 사용자 신뢰 저하. | 



- [Criticism of Spotify - Wikipedia](https://en.wikipedia.org/wiki/Criticism_of_Spotify)
- [Drake promotion on Spotify goes too far, users demand refunds - Karen Civil](https://karencivil.com/2018/07/03/spotify-subscribers-are-demanding-refunds-over-too-much-drake-promotion)
- [Users Demand Refund From Spotify After Heavy-Handed Drake Promotion - Okayplayer](https://okayplayer.com/music/drake-scorpion-spotify-takeover.html)
- [Controversy over fake artists on Spotify - Wikipedia](https://en.wikipedia.org/wiki/Controversy_over_fake_artists_on_Spotify)

<br>

## (2024년 1분기 ~ 2024년 2분기)

<br>

![image](https://github.com/user-attachments/assets/3c3ca461-92f1-4d64-96b6-12d7f68ecbf6)

**긍정적인 리뷰가 급증한 이유**

| 기능 명칭 | 설명 | 의도된 사용자 혜택 | 
|-----------|------|---------------------|
| **AI 플레이리스트** | 사용자의 창의적인 아이디어를 기반으로 플레이리스트를 생성하는 AI 기반 기능. | 개인화된 음악 발견 및 손쉬운 플레이리스트 큐레이션. | 
| **DJ** | AI가 사용자의 청취 습관에 맞춰 음악을 선별하고 해설을 제공하는 기능. | 개인화된 라디오 경험 및 새로운 음악 발견. | 
| **데이리스트 (Daylist)** | 시간대에 따라 변하는 사용자의 기분과 취향에 맞는 맞춤형 플레이리스트를 제공. | 맥락에 맞는 음악 추천 및 다양한 청취 경험. | 
| **대기열(Queue) 업그레이드** | 재생 대기열의 새로운 디자인으로 셔플, 스마트 셔플, 반복, 취침 타이머 등의 제어 기능 포함. | 향상된 재생 제어 및 사용 편의성. | 
| **숨기기(Hide) 버튼 개선** | 특정 플레이리스트에서 원치 않는 트랙을 숨기는 기능이 더 직관적으로 개선. | 원치 않는 음악을 제거하여 청취 경험 최적화. | 
| **30일 스누즈(Snooze) 기능** | 추천 목록에서 특정 트랙을 30일 동안 일시적으로 제거하는 옵션. | 추천의 신선도 유지 및 일시적인 음악 회피. | 
| **모바일 플레이리스트 관리 도구** | 플레이리스트 상단에 추가, 정렬, 편집 기능에 쉽게 접근할 수 있도록 함. | 플레이리스트 큐레이션 및 관리를 간소화. | 
| **좋아요 표시된 노래로 플레이리스트 생성** | 좋아요 표시된 노래 목록을 필터링하여 새로운 플레이리스트를 만들 수 있는 기능. | 개인 라이브러리에서 새로운 플레이리스트 생성을 용이하게 함. | 
| **만들기(Create) 버튼 개선** | 모바일 앱 하단에 위치한 '+' 버튼을 통해 플레이리스트 생성, 친구와 협업, 블렌드 가입을 쉽게 할 수 있도록 함. | 콘텐츠 생성 및 소셜 기능에 대한 접근성 향상. | 
| **오디오북 통합** | 프리미엄 구독자에게 25만 개 이상의 오디오북에 대한 접근 권한 제공. | 프리미엄 구독의 가치 제안 확장 및 콘텐츠 다양성 증대. | 
| **스포티파이 광고 익스체인지/관리자** | 광고주가 스포티파이의 사용자에게 실시간 경매를 통해 접근하고, 고급 타겟팅 및 측정 기능을 사용할 수 있도록 함. | 광고주를 위한 효과적인 광고 캠페인 생성 및 최적화. | 
| **생성형 AI 광고 도구** | 광고 관리자 내에서 스크립트 및 보이스오버를 생성할 수 있는 AI 기반 도구. | 고품질 오디오 광고 생성을 간소화하고 확장성 제공. | 


- [Spotify Q1'25 Preview: Resilient Business Model Amid Tariff and Economic Turmoil - Inderes](https://inderes.dk/en/analyst-comments/spotify-q125-preview-resilient-business-model-amid-tariff-and-economic-turmoil)
- [Q2 2024 Earnings Call Prepared Remarks (PDF)](https://s29.q4cdn.com/175625835/files/doc_financials/2024/q2/Q2-24-Earnings-Call-Prepared-Remarks.pdf)
- [Culture Next 2024: The Major Gen Z Trends That Are Shaping Audio Streaming - Spotify Newsroom](https://newsroom.spotify.com/2024-11-04/culture-ne)
- [Experience a New Dimension of Music Discovery With More Controls and Enhanced Tools - Spotify Newsroom](https://newsroom.spotify.com/2025-05-07/experience-a-new-dimension-of-music-discovery-with-more-controls-and-enhanced-tools)
- [Spotify Admits It Made Mistakes With Your Wrapped 2024 – Here's What Could Change This Year | TechRadar](https://techradar.com/audio/spotify/spotify)

## 6. 마무리

2018-2019년의 부정적인 서비스 기간은 주로 제품 관리의 내부적인 실수(열악한 UI, 강제적인 팟캐스트 통합), 논란이 된 마케팅(드레이크 인수), 그리고 윤리적 문제(가짜 아티스트, 페이-포-플레이)에 기인했으며, 이는 핵심 서비스 안정성 문제와 경쟁 환경에서의 ARPU 감소로 더욱 심화되었습니다. 이러한 문제들은 사용자 신뢰와 만족도에 직접적인 영향을 미쳤습니다.

대조적으로, 2024년의 긍정적인 서비스 기간은 스포티파이가 보다 성숙한 비즈니스 모델로 성공적으로 전환했음을 반영합니다. 여기에는 효과적인 수익화 전략(낮은 이탈률과 함께 가격 인상), AI 기반 개인화에 대한 상당한 투자, 그리고 다양한 오디오 콘텐츠(팟캐스트, 오디오북)로의 전략적 확장이 포함됩니다. 회사는 운영 효율성 개선과 시장 탄력성을 입증했습니다.



## 사용 기술
<img src="https://img.shields.io/badge/pycharm-%23000000.svg?&style=for-the-badge&logo=pycharm&logoColor=white" />
<img src="https://img.shields.io/badge/spotify-%231ED760.svg?&style=for-the-badge&logo=spotify&logoColor=white" />
<img src="https://img.shields.io/badge/kaggle-%2320BEFF.svg?&style=for-the-badge&logo=kaggle&logoColor=white" />







##  출처



 [참고자료](참고자료)(https://bytebridge.medium.com/spotifys-transformative-impact-on-the-music-industry-and-its-innovative-revenue-model-b11d6b5110fd)

[원본데이터](원본데이터)(https://www.kaggle.com/datasets/ashishkumarak/spotify-reviews-playstore-daily-update?resource=download)







