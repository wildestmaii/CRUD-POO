from collections import defaultdict


class Capivara:
    def __init__(self, nome, sexo, peso, cidade):
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.cidade = cidade

    def __str__(self):
        return f"{self.nome} - {self.sexo} anos - {self.peso} kg - cidade {self.cidade}"


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

    def alterar_capivara(self, nome, sexo, peso, cidade):
        capivaras = self.consultar_capivara(nome)
        for capivara in capivaras:
            capivara.sexo = sexo
            capivara.peso = peso
            capivara.cidade = cidade

    def remover_capivara(self, nome):
        del self.capivaras[nome]

    def exibir_capivaras(self):
        for nome, capivaras in self.capivaras.items():
            for capivara in capivaras:
                print(capivara)


programa = Programa()

logado = False
usuario = "admin"
senha = "1234"

while not logado:
    user = input("Digite o usuário: ")
    pwd = input("Digite a senha: ")

    if user == usuario and pwd == senha:
        logado = True
    else:
        print("Usuário ou senha incidaderetos.")

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
        sexo = int(input("Digite o sexo da capivara: "))
        peso = float(input("Digite o peso da capivara: "))
        cidade = input("Digite a cidade da capivara: ")
        capivara = Capivara(nome, sexo, peso, cidade)
        programa.inserir_capivara(capivara)

    elif opcao == "2":
        nome = input("Digite o nome da capivara: ")
        capivaras = programa.consultar_capivara(nome)
        if capivaras:
            for capivara in capivaras:
                print(capivara)
        else:
            print("Capivara não encontrada.")

    elif opcao == "3":
        nome = input("Digite o nome da capivara: ")
        sexo = int(input("Digite o nova sexo da capivara: "))
        peso = float(input("Digite o novo peso da capivara: "))
        cidade = input("Digite a nova cidade da capivara: ")
        programa.alterar_capivara(nome, sexo, peso, cidade)

    elif opcao == "4":
        nome = input("Digite o nome da capivara: ")
        programa.remover_capivara(nome)

    elif opcao == "5":
        programa.exibir_capivaras()

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")
