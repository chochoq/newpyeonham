from flask import Flask, render_template, jsonify, request
import jwt
import datetime
import hashlib

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
def signup():
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    
    pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    db.user.insert_one({'name': name, 'email': email, 'password': pw_hash})

    return jsonify({'result': 'success'})


# 로그인
SECRET_KEY = 'WECANDOANYTHING'
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

# 검색
@app.route('/index/search', methods=['GET'])
def show_stars():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': 'list 연결되었습니다!'})

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


def delete_letter():
    title_receive = request.form['title_give']
    db.letters.delete_one({'title': title_receive})
    return jsonify({'msg': '삭제'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
