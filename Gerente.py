import json


with open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_de_dados.json",  encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

with open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_gerente.json",  encoding="utf-8") as arquivo1:
            dados1 = json.load(arquivo1)

class Gerente():

    def login_gerente(self, cpf, senha):
        
        for key in range(len(dados)):
            if dados1[key].get("senha") == senha and dados1[key].get("cpf") == cpf:      
                return [True,key]    
        return [False]
         
    def RegistrarConta(self, nome, cpf, telefone, endereco, saldo, senha):

        
        # Variavel que direcionára as modificação no arquivo json
        carregar_arquivo = open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_de_dados.json","w")

        
                            

        dados.append({"nome":nome, "cpf":cpf, "telefone":telefone, "endereco":endereco, "saldo":saldo, "senha":senha, "Programados":"", "Extrado":""})
        
        json.dump(dados, carregar_arquivo, indent=6)

        
        
         

    def deletarConta(self, nome, cpf):
    
        try:
            
            for i in range(len(dados)):
                if (dados[i].get("nome") == nome) and (dados[i].get("cpf") == cpf):
                    carregar_arquivo = open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_de_dados.json","w")
                    dados.pop(i)
                    json.dump(dados, carregar_arquivo, indent=6)
                else:
                    print("Usuário não encontrado!, verifique os dados informados")
        except ValueError:
            print("Dados fornecidos incorretamente!")        
                 
       



    def ListarContas():
        for i in range(len(dados)):
            print(dados[i])


        
gerente1 = Gerente()
print(gerente1.login_gerente("12","12")[0])