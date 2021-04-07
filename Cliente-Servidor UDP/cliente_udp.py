from socket import socket, AF_INET, SOCK_DGRAM

UDPSocket = socket(AF_INET, SOCK_DGRAM)

print("Teste Cliente-Servidor UDP")
print("Eu sou o cliente!")

ja_iniciou = False


while True:
    global ja_iniciou

    
    
    #Envia mensagem para o servidor:
    mensagem = input("\nDigite uma nova mensagem para enviar: ")
    mensagem_codificada = mensagem.encode() 
    UDPSocket.sendto(mensagem_codificada,('localhost', 9500)) 
    print("Enviou",mensagem,"para o servidor")

    #Aguarda mensagem do servidor:
    resposta_servidor = UDPSocket.recvfrom(1024)  
    resposta = str(resposta_servidor[0].decode()) #([0]mensagem,([0]IP, [1]PORTA))

    print(f'E o servidor respondeu: {resposta}')    

    
    
