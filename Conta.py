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

    def transferir(self, valor, destinatario):
        if valor > 0 and valor <= self.saldo + self.limite:
            self.saldo -= valor
            destinatario.saldo += valor
            print("Transferência realizada!")
        else:
            print("Saldo insuficiente!")
