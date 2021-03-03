from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('./chromedriver')

url = "https://brunch.co.kr/@moneyfire/256"
driver.get(url)
sleep(3)

driver.execute_script("window.scrollTo(0, 1000)")  # 1000픽셀만큼 내리기
sleep(1)
# 맨 밑까지 내리기
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(10)


req = driver.page_source
driver.quit()

soup = BeautifulSoup(req, 'html.parser')
images = soup.select(".tile_item._item ._image._listImage")


aTag = body > div.service_contents.article_contents.\#post_view.beyond_content > div.wrap_view_article.wrap_article.article_view_disable_selection > div.wrap_body_frame > div.wrap_body.text_align_left.finish_txt > h4:nth-child(15) > span > span > a


body > div.service_contents.article_contents.\#post_view.beyond_content > div.wrap_view_article.wrap_article.article_view_disable_selection > div.wrap_body_frame > div.wrap_body.text_align_left.finish_txt > h2   :nth-child(9)
body > div.service_contents.article_contents.\#post_view.beyond_content > div.wrap_view_article.wrap_article.article_view_disable_selection > div.wrap_body_frame > div.wrap_body.text_align_left.finish_txt > h2:nth-child(14)


body > div.service_contents.article_contents.\#post_view.beyond_content > div.wrap_view_article.wrap_article.article_view_disable_selection > div.wrap_body_frame > div.wrap_body.text_align_left.finish_txt > p:nth-child(10) > a
body > div.service_contents.article_contents.\#post_view.beyond_content > div.wrap_view_article.wrap_article.article_view_disable_selection > div.wrap_body_frame > div.wrap_body.text_align_left.finish_txt > p:nth-child(11) > span > span
body > div.service_contents.article_contents.\#post_view.beyond_content > div.wrap_view_article.wrap_article.article_view_disable_selection > div.wrap_body_frame > div.wrap_body.text_align_left.finish_txt > p:nth-child(12)



print(len(images))

for image in images:
    src = image["src"]
    print(src)

