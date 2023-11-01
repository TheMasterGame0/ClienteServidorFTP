from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
# Coisas a fazer.
# Mexer com a questão das imagens.
# Pensar em como mostrar a busca dos itens no servidor.
# A busca do servidor será uma lista de strings
# Abrir uma nova tela na função do botão. Na nova tela deverá ter um botão para selecionar o item escolhido.


# Cliente criado
from Cliente import *

def conectarServidor():
    try: 
        status = "Online"
        socket = Conectar(user, senha)
        # Botão para desconectar o servidor
        global btnDesconectar;
        btnDesconectar = (Button(telaMain, text="Desconecte do Servidor", command= lambda: desconectaServidor(socket)))
        btnConectar.destroy()
        btnDesconectar.grid(column=1, row=1)
    except:
        status = "Offline"
    
    bio = Label(telaMain,text = "Faça upload e download de arquivos no servidor! \n Status: " + status)
    bio.grid(column=1, row=0)

    return socket

def desconectaServidor(socket):
    try:
        fecharSocket(socket)
        # Botão para conectar no servidor
        btnConectar = (Button(telaMain, text="Conectar ao Servidor", command= lambda: socket == conectarServidor()))
        btnDesconectar.destroy()
        btnConectar.grid(column=1, row=1)
        status = "Offline"
    except:
        status = "Online"

    bio = Label(telaMain,text = "Faça upload e download de arquivos no servidor! \n Status: " + status)
    bio.grid(column=1, row=0)

def enviarImg():
    pass

def baixarImg():
    pass

def selecionarDl():
    pass

def selecionarUp():
    # Ainda precisa definir mais tipos de arquivos para envio
    # Separa o que será mostrado na tela dependendo do arquivo:
    # Imagem: Mostrar a imagem (Tentar controlar o tamanho dela).
    # Txt: Mostrar um ícone padrão 
    global img
    try:
        telaMain.filename = filedialog.askopenfilename(initialdir="/Users/PC/Downloads", title="Selecionar Imagem", filetypes=(("PNG files", "*.png"),("JPEG files","*.jpeg")))
        img = ImageTk.PhotoImage(Image.open(telaMain.filename))
        imgLabel = Label(image=img)
        imgLabel.grid(column=1, row=2)
    except:
        print("Nenhuma imagem selecionada ou erro na seleção!")

################################# CÓDIGO PRINCIPAL ################################

telaMain = Tk()
telaMain.title("EzShare")
telaMain.maxsize(790, 660)
#telaMain.geometry("790x660")
status = "Offline"

#Cria os textos informativos#
bio = Label(telaMain,text = "Faça upload e download de arquivos no servidor! \n Status: " + status) #Header
bio.grid(column=1, row=0)

acao = Label(telaMain,text = "Aguardando Ação...") #Texto informando a ação tomada
acao.grid(column=1, row=4)

bio = Label(telaMain,text = "Upload")
bio.grid(column=0, row=3)

bio = Label(telaMain,text = "Download")
bio.grid(column=2, row=3)


socket = 0
#Cria todos os botões do menu principal
# Botão para conectar no servidor
btnConectar = (Button(telaMain, text="Conectar ao Servidor", command= lambda: socket == conectarServidor()))

#Botões de download
btnBaixarDl = Button(telaMain, text="Baixar", command=baixarImg)
btnSelecionarDl = Button(telaMain, text="Selecionar", command=selecionarDl)

#Botões de upload
btnEnviarUp = Button(telaMain, text="Enviar", command=enviarImg)
btnAbrirUp = Button(telaMain, text="Abrir", command=selecionarUp)


#Dispõe os botões no display#
btnConectar.grid(column=1, row=1)
btnBaixarDl.grid(column=2, row=4)
btnSelecionarDl.grid(column=2, row=5)
btnEnviarUp.grid(column=0, row=4)
btnAbrirUp.grid(column=0, row=5)

telaMain.mainloop()



################################# CÓDIGO ANTIGO #################################
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