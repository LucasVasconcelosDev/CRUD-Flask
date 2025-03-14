# Importamos a função create_app do módulo app
from app import create_app  
from flask_cors import CORS  # Importamos o CORS para ocorrer comunicação entre a pagina WEB e o servidor

# Criamos a instância do aplicativo Flask chamando a função create_app
app = create_app()  

# Habilitamos CORS para permitir requisições da página HTML
CORS(app)

# Verificamos se o script está sendo executado diretamente
if __name__ == '__main__':  
    # Iniciamos o servidor Flask no modo debug
    app.run(debug=True)  
