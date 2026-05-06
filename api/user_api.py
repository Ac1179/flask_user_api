from flask import Blueprint, request, jsonify
from service.user_service import UserService

user_bp = Blueprint("user_bp", __name__)
user_service = UserService()

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    res = user_service.register(username, password)
    return jsonify(res), res["code"]

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")
    res = user_service.login(username, password)
    return jsonify(res), res["code"]