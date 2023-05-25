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

    def PagamentoProgramado(self, destinatario):
        self.destinatario = destinatario
        a = datetime.now()
        hora_atual = a.strftime("%H:%M")
        print("Hora atual: ", hora_atual)
        print("Para qual horário você quer realizar o pagamento?")
        self.horario_programado = input()
        print("O quanto você quer transferir?")
        self.valor = int(input())
        if self.valor > 0 and self.valor <= self.saldo + self.limite:
            self.saldo -= self.valor
            destinatario.saldo += self.valor
            print(f"Pagamento no valor de {self.valor} R$ programado para às {self.horario_programado}")
        else:
            print("Saldo insuficiente!")

        #if hora_atual == self.horario_programado:
           # print("Pagamento programado realizado!")
        #else:
          #  print("Fora do horário para o pagamento!")