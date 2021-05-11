from flask_login import UserMixin
from batepapo import loginmanager, db

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))

    '''
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
    def get_id(self):
        for key in usuarios.keys():
            if self.nome == usuarios[key].nome:
                return str(key)
    '''


# Dicionário a preencher com o par id:usuario
# (onde id é a chave inteira e usuario é instância da classe Usuario)
#usuarios = {}

@loginmanager.user_loader
def loadUser(id):
    return Usuario.query.get(id)