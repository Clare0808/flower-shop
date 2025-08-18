from flask import request, jsonify
from . import api_bp
from database import db
from model.review import Review

@api_bp.route("/storereview", methods=["POST"])
def storereview():
    data = request.get_json()

    name = data.get("name")
    img = data.get("img")
    date = data.get("date")
    score = data.get("score")
    content = data.get("content")

    review = Review(name=name, img=img, date=date, score=score, content=content)

    db.session.add(review)
    db.session.commit()

    return jsonify({"name": name, "img": img, "date": date, "score": score, "content": content})

@api_bp.route("/getreview", methods=["GET"])
def getreview():
    infos = Review.query.all()

    data_list = [{"name": info.name, "img": info.img, "date": info.date, "score": info.score, "content": info.content} for info in infos]

    return jsonify({"data": data_list}), 200