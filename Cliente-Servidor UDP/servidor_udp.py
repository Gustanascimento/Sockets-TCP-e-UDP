from socket import socket, AF_INET, SOCK_DGRAM

UDPServerSocket = socket(AF_INET, SOCK_DGRAM)
UDPServerSocket.bind(('localhost', 9500))

print("Teste Cliente-Servidor UDP")
print("Eu sou o servidor!")
print("Aguardando mensagens de clientes...")

while True:

    mensagem_cliente = UDPServerSocket.recvfrom(1024)   
    msg = str(mensagem_cliente[0].decode()) 
    endereco = mensagem_cliente[1]
    print(f'\nO cliente {endereco} enviou: "{msg}"')
    
    resposta = ('Você me enviou: ')
    resposta+=msg
    resposta_cliente = str.encode(resposta)
    
    UDPServerSocket.sendto(resposta_cliente, endereco) 
    print("Resposta enviada ao cliente")
    
    
          

              


    
