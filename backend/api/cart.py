from flask import request, jsonify
from . import api_bp
from database import db
from model.cart import Cart

@api_bp.route("/storecart", methods=["POST"])
def storecart():
    data = request.get_json()

    email = data.get("email")
    name = data.get("name")
    price = data.get("price")
    img = data.get("img")
    quantity = data.get("quantity")
    total = data.get("total")

    cart = Cart(email=email, name=name, price=price, img=img, quantity=quantity, total=total)

    db.session.add(cart)
    db.session.commit()

    return jsonify({"email": email, "name": name, "price": price, "img": img, "quantity": quantity, "total": total})

@api_bp.route("/getcart", methods=["GET"])
def getcart():
    infos = Cart.query.all()

    data_list = [{"email": info.email, "name": info.name, "price": info.price, "img": info.img, "quantity": info.quantity, "total": info.total} for info in infos]

    return jsonify({"data": data_list}), 200