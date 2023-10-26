from tkinter import *
from tkinter import ttk

def conectarServidor():
    pass

telaMain = Tk()
telaMain.title("EzShare")
#telaMain.geometry("400x200")

bio = Label(telaMain,text = "Faça upload e download de arquivos no servidor!")
bio.grid(column=0, row=0)

btConectar = Button(telaMain, text="Conectar ao Servidor", command=conectarServidor).grid(column=0, row=1)

'''
#Cria e dispôe os botões no display
btnEnviarDl = Button(telaMain, text="Enviar").grid(column=0, row=1)
btnSelecionarDl = Button(telaMain, text="Selecionar").grid(column=0, row=2)

btnEnviarUp = Button(telaMain, text="Enviar").grid(column=2, row=1) ##pack(expand=1, side="right", padx=10, pady= 50)
btnSelecionarUp = Button(telaMain, text="Selecionar").grid(column=2, row=2) ##pack(expand=1, side="right", padx=10, pady= 50)
'''

telaMain.mainloop()





###################### CÓDIGO ANTIGO ########################
'''
import tkinter as tk
#from tkinter import ttk

#Cria a tela principal
telaMain = tk.Tk()
telaMain.title("Teste")
telaMain.geometry("600x400")

#Cria os botões no display
btnEnviar = tk.Button(telaMain, text="Enviar", padx=10)
btnEnviar.pack(expand=1, side="right")

btnSelecionar = tk.Button(telaMain, text="Selecionar", padx=10)
btnSelecionar.pack(expand=1, side="right")

#Roda a tela principal
telaMain.mainloop()
'''