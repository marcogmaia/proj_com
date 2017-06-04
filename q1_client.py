#!/usr/bin/env python3
import socket

host = 'localhost'
port = 5555

# def send_tcp():
#     connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     connection.connect(('localhost', 5555)) # 3-way handshake kkk
#     while True:
#         var = input()
#         connection.send(bytes(var, 'UTF-8'))

# def send_udp():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     while 1:
#         data = input()
#         if data == 'stop':
#             sock.sendto(bytes(data, 'utf8'), ('localhost', 5555))
#             exit()
#         else:
#             sock.sendto(bytes(data, 'utf8'), ('localhost', 5555))


class protocol():
    def __init__(self, protocol='tcp'):
        self.protocol = protocol
        self.sock = None
        self.send()

    def send(self):
        if self.protocol == 'tcp':
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, port))
            while 1:
                data = input()
                self.sock.send(bytes(data, 'utf8'))

        elif self.protocol == 'udp':
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while 1:
                data = input()
                self.sock.sendto(bytes(data, 'utf8'), (host, port))

        else:
            print('ERROR: protocol not defined')

if __name__ == "__main__":
    with open('protocol.txt', 'r') as f:
        protocol(f.readline())

