import socket
import pickle

def tcp_client():
	HOST = str(input("Qual o endereco IP do servidor? "))
	PORT = input("Qual a porta do servidor? ")

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.settimeout(2)
	dest = (HOST, PORT)
	tcp.connect(dest)
	
	print ('Para sair use CTRL+X\n')
	msg = input()
	while msg != '\x18':
		msg = pickle.dumps(msg)
		tcp.send (msg)
		msg = input()
	tcp.close()

if __name__ == "__main__":
	tcp_client()