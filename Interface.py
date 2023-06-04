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
        self.tela_login()
    
    def configuracoes(self):
        self.geometry(f"{700}x{400}")
        self.title("Sistema de Login")
        self.resizable(0, 0)
        self.configure(bg="black")

    def tela_login(self):

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

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Digite seu CPF")
        self.username_login_entry.grid(row=2, column=0, padx=10, pady=10) 

        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Digite sua senha")
        self.senha_login_entry.grid(row=3, column=0, padx=10, pady=10)
        
        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique no checkbox para visualizar a senha")
        self.ver_senha.grid(row=4, column=0, padx=10, pady=10)

        self.btn_login_sub = ctk.CTkButton(self.frame_login, text="Login".upper(), width=300, corner_radius=15)
        self.btn_login_sub.grid(row=5, column=0, padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

