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
    socket.close()

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
    while not TimeOut:                          # Recebe so servidor até superar o limite de tempo
        try:
            socket.settimeout(0.2)             # Tempo do time out
            resposta = socket.recv(2048)
            dados = resposta.decode('utf-8')
            print(dados)
            return dados
        except:
            TimeOut = True

# Envia uma mensagem e obtêm as respostas 
def comunicar(socket, mensagem):
    mandarMensagem(socket,mensagem)
    receberMensagem(socket)

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
    receberMensagem(socket)
    receberMensagem(caminho)
    receberMensagem(socket)
    caminho.close()

############################################################################
# Parâmetros universais para o código
host = "127.0.0.1"  # IP do host utilizado
port = 21           # Porta de acesso
user = "ftpUser"    # Usuário utilizado para logar no Servidor
senha = "12345"     # Senha do usuário

# Constantes
final = "\r\n"

socket = Conectar(user, senha)
while(True):
    entrada = input()
    if entrada == "Conectar":
        socket.close()
        socket = Conectar()
    elif (entrada.split(" ")[0] == "Listar"):
        msg = entrada.split(" ")[-1]
        if msg == "Listar":
            Listar(socket, "")
        else:
            Listar(socket, msg)
    else:
        msg = entrada + final
        comunicar(socket, msg)