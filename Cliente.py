import socket as s
# Parâmetros universais para o código
host = "127.0.0.1"  # IP do host utilizado
port = 21           # Porta de acesso
user = "ftpUser"    # Usuário utilizado para logar no Servidor
senha = "12345"     # Senha do usuário

# Função responsável por criar o socket 
def criarSocket(host,port):   
    socket = s.socket(socket.AF_INET, socket.SOCK_STREAM)
    endereco = (host, port) # Endereço IP e a porta do servidor
    socket.connect(endereco)
    receive_msg(socket) 
    return socket

def fecharSocket(socket):
    socket.close()

def send_msg(socket, message):
    try:
        socket.settimeout(0.2)                 # Tempo do time out
        socket.send(message.encode('utf-8'))   # Retorna o tamanho da mensagem enviada
        receive_msg(socket)                    # Pega a mensagem recebida
    except:
        print("Time out")

def receive_msg(socket):
    TimeOut = False
    while not TimeOut:                          # Recebe so servidor até superar o limite de tempo
        try:
            socket.settimeout(0.2)             # Tempo do time out
            resposta = socket.recv(2048)
            print(resposta.decode('utf-8'))
        except:
            TimeOut = True

def Conectar():
    socket = criarSocket(host, port)
    Login(socket, user, senha)
    send_msg(socket, "opts UTF8 ON\r\n")       # Configura o tipo de ASCII utilizado
    return socket

def Login(socket, user, senha):
    send_msg(socket, "user {u}\r\n").format(u = user)       # Login
    send_msg(socket, "pass {s}\r\n").format(s = senha)      # Senha

socket = Conectar()
while(True):
    final = "\r\n"
    entrada = input()
    if entrada == "Conectar":
        socket.close()
        socket = Conectar()
    # elif (entrada.split(" ")[0] == "list"):
    #     msg = entrada + final
    #     send_msg(cliente, msg)
    #     cliente.close()
    else:
        msg = entrada + final
        send_msg(socket, msg)