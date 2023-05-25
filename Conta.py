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
            print("Hora atual: ", hora_atual)
            print("Para que dia você quer realizar o pagamento?")
            data_programada_str = input()
            print("E para qual horário?")
            self.horario_programado = input()
            print("O quanto você quer transferir?")
            self.valor = int(input())
            dia, mes, ano = map(int, data_programada_str.split('-'))
            data_programada = date(ano, mes, dia)
            data_atual = date.today()
            if self.valor > 0 and self.valor <= self.saldo + self.limite and data_programada >= data_atual:
                data_corrigida = data_programada.strftime("%d-%m-%Y")
                print(f"Pagamento no valor de {self.valor} R$ programado para às {self.horario_programado} do dia {data_corrigida}")
            else:
                print("Saldo insuficiente!")
            if data_atual.strftime("%Y-%m-%d") == data_programada.strftime("%Y-%m-%d"):
                if hora_atual == self.horario_programado:
                    data_corrigida = data_programada.strftime("%d-%m-%Y")
                    self.saldo -= self.valor
                    destinatario.saldo += self.valor
                    print(f"Pagamento no valor de {self.valor} R$ efetuado!")
                else:
                    print("Horário fornecido inválido!")
            else:
                print(f"Quando a data solicitada: {data_corrigida} , {self.horario_programado} o pagamento será efetuado!")
        except ValueError:
            print("Data fornecida é inválida!")

    def SolicitarCredito(self):
        valor_credito = float(input("Digite o valor do crédito: "))
        data_programada_str = input("Digite a data programada (no formato 'DD-MM-AAAA'): ")
        try:
            dia, mes, ano = map(int, data_programada_str.split('-'))
            data_programada = date(ano, mes, dia)
            data_atual = date.today()
            if valor_credito > 0 and data_programada >= data_atual:
                data_corrigida = data_programada.strftime("%d-%m-%Y")
                print(f"Solicitação de crédito no valor de {valor_credito} R$ para a data {data_corrigida} realizada!")
            else:
                print("Valor ou data inválida para solicitar crédito!")
            if data_atual.strftime("%Y-%m-%d") == data_programada.strftime("%Y-%m-%d"):
                self.saldo += valor_credito  
                data_corrigida = data_programada.strftime("%d-%m-%Y")
                print(f"Solicitação de crédito no valor de {valor_credito} R$ inserida ao banco!")
            else: 
                print(f"Quando a data fornecida: {data_corrigida} chegar, será inserida ao banco o valor!")
        except ValueError:
            print("Data fornecida é inválida!")

