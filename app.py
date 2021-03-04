from flask import Flask, render_template, jsonify, request
from flask.helpers import url_for
import jwt
import datetime
import hashlib
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

from pymongo import MongoClient

load_dotenv(verbose=True)

client = MongoClient('localhost', 27017)
db = client.dbsparta


## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    print(token_receive)

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"email": payload['email']})

        newsletters = list(db.newsletters.aggregate([{'$match': {'title': {'$nin': user_info['hide']}}},
                                                     {'$sample': {'size': 8}},
                                                     {'$project': {'_id': False}}
                                                     ]))

        like = user_info['like']

        if len(like) > 0:
            for letter in newsletters:
                if (letter['title'] in like):
                    letter['like'] = 1

        commentList = user_info['comment'];
        if len(commentList) > 0:
            for letter in newsletters:
                for comment in commentList:
                    if (letter['title'] == comment['title']):
                        letter['comment'] = comment['comment']

        return render_template('index.html', status=user_info, newsletters=newsletters)
    except jwt.ExpiredSignatureError:
        newsletters = list(db.newsletters.aggregate([{'$sample': {'size': 8}}, {'$project': {'_id': False}}]))
        return render_template('index.html', status="expire", newsletters=newsletters)
    except jwt.exceptions.DecodeError:
        newsletters = list(db.newsletters.aggregate([{'$sample': {'size': 8}}, {'$project': {'_id': False}}]))
        return render_template('index.html', newsletters=newsletters)
    # DB에서 저장된 단어 찾아서 HTML에 나타내기


## API 역할을 하는 부분
# 회원가입
@app.route('/index/signup', methods=['POST'])
def signup():
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']

    pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    db.user.insert_one({'name': name, 'email': email, 'password': pw_hash, 'hide': [], 'comment': [], 'like': []})

    return jsonify({'result': 'success'})


@app.route('/index/insertSample', methods=['POST'])
def insertSample():
    letter1 = {

            "title": "그랩의 IT 뉴스레터",
            "url": "https://maily.so/grabnews",
            "category": "IT",
            "image": "https://cdn.maily.so/maily66df3af8fbfb998cda1caa2f235e7e8f1600609966",
            "desc": "매주 월요일, IT 콘텐츠 큐레이션 & 잘 읽히는 IT 개발지식을 제공합니다."
        }


    letter2 = {

        "title": "ㅇㅎ! 아하레터",
        "url": "https://page.stibee.com/subscriptions/61765?groupIds=56635",
        "category": "자기계발",
        "image": "https://s3.ap-northeast-2.amazonaws.com/img.stibee.com/26042_list_61765_header_image.jpg?v=1598419760",
        "desc": "작심삼일 반복하면 못할것이 없습니다"
    }

    letter3 = {

        "title": "newneek",
        "url": "https://newneek.co/?utm_medium=newsletter&utm_source=newneek&utm_campaign=dec21",
        "category": "종합",
        "image": "https://newneek.co/static/media/gosum-home.7b7f5b6b.png",
        "desc": "월/수/금 아침마다 세상 돌아가는 소식을 메일로 받아보세요"
    }

    letter4 = {

        "title": "위클리 호박너구리",
        "url": "https://pumpkin-raccoon.com/newsletter",
        "category": "종합",
        "image": "https://pumpkin-raccoon.com/images/projects/newsletter-mockup.png",
        "desc": "취준생, 직장인을 위한 종합 경제 뉴스레터! IT, 경영, 산업, 스타트업 등 호박너구리의 관심이 듬뿍 담긴 지식을  매주 수요일, 5분만에 배워보세요!"
    }

    letter5 = {

        "title": "웬뉴",
        "url": "https://www.fastcampus.co.kr/page_wennew/?ref=letterist",
        "category": "트렌드",
        "image": "https://storage.googleapis.com/static.fastcampus.co.kr/prod/uploads/202008/103259-213/title.png",
        "desc": "매주 수요일 당신의 메일함으로 트렌디한 실무 소식이 찾아갑니다"
    }

    letter6 = {

        "title": "클링크 뉴스레터",
        "url": "https://page.stibee.com/subscriptions/93381?ref=letterist",
        "category": "마케팅팅",
        "image": "https://s3.ap-northeast-2.amazonaws.com/img.stibee.com/26382_list_93381_subscriptions_header_image.png?v=1606812270",
        "desc": "매 월 딱 한 번! 인플루언서 마케팅 업계의 따끈따끈한 소식을 모아 뉴스레터를 보내 드립니다. :) 지금 바로 구독해보세요!"
    }

    letter7 = {

        "title": "Moya 글로벌 뉴스",
        "url": "https://www.wisetranslate.net/moya/global_news/newsletter?ref=letterist",
        "category": "글로벌",
        "image": "https://www.wisetranslate.net/static/newsletter/images/banner-img.png",
        "desc": "해외 주요 기업 뉴스를 한글로 번역해서 매일 보내드립니다. 전문 번역사가 정확하게 번역한 글로벌 주요 기업 뉴스를 매일 받아볼 수 있습니다."
    }

    letter8 = {

        "title": "더슬랭",
        "url": "https://theslang.co/?ref=letterist",
        "category": "시사",
        "image": "https://cdn.imweb.me/upload/S20210205b19337d7869d2/f3665a00b5bb5.png",
        "desc": "밀레니얼 세대에게 정치 경제 사회 세계 이슈 취미 등 다양한 주제들에 대해 쉽고 재미있게 알려주는 무료 뉴스레터입니다. 당신의 삶에 관련된 다양한 사건과 정보들을 만나보세요!"
    }

    letter9 = {

        "title": "식물알림장",
        "url": "https://page.stibee.com/subscriptions/75404?ref=letterist",
        "category": "과학",
        "image": "https://s3.ap-northeast-2.amazonaws.com/img.stibee.com/31074_list_75404_header_image.png?v=1595157977",
        "desc": "샐러드연맹은 다양한 방식으로 식물을 알아가는 동물들의 단체에요. 단원들에게는 식물에 대한 이야기를 담은 📩 이메일 뉴스레터(식물 알림장)를 24절기에 무료로 보내드려요."
    }

    letter10 = {

        "title": "weekly D",
        "url": "https://www.notion.so/weekly-D-12b48b1a9fbd460ea0b3a9ad63d9046a",
        "category": "디자인",
        "image": "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F2f4a6374-3e61-4f57-82dc-6ef56b560246%2F_.png?table=block&id=12b48b1a-9fbd-460e-a0b3-a9ad63d9046a&width=2730&userId=2d906b43-bc1c-4410-a8eb-7f3977a741fc&cache=v2",
        "desc": "주로 국내 디자이너가 쓴 글이나 디자인 관련 글을 수집합니다. 매주 수요일 오전 8시에 만나요"
    }

    letter11 = {

        "title": "슬점",
        "url": "https://lnky.in/wiselunchtime?ref=letterist",
        "category": "음식",
        "image": "https://res.cloudinary.com/damirlzfy/image/upload/c_thumb,dpr_3.0,h_100,w_100/v1604838711/h138xjbmltrrrbuyza5l.jpg",
        "desc": "오늘 점심시간에 뭘 먹을지 고민되고, 동료와 또 무슨 주제로 얘기를 해야하나... 고민되시죠? 뉴스레터 슬점이 도와드립니다! 메뉴추천과 함께 가벼운 대화 주제들도 알려드려요. 화요일 아침마다 여러분의 메일함으로 찾아갈게요"
    }

    letter12 = {

        "title": "플롯레터",
        "url": "https://page.stibee.com/subscriptions/64956?ref=letterist",
        "category": "문화예술",
        "image": "https://s3.ap-northeast-2.amazonaws.com/img.stibee.com/26703_list_64956_header_image.PNG?v=1599380573",
        "desc": "바쁜 일상에도 교양은 포기할 수 없잖아요. 인문학과 교양, 한 주의 시작은 월요일 플롯레터의 쏠쏠한 지식과 함께하세요!"
    }

    letter13 = {

        "title": "두부 DuBu",
        "url": "https://page.stibee.com/subscriptions/98179?groupIds=73628&ref=letterist",
        "category": "부동산",
        "image": "https://s3.ap-northeast-2.amazonaws.com/img.stibee.com/39705_list_98179_subscriptions_header_image.png?v=1609745965",
        "desc": "부초(부동산초보)를 위한 부동산 트렌드 내집레터! 두부가 기다리는 부초는! 헌집줄게, '내집'다오를 열렬히 외치는 부초, 부동산 뉴스가 남얘기 같은 부초, 숫자, %만 나오면 까막눈이 되는 부초, 집값이 미쳤어...만 외치기보다 왜 그런지 알고 싶은 부초!"
    }

    letter14 = {

        "title": "큐레터, Q-Letter",
        "url": "https://qletter.i-boss.co.kr/",
        "category": "마케팅",
        "image": "https://s3.ap-northeast-2.amazonaws.com/img.stibee.com/4650_1605601286.png",
        "desc": "아이보스의 마케팅 내공 업그레이드 프로젝트! 마케터를 위한 아이디어 조각을 큐레이션 해 보내 드려요. 마케팅 뉴스, 트렌드, 책 등을 보면서 우리는 한 뼘씩 더 성장해갑니다. 구독, Q!"
    }

    letter15 = {

        "title": "Ogle",
        "url": "https://mailchi.mp/4dc5e88c3112/subscribe_ogle",
        "category": "문화예술",
        "image": "https://mcusercontent.com/9fd764107d75bd33827481d56/images/fed91c20-c7f9-4b73-ae7b-08963a4b7510.png",
        "desc": "뮤지컬, 연극, 오페라 등 공연과 관련된 다양한 소식과 이야기를 전해주는 뉴스레터입니다. 공연 러버가 들려주는 이야기를 매주 금요일에 만나보세요!"
    }

    letter16 = {

        "title": "디독",
        "url": "https://page.stibee.com/subscriptions/31254?ref=letterist",
        "category": "디자인",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXBHEcu4EZ5OahLOjvlXNX6jWGWCi8MEEHIg&usqp=CAU",
        "desc": "해외 디자인 아티클 번역 뉴스레터, 읽는 디자인 디독. 디독은 Design+讀(읽을 독)의 합성어로, 인사이트 넘치는 해외 디자인 아티클을 읽기 쉽게 번역하여 보내드립니다."
    }

    db.newsletters.insert_one(letter1)
    db.newsletters.insert_one(letter2)
    db.newsletters.insert_one(letter3)
    db.newsletters.insert_one(letter4)
    db.newsletters.insert_one(letter5)
    db.newsletters.insert_one(letter6)
    db.newsletters.insert_one(letter7)
    db.newsletters.insert_one(letter8)
    db.newsletters.insert_one(letter9)
    db.newsletters.insert_one(letter10)
    db.newsletters.insert_one(letter11)
    db.newsletters.insert_one(letter12)
    db.newsletters.insert_one(letter13)
    db.newsletters.insert_one(letter14)
    db.newsletters.insert_one(letter15)
    db.newsletters.insert_one(letter16)

    return jsonify({'result': 'success'})

# 로그인
SECRET_KEY = os.getenv('SECRET')


@app.route('/index/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    result = db.user.find_one({'email': email, 'password': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')  # .decode('utf-8')
        print('token', token)
        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


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

    image = soup.select_one('meta[property="og:image"]')['content']

    doc = {
        'image': image,
        'url': url_receive,
        'title': title_receive,
        'desc': desc_receive,
        'category': category_receive
    }

    db.newsletters.insert_one(doc)
    return jsonify({'msg': '저장완료'})


# 코멘트
@app.route('/index/comment', methods=['POST'])
def comment():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

    comment_receive = request.form['comment']
    title_receive = request.form['title']

    db.user.update_one({"email": payload['email']},
                       {"$push": {"comment": {"title": title_receive, "comment": comment_receive}}})

    return jsonify({'msg': title_receive + '에 코멘트를 작성했습니다.'})


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


@app.route('/api/list', methods=['GET'])
def show_letters():
    news_letters = list(db.newsletters.find({}, {'_id': False}))
    return jsonify({'news_letters': news_letters})


@app.route('/api/delete', methods=['POST'])
def delete_letters():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

    title_receive = request.form['title_give']
    db.user.update_one({"email": payload['email']}, {"$push": {"hide": title_receive}})

    return jsonify({'msg': '이제 [' + title_receive + '] 뉴스레터는 보이지않아요!'})


@app.route('/api/like', methods=['POST'])
def like_letters():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

    title_receive = request.form['title']
    is_like = request.form['isLike']
    print(title_receive, is_like)

    if is_like == 'true':
        db.user.update_one({"email": payload['email']}, {"$push": {"like": title_receive}})
        msg = title_receive + ' 좋아요!'
    else:
        db.user.update_one({"email": payload['email']}, {"$pull": {"like": title_receive}})
        msg = title_receive + '는 이제 안 좋아요..'

    return jsonify({'msg': msg})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
