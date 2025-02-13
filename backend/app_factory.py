from flask import Flask
from flask_restx import Api, Resource
from logger.logging import AppLogger

# Criação do logger
logger = AppLogger().get_logger()

# Função que cria o aplicativo Flask
def create_app() -> Flask:
    # Inicializando a aplicação Flask
    app = Flask(__name__)

    # Inicializando a API com Swagger
    api = Api(app, 
              title="Flask-ml-dashboard",
              version="1.1.0",
              description="Uma simples API sobre saudação e soma",
              contact={
                  "name": "Vincenzo Amendola",
                  "github": "https://github.com/Vincenzo140",
                  "email": "vincenzo.amendola141@gmail.com",
                  "linkedin": "https://www.linkedin.com/in/vincenzo-amendola-9aab38264/",
              },
              swagger_ui_parameters={
                  "syntaxHighlight.theme": "monokai",
                  "layout": "BaseLayout",
                  "filter": True,
                  "tryItOutEnabled": True,
                  "onComplete": "Ok",
                  "docExpansion": "full",
                  "showExtensions": True,
                  "apisSorter": "alpha",
                  "supportedSubmitMethods": ["get", "post"],
                  "defaultModelsExpandDepth": 0,
              })

    # Importando as rotas reais
    try:
        from routes import saudacao as greet_route  # Importa a rota de saudação
        from routes import soma as sum_route  # Importa a rota de soma
        
        # Registrando as Blueprints
        app.register_blueprint(greet_route.greet)
        app.register_blueprint(sum_route.sum)
        
        logger.info("Rotas configuradas com sucesso.")
    except ImportError as e:
        logger.error(f"Erro ao importar rotas: {e}")
        raise e

    return app
