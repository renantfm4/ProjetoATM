#pip install customtkinter
#pip install pillow

#import tkinter 

#janela = tkinter.Tk()
#janela.geometry("500x300")

#texto = tkinter.Label(text = "Você é gerente ou usuário?")
#texto.pack(padx=10, pady=10)

#gerente = tkinter.Button(janela, text="Gerente")
#gerente.pack(padx=10, pady=10)

#usuario = tkinter.Button(janela, text="Usuário")
#usuario.pack(padx=10, pady=10)

#janela.mainloop()

########################


#janela = customtkinter.CTk()
#janela.geometry("500x300")

#def clique():
    #print("Fazer Login")

#texto = customtkinter.CTkLabel(janela, text="Você é gerente ou usuário?")
#texto.pack(padx=10, pady=10)

#gerente = customtkinter.CTkButton(janela, text="Gerente", command=clique)
#gerente.pack(padx=10, pady=10)
#usuario = customtkinter.CTkButton(janela, text="Usuário", command=clique)
#usuario.pack(padx=10, pady=10)

#janela.mainloop()


import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import warnings

ctk.set_appearance_mode("dark")
warnings.filterwarnings("ignore", category=UserWarning) 


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
        img = img.resize((300, 300))  # Redimensiona a imagem para 200x200 pixels
        
        photo = ImageTk.PhotoImage(img)
        
        self.lb_img = ctk.CTkLabel(self, text=None, image=photo)
        self.lb_img.grid(row=2, column=0, padx=3)
        
        self.title = ctk.CTkLabel(self, text="Login de Usuário", font=("Comic Sans MS", 20))
        self.title.grid(row=0, column=0, pady=10)


        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=80)

        self.lab_title = ctk.CTkLabel(self.frame_login, text="Faça o seu Login", font=("Century Gothic bold", 22))
        self.lab_title.grid(row=1, column=0, padx=10, pady=10)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Digite seu CPF", corner_radius=15)
        self.username_login_entry.grid(row=2, column=0, padx=10, pady=10) 

        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Digite sua senha", corner_radius=15, show="*")
        self.senha_login_entry.grid(row=3, column=0, padx=10, pady=10)
        
        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique no checkbox para visualizar a senha")
        self.ver_senha.grid(row=4, column=0, padx=10, pady=10)

        self.btn_login_sub = ctk.CTkButton(self.frame_login, text="Login".upper(), width=300, corner_radius=15)
        self.btn_login_sub.grid(row=5, column=0, padx=10, pady=10)

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
        
        self.ver_senha = ctk.CTkCheckBox(self.frame_login_gerente, text="Clique no checkbox para visualizar a senha")
        self.ver_senha.grid(row=4, column=0, padx=10, pady=10)

        self.btn_login_sub = ctk.CTkButton(self.frame_login_gerente, text="Login".upper(), width=300, corner_radius=15,
        command=self.menu_gerente)
        self.btn_login_sub.grid(row=5, column=0, padx=10, pady=10)
    
    def menu_gerente(self):
        self.frame_login_gerente.place_forget()
        self.frame_login_gerente2.place_forget()

        self.menu = ctk.CTkFrame(self, width=350, height=380)
        self.menu.place(x=350, y=80)


if __name__ == "__main__":
    app = App()
    app.mainloop()

