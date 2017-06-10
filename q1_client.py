#!/usr/bin/env python3
import socket
import sys

host = 'localhost'
port = 5555

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
                if data == '\x18': # CTRL+x pra terminar
                    self.sock.send(bytes('stop', 'utf8'))
                    sys.exit()
                else:
                    self.sock.send(bytes(data, 'utf8'))

        elif self.protocol == 'udp':
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while 1:
                data = input()
                if data == '\x18':
                    self.sock.sendto(bytes('stop', 'utf8'), (host, port))
                else:
                    self.sock.sendto(bytes(data, 'utf8'), (host, port))

        else:
            print('ERROR: protocol not defined')

if __name__ == '__main__':
    with open('protocol.txt', 'r') as f:
        protocol(f.readline())

