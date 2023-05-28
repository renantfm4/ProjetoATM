import json
import shutil
import tempfile
from glob import glob

with open("C:\WORKSPACE\Python\ATM\Banco_de_dados.json",  encoding="utf-8") as arquivo:
            dados = json.load(arquivo)


class Gerente():

    
    def RegistrarConta():

        
        # Variavel que direcionára as modificação no arquivo json
        carregar_arquivo = open("C:\WORKSPACE\Python\ATM\Banco_de_dados.json","w")

        nome, cpf, telefone, endereco = input("Insira os dados do cliente! (nome), (cpf), (telefone), (endereco)").split(" ")                      

        dados.append({"nome":nome, "cpf":cpf, "telefone":telefone, "endereco":endereco})
        
        json.dump(dados, carregar_arquivo, indent=6)

        
        
         

    def deletarConta():
    
        try:
            nome, cpf = input("Coloque o nome do cliente e suas senha para a remoção\n").split(" ")
            for i in range(len(dados)):
                if (dados[i].get("nome") == nome) and (dados[i].get("cpf") == cpf):
                    carregar_arquivo = open("C:\WORKSPACE\Python\ATM\Banco_de_dados.json","w")
                    dados.pop(i)
                    json.dump(dados, carregar_arquivo, indent=6)
                else:
                    print("Usuário não encontrado!, verifique os dados informados")
        except ValueError:
            print("Dados fornecidos incorretamente!")        
                 
       



    def ListarContas():
        for i in range(len(dados)):
            print(dados[i])

class Usuario():
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf,
        self.telefone = telefone
        self.endereco = endereco,
        
gerente1 = Gerente
gerente1.ListarContas()