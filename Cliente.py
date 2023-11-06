import socket as s

# Responsável por criar o socket 
def criarSocket(host,port):   
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    endereco = (host, port) # Endereço IP e a porta do servidor
    socket.connect(endereco)
    receberMensagem(socket) 
    return socket

# Fechar o socket
def fecharSocket(socket):
    mensagem = "QUIT\r\n"
    socket.send(mensagem.encode('utf-8')) 
    receberMensagem(socket)
    socket.close()

# Faz login no servidor
def Login(socket, user, senha):
    usuario = "user {u}\r\n".format(u = user)
    comunicar(socket, usuario)       # Login
    password = "pass {s}\r\n".format(s = senha)
    comunicar(socket, password)      # Senha

# Estabelece uma conexão com o servidor (com login) e configura
def Conectar(Usuario, Senha):
    socket = criarSocket(host, port)
    Login(socket, Usuario, Senha)
    comunicar(socket, "opts UTF8 ON\r\n")      # Configura o tipo de ASCII utilizado
    return socket

# Tenta enviar uma mensagem ao servidor
def mandarMensagem(socket, mensagem):
    try:
        socket.settimeout(0.2)                 # Tempo do time out
        socket.send(mensagem.encode('utf-8'))   # Retorna o tamanho da mensagem enviada
    except:
        print("Time out")

# Tenta recebe as mensagens do servidor
def receberMensagem(socket):
    TimeOut = False
    mensagemTotal = ""
    Vazio = 0
    while not TimeOut:              # Recebe so servidor até superar o limite de tempo
        try:
            socket.settimeout(0.2)  # Tempo do time out
            resposta = socket.recv(2048)
            dados = resposta.decode('utf-8')
            if dados in ["","\n","\r","\r\n"]:
                Vazio += 1
                if Vazio >= 2:
                    return mensagemTotal
            else:
                print(dados)
                mensagemTotal = mensagemTotal + dados
        except:
            TimeOut = True
    return mensagemTotal

# Envia uma mensagem e obtêm as respostas 
def comunicar(socket, mensagem):
    mandarMensagem(socket,mensagem)
    receberMensagem(socket)

# Cria um caminho de dados para transferir os dados 
def caminhoDeDados(socket):
    mandarMensagem(socket, "pasv\r\n")      # Estabelece a conexão como passiva
    dados = receberMensagem(socket)         # Recebe os dados retornados pelo servidor
    
    eliminar = ",.()\r\n"
    endereco = [item for item in dados.split(" ")[-1].split(",")]
    P1 = endereco[-2]
    P2 = "".join([caracter for caracter in endereco[-1] if caracter not in eliminar])
    porta = int(P1)*256 + int(P2)
    caminho = s.socket(s.AF_INET, s.SOCK_STREAM)
    end = (host, porta)
    caminho.connect(end)
    receberMensagem(caminho)
    return caminho

#Lista os objetos no caminho indicado
def Listar(socket, path):
    caminho = caminhoDeDados(socket)
    mensagem = "list "+path+final
    mandarMensagem(socket, mensagem)
    confirmacao = receberMensagem(socket)   # Resposta de confirmação da conexão
    conteudo = receberMensagem(caminho)     # Conteúdo retornado
    receberMensagem(socket)
    caminho.close()
    # Colocar o retorno que será utilizado pela tela
    return confirmacao, conteudo

# Faz download de algo que está no servidor
# É preciso colocar o nome do arquivo desejado no path
def Download(socket, pathServidor, pathLocal):
    caminho = caminhoDeDados(socket)
    mensagem = "RETR "+pathServidor+final
    mandarMensagem(socket, mensagem)
    confirmacao = receberMensagem(socket)   # Resposta de confirmação da conexão
    conteudo = receberMensagem(caminho)     # Conteúdo retornado
    receberMensagem(socket)
    caminho.close()
    # Colocar o retorno que será utilizado pela tela
    # Criar o arquivo que será salvo com o caminho informado pela tela
    criarArquivo(pathLocal, conteudo) 
    return confirmacao

# Salva o arquivo no path informado no Servidor no diretório atual
# O path Local deve ser um path relativo para o servidor FTP compreender
def Upload(socket, pathServidor, pathLocal):
    caminho = caminhoDeDados(socket)
    path = "".join(x for x in pathServidor)
    mensagem = "STOR "+path+final 
    texto = mandarArquivo(caminho, pathLocal)   # Responsável por abrir o aquivo do sistema e mandá-lo pelo caminho de dados
    mandarMensagem(socket, mensagem)
    confirmacao = receberMensagem(socket)   # Resposta de confirmação da conexão
    conteudo = receberMensagem(caminho)     # Conteúdo retornado
    receberMensagem(socket)
    caminho.close()    
    return confirmacao

# Criar o arquivo que será salvo com o caminho informado pela tela
def criarArquivo(pathLocal, conteudo):
    try:
        if type(pathLocal) == type(["lista", "de", "teste"]):
            path = "".join(x+" " for x in pathLocal)
            with open(path, "x") as f:
                f.write(conteudo)
        else:
            with open(pathLocal, "x") as f:
                f.write(conteudo)
    except FileNotFoundError:
        print("O path fornecido tem problemas")
    except FileExistsError:
        print("Existe um arquivo com o mesmo nome fornecido")

# Seleciona um arquivo do cliente 
def mandarArquivo(socket, pathLocal):
    try:
        if type(pathLocal) == type(["lista", "de", "teste"]):
            path = "".join(x+" " for x in pathLocal)
            mandarMensagem(socket, lerArquivo(path))     # Manda o conteúdo do arquivo
        else:
            mandarMensagem(socket, lerArquivo(pathLocal))# Manda o conteúdo do arquivo
    except FileNotFoundError:
        print("O path fornecido tem problemas")
    except FileExistsError:
        print("Existe um arquivo com o mesmo nome fornecido")

# Escreve texto em um arquivo
def lerArquivo(pathLocal):
    with open(pathLocal, "r") as f:
        textoCompleto = f.readlines()
        string = "".join([x for x in textoCompleto])
        return string

################### Constantes e Loop de testes ######################
# Parâmetros universais para o código
host = "127.0.0.1"  # IP do host utilizado
port = 21           # Porta de acesso
user = "ftpUser"    # Usuário utilizado para logar no Servidor
senha = "12345"     # Senha do usuário

# Constantes
final = "\r\n"

# socket = Conectar(user, senha)
# while(True):
#     entrada = input()
#     if entrada == "Conectar":
#         socket.close()
#         socket = Conectar(user, senha)
#     elif (entrada.split(" ")[0] == "Listar"):
#         msg = entrada.split(" ")[-1]
#         if msg == "Listar":
#             Listar(socket, "")
#         else:
#             Listar(socket, msg)
#     elif (entrada.split(" ")[0] == "Download"):
#         if entrada != "Download":
#             pathServidor = entrada.split(" ")[1]
#             pathLocal = entrada.split(" ")[2:]
#             Download(socket, pathServidor, pathLocal)
#         else:
#             print("Precisa dos paths")
#     elif (entrada.split(" ")[0] == "Upload"):
#         if entrada != "Upload":
#             pathServidor = entrada.split(" ")[1:]
#             pathLocal = input()
#             Upload(socket, pathServidor, pathLocal)
#         else:
#             print("Precisa dos paths")
#     else:
#         msg = entrada + final
#         comunicar(socket, msg)
