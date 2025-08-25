from flask import request, jsonify
from . import api_bp
from database import db
from model.buy import Buy

@api_bp.route("/storebuy", methods=["POST"])
def storebuy():
    data = request.get_json()

    email = data.get("email")
    product = data.get("product")
    price = data.get("price")
    img = data.get("img")
    quantity = data.get("quantity")
    total = data.get("total")

    buy = Buy(email=email, product=product, price=price, img=img, quantity=quantity, total=total)

    db.session.add(buy)
    db.session.commit()

    return jsonify({"email": email, "product": product, "price": price, "img": img, "quantity": quantity, "total": total})

@api_bp.route("/getbuy", methods=["GET"])
def getbuy():
    infos = Buy.query.all()

    data_list = [{"email": info.email, "product": info.product, "price": info.price, "img": info.img, "quantity": info.quantity, "total": info.total} for info in infos]

    return jsonify({"data": data_list}), 200