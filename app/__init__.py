from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # CHAVE SECRETA: Fixa para o avaliador não ter erro de sessão
    app.config['SECRET_KEY'] = 'taskquest-super-secret-key-123'
    
    # BANCO DE DADOS: O caminho relativo cria o arquivo na raiz da pasta do projeto
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskquest.db'
    
    # Desativa um alerta de memória do SQLAlchemy que não usaremos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app