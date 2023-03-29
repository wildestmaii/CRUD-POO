#codigo com bd dando erro
#ERRO ATUAL:
# Traceback (most recent call last):
#  File "main.py", line 102, in <module>
#    programa.inserir_capivara(capivara)
#  File "main.py", line 60, in inserir_capivara
#    comando = f"INSERT INTO capivaras (id, nome, sexo, peso, cidade) values ('{self.id}','{self.nome}', '{self.sexo}', '{self.peso}', '{self.cidade}')"
#AttributeError: 'Programa' object has no attribute 'id' 
from flask import Flask, render_template, request, flash, redirect, jsonify
import random
import string
import mysql.connector
from collections import defaultdict
from werkzeug.security import generate_password_hash, check_password_hash
import datetime as dt


class Banco:
    def __init__(self, host="localhost", user="root", password="teste", database ="capivarinhas"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        def conectar(self):
    
          self.conexao = mysql.connector.connect(host = self.host, user = self.user, password = self.password,database = self.database)
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()

    def executarDQL(self, comando): 
        self.conectar()
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() 
        self.desconectar()
        return print(resultado)

    def executarDML(self, comando):
        self.conectar()
        self.cursor.execute(comando)
        self.conexao.commit() 
        self.desconectar()


  
class Capivara:
    def __init__(self, id, nome, sexo, peso, cidade):
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.cidade = cidade

  #olhar
    def __str__(self):
        return f"{self.id} - {self.nome} - nasceu em {self.sexo} - {self.peso} kg - {self.cidade}"



class Programa:
    def __init__(self):
        self.capivaras = defaultdict(list)

    def inserir_capivara( Capivara):
       
        comando = f"INSERT INTO capivaras (id, nome, sexo, peso, cidade) values ('{id}','{nome}', '{sexo}', '{peso}', '{cidade}')"
        Banco.dml(comando)

    def consultar_capivara(self, id):
        comando = f"'SELECT * FROM capivaras WHERE id = {id}'"
        resultado = Banco.dql(comando)
        return resultado

    def alterar_capivara(self, id, nome, sexo, peso, cidade):
        comando = f"UPDATE capivaras SET nome ='{nome}', sexo = '{sexo}', peso = '{peso}', cidade = '{cidade}' WHERE id ='{id}'"
        Banco.dml(comando)

    def remover_capivara(self, id):
        comando = f"DELETE FROM capivaras WHERE id ='{id}'"
        Banco.dml(comando)

    def exibir_capivaras(self):
        comando = f"SELECT * FROM capivaras'"
        resultado = Banco.dql(comando)
        return resultado
                
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
  

#####mudar tipos de dados
    if opcao == "1":
        nome = input("Digite o nome da capivara: ")
        sexo = input("Digite o sexo da capivara: ")
        peso = float(input("Digite o peso da capivara: "))
        cidade = input("Digite a cidade da capivara: ")
        capivara = Capivara(nome=nome, sexo=sexo, peso=peso, cidade=cidade)
        programa.inserir_capivara(capivara)
        print(f"Capivara inserida com ID {capivara.id}")

    elif opcao == "2":
        nome = input("Digite o ID da capivara: ")
        capivaras = programa.consultar_capivara(id)
        if capivaras:
            for capivara in capivaras:
                print(capivara)
        else:
            print("Capivara não encontrada.")

    elif opcao == "3":
        id = input("Digite o ID da capivara que deseja mudar: ")
        peso = float(input("Digite o novo peso da capivara: "))
        cidade = input("Digite a nova cidade da capivara: ")
        programa.alterar_capivara(id, peso, cidade)

    elif opcao == "4":
        nome = input("Digite o ID da capivara que deseja remover: ")
        programa.remover_capivara(id)

    elif opcao == "5":
        programa.exibir_capivaras()

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")
   