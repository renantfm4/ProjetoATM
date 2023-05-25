# ESSE ARQUIVO ESTÁ SENDO APENAS NO MOMENTO PRA TESTAR O FRONT

from Conta import Conta
import datetime

# Criar instância da classe Conta
minha_conta = Conta(senha="senha123", instituicao="Banco XYZ", saldo=1000, limite=500, extrato=[])



# Chamar a função sacar() para fazer um saque
minha_conta.sacar(valor=200)

# Acessar os atributos atualizados
print("Saldo atual:", minha_conta.saldo)
print("Extrato atual:", minha_conta.extrato)


# Chamar a função depositar() para fazer um depósito
#minha_conta.depositar(valor=300)

# Acessar o saldo atualizado
#print("Saldo atual:", minha_conta.saldo)

minha_conta.PagamentoProgramado()
