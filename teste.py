import json
with open("C:\WORKSPACE\Python\ATM\Banco_de_dados.json",  encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

dados.append("oi")
print(dados)