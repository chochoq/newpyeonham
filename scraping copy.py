from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

driver = webdriver.Chrome('./chromedriver')


url2 = "https://m.blog.naver.com/yoyoland/221846052931"

driver.get(url2)
sleep(3)

# 맨 밑까지 내리기
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)


req = driver.page_source
driver.quit()

soup = BeautifulSoup(req, 'html.parser')

btitleList = soup.select("#SE-e0b12b07-8162-426b-807d-90417ba0c65e > div > div > div")

print(btitleList)
""" for idx in range(len(btitleList)):
    
    if (idx>=0 and idx<4):
        db.newsletters.insert_one({'title':btitleList[idx].text.replace(':',''), 'url':btitleList[idx]['href'], 'desc':desList[idx].text, 'category':'시사 경제' })
    elif  (idx>=4 and idx<10):
        db.newsletters.insert_one({'title':btitleList[idx].text.replace(':',''), 'url':btitleList[idx]['href'], 'desc':desList[idx].text, 'category':'마케팅 트렌드' })
    elif  idx>=10:
        db.newsletters.insert_one({'title':btitleList[idx].text.replace(':',''), 'url':btitleList[idx]['href'], 'desc':desList[idx].text, 'category':'문학 매거진' })
 """