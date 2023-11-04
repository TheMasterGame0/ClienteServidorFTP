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
        #socket = Conectar(user, senha)
        socket = 0 #Para teste sem o servidor

        # Botão para desconectar o servidor
        global btnDesconectar;
        btnDesconectar = (Button(telaMain, text="Desconecte do Servidor", command= lambda: desconectaServidor(socket)))
        btnConectar.destroy()
        iniciarBotoes(socket)   # Cria os demais botões da tela
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

def selecionarDl(socket):
    #confirmacao, conteudo = Listar(socket, "") 
    confirmacao, conteudo = "125 Data connection already open; Transfer starting.\n226 Transfer complete.", "03-10-22  01:35AM               419965 Imagem.png\n11-02-23  09:53PM       <DIR>          Pasta\n11-03-23  02:20PM                   29 Teste.txt\n11-03-23  10:12PM                    0 Teste4.txt"      #Para teste sem o servidor


    if "transfer complete" in confirmacao.lower(): # Verifica se a conexão foi estabelecida
        # Cria a telinha de seleção por cima da Main
        telaSelecao = Toplevel(telaMain)
        telaSelecao.geometry("400x200") # X, Y
        telaSelecao.maxsize(400, 400)
        telaSelecao.title("Selecionar Arquivo")

        # Cria a caixa vazia que receberá as informações dos arquivos
        listaConteudo = Listbox(telaSelecao)
        listaConteudo.pack(expand = True, fill = BOTH, padx=15, pady = 15)

        # Divide o conteúdo recebido em listas de 4 itens
        conteudo = conteudo.split()
        conteudo = [conteudo[i:i + 4] for i in range(0, len(conteudo), 4)]
        print(conteudo)

        # Insere os itens na lista vazia
        for item in conteudo:
            listaConteudo.insert(END, item)

        # Determina e registra qual item foi selecionado pelo usuário
        for i in listaConteudo.curselection():
            arquivoSelecionado = listaConteudo.get(i)[4]
            tipoArquivo = listaConteudo.get(i)[3]

            print(arquivoSelecionado)

    else:
        print("erro")
        pass # Atualizar texto informativo para dizer que a conexao nao foi estabelecida



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


def iniciarBotoes(socket):
############ Labels ############
    acao = Label(telaMain,text = "Aguardando Ação...") # Texto informando a ação tomada
    acao.grid(column=1, row=4)

    bio = Label(telaMain,text = "Upload")
    bio.grid(column=0, row=3)

    bio = Label(telaMain,text = "Download")
    bio.grid(column=2, row=3)

############ Botões ############    
    # Botões de download
    btnBaixarDl = Button(telaMain, text="Baixar", command=baixarImg)
    btnSelecionarDl = Button(telaMain, text="Selecionar", command= lambda: selecionarDl(socket)) 

    # Botões de upload
    btnEnviarUp = Button(telaMain, text="Enviar", command=enviarImg)
    btnAbrirUp = Button(telaMain, text="Abrir", command=selecionarUp)

######### Dispõe os botões no display #########
    btnBaixarDl.grid(column=2, row=4)
    btnSelecionarDl.grid(column=2, row=5)
    btnEnviarUp.grid(column=0, row=4)
    btnAbrirUp.grid(column=0, row=5)


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


#Cria todos os botões do menu principal#
# Botão para conectar no servidor
btnConectar = (Button(telaMain, text="Conectar ao Servidor", command= conectarServidor))

# Dispõe os botões no display#
btnConectar.grid(column=1, row=1)

telaMain.mainloop()