from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController


user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    response, status_code = UserController.register_user(
        request.get_json()
    )

    return jsonify(response), status_code


@user_bp.route('/login', methods=['POST'])
def login():
    response, status_code = UserController.login_user(
        request.get_json()
    )

    return jsonify(response), status_code