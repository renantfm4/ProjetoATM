class Conta:
    def __init__(self, senha, instituicao, saldo, limite, extrato):
        self.senha = senha
        self.instituicao = instituicao
        self.saldo = saldo
        self.limite = limite
        self.extrato = extrato

    def sacar(self, saldo, limite, valor):
        super().__init__(limite,saldo)
        self.saldo = saldo
        self.limite = limite
        if valor > 0 and valor <= self.saldo + self.limite:
            self.saldo -= valor
            print("Saque realizado")
        else:
            print("Saldo insuficiente")

    
