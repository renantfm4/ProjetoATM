from datetime import datetime,date
import json
from operacoes import *

with open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_de_dados.json", "r") as arquivo:
    dados = json.load(arquivo) 

class Conta(Operacoes):

    def login(self, nome, cpf):
        
        for key in range(len(dados)):
            if dados[key].get("nome") == nome and dados[key].get("cpf") == cpf:
                print(f"Logged! {nome}")
                return key
        print("Usuário não encontrado")
        return False    
    

    def acessa_conta(self):
        nome, cpf = input("nome,cpf").split(" ") 
        if self.login(nome,cpf) != False:
            return
        else:
            
            print("Digite a operação desejada\n 1-Saque\n 2-Deposito \n 3-Pagamento Programado")
            x = input()
            if x == "1":self.sacar(self.login(nome,cpf));
            elif x == "2":self.depositar(self.login(nome,cpf))
            elif x == "3":self.PagamentoProgramado(self.login(nome,cpf))
            
    

conta1 = Conta()
conta1.acessa_conta() 