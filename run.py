# Importamos a função create_app do módulo app
from app import create_app  

# Criamos a instância do aplicativo Flask chamando a função create_app
app = create_app()  

# Verificamos se o script está sendo executado diretamente
if __name__ == '__main__':  
    # Iniciamos o servidor Flask no modo debug
    app.run(debug=True)  
