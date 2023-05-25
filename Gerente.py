import json



class Gerente():
#Criação da classe gerente para melhor visualização, focar na classe conta e usuário!!!
    def RegistrarConta():
        #nome, cpf, telefone, endereco = input("Insira os dados do cliente!").split(" ")
        #dados = f'{nome}, {cpf}, {telefone}, {endereco}'
        with open("Banco.json", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        print(dados)
    def deletarConta():
        pass
    def ListarContas():
        pass

class Usuario():
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf,
        self.telefone = telefone
        self.endereco = endereco,
        
gerente1 = Gerente
gerente1.RegistrarConta()