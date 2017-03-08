# 출근했는지 로그를 남기자!

## 사용법
  ```bash
  ifconfig [무선인터페이스] down
  iwconfig [무선인터페이스] mode monitor
    - iwconfig [무선인터페이스] mode managed
  ifconfig [무선인터페이스] up
  ```
  - 이렇게 했는데 결과 출력이 안 될 경우(Wireshark 에서도 안 보일 경우)
    무선인터페이스가 모니터링 모드를 지원하지 않아서 그렇습니다.
    작은 동글하나 구매해서 진행하세요.

## 목표와 버전히스토리

### 버전히스토리
  - 1.1.3c
    - class scanner crontab script 수정
  - 1.1.3b
    - class scanner crontab script
  - 1.1.3a
    - class server crontab script
  - 1.1.3
    - MAC 주소 중복 확인
  - 1.1.2
    - MAC 주소 단방향 해쉬 적용(SHA256)
    - 무선인터페이스 활성화 스크립트
  - 1.1.1
    - 소스코드 클래스별로 분류
  - 1.1.0
    - 강의실용 출석부 완성
  - 1.0.0
    - 클래스 형태로 변경
    - MAC 주소와 인원 매칭 제거
  - 0.1.4
    - Apple Macbook은 Padding을 통해서 60Bytes Packet으로 보냄
    - struct unpack 버그 수정
  - 0.1.3
    - 출근한 사람이 없을 경우 기록하지 않음
  - 0.1.2
    - 출근한 인원 Set 형식으로 출력
    - 잠자는 시간을 위해 ini 템플릿 수정
    - 대문자로 등록된 MAC 소문자로 변환
  - 0.1.1
    - 잠자는 시간 설정파일로 조정 가능
  - 0.1.0
    - 초기버전 완성

### 해결한 목표
  - 잠자는 시간 설정파일로 조정(0.1.1 패치)
  - 출근한 인원 Set 형식으로 출력(0.1.2 패치)
    - False Negative를 줄이기 위해 여러 MAC Address 등록할 수 있도록 위함
  - 대문자로 등록된 MAC을 소문자로 변환(0.1.2 패치)
  - 출근한 사람이 없을 경우 출력하지 않음(0.1.3 패치)
  - 소켓 자는 시간 설정 파일에서 확인(1.0.0 패치)
  - Wireless interface를 활용해 Probe Request 메시지를 탐색(1.0.0 패치)
    - AP에 연결하지 않고도 확인 가능
  - 클래스로 구조 변경(1.0.0 패치)
    - 상속 고려: 여러 환경에서 동작할 수 있도록 하기 위함
  - 시각화(1.1.0 패치)
  - 개인 출근 내역 익스포트 기능(1.1.0 패치)
    - 개인 인증 서비스가 있어야 함
  - MAC 주소 단방향 해시를 이용해 비식별화 조치(1.1.2 패치)
  - MAC 주소 중복 체크(1.1.3 패치)
    - 단일 기기로 여러 사람 체크할 수 있음
  - crontab에 등록할 수 있는 자동 스크립트(1.1.3a 패치)

### 추가해야할 목표
  - Self-signed Certificate 를 만들어 암호화 통신
    - S.S.C.는 github에 올리지 말아야 함
  - 웹 페이지에서 자동으로 MAC 주소 등록

### 제거한 목표
  - 출력 파일 csv 헤더 추가(170302)
  - 출력 파일 이름을 설정 파일에서 확인(170302)


## 정책

### 코딩룰
  - \*.ini 파일의 이름은 하드코딩을 허용
    - .cgi 모듈로 인자 전달이 어렵기 때문에 이렇게 결정
  - 이외의 다른 파일 이름은 설정 파일을 통해서 입력받는 것으로 장려
    - 로그, 데이터베이스 이름 등
