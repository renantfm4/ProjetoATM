# ESSE ARQUIVO ESTÁ SENDO APENAS NO MOMENTO PRA TESTAR O FRONT

from Conta import Conta
import datetime

# Criar instância da classe Conta
minha_conta = Conta(senha="senha123", instituicao="Banco XYZ", saldo=1000, limite=500, extrato=[])
conta_destinatario = Conta(senha="senha456", instituicao="Banco ABC", saldo=0, limite=0, extrato=[])




# Chamar a função sacar() para fazer um saque
#minha_conta.sacar(valor=200)

# Acessar os atributos atualizados
#print("Saldo atual:", minha_conta.saldo)
#print("Extrato atual:", minha_conta.extrato)


# Chamar a função depositar() para fazer um depósito
#minha_conta.depositar(valor=300)

# Acessar o saldo atualizado
#print("Saldo atual:", minha_conta.saldo)

# Chamar a função transferir() para realizar uma transferência
minha_conta.PagamentoProgramado(destinatario=conta_destinatario)
#minha_conta.SolicitarCredito()

# Acessar os atributos atualizados
print("Saldo atual da minha conta:", minha_conta.saldo)
print("Saldo atual da conta destinatário:", conta_destinatario.saldo)
print("Extrato atual da minha conta:", minha_conta.extrato)
print("Extrato atual da conta destinatário:", conta_destinatario.extrato)
