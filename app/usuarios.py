from flask import jsonify, request

# Lista para armazenar os dados temporariamente
usuarios = [
    {
        "id": 1,
        "nome": "lucas de jesus",
        "idade": 24,
        "solteiro": True
    }
]

def listar_usuarios():
    """Retorna todos os usuários."""
    return jsonify(usuarios)

def criar_usuario():
    """Cria um novo usuário a partir do JSON enviado na requisição."""
    novo_usuario = request.get_json()
    novo_usuario["id"] = len(usuarios) + 1  # Gera um ID único
    usuarios.append(novo_usuario)
    return jsonify({"mensagem": "Usuário criado com sucesso!", "usuario": novo_usuario}), 201

def atualizar_usuario(id):
    """Atualiza um usuário pelo ID."""
    dados = request.get_json()
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario.update(dados)
            return jsonify({"mensagem": "Usuário atualizado!", "usuario": usuario})
    
    return jsonify({"erro": "Usuário não encontrado"}), 404

def deletar_usuario(id):
    """Remove um usuário pelo ID."""
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario["id"] != id]
    return jsonify({"mensagem": f"Usuário {id} deletado com sucesso!"})
