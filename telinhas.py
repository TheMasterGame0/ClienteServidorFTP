from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
# Coisas a fazer.
# Fazer o menu para decidir o que baixar.
#   Pegar o texto retornado pelo servidor e colocá-lo em uma "lista" para ser selecionado
#   Pegar a string retornada, utilizar um split com os espaços e percorrer de maneira padronizada em grupos de 4 em 4. 
#   Fazer a verificação da 3º posição para ver se é um int ou a string "<DIR>".
#   Para saber quantos elementos tem no diretório atual será obtido com o len da lista montada dividida por 4.
#   O retorno do item escolhido deverá ser no formato:
#       - Diretório raiz: Apenas o nome do arquivo. Ex: \Teste.txt
#       - Uma pasta: O caminho do raiz até o arquivo. Ex: \Pasta\OutroTeste.txt
#
# Fazer o menu de decidir onde baixar.
# Fazer no botão de Enviar no Upload a opção de criar pastas no servidor e selecionar onde será salvo (Mesmo que o item anterior).
# Código de sucesso da transferência: 226 Transfer complete.


# Cliente criado
from Cliente import *

# Função acionada pelo botão para conectar ao servidor e atualizar a tela
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

# Função acionada pelo botão para desconectar do servidor e atualizar a tela
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

def selecionarDl():
    # Cria a telinha de seleção por cima da Main
    telaSelecao = Toplevel(telaMain)
    telaSelecao.geometry("400x100")
    telaSelecao.maxsize(600,350)
    telaSelecao.title("Selecionar Imagem")



def selecionarUp():
    # Ainda precisa definir mais tipos de arquivos para envio
    # Separa o que será mostrado na tela dependendo do arquivo:
    # Imagem: Mostrar a imagem (Tentar controlar o tamanho dela).
    # Txt: Mostrar um ícone padrão

    global img

    # print("Texto!")
    # iconeAjustado = Image.open("C:/Users/PC/Desktop/iconeTXT.png").resize((200, 200))
    # icone = ImageTk.PhotoImage(iconeAjustado)
    # iconeLabel = Label(image=icone)
    # iconeLabel.grid(column=1, row=2)

    try:
        # ERRO: Algumas imagens com dimensoes muito grandes e/ou certas razões não passam para a tela
        telaMain.filename = filedialog.askopenfilename(initialdir="/Users/PC/Downloads", title="Selecionar Imagem",
                                                       filetypes=(("All files", "*.*"), ("PNG files", "*.png"),
                                                                  ("JPEG files", "*.jpeg")))
        tipoArquivo = telaMain.filename.split('.', 1)[1] # Determina o tipo de extensão do arquivo selecionado

        match tipoArquivo: # Casos de tipo de arquivo: Decide qual ícone será mostrado na tela
            case "png": # Mostra a imagem selecionada
                print("Imagem!")
                imgAjustada = Image.open(telaMain.filename).resize((200, 200))
                img = ImageTk.PhotoImage(imgAjustada)
                imgLabel = Label(image=img)
                imgLabel.grid(column=1, row=2)
            case "txt": # Mostra a icone correspondente
                print("Texto!")
                iconeAjustado = Image.open("Recursos\\iconeTXT.png").resize((200, 200))
                icone = ImageTk.PhotoImage(iconeAjustado)
                iconeLabel = Label(image=icone)
                iconeLabel.grid(column=1, row=2)
            case"pdf":
                print("PDF!")

    except:
        print("Nenhuma imagem selecionada ou erro na seleção!")

################################# CÓDIGO PRINCIPAL ################################

# Cria a tela principal e limita seu tamanho
telaMain = Tk()
telaMain.title("EzShare")
telaMain.maxsize(790, 660)
#telaMain.geometry("790x660")

# Define o ícone da janela (Canto esquerdo superior)
icone = Image.open("Recursos\\iconeApp.png")
imgIcone = ImageTk.PhotoImage(icone)
telaMain.wm_iconphoto(False, imgIcone)

status = "Offline"

#Cria os textos informativos#
bio = Label(telaMain,text = "Faça upload e download de arquivos no servidor! \n Status: " + status) # Header
bio.grid(column=1, row=0)

acao = Label(telaMain,text = "Aguardando Ação...") # Texto informando a ação tomada
acao.grid(column=1, row=4)

bio = Label(telaMain,text = "Upload")
bio.grid(column=0, row=3)

bio = Label(telaMain,text = "Download")
bio.grid(column=2, row=3)


socket = 0

#Cria todos os botões do menu principal#
# Botão para conectar no servidor
btnConectar = (Button(telaMain, text="Conectar ao Servidor", command= lambda: socket == conectarServidor()))

# Botões de download
btnBaixarDl = Button(telaMain, text="Baixar", command=baixarImg)
btnSelecionarDl = Button(telaMain, text="Selecionar", command=selecionarDl)

# Botões de upload
btnEnviarUp = Button(telaMain, text="Enviar", command=enviarImg)
btnAbrirUp = Button(telaMain, text="Abrir", command=selecionarUp)

# Dispõe os botões no display#
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