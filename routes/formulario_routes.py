from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identify
from controllers.formulario_controller import formulario_controller

formulario_bp = Blueprint('Formulario',__name__)

@formulario_bp.route('/', methods=['POST'])
@jwt_required()
def create_formulario():
    user_id = get_jwt_identify()
    return jsonify(formularioController.create_formulario(user_id, request.get_json()))