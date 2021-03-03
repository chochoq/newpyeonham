from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

driver = webdriver.Chrome('./chromedriver')

url = "https://www.i-boss.co.kr/ab-6141-52815"

driver.get(url)
sleep(3)


# 맨 밑까지 내리기
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)


req = driver.page_source
driver.quit()

list = [];

soup = BeautifulSoup(req, 'html.parser')
#btitleList = soup.select("div.wrap_body_frame > div.wrap_body.text_align_left.finish_txt > h2 > b ")
#btitleList = soup.select("#contentDetailContent > p > span > strong")

btitleList = soup.select("#ABA-wrapper-box-set > div.ABA-view-body.ABA-article-contents > ul > li >a ")

desList = soup.select("#ABA-wrapper-box-set > div.ABA-view-body.ABA-article-contents > ul > li ")

print(desList)
for idx in range(len(btitleList)):
    
    if (idx>=0 and idx<4):
        db.newsletters.insert_one({'title':btitleList[idx].text.replace(':',''), 'url':btitleList[idx]['href'], 'desc':desList[idx].text, 'category':'시사 경제' })
    elif  (idx>=4 and idx<10):
        db.newsletters.insert_one({'title':btitleList[idx].text.replace(':',''), 'url':btitleList[idx]['href'], 'desc':desList[idx].text, 'category':'마케팅 트렌드' })
    elif  idx>=10:
        db.newsletters.insert_one({'title':btitleList[idx].text.replace(':',''), 'url':btitleList[idx]['href'], 'desc':desList[idx].text, 'category':'문학 매거진' })



