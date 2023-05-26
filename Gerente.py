import json


with open("C:\WORKSPACE\Python\ATM\Banco_de_dados.json",  encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

class Gerente():
#Criação da classe gerente para melhor visualização, focar na classe conta e usuário!!!
    def RegistrarConta():

        nome, cpf, telefone, endereco = input("Insira os dados do cliente! (nome), (cpf), (telefone), (endereco)").split(" ")               

        carregar_arquivo = open("C:\WORKSPACE\Python\ATM\Banco_de_dados.json","w")
        dados.append({"nome":nome, "cpf":cpf, "telefone":telefone, "endereco":endereco})
        json.dump(dados, carregar_arquivo, indent=6)

        
        
         

    def deletarConta():
        nome, senha = input("Coloque o nome do cliente e suas senha para a remoção").split(" ")

        for i in dados:
            print(dados[i])



    def ListarContas():
        pass

class Usuario():
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf,
        self.telefone = telefone
        self.endereco = endereco,
        
gerente1 = Gerente
gerente1.deletarConta()