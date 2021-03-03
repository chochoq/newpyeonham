from flask import Flask, render_template, jsonify, request
from flask.helpers import url_for
import jwt
import datetime
import hashlib

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


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


@app.route('/index/insertSample', methods=['POST'])
def insertSample():
    letter1 = {
        'title': 'ㅇㅎ! 아하레터',
        'url': 'https://page.stibee.com/subscriptions/61765?groupIds=56635',
        'category': '자기계발',
        'img': 'https://s3.ap-northeast-2.amazonaws.com/img.stibee.com/26042_list_61765_header_image.jpg?v=1598419760',
        'desc': '작심삼일 반복하면 못할것이 없습니다'
    }

    letter2 = {
        'title': '그랩의 IT 뉴스레터',
        'url': 'https://maily.so/grabnews',
        'category': 'IT',
        'img': 'https://cdn.maily.so/maily66df3af8fbfb998cda1caa2f235e7e8f1600609966',
        'desc': '매주 월요일, IT 콘텐츠 큐레이션 & 잘 읽히는 IT 개발지식을 제공합니다.'
    }

    letter3 = {
        'title': 'newneek',
        'url': 'https://newneek.co/?utm_medium=newsletter&utm_source=newneek&utm_campaign=dec21',
        'category': '종합',
        'img': 'https://newneek.co/static/media/gosum-home.7b7f5b6b.png',
        'desc': '월/수/금 아침마다 세상 돌아가는 소식을 메일로 받아보세요'
    }

    db.newsletters.insert_one(letter1)
    db.newsletters.insert_one(letter2)
    db.newsletters.insert_one(letter3)

    return jsonify({'result': 'success'})


# 로그인
SECRET_KEY = 'WECANDOANYTHING'


@app.route('/index/login', methods=['POST'])
def login():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})

@app.route('/index/insert', methods=['POST'])
def post_articles():
    url_receive = request.form['url_give']
    title_receive = request.form['title_give']
    desc_receive = request.form['desc_give']
    category_receive = request.form['category_give']

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
        'title_news': title_receive,
        'desc_news': desc_receive,
        'category_news': category_receive
    }

    db.newsletters.insert_one(doc)
    return jsonify({'msg': '저장완료'})


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
