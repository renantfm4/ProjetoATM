from datetime import datetime,date

import json

with open("Banco_de_dados.json", "r") as arquivo:
    dados = json.load(arquivo)



class Operacoes():
    

    def __init__(self):
        self.deposito = 0
        self.saque = 0

    def sacar(self, index, valor):
        
        saldo = dados[index].get("saldo")
        saque = dados[index].get("saque")
        if valor > 0 and valor <= saldo:
            
            saldo -= valor
            atualizar = {"saldo":saldo}
            dados[index].update(atualizar)

            carregar_arquivo = open("Banco_de_dados.json","w")
            json.dump(dados, carregar_arquivo, indent=6)

            saque += valor
            
            atualizar_saq = {"saque":saque}
            dados[index].update(atualizar_saq)
            return True
        else:
            return False
        
    def extrato(self, index):
        saque = dados[index].get("saque")
        deposito = dados[index].get("deposito")
        return f"Hoje suas transações totais foram: {saque}R$ em saques e {deposito}R$"
    
    def depositar(self, index, valor):
        deposito = dados[index].get("deposito")
        saldo = dados[index].get("saldo")
        if valor > 0:
            saldo += valor
            atualizar = {"saldo":saldo}
            dados[index].update(atualizar)

            deposito += valor
            
            atualizar_dep = {"deposito":deposito}
            dados[index].update(atualizar_dep)

            carregar_arquivo = open("Banco_de_dados.json","w")
            json.dump(dados, carregar_arquivo, indent=6)

            return True
        else:
            return False

    def PagamentoProgramado(self,index, valor, data_programada_str):
        try:
            saldo = dados[index].get("saldo")
    

            dia, mes, ano = map(int, data_programada_str.split('-'))
            data_programada = date(ano, mes, dia)
            data_atual = date.today()

            if valor > 0 and valor <= saldo:

                if data_programada > data_atual:
                    data_corrigida = data_programada.strftime("%d-%m-%Y")
                     
                    atualizar_prog = {"Programado":{valor:data_corrigida}}
                    dados[index].update(atualizar_prog)
                                

                    carregar_arquivo = open("Banco_de_dados.json","w")
                    json.dump(dados, carregar_arquivo, indent=6)
                    
                    
                    return [True, f"Pagamento no valor de {valor} R$ programado para data {data_programada} "]
                    
                elif data_atual == data_programada:

                       
                                
                    saldo -= valor
                                

                    atualizar = {"saldo":saldo}
                               
                    dados[index].update(atualizar)
                                

                    carregar_arquivo = open("Banco_de_dados.json","w")
                    json.dump(dados, carregar_arquivo, indent=6)
                    return [True, f"Pagamento no valor de {valor} realizada com sucesso! "]
                    

                else:
                        #print(f"Pagamento no valor de {valor} R$ programado para data {data_corrigida} às {horario_programado}")
                    return [False, "Data não corresponde"]

            else:
                return [False, "Saldo insuficiente!"]

        except ValueError:
            return [False, "Data fornecida é inválida!"] 

    
    def verificar_credito(self, index, valor_solic):
        valor_cred = dados[index].get("credito")
        dias = valor_cred.get(valor_solic)
        dia_atual = date.today().day
        if dias < dia_atual:
            dia_atual -= dias
            total = valor_solic * (1.01)**dia_atual
            return f"O valor do montante incidido pelo juros é {total}"

    def SolicitarCredito(self,index, valor_credito):
        try:
            
            
            
            
        
            dia_atual = date.today().day

            if valor_credito > 0:
                atualizar_cred = {"credito":{valor_credito:dia_atual}}
                dados[index].update(atualizar_cred)
                


                carregar_arquivo = open("Banco_de_dados.json","w")
                json.dump(dados, carregar_arquivo, indent=6)
                
                return [True, f"Crédito acrescido com sucesso!, taxa de 10% a.d "]
            else:
                return [False, f"Crédito requisitado não aceito"]
                    
    

               
        except ValueError:
            print("Data fornecida é inválida!")
