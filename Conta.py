from datetime import datetime,date

class Conta:
    def __init__(self, senha, instituicao, saldo, limite, extrato):
        self.senha = senha
        self.instituicao = instituicao
        self.saldo = saldo
        self.limite = limite
        self.extrato = extrato

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo + self.limite:
            self.saldo -= valor
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado!")
        else:
            print("Valor inserido é inválido!")

    def PagamentoProgramado(self, destinatario):
        try:
            self.destinatario = destinatario
            a = datetime.now()
            hora_atual = a.strftime("%H:%M")
            print("Hora atual:", hora_atual)
            print("Para qual dia você quer realizar o pagamento? Digite (no formato 'DD-MM-AAAA'):")
            data_programada_str = input()
            print("E para qual horário?")
            self.horario_programado = input()
            print("Qual valor você deseja transferir?")
            self.valor = float(input())
            dia, mes, ano = map(int, data_programada_str.split('-'))
            data_programada = date(ano, mes, dia)
            data_atual = date.today()
            if self.valor > 0 and self.valor <= self.saldo + self.limite:
                if data_programada >= data_atual:
                    data_corrigida = data_programada.strftime("%d-%m-%Y")
                    if data_atual == data_programada:
                        if self.horario_programado >= hora_atual:
                            if self.horario_programado == hora_atual:
                                print(f"Pagamento no valor de {self.valor} R$ programado para data {data_corrigida} às {self.horario_programado}")
                                self.saldo -= self.valor
                                destinatario.saldo += self.valor
                                print(f"Pagamento no valor de {self.valor} R$ efetuado!")
                            else:
                                print(f"Pagamento no valor de {self.valor} R$ programado para data {data_corrigida} às {self.horario_programado}")
                                print(f"Quando a data solicitada: {data_corrigida} às {self.horario_programado}, o pagamento será efetuado!")
                        else:
                            print("Horário fornecido inválido!")
                    else:
                        print(f"Pagamento no valor de {self.valor} R$ programado para data {data_corrigida} às {self.horario_programado}")
                        print(f"Quando a data solicitada: {data_corrigida} às {self.horario_programado}, o pagamento será efetuado!")
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

