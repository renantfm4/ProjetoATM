import json

with open("D:\Workspace\Repositório_VS\miniprojeto4\Banco.json", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            print(dados)