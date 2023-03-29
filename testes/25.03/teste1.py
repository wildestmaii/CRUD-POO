import sqlite3
from collections import defaultdict

class Capivara:
    def __init__(self, nome, idade, peso, cor):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.cor = cor

    def __str__(self):
        return f"{self.nome} - {self.idade} anos - {self.peso} kg - cor {self.cor}"

class Programa:
    def __init__(self):
        self.conexao = sqlite3.connect('capivaras.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS capivaras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                peso REAL,
                cor TEXT
            );
        """)
        self.conexao.commit()

    def inserir_capivara(self, capivara):
        self.cursor.execute("""
            INSERT INTO capivaras (nome, idade, peso, cor) 
            VALUES (?, ?, ?, ?)
        """, (capivara.nome, capivara.idade, capivara.peso, capivara.cor))
        self.conexao.commit()

    def consultar_capivara(self, nome):
        self.cursor.execute("""
            SELECT nome, idade, peso, cor FROM capivaras
            WHERE nome = ?
        """, (nome,))
        resultado = self.cursor.fetchall()
        if resultado:
            capivaras = []
            for capivara in resultado:
                nome, idade, peso, cor = capivara
                capivaras.append(Capivara(nome, idade, peso, cor))
            return capivaras
        else:
            return []

    def alterar_capivara(self, nome, idade, peso, cor):
        self.cursor.execute("""
            UPDATE capivaras SET idade = ?, peso = ?, cor = ?
            WHERE nome = ?
        """, (idade, peso, cor, nome))
        self.conexao.commit()

    def remover_capivara(self, nome):
        self.cursor.execute("""
            DELETE FROM capivaras
            WHERE nome = ?
        """, (nome,))
        self.conexao.commit()

    def exibir_capivaras(self):
        self.cursor.execute("""
            SELECT nome, idade, peso, cor FROM capivaras
        """)
        resultado = self.cursor.fetchall()
        if resultado:
            for capivara in resultado:
                nome, idade, peso, cor = capivara
                print(Capivara(nome, idade, peso, cor))
        else:
            print("Não há capivaras cadastradas.")

programa = Programa()

while True:
    print("------ MENU ------")
    print("1. Inserir capivara")
    print("2. Consultar capivara")
    print("3. Alterar capivara")
    print("4. Remover capivara")
    print("5. Exibir capivaras")
    print("0. Sair")
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da capivara: ")
        idade = int(input("Digite a idade da capivara: "))
        peso = float(input("Digite o peso da capivara: "))
        cor = input("Digite a cor da capivara: ")
        capivara = Capivara(nome, idade, peso, cor)
        programa.inserir_capivara(capivara)
        print("Capivara cadastrada com sucesso.")

    elif opcao ==
