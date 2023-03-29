1
from models import Capivaras

class Capivara():
    def get(self, id):
        capivara = Capivaras.query.filter_by(id=id).first()
        try:
            response = {
                'nome':capivara.nome,
                'id':capivara.id,
                'cidade':capivara.cidade,
                'sexo': capivara.sexo
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Capivara não encontrada'
            }
        return response
    
    def put(self, id, data):
        capivara = Capivaras.query.filter_by(id=id).first()
        capivara.nome = data['nome']
        capivara.cidade = data['cidade']
        capivara.sexo = data['sexo']
        capivara.peso = data['peso']
        capivara.save()

        response = {
            'id':capivara.id,
            'nome':capivara.nome,
            'peso':capivara.peso,
            'cidade':capivara.cidade,
            'sexo':capivara.sexo  
        }
        return response
    
    def delete(self, id):
        capivara = Capivaras.query.filter_by(id=id).first()
        mensagem = f'Capivara {capivara.nome} foi excluida com sucesso'
        capivara.delete()
        return {'status':'sucesso', 'mensagem':mensagem}
  
class ListaCapivaras():

    def get(self):
        capivaras = Capivaras.query.all()
        response = [{'id':capivara.id, 'nome':capivara.nome, 'peso':capivara.peso, 'cidade':capivara.cidade, 'sexo':capivara.sexo} for capivara in capivaras]  
        return response
    
    def post(self, data):
        # data = request.json
        capivara = Capivaras(nome=data['nome'], peso=data['peso'], cidade=data['cidade'], sexo=data['sexo'])
        capivara.save()
        response = {
            'nome':capivara.nome,
            'peso':capivara.peso,
            'sexo':capivara.sexo,
            'cidade':capivara.cidade,
            'id':capivara.id
        }
        return response


if __name__ == '__main__':
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
            print(f"Opção selecionada = {opcao}")
            data = {}
            data.update(nome = input("Digite o nome da capivara: "))
            data.update(sexo = input("Digite o sexo da capivara: "))
            data.update(cidade = input("Digite a cidade da capivara: "))
            data.update(peso = float(input("Digite o peso da capivara: ")))
            response = ListaCapivaras.post(ListaCapivaras, data)
            print(response)

        elif opcao == "2":
            print(f"Opção selecionada = {opcao}")
            id = input('Insira o id da Capivara para consulta: ')
            response = Capivara.get(Capivara, id)
            print(response)
            
        elif opcao == "3":
            print(f"Opção selecionada = {opcao}")
            id = input('Insira o id da Capivara que você deseja aterar os dados: ')
            data = {}
            data.update(nome = input("Digite o novo nome da capivara: "))
            data.update(sexo = input("Digite o novo sexo da capivara: "))
            data.update(cidade = input("Digite a nova cidade da capivara: "))
            data.update(peso = float(input("Digite o novo peso da capivara: ")))
            response = Capivara.put(Capivara, id, data)
            print(response)
            
        elif opcao == "4":    
            print(f"Opção selecionada = {opcao}")
            id = input('Insira o id da Capivara que você deseja remover: ')
            response = Capivara.delete(Capivara, id)
            print(response) 

        elif opcao == "5":
            print(f"Opção selecionada = {opcao}")
            response = ListaCapivaras.get(ListaCapivaras)
            print(response)

        elif opcao == "0":
            print(f"Opção selecionada = {opcao}")
            print("Até mais!!!!")
            break