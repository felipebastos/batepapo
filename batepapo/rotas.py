from flask import jsonify, request, abort, render_template, session, redirect
from flask import current_app as app

# entidades do sistema
from batepapo.entidades import usuarios, Usuario

# gerenciador de acesso do projeto
from batepapo import loginmanager

# controle de acesso do plugin
from flask_login import login_user, logout_user, login_required, current_user

bccdw = []
animes = []
viagens = []

loginmanager.login_view = '/login'



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
                login_user(usuario)
                return render_template('logou.html')
        return 'usuário ou senha incorretos'
    else:
        return abort(405)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/teste')
@login_required
def teste():
    return current_user.nome


@app.route('/home')
@login_required
def home():
    return render_template('index.html')


@app.route("/chat", methods=['POST'])
@login_required
def chat():
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
@login_required
def le_chat(chat):
    if chat == 'bccdw':
        return jsonify(bccdw), 200
    elif chat == 'animes':
        return jsonify(animes), 200
    elif chat == 'viagens':
        return jsonify(viagens), 200
    abort(404)
