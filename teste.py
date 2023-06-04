import json
with open("D:\Workspace\Repositório_VS\miniprojeto4\Banco_de_dados.json", "r") as arquivo:
    dados = json.load(arquivo)

x = input()
switch = {
            "1":"Foi um",
            "2":"Foi dois",
            "3":"Foi tres",
                      }
print(switch["1"])