# Importamos a classe Flask para criar o aplicativo
from flask import Flask  

# Função responsável por criar e configurar o aplicativo Flask
def create_app():  
    app = Flask(__name__)  # Criamos uma instância do Flask

    # Importamos as rotas e registramos o Blueprint no aplicativo
    from app.routes import api_routes  
    app.register_blueprint(api_routes)  

    return app  # Retornamos a instância do aplicativo Flask
