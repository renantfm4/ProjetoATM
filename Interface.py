#pip install customtkinter
#pip install pillow

#import tkinter 
from Gerente import *
from Conta import *
import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import warnings

ctk.set_appearance_mode("dark")
warnings.filterwarnings("ignore", category=UserWarning) 

conta = Conta()
gerente = Gerente()
class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.configuracoes()
        self.tipo()
        
    
    def configuracoes(self):
        self.geometry(f"{700}x{400}")
        self.title("Sistema de Login")
        self.resizable(0, 0)
        self.configure(bg="black")
        

    def tipo(self):
        self.frame_tipo = ctk.CTkFrame(self, width=350, height=380)
        self.frame_tipo.place(x=250, y=80)

        self.otipo = ctk.CTkLabel(self.frame_tipo, text="Que tipo você é?", font=("Comic Sans MS", 20))
        self.otipo.grid(row=0, column=0, padx=10, pady=10)

        self.btn_gerente_sub = ctk.CTkButton(self.frame_tipo, text="Gerente".upper(), command=
        self.tela_login_gerente)
        self.btn_gerente_sub.grid(row=1, column=0, padx=10, pady=10)
        self.btn_usuario_sub = ctk.CTkButton(self.frame_tipo, text="Usuário".upper(), command=
        self.tela_login_usuario)
        self.btn_usuario_sub.grid(row=3, column=0, padx=10, pady=10)
        

    def tela_login_usuario(self):

        self.frame_tipo.place_forget()
        img = Image.open("login.png")
        img = img.resize((350, 350))  # Redimensiona a imagem para 200x200 pixels
        
        photo = ImageTk.PhotoImage(img)

        self.frame_login_usuario = ctk.CTkFrame(self, width=900, height=900)
        self.frame_login_usuario.place(x=0, y=0)
        
        self.lb_img = ctk.CTkLabel(self.frame_login_usuario, text=None, image=photo)
        self.lb_img.grid(row=2, column=0, padx=3)
        
        self.title = ctk.CTkLabel(self.frame_login_usuario, text="Login de Usuário", font=("Comic Sans MS", 20))
        self.title.grid(row=0, column=0, pady=10)
        
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=368, y=80)

        self.lab_title = ctk.CTkLabel(self.frame_login, text="Faça o seu Login", font=("Century Gothic bold", 22))
        self.lab_title.grid(row=1, column=0, padx=10, pady=10)

        self.username_login_entry = tk.Entry(self.frame_login)
       
        self.username_login_entry.grid(row=2, column=0, padx=10, pady=10) 
        

        self.senha_login_entry = tk.Entry(self.frame_login,  show="*")
        
        self.senha_login_entry.grid(row=3, column=0, padx=10, pady=10)
        


        self.checkbox_var = tk.IntVar()
        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique no checkbox para visualizar a senha", variable=self.checkbox_var, command=lambda: self.senha_login_entry.configure(show="" if self.checkbox_var.get() else "*"))
        self.ver_senha.grid(row=4, column=0, padx=10, pady=10)

        self.btn_login_sub = ctk.CTkButton(self.frame_login, text="Login".upper(), width=300, corner_radius=15,
        command= self.entrada)
        self.btn_login_sub.grid(row=5, column=0, padx=10, pady=10)


    








    def janela (self, mensagem):
        self.frame_tipo = ctk.CTkFrame(self, width=350, height=380)
        self.frame_tipo.place(x=250, y=80)

        self.otipo = ctk.CTkLabel(self.frame_tipo, text=f"{mensagem}", font=("Comic Sans MS", 20))
        self.otipo.grid(row=0, column=0, padx=10, pady=10)


    def entrada(self):
        cpf = str(self.username_login_entry.get())
        senha = str(self.senha_login_entry.get())
        if conta.login(cpf,senha)[0] == False:   
            return self.janela("Usuário não encontrado")
        else:
            self.usuario = conta.login(cpf,senha)[1]
            return self.menu_usuario()
        
    def entrada_gerente(self):
        cpf = str(self.username_login_entry.get())
        senha = str(self.senha_login_entry.get())

        if gerente.login_gerente(cpf,senha)[0] == False:   
            return self.janela(cpf)
        else:
            return self.menu_gerente()
        
    def tela_login_gerente(self):

        self.frame_tipo.place_forget()
        img = Image.open("login.png")
        img = img.resize((350, 350))  # Redimensiona a imagem para 200x200 pixels
        
        photo = ImageTk.PhotoImage(img)

        self.frame_login_gerente2 = ctk.CTkFrame(self, width=900, height=900)
        self.frame_login_gerente2.place(x=0, y=0)
        
        self.lb_img = ctk.CTkLabel(self.frame_login_gerente2, text=None, image=photo)
        self.lb_img.grid(row=2, column=0, padx=3)
        
        self.title = ctk.CTkLabel(self.frame_login_gerente2, text="Login de Gerente", font=("Comic Sans MS", 20))
        self.title.grid(row=0, column=0, pady=10)


        self.frame_login_gerente = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login_gerente.place(x=368, y=80)

        self.lab_title = ctk.CTkLabel(self.frame_login_gerente, text="Faça o seu Login", font=("Century Gothic bold", 22))
        self.lab_title.grid(row=1, column=0, padx=10, pady=10)

        self.username_login_entry = ctk.CTkEntry(self.frame_login_gerente, width=300, placeholder_text="Digite seu CPF", corner_radius=15)
        self.username_login_entry.grid(row=2, column=0, padx=10, pady=10) 

        self.senha_login_entry = ctk.CTkEntry(self.frame_login_gerente, width=300, placeholder_text="Digite sua senha", corner_radius=15, show="*")
        self.senha_login_entry.grid(row=3, column=0, padx=10, pady=10)
        

        self.checkbox_var = tk.IntVar()
        self.ver_senha = ctk.CTkCheckBox(self.frame_login_gerente, text="Clique no checkbox para visualizar a senha", variable=self.checkbox_var, command=lambda: self.senha_login_entry.configure(show="" if self.checkbox_var.get() else "*"))
        self.ver_senha.grid(row=4, column=0, padx=10, pady=10)


        self.btn_login_sub = ctk.CTkButton(self.frame_login_gerente, text="Login".upper(), width=300, corner_radius=15,
        command=self.entrada_gerente)
        self.btn_login_sub.grid(row=5, column=0, padx=10, pady=10)
    
    def menu_gerente(self):
        self.frame_login_gerente.place_forget()
        self.frame_login_gerente2.place_forget()

        self.menu = ctk.CTkFrame(self, width=350, height=380)
        self.menu.place(x=250, y=80)

        self.registrar = ctk.CTkButton(self.menu, text="Registrar Usuário".upper(), command=self.registrar)
        self.registrar.grid(row=1, column=0, padx=10, pady=10)
        self.deletar = ctk.CTkButton(self.menu, text="Deletar Usuário".upper(), command=self.deletar)
        self.deletar.grid(row=3, column=0, padx=10, pady=10)
        self.listar = ctk.CTkButton(self.menu, text="Listar Contas".upper())
        self.listar.grid(row=5, column=0, padx=10, pady=10)
        

    def realizar_registro(self):
        nome = str(self.nome_usuario.get())
        cpf = str(self.cpf_usuario.get())
        telefone = str(self.telefone_usuario.get())
        endereco = str(self.endereco_usuario.get())
        saldo = float(self.saldo_usuario.get())
        senha = str(self.senha_usuario.get())
        gerente.RegistrarConta(nome,cpf,telefone, endereco,saldo,senha )


    def registrar(self):

        self.menu.place_forget()

        self.registro_menu = ctk.CTkFrame(self, width=350, height=380)
        self.registro_menu.place(x=130, y=7)

        self.registrar_titulo = ctk.CTkLabel(self.registro_menu, text="Registrar", font=("Century Gothic bold", 22))
        self.registrar_titulo.grid(row=0, column=0, padx=175, pady=10)

        self.nome_usuario = ctk.CTkEntry(self.registro_menu, width=300, placeholder_text="Nome", corner_radius=15)
        self.nome_usuario.grid(row=1, column=0, padx=10, pady=10) 

        self.cpf_usuario = ctk.CTkEntry(self.registro_menu, width=300, placeholder_text="CPF", corner_radius=15)
        self.cpf_usuario.grid(row=2, column=0, padx=10, pady=10) 

        self.telefone_usuario = ctk.CTkEntry(self.registro_menu, width=300, placeholder_text="Telefone", corner_radius=15)
        self.telefone_usuario.grid(row=3, column=0, padx=10, pady=10) 

        self.endereco_usuario = ctk.CTkEntry(self.registro_menu, width=300, placeholder_text="Endereço", corner_radius=15)
        self.endereco_usuario.grid(row=4, column=0, padx=10, pady=10) 

        self.saldo_usuario = ctk.CTkEntry(self.registro_menu, width=300, placeholder_text="Saldo", corner_radius=15)
        self.saldo_usuario.grid(row=5, column=0, padx=10, pady=10) 

        self.senha_usuario = ctk.CTkEntry(self.registro_menu, width=300, placeholder_text="Senha", corner_radius=15)
        self.senha_usuario.grid(row=6, column=0, padx=10, pady=10) 

        self.confirmar = ctk.CTkButton(self.registro_menu, text="Confirmar".upper(), width=300, corner_radius=15, command=self.realizar_registro)
        self.confirmar.grid(row=7, column=0, padx=10, pady=10)
    
    #def realizar_delete(self):


    def deletar(self):

        self.menu.place_forget()

        self.deletar_menu = ctk.CTkFrame(self, width=350, height=380)
        self.deletar_menu.place(x=130, y=7)

        self.deletar_titulo = ctk.CTkLabel(self.deletar_menu, text="Deletar", font=("Century Gothic bold", 22))
        self.deletar_titulo.grid(row=0, column=0, padx=175, pady=10)

        self.selecionar_usuario = ctk.CTkCheckBox(self.deletar_menu, text="*usuario*",)
        self.selecionar_usuario.grid(row=4, column=0, padx=10, pady=10)

        self.confirmar = ctk.CTkButton(self.deletar_menu, text="Confirmar".upper(), width=300, corner_radius=15)
        self.confirmar.grid(row=7, column=0, padx=10, pady=10)


    def menu_usuario(self):

        self.frame_login.place_forget()
        self.frame_login_usuario.place_forget()


        self.menu_user = ctk.CTkFrame(self, width=350, height=250)
        self.menu_user.place(x=20, y=15)

        self.lab_titulo = ctk.CTkLabel(self.menu_user, text="Menu", font=("Century Gothic bold", 22))
        self.lab_titulo.grid(row=0, column=0, padx=175, pady=10)
        
        
        self.lab_extrato = ctk.CTkLabel(self.menu_user, text="1- Extrato", font=("Arial", 20))
        self.lab_extrato.grid(row=1, column=0, padx=0, pady=(0,200), sticky="w")

        self.lab_saque = ctk.CTkLabel(self.menu_user, text="2- Saque", font=("Arial", 20))
        self.lab_saque.grid(row=1, column=0, padx=0, pady=(0,150), sticky="w")

        self.lab_deposito = ctk.CTkLabel(self.menu_user, text="3- Depósito", font=("Arial", 20))
        self.lab_deposito.grid(row=1, column=0, padx=0, pady=(0,100), sticky="w")

        self.lab_pagamento = ctk.CTkLabel(self.menu_user, text="4- Realizar pagamento programado", font=("Arial", 20))
        self.lab_pagamento.grid(row=1, column=0, padx=0, pady=(0,50), sticky="w")

        self.lab_credito = ctk.CTkLabel(self.menu_user, text="5- Solicitar crédito", font=("Arial", 20))
        self.lab_credito.grid(row=1, column=0, padx=0, pady=(0,0), sticky="w")

        self.lab_sair = ctk.CTkLabel(self.menu_user, text="6- Sair", font=("Arial", 20))
        self.lab_sair.grid(row=1, column=0, padx=0, pady=(50,0), sticky="w")

        

        self.lab_teste = ctk.CTkLabel(self.menu_user, text="Entre com sua opção:", font=("Arial", 17))
        self.lab_teste.grid(row=1, column=0, padx=0, pady=(205,0), sticky="w")

        self.menu_botao = ctk.CTkFrame(self, width=320, height=250)
        self.menu_botao.place(x=500, y=16)
        
        self.um = ctk.CTkButton(self.menu_botao, text="1", font=("Arial", 20), width=50, height=50)
        self.um.grid(row=1, column=0, padx=(10,2), pady=5, sticky="w")

        self.dois = ctk.CTkButton(self.menu_botao, text="2", font=("Arial", 20), width=50, height=50, command=self.saque)
        self.dois.grid(row=1, column=1, padx=(10,2), pady=10, sticky="w")

        self.tres = ctk.CTkButton(self.menu_botao, text="3", font=("Arial", 20), width=50, height=50, command=self.deposito)
        self.tres.grid(row=1, column=2, padx=(10,2), pady=10, sticky="w")

        self.quatro = ctk.CTkButton(self.menu_botao, text="4", font=("Arial", 20), width=50, height=50, command=self.pagamento_programado)
        self.quatro.grid(row=2, column=0, padx=(10,2), pady=10, sticky="w")

        self.cinco = ctk.CTkButton(self.menu_botao, text="5", font=("Arial", 20), width=50, height=50, command=self.credito)
        self.cinco.grid(row=2, column=1, padx=(10,2), pady=10, sticky="w")

        self.seis = ctk.CTkButton(self.menu_botao, text="6", font=("Arial", 20), width=50, height=50)
        self.seis.grid(row=2, column=2, padx=(10,2), pady=10, sticky="w")

        self.sete = ctk.CTkButton(self.menu_botao, text="7", font=("Arial", 20), width=50, height=50)
        self.sete.grid(row=5, column=0, padx=(10,2), pady=10, sticky="w")

        self.oito = ctk.CTkButton(self.menu_botao, text="8", font=("Arial", 20), width=50, height=50)
        self.oito.grid(row=5, column=1, padx=(10,2), pady=10, sticky="w")


        self.zero = ctk.CTkButton(self.menu_botao, text="0", font=("Arial", 20), width=50, height=50)
        self.zero.grid(row=6, column=0, padx=(10,2), pady=10, sticky="w")

        self.enter = ctk.CTkButton(self.menu_botao, text="OK", font=("Arial", 20), width=50, height=50)
        self.enter.grid(row=6, column=1, padx=(10,2), pady=10, sticky="w")

        self.nove = ctk.CTkButton(self.menu_botao, text="9", font=("Arial", 20), width=50, height=50)
        self.nove.grid(row=5, column=2, padx=(10,2), pady=10, sticky="w")

    def realizar_saque(self):
        valor = float(self.digito_saque.get())
        if conta.sacar(self.usuario, valor):
            return self.janela("Saque realizado com sucesso!")
        else:
            return self.janela("Saldo insuficiente!")
        
    def realizar_deposito(self):
        valor = float(self.digito_deposito.get())
        if conta.depositar(self.usuario, valor):
            return self.janela("Deposito realizado com sucesso!")
        else:
            return self.janela("Número digitado invalido!")
        


    def saque(self):

        self.menu_user.place_forget()
        self.menu_botao.place_forget()


        self.registro_menu = ctk.CTkFrame(self, width=350, height=250)
        self.registro_menu.place(x=20, y=15)

        self.saque_titulo = ctk.CTkLabel(self.registro_menu, text="Saque", font=("Century Gothic bold", 22))
        self.saque_titulo.grid(row=0, column=0, padx=175, pady=10)

        self.digito_saque = ctk.CTkEntry(self.registro_menu, width=300, placeholder_text="Insira o valor do saque", corner_radius=15)
       
        self.digito_saque.grid(row=1, column=0, padx=10, pady=10) 

        self.lab_teste = ctk.CTkLabel(self.registro_menu, text=f"Saldo: ", font=("Arial", 20))
        self.lab_teste.grid(row=2, column=0, padx=0, pady=(155,0), sticky="w")
        
        
        self.enter = ctk.CTkButton(self.registro_menu, text="OK", font=("Arial", 20), width=50, height=50, command=self.realizar_saque)
        self.enter.grid(row=6, column=1, padx=(10,2), pady=10, sticky="w")

    

    
    def deposito(self):

        self.menu_user.place_forget()
        self.menu_botao.place_forget()


        self.credito_menu = ctk.CTkFrame(self, width=350, height=250)
        self.credito_menu.place(x=20, y=15)

        self.deposito_titulo = ctk.CTkLabel(self.credito_menu, text="Depósito", font=("Century Gothic bold", 22))
        self.deposito_titulo.grid(row=0, column=0, padx=175, pady=10)

        self.digito_deposito = ctk.CTkEntry(self.credito_menu, width=300, placeholder_text="Insira o valor do depósito", corner_radius=15)
        self.digito_deposito.grid(row=1, column=0, padx=10, pady=10) 

        self.lab_teste = ctk.CTkLabel(self.credito_menu, text="Saldo: ", font=("Arial", 20))
        self.lab_teste.grid(row=2, column=0, padx=0, pady=(155,0), sticky="w")


        self.credito_botao = ctk.CTkFrame(self, width=320, height=250)
        self.credito_botao.place(x=500, y=16)
        

        self.enter = ctk.CTkButton(self.credito_botao, text="OK", font=("Arial", 20), width=50, height=50, command = self.realizar_deposito)
        self.enter.grid(row=6, column=1, padx=(10,2), pady=10, sticky="w")

    
  

    def pagamento_programado(self):

        self.menu_user.place_forget()
        self.menu_botao.place_forget()


        self.credito_menu = ctk.CTkFrame(self, width=350, height=250)
        self.credito_menu.place(x=20, y=15)

        self.pagamento_titulo = ctk.CTkLabel(self.credito_menu, text="Programado", font=("Century Gothic bold", 22))
        self.pagamento_titulo.grid(row=0, column=0, padx=(0,20), pady=10)

        self.valor_pagamento = ctk.CTkEntry(self.credito_menu, width=300, placeholder_text="Insira o valor do pagamento", corner_radius=15)
        self.valor_pagamento.grid(row=1, column=0, padx=10, pady=10) 

        self.data_credito = ctk.CTkEntry(self.credito_menu, width=300, placeholder_text="Insira a data do pagamento (no formato 'DD-MM-AAAA')", corner_radius=15)
        self.data_credito.grid(row=2, column=0, padx=10, pady=10) 


        self.lab_teste = ctk.CTkLabel(self.credito_menu, text="Saldo: ", font=("Arial", 20))
        self.lab_teste.grid(row=2, column=0, padx=0, pady=(155,0), sticky="w")

        


        self.credito_botao = ctk.CTkFrame(self, width=320, height=250)
        self.credito_botao.place(x=500, y=16)
        


        self.enter = ctk.CTkButton(self.credito_botao, text="OK", font=("Arial", 20), width=50, height=50, command=self.realizar_programado)
        self.enter.grid(row=6, column=1, padx=(10,2), pady=10, sticky="w")

    def realizar_programado(self):
        valor = float(self.valor_pagamento.get())
        data = str(self.data_credito.get())
        conta.PagamentoProgramado(self.usuario, valor, data)
        return self.janela(conta.PagamentoProgramado(self.usuario, valor, data)[1])
     
    def credito(self):

        self.menu_user.place_forget()
        self.menu_botao.place_forget()


        self.credito_menu = ctk.CTkFrame(self, width=350, height=250)
        self.credito_menu.place(x=20, y=15)

        self.credito_titulo = ctk.CTkLabel(self.credito_menu, text="Crédito", font=("Century Gothic bold", 22))
        self.credito_titulo.grid(row=0, column=0, padx=175, pady=10)

        self.valor_credito = ctk.CTkEntry(self.credito_menu, width=300, placeholder_text="Insira o valor do crédito", corner_radius=15)
        self.valor_credito.grid(row=1, column=0, padx=10, pady=10) 

        self.data_credito = ctk.CTkEntry(self.credito_menu, width=300, placeholder_text="Insira a data do pagamento", corner_radius=15)
        self.data_credito.grid(row=2, column=0, padx=10, pady=10) 

        self.hora_credito = ctk.CTkEntry(self.credito_menu, width=300, placeholder_text="Insira a hora do pagamento", corner_radius=15)
        self.hora_credito.grid(row=2, column=0, padx=10, pady=(0,120)) 

        self.lab_teste = ctk.CTkLabel(self.credito_menu, text="Saldo: ", font=("Arial", 20))
        self.lab_teste.grid(row=2, column=0, padx=0, pady=(155,0), sticky="w")

        self.credito_botao = ctk.CTkFrame(self, width=320, height=250)
        self.credito_botao.place(x=500, y=16)
        
        self.um = ctk.CTkButton(self.credito_botao, text="1", font=("Arial", 20), width=50, height=50)
        self.um.grid(row=1, column=0, padx=(10,2), pady=5, sticky="w")

        self.dois = ctk.CTkButton(self.credito_botao, text="2", font=("Arial", 20), width=50, height=50)
        self.dois.grid(row=1, column=1, padx=(10,2), pady=10, sticky="w")

        self.tres = ctk.CTkButton(self.credito_botao, text="3", font=("Arial", 20), width=50, height=50)
        self.tres.grid(row=1, column=2, padx=(10,2), pady=10, sticky="w")

        self.quatro = ctk.CTkButton(self.credito_botao, text="4", font=("Arial", 20), width=50, height=50)
        self.quatro.grid(row=2, column=0, padx=(10,2), pady=10, sticky="w")

        self.cinco = ctk.CTkButton(self.credito_botao, text="5", font=("Arial", 20), width=50, height=50)
        self.cinco.grid(row=2, column=1, padx=(10,2), pady=10, sticky="w")

        self.seis = ctk.CTkButton(self.credito_botao, text="6", font=("Arial", 20), width=50, height=50)
        self.seis.grid(row=2, column=2, padx=(10,2), pady=10, sticky="w")

        self.sete = ctk.CTkButton(self.credito_botao, text="7", font=("Arial", 20), width=50, height=50)
        self.sete.grid(row=5, column=0, padx=(10,2), pady=10, sticky="w")

        self.oito = ctk.CTkButton(self.credito_botao, text="8", font=("Arial", 20), width=50, height=50)
        self.oito.grid(row=5, column=1, padx=(10,2), pady=10, sticky="w")


        self.zero = ctk.CTkButton(self.credito_botao, text="0", font=("Arial", 20), width=50, height=50)
        self.zero.grid(row=6, column=0, padx=(10,2), pady=10, sticky="w")

        self.enter = ctk.CTkButton(self.credito_botao, text="OK", font=("Arial", 20), width=50, height=50)
        self.enter.grid(row=6, column=1, padx=(10,2), pady=10, sticky="w")

        self.nove = ctk.CTkButton(self.credito_botao, text="9", font=("Arial", 20), width=50, height=50)
        self.nove.grid(row=5, column=2, padx=(10,2), pady=10, sticky="w")

    






if __name__ == "__main__":
    app = App()
    app.mainloop()

