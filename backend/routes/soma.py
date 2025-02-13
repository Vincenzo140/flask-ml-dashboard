from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from schemas.somas import Soma  
from logger.logging import AppLogger

logger = AppLogger().get_logger()

sum = Blueprint('soma', __name__)

@sum.route("/soma", methods=["POST"])
def soma():
    try:
        # Obteem os dados do corpo da requisição
        data = request.get_json()

        # Validar os dados usando Pydantic do meu schema com basemodel
        soma_data = Soma(**data)

        # aqui ele realiza a soma
        result = soma_data.number1 + soma_data.number2

        # Log e resposta
        logger.info(f"O resultado da soma é: {result}")
        return jsonify({"result": result}), 200

    except ValidationError as e:
        logger.error(f"Erro de validação: {e}")
        return jsonify({"error": "Dados inválidos tente novamente a request", "details": e.errors()}), 400
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        return jsonify({"error": "Erro interno do servidor"}), 500
