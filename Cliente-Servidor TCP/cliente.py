from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time


class ClienteTCP:
    def __init__(self, endereco, porta):
        self.endereco = endereco
        self.porta = porta

        self.sock = socket(AF_INET, SOCK_STREAM)

        print('Procurando servidores..')
        self.sock.connect((endereco, porta))
        print('Conexão estabelecida.\n')

        Thread(target=self.receive, args=()).start()

        while True:
            message = input('\nDigite mensagem para enviar ao servidor:')
            self.sock.send(message.encode())
            time.sleep(1)

    def receive(self):
        while True:
            received_data = self.sock.recv(2048)
            print(f'\nServidor disse: {received_data.decode()}')


try:
    ClienteTCP('localhost', 9501)
except ConnectionRefusedError:
    print('Conexão negada')
