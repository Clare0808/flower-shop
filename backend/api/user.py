from flask import request, jsonify
from . import api_bp
from database import db
from model.user import User

@api_bp.route('/user', methods=['POST'])
def user():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    birthday = data.get('birthday')
    number = data.get('number')

    user = User(name=name, email=email, birthday=birthday, number=number)

    db.session.add(user)
    db.session.commit()

    return jsonify({"name": name, "email": email, "birthday": birthday, "number": number}), 202

@api_bp.route('/info', methods=['GET'])
def info():
    infos = User.query.all()

    data_list = [{"name": info.name, "email": info.email, "birthday": info.birthday, "number": info.number} for info in infos]

    return jsonify({"data": data_list}), 203

@api_bp.route('/modify', methods=['PUT'])
def modify():
    data = request.get_json()

    email = data.get('email')
    title = data.get('title')
    value = data.get('value')

    user = User.query.filter_by(email=email).first() # 尋找第一個符合的資料

    setattr(user, title, value) # 設定欄位的值
    db.session.commit()

    return jsonify({"email": email, "title": title, "value": value})