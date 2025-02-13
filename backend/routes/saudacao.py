from flask import Blueprint, jsonify
from logger.logging import AppLogger
from flask_restx import Api, Resource

logger = AppLogger().get_logger()

greet = Blueprint('saudacao', __name__)

## modelo simples de saudação 
@greet.get("/saudacao")
def saudacao():
        logger.info("Seja bem-vindo a api")
        return jsonify({"message": "Seja bem vindo a api!"}), 200
