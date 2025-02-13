from flask import Flask
from flask_restx import Api, Resource
from logger.logging import AppLogger

logger = AppLogger().get_logger()

def create_app() -> Flask:
    app = Flask(__name__)


    # Importando as routes reais
    try:
        from routes import saudacao as greet_route  # Importa a rota de saudação
        from routes import soma as sum_route  # Importa a rota de soma
        
        # Registrando as Blueprints do flaks
        app.register_blueprint(greet_route.greet)
        app.register_blueprint(sum_route.sum)
        
        logger.info("Rotas configuradas com sucesso.")
    except ImportError as e:
        logger.error(f"Erro ao importar rotas: {e}")
        raise e

    return app
