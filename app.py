from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
# 회원가입
@app.route('/index/signup', methods=['POST'])
def write_review():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


# 로그인
@app.route('/index/login', methods=['POST'])
def login():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


# 뉴스레터 추가
@app.route('/index/insert', methods=['POST'])
def insert_newsletter():
    title_receive = request.form['title_give']
    category_receive = request.form['category_give']
    url_receive = request.form['url_give']
    desc_receive = request.form['desc_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title': title,
        'image': image,
        'desc': desc,
        'url': url_receive,
        'title': title_receive,
        'category': category_receive,
        'desc_newsletter': desc_receive
    }
    db.newsletters.insert_one(doc)

    return jsonify({'msg': '뉴스레터 완료되었습니다'})


# 좋아요 관심
@app.route('/index/like', methods=['POST'])
def like():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


# 구독페이지 숨김
@app.route('/index/hide', methods=['POST'])
def hide():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


# 코멘트
@app.route('/index/comment', methods=['POST'])
def comment():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


# 검색
@app.route('/index/search', methods=['GET'])
def search():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '이 요청은 GET!'})


# 카테고리분류
@app.route('/index/category', methods=['GET'])
def category():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '이 요청은 GET!'})


# 새로고침
@app.route('/index/refresh', methods=['GET'])
def refresh():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
