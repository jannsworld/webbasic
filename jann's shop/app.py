from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjann

#HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# 주문을 받는 API
@app.route('/order', methods=['POST'])
def make_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    memo_receive = request.form['memo_give']

    doc = {
        'name':name_receive,
        'count':count_receive,
        'address':address_receive,
        'memo': memo_receive
    }
    db.order.insert_one(doc) #doc 형태로 db 저장

    return jsonify({'msg': '주문 해주셔서 감사합니다:) 행복이 곧 배송될 거에요!'})

# 주문 보여주는 API
@app.route('/order', methods=['GET'])
def show_order():
    orders = list(db.order.find({}, {'_id':False}))
    return jsonify({'all_orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)