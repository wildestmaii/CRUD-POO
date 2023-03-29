from collections import defaultdict
from flask import Flask, render_template, request, redirect, url_for


class Capivara:
    def __init__(self, nome, idade, peso, cidade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.cidade = cidade

    def __str__(self):
        return f"{self.nome} - {self.idade} anos - {self.peso} kg - cidade {self.cidade}"


class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha


usuarios = [Usuario("admin", "1234"), Usuario("admin1", "1234")]


class Menu:
    def __init__(self, inserir, consultar, alterar, remover, exibir):
        self.inserir = inserir
        self.consultar = consultar
        self.alterar = alterar
        self.remover = remover
        self.exibir = exibir


opcoes = [Menu("0", "1", "2" "3", "4", "5")]


class Programa:
    def __init__(self):
        self.capivaras = defaultdict(list)

    def inserir_capivara(self, capivara):
        self.capivaras[capivara.nome].append(capivara)

    def consultar_capivara(self, nome):
        if nome in self.capivaras:
            return self.capivaras[nome]
        else:
            return []

    def alterar_capivara(self, nome, idade, peso, cidade):
        capivaras = self.consultar_capivara(nome)
        for capivara in capivaras:
            capivara.idade = idade
            capivara.peso = peso
            capivara.cidade = cidade

    def remover_capivara(self, nome):
        del self.capivaras[nome]

    def exibir_capivaras(self):
        for nome, capivaras in self.capivaras.items():
            for capivara in capivaras:
                print(capivara)


programa = Programa()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    nome = request.form['nome']
    senha = request.form['senha']

    for usuario in usuarios:
        if usuario.usuarios == nome and usuario.senha == senha:
            return redirect(url_for('/menu'))

    return redirect(url_for('/login'))


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    receber = request.form['opcoes']
    '''
    consultar = request.form['consultar']
    alterar = request.form['alterar']
    remover = request.form['remover']
    exibir = request.form['exibir']
    '''

    for op in opcoes:
        if op.opcoes == 1:
            return redirect(url_for('/inserir_capivara'))

        elif op.inserir == 2:
            return redirect(url_for('/consultar_capivara'))

        elif op.inserir == 3:
            return redirect(url_for('/alterar_capivara'))

        elif op.inserir == 4:
            return redirect(url_for('/remover_capivara'))

        elif op.inserir == 5:
            return redirect(url_for('/exibir_capivaras'))


@app.route('/inserir_capivara', methods=['POST'])
def inserir_capivara():
    nome = request.form['nome']
    idade = int(request.form['idade'])
    peso = float(request.form['peso'])
    cidade = request.form['cidade']
    capivara = Capivara(nome, idade, peso, cidade)
    programa.inserir_capivara(capivara)
    #return 'Capivara inserida com sucesso!'
    return redirect(url_for('/menu'))


@app.route('/consultar_capivara', methods=['GET', 'POST'])
def consultar_capivara():
    if request.method == 'POST':
        nome = request.form['nome']
        capivaras = programa.consultar_capivara(nome)
        if capivaras:
            return render_template('consulta.html', capivaras=capivaras)
        else:
            return render_template('consulta.html', mensagem='Capivara não encontrada.')
    return render_template('consulta.html')


@app.route('/alterar_capivara', methods=['GET', 'POST'])
def alterar_capivara():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        peso = float(request.form['peso'])
        cidade = request.form['cidade']
        programa.alterar_capivara(nome, idade, peso, cidade)
        return 'Capivara alterada com sucesso!'
    return render_template('alterar.html')


@app.route('/remover_capivara', methods=['GET', 'POST'])
def remover_capivara():
    if request.method == 'POST':
        nome = request.form['nome']
        programa.remover_capivara(nome)
        return 'Capivara removida com sucesso!'
    return render_template('remover.html')


if __name__ == '__main__':
    app.run(debug=True)
