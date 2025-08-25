from flask import request, jsonify
from . import api_bp
from database import db
from model.comment import Comment

@api_bp.route("/sendcomment", methods=["POST"])
def sendcomment():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    number = data.get("number")
    date = data.get("date")
    content = data.get("content")

    comment = Comment(name=name, email=email, number=number, date=date, content=content)

    db.session.add(comment)
    db.session.commit()

    return jsonify({"name": name, "email": email, "number": number, "date": date, "content": content})

@api_bp.route("/getcomment", methods=["GET"])
def getcomment():
    infos = Comment.query.all()

    data_list = [{"name": info.name, "email": info.email, "number": info.number, "date": info.date, "content": info.content} for info in infos]

    return jsonify({"data": data_list}), 200