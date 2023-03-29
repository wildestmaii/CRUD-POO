from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class User:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

users = [User("admin", "1234"), User("admin1", "1234")]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['nome']
    senha = request.form['senha']

    for user in users:
        if user.usuario == usuario and user.senha == senha:
            return redirect(url_for('sucesso'))

    return redirect(url_for('falha'))

@app.route('/sucesso')
def sucesso():
    return "passa logo antes q eu mude de ideia..."

@app.route('/falha')
def falha():
    return "achou que ia entrar? achou errado otário!"

if __name__ == '__main__':
    app.run(debug=True)
