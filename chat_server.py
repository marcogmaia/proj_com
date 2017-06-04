import socket, select, sys

HOST = ''
PORT = 4321
BUFFER = 2048
SOCKET_LIST = []



def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    SOCKET_LIST.append(server_socket)

    print("Chat Server is up and running!")

    while 1:
        ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [], 0)

        for sock in ready_to_read:
            if sock == server_socket:
                new_sock, addr = server_socket.accept()
                SOCKET_LIST.append(new_sock)
                print("New Client!, addr :" + str(addr))

                msg = str(addr) + "Entered the room"

                broadcast(server_socket, new_sock, msg)
                
            else:
                response = sock.recv(BUFFER)
                response = response.decode()
                print(response)
                if response:
                    broadcast(server_socket, sock, " (" +  str(sock.getpeername()) + ")  " + response)

                else:
                    if sock in SOCKET_LIST:
                        SOCKET_LIST.remove(sock)

                    broadcast(server_socket, sock, " User " + str(sock.getpeername()) + "has left the server")

    server_socket.close()



def broadcast(server, sock, msg):
    for s in SOCKET_LIST:
        try:
            if s != server and s != sock:
                s.send(msg.encode())

        except:
            s.close()
            if s in SOCKET_LIST:
                SOCKET_LIST.remove(s)


if __name__ == '__main__':
    chat_server()
