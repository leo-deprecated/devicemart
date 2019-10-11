from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests

#############################################################
# have to write your own information
driver = webdriver.Chrome("# input your webdriver path here")
id = "아이디"
pw = "비밀번호"
bname = "업체명"
bceo = "대표자명"
# soma@fkii.com
email0 = "soma"
email1 = "fkii.com"
# 010-1234-5678
phone0 = "010"
phone1 = "1234"
phone2 = "5678"
#############################################################

# 필수 입력 정보
necessary = {
    "userid":id,
    "password":pw,
    "re_password":pw,
    "bname":bname,
    "bceo":bceo,
    "email[0]":email0,
    "email[1]":email1,
}

# webdriver 연결
driver.get("http://www.devicemart.co.kr/member/register?join_type=business")

# 사업자 등록번호 규칙에 기반한 코드 모음
# 참고: http://seoulcredit.co.kr/business_id
# 현재 서울지역에 등록된 사업자에 대해서만 동작하도록 작성되어 있음
seoul_codes = (101,104,105,106,107,108,109,110,113, 114, 117, 119, 120, 201, 204, 206, 209, 210, 211, 212, 214, 215, 220)
bubin_codes = (i for i in range(81,88))
fin_codes = (i for i in range(10000, 100000))

for seoul_code in seoul_codes:
    for bubin_code in bubin_codes:
        for fin_code in fin_codes:
            driver.find_element_by_name("bno").clear() # 새로운 입력을 위한 test area 클린 작업
            driver.find_element_by_name("bno").send_keys(f"{seoul_code}-{bubin_code}-{fin_code}") # 코드 조합 테스트
            driver.find_element_by_name("bname").click() # bno_info 업데이트를 위한 클릭
            time.sleep(1) # 웹 자원 로딩을 위한 기다림
            results = driver.find_element_by_id("bno_info").text # 디바이스마트 사업자 등록번호 규칙을 통과했는지 여부 확인
            if results =="": # 성공 코드 도달 시 loop 해제
                break
        if results =="": # 성공 코드 도달 시 loop 해제
            break
    if results =="": # 성공 코드 도달 시 loop 해제
        break

# 필수 정보 추가 입력 후 가입완료
for key, value in necessary.items():
    driver.find_element_by_name(key).send_keys(value)
driver.find_element_by_name("bcellphone[]").send_keys(f"{phone0}\t{phone1}\t{phone2}\n")

# 입력한 이메일과 핸드폰으로 가입완료 메시지 리턴