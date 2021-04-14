from flask import jsonify, request, abort, render_template, session, redirect
from flask import current_app as app

bccdw = []
animes = []
viagens = []

class Usuario():
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

# Dicionário a preencher com o par id:usuario
# (onde id é a chave inteira e usuario é instância da classe Usuario)
usuarios = {}

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('teladecadastro.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        for id in usuarios.keys():
            usuario = usuarios[id]
            if nome == usuario.nome:
                return 'Usuário já existe.'
        novo = Usuario(nome, senha)
        usuarios[len(usuarios)+1] = novo

        return 'cadastro bem sucedido!'

    else:
        return abort(405)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('teladelogin.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        for id in usuarios.keys():
            usuario = usuarios[id]
            if nome == usuario.nome and senha == usuario.senha:
                session['usuario'] = usuario.nome
                return render_template('logou.html')
        return 'usuário ou senha incorretos'
    else:
        return abort(405)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/login')


@app.route('/teste')
def teste():
    if 'usuario' not in session:
        return abort(403)
    return session['usuario']


@app.route('/home')
def home():
    if 'usuario' not in session:
        return abort(403)
    return render_template('index.html')


@app.route("/chat", methods=['POST'])
def chat():
    if 'usuario' not in session:
        return abort(403)
    if request.method == 'POST':
        data = request.get_json()
        if data['chat'] == 'bccdw':
            bccdw.append(data)
            return jsonify(bccdw), 200
        elif data['chat'] == 'animes':
            animes.append(data)
            return jsonify(animes), 200
        elif data['chat'] == 'viagens':
            viagens.append(data)
            return jsonify(viagens), 200

@app.route('/chat/<chat>')
def le_chat(chat):
    if 'usuario' not in session:
        return abort(403)
    if chat == 'bccdw':
        return jsonify(bccdw), 200
    elif chat == 'animes':
        return jsonify(animes), 200
    elif chat == 'viagens':
        return jsonify(viagens), 200
    abort(404)
