from datetime import datetime

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

    def PagamentoProgramado(self):
        a = datetime.now()
        hora_atual = a.strftime("%H:%M")
        print("Hora atual: ", hora_atual)
        self.valor = input("Entre com valor: ")
        if hora_atual == self.valor:
            print("Pagamento programado realizado!")
        else:
            print("Fora do horário para o pagamento!")

