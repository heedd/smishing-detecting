# Smishing Detecting Service
스미싱 탐지 프로그램

## 프로젝트 개요
- KB금융그룹 및 KISA에서 제공받은 정상 문자와 스미싱 문자 30만건을 활용하여 금융문자 분석 **딥러닝 모델 설계**
- flask, 도커, AWS를 활용하여 딥러닝 기반 **스미싱 탐지 웹서비스 배포**

※데이터 출처 : https://dacon.io/competitions/official/235401/data
<br>

## 서비스 아키텍쳐
- 자연어 처리 딥러닝 알고리즘 설계
- AWS EC2 인스턴스에서 docker container를 통해 flask 웹서버 배포
<img src="https://user-images.githubusercontent.com/58112670/152678647-f9f5507f-2218-45f3-a876-c6dead5b0c3a.png" width="450"/>
<br>



## 웹 구현 영상
- 정상 문자 탐지
<img src="https://user-images.githubusercontent.com/58112670/152694815-e75f2d05-63c1-4ece-ab25-522dadeb6a03.gif" width="350"/>  
<br>

- 스미싱 문자 탐지
<img src="https://user-images.githubusercontent.com/58112670/152694816-d7f94f32-5082-42cb-9dce-d5fb7105e5cc.gif" width="350"/>
