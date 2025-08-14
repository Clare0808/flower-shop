from flask import request, jsonify
from . import api_bp
from database import db
from model.login import Login

@api_bp.route('/signin', methods=['POST'])
def signIn():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    login = Login(name=name, email=email, password=password)

    db.session.add(login)
    db.session.commit()

    return jsonify({"name": name, "email": email, "password": password}), 201

@api_bp.route('/login', methods=['GET'])
def login():
    infos = Login.query.all()

    data_list = [{"name": info.name, "email": info.email, "password": info.password} for info in infos]

    return jsonify({"data": data_list}), 200

@api_bp.route('/login/modify', methods=['PUT'])
def loginModify():
    data = request.get_json()

    email = data.get('email')
    title = data.get('title')
    value = data.get('value')

    login = Login.query.filter_by(email=email).first() # 尋找第一個符合的資料

    setattr(login, title, value) # 設定欄位的值
    db.session.commit()

    return jsonify({"email": email, "title": title, "value": value})