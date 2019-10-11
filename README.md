# 디바이스마트 자동 가입

- 개요: 디바이스마트에 가짜 사업자등록번호를 넣어야해서 가입하는데 짜증나 있는 소마인들을 위한 자동가입 툴

- dependency:
    - python3.6 이상
    - selenium
    - bs4 (BeautifulSoup)
    - requests

- 사용방법
    1. [webdriver를 다운받는다](https://sites.google.com/a/chromium.org/chromedriver/downloads)
        - 주의사항: 크롬 브라우저를 대상으로 구현되어 있음
        - 주의사항: 기 설치되어 있는 크롬과 메이저 버전이 같은 webdriver를 사용하지 않으면 에러가 뜰 수도
    2. devicemart.py에 필수 정보를 입력한 뒤 실행한다.
    3. 문자와 이메일로 가입완료 문자가 온다.