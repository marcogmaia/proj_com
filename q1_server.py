#!/usr/bin/env python3
import socket

hostname = 'localhost'
port = 5555


class protocol():
    def __init__(self, protocol = 'tcp'):
        self.protocol = protocol
        self.sock = None

        if protocol == 'udp':
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind((hostname, port))
            self.listen()

        elif protocol == 'tcp':
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((hostname, port))
            # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # self.sock.listen(10)
            self.listen()
        else:
            print('Protocol not defined. Use tcp or udp')

    def __del__(self):
        self.sock.shutdown(1)
        self.sock.close()
        
    def listen(self):
        if self.protocol == 'udp':
            while 1:
                data, addr = self.sock.recvfrom(1024)
                data = data.decode('utf8')
                if data == 'stop':
                    exit()
                else:
                    print(addr, data)

        if self.protocol == 'tcp':
            self.sock.listen()
            current_connection, address = self.sock.accept()
            while 1:
                data = current_connection.recv(1024)
                datadecode = data.decode('utf8')
                if  datadecode == 'stop':
                    print('STOP command received. Server shutdown.')
                    exit()
                elif data:
                    current_connection.send(data)
                    print(address, datadecode)

        

if __name__ == '__main__':
    with open('protocol.txt', mode='r') as f:
        protocol(f.readline())