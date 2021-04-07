from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class ServidorTCP:
    def __init__(self, endereco, porta):
        self.endereco = endereco
        self.porta = porta

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((endereco, porta))
        self.sock.listen()
        print('Servidor TCP ouvindo requisições...')
        
        while True:
            client_sock, client_address = self.sock.accept()
            print('Conexão estabelecida.')
            Thread(target=ServidorTCP.thread_communication, args=(client_sock, client_address)).start()
            print('Ouvindo novas requisições')

    @staticmethod
    def thread_communication(client_sock, client_address):
        while True:
            received_data = client_sock.recv(2048)
            print(f'Cliente ({client_address}) enviou: {received_data.decode()}')

            msg_return = "Recebi sua mensagem: "
            msg_return += str(received_data.decode())
            client_sock.send(msg_return.encode())


ServidorTCP('localhost', 9501)
