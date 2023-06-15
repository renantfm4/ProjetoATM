from datetime import datetime,date
import json
from operacoes import *

with open("Banco_de_dados.json", "r") as arquivo:
    dados = json.load(arquivo) 

class Conta(Operacoes):

    def login(self, cpf, senha):
        
        for key in range(len(dados)):
            if dados[key].get("senha") == senha and dados[key].get("cpf") == cpf:      
                return [True,key]    
        return [False]    
    

    def acessa_conta(self,cpf,senha):
       
        if self.login(cpf,senha)[0] == False:
            return "Usuário não encontrado"
        else:
            nome = dados[self.login(cpf,senha)[1]].get("nome")
            print(f"Logged! {nome}\n")
            print("Digite a operação desejada\n 1-Saque\n 2-Deposito \n 3-Pagamento Programado")
            x = input()
            if x == "1":self.sacar(self.login(nome,cpf));
            elif x == "2":self.depositar(self.login(nome,cpf))
            elif x == "3":
                nome_dest, cpf_dest = input("Digite o nome e o cpf do Destinatário").split(" ")
                self.PagamentoProgramado(index_dest=self.login(nome_dest, cpf_dest), index=self.login(nome,cpf))
            
    
