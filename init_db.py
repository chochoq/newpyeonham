import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.hellodigital.kr/blog/dmkt-general-18-newsletter-we-love-01/',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

print(soup)
#
# # select를 이용해서, tr들을 불러오기
# news = soup.select('#contentDetailContent > p')
#
# # movies (tr들) 의 반복문을 돌리기
# for new in news:
#     # movie 안에 a 가 있으면,
#     a_tag = new.select_one('span > strong').text
#     print(a_tag)


# 제목
#contentDetailContent > p:nth-child(13) > span
#contentDetailContent > p:nth-child(19) > span > strong
#contentDetailContent > p:nth-child(24) > span > strong

# url
#contentDetailContent > p:nth-child(20) > a > span
#contentDetailContent > p:nth-child(25) > a > span


# 카테고리
#contentDetailContent > p:nth-child(31) > span
#contentDetailContent > p:nth-child(36) > span


# desc
#contentDetailContent > p:nth-child(37) > span
#contentDetailContent > p:nth-child(47) > span