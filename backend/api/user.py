from flask import request, jsonify
from . import api_bp
from database import db
from model.user import User
import os
import uuid
from werkzeug.utils import secure_filename

@api_bp.route('/user', methods=['POST'])
def user():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    birthday = data.get('birthday')
    number = data.get('number')
    img = data.get('img')

    user = User(name=name, email=email, birthday=birthday, number=number, img=img)

    db.session.add(user)
    db.session.commit()

    return jsonify({"name": name, "email": email, "birthday": birthday, "number": number, "img": img}), 202

@api_bp.route('/info', methods=['GET'])
def info():
    infos = User.query.all()

    data_list = [{"name": info.name, "email": info.email, "birthday": info.birthday, "number": info.number, "img": info.img} for info in infos]

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

@api_bp.route('/upload', methods=['POST'])
def upload():
    image = request.files.get('image')  # 圖片檔案
    title = request.form.get('title') 

    original_name = secure_filename(image.filename)  # 安全處理原始檔名
    ext = os.path.splitext(original_name)[1]        # 取得副檔名 (.jpg, .png...)

    # 建立新檔名：UUID + 副檔名
    new_filename = f"{title}{ext}"
    save_path = os.path.join("public/assets/users", new_filename)

    image.save(save_path)
    return jsonify({"newName": new_filename})