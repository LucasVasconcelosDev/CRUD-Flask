# Importamos Blueprint para definir um conjunto de rotas e jsonify para retornar respostas JSON
from flask import Blueprint, jsonify
from app.usuarios import listar_usuarios, criar_usuario, atualizar_usuario, deletar_usuario  

# Criamos um Blueprint chamado 'api_routes', que agrupa as rotas da API
api_routes = Blueprint('api_routes', __name__)  

# === ROTAS ANTIGAS ===

# Definimos uma rota para '/ping' que aceita requisições GET
@api_routes.route('/ping', methods=['GET'])  
def ping():  
    return jsonify({"message": "Pong!"})  

# Definimos uma rota para '/marco' que aceita requisições GET
@api_routes.route('/marco', methods=['GET'])  
def marco():  
    return jsonify({"message": "Polo!"})  

# Rota GET para informações sobre Lucas
@api_routes.route('/lucas', methods=['GET'])
def lucas():
    return jsonify({
        "nome": "lucas de jesus",
        "idade": 24,    
        "solteiro": True,  
        "notas": [8, 9.5, 10],
        "endereco": {
            "rua": "rua dos estudantes",
            "numero": 100  
        }
    })

# === NOVAS ROTAS DE USUÁRIOS ===

# Rota GET para listar usuários
api_routes.route('/usuarios', methods=['GET'])(listar_usuarios)

# Rota POST para criar usuário
api_routes.route('/usuarios', methods=['POST'])(criar_usuario)

# Rota PUT para atualizar usuário
api_routes.route('/usuarios/<int:id>', methods=['PUT'])(atualizar_usuario)

# Rota DELETE para remover usuário
api_routes.route('/usuarios/<int:id>', methods=['DELETE'])(deletar_usuario)
