from app import create_app, db
from app.models.tasks import Task
from app.models.user import User

app = create_app()

with app.app_context():
    # TESTE DE DIAGNÓSTICO:
    print("Tabelas detectadas pelo SQLAlchemy:", db.metadata.tables.keys())
    
    print("Criando banco de dados...")
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Setup concluído com sucesso!")