from datetime import datetime,date
import json

with open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_de_dados.json", "r") as arquivo:
    dados = json.load(arquivo)

class Operacoes():
    

    def __init__(self):
        extrato = []

    def sacar(self, index, valor):
        
        saldo = dados[index].get("saldo")
        if valor > 0 and valor <= saldo:
            
            saldo -= valor
            atualizar = {"saldo":saldo}
            dados[index].update(atualizar)

            carregar_arquivo = open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_de_dados.json","w")
            json.dump(dados, carregar_arquivo, indent=6)

            return True
        else:
            return False

    def depositar(self, index, valor):
        
        saldo = dados[index].get("saldo")
        if valor > 0:
            saldo += valor
            atualizar = {"saldo":saldo}
            dados[index].update(atualizar)

            carregar_arquivo = open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_de_dados.json","w")
            json.dump(dados, carregar_arquivo, indent=6)

            return True
        else:
            return False

    def PagamentoProgramado(self, index_dest, index):
        try:
            saldo = dados[index].get("saldo")
            saldo_dest = dados[index_dest].get("saldo")

            a = datetime.now()
            hora_atual = a.strftime("%H:%M")

            print("Hora atual:", hora_atual)
            print("Para qual dia você quer realizar o pagamento? Digite (no formato 'DD-MM-AAAA'):\n")
            data_programada_str = input()

            print("E para qual horário?")
            horario_programado = input()

            print("Qual valor você deseja transferir?")
            valor = float(input())

            dia, mes, ano = map(int, data_programada_str.split('-'))
            data_programada = date(ano, mes, dia)
            data_atual = date.today()

            if valor > 0 and valor <= saldo:

                if data_programada >= data_atual:
                    data_corrigida = data_programada.strftime("%d-%m-%Y")

                    if data_atual == data_programada:

                        if horario_programado >= hora_atual:

                            if horario_programado == hora_atual:
                                print(f"Pagamento no valor de {valor} R$ programado para data {data_corrigida} às {horario_programado}")
                                saldo -= valor
                                saldo_dest += valor

                                atualizar = {"saldo":saldo}
                                atualizar_dest = {"saldo":saldo_dest}
                                dados[index].update(atualizar)
                                dados[index_dest].update(atualizar_dest)

                                carregar_arquivo = open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_de_dados.json","w")
                                json.dump(dados, carregar_arquivo, indent=6)

                                print(f"Pagamento no valor de {valor} R$ efetuado!")

                            else:
                                print(f"Pagamento no valor de {valor} R$ programado para data {data_corrigida} às {horario_programado}")
                                print(f"Quando a data solicitada: {data_corrigida} às {horario_programado}, o pagamento será efetuado!")

                        else:
                            print("Horário fornecido inválido!")

                    else:
                        print(f"Pagamento no valor de {valor} R$ programado para data {data_corrigida} às {horario_programado}")
                        print(f"Quando a data solicitada: {data_corrigida} às {horario_programado}, o pagamento será efetuado!")

                else:
                    print("Data fornecida inválida!")

            else:
                print("Saldo insuficiente!")

        except ValueError:
            print("Data fornecida é inválida!") 

            
    def SolicitarCredito(self):
        try:
            a = datetime.now()
            hora_atual = a.strftime("%H:%M")
            valor_credito = float(input("Digite o valor do crédito: "))
            data_programada_str = input("Para que dia você quer solicitar o valor? Digite (no formato 'DD-MM-AAAA'): ")
            dia, mes, ano = map(int, data_programada_str.split('-'))
            data_programada = date(ano, mes, dia)
            print("E para qual horário?")
            self.horario_programado = input()
            data_atual = date.today()
            if valor_credito > 0:
                if data_programada >= data_atual:
                    data_corrigida = data_programada.strftime("%d-%m-%Y")
                    if data_atual == data_programada:
                        if self.horario_programado >= hora_atual:
                            if self.horario_programado == hora_atual:
                                print(f"Solicitação de crédito no valor de {valor_credito} R$ para a data {data_corrigida} às {self.horario_programado} realizada!")
                                self.saldo += valor_credito  
                                data_corrigida = data_programada.strftime("%d-%m-%Y")
                                print(f"Solicitação de crédito no valor de {valor_credito} R$ inserida ao banco!")
                            else:
                                print(f"Solicitação de crédito no valor de {valor_credito} R$ para a data {data_corrigida} às {self.horario_programado} realizada!")
                                print(f"Quando a data fornecida: {data_corrigida} às {self.horario_programado} chegar, será inserida ao banco o valor!")
                        else:
                            print("Horário fornecido inválido!")
                    else:
                        print(f"Solicitação de crédito no valor de {valor_credito} R$ para a data {data_corrigida} às {self.horario_programado} realizada!")
                        print(f"Quando a data fornecida: {data_corrigida} às {self.horario_programado} chegar, será inserida ao banco o valor!")
                else:
                    print("Data fornecida é inválida!")
        except ValueError:
            print("Data fornecida é inválida!")