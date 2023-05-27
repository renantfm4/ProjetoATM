import json

# Carregando o arquivo json dentro da variavel "dados"
with open("C:\WORKSPACE\Python\ATM\Banco_de_dados.json",  encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
# Variavel que direcionára as modificação no arquivo json
carregar_arquivo = open("C:\WORKSPACE\Python\ATM\Banco_de_dados.json","w")



class Gerente():
#Criação da classe gerente para melhor visualização, focar na classe conta e usuário!!!
    def RegistrarConta():

        nome, cpf, telefone, endereco = input("Insira os dados do cliente! (nome), (cpf), (telefone), (endereco)").split(" ")                      

        dados.append({"nome":nome, "cpf":cpf, "telefone":telefone, "endereco":endereco})
        
        json.dump(dados, carregar_arquivo, indent=6)

        
        
         

    def deletarConta():
        nome, cpf = input("Coloque o nome do cliente e suas senha para a remoção").split(" ")
        try:
            for i in range(len(dados)):
                if (dados[i].get("nome") == nome) and (dados[i].get("cpf") == cpf):
                    dados.pop(i)
                    json.dump(dados, carregar_arquivo, indent=6)
                else:
                     pass
        except IndexError:
             print("Usuário não encontrado!")
                 
                 
       



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