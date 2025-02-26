# Importamos Blueprint para definir um conjunto de rotas e jsonify para retornar respostas JSON
from flask import Blueprint, jsonify  

# Criamos um Blueprint chamado 'api_routes', que agrupa as rotas da API
api_routes = Blueprint('api_routes', __name__)  

# Definimos uma rota para '/ping' que aceita requisições GET
@api_routes.route('/ping', methods=['GET'])  
def ping():  
    # Retorna uma resposta JSON com a mensagem "Pong!"
    return jsonify({"message": "Pong!"})  
