from flask import request, jsonify
from . import api_bp
from database import db
from model.like import Like

@api_bp.route('/storelike', methods=['POST'])
def storelike():
    data = request.get_json()

    email = data.get('email')
    product = data.get('product')
    price = data.get('price')
    image = data.get('image')

    like = Like(email=email, product=product, price=price, image=image)

    db.session.add(like)
    db.session.commit()

    return jsonify({"email": email, "product": product, "price": price, "image": image}), 205

@api_bp.route('/getlike', methods=['GET'])
def getlike():
    infos = Like.query.all()

    data_list = [{"email": info.email, "product": info.product, "price": info.price, "image": info.image} for info in infos]

    return jsonify({"data": data_list}), 206

@api_bp.route('/delete', methods=["POST"])
def delete():
    data = request.get_json()
    
    like_id = data.get('like_id')

    like = Like.query.get(like_id)

    if like:
        db.session.delete(like)
        db.session.commit()
        return jsonify({"message": "刪除成功"}), 204
    else:
        return jsonify({"error": "找不到指定的 Like"}), 404