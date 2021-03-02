from flask import Flask, render_template, jsonify, request

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
@app.route('/review', methods=['POST'])
def write_review():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': '이 요청은 POST!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': '이 요청은 GET!'})


def delete_letter():
    title_receive = request.form['title_give']
    db.letters.delete_one({'title': title_receive})
    return jsonify({'msg': '삭제'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

