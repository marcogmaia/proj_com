import socket
import sys
import pickle

def udp_pack(src, dest, data):
	length = 8 + len(data)
	checksum = 0 '''n sei implementar isso ainda'''
	header = (src<<48) + (dest<<32) + (length<<16) + (checksum)
	udp_seg = [header, data]
	return pickle.dumps(udp_seg)


def udp_client():
	HOST = str(input("Qual o endereco IP do servidor? "))
	PORT = input("Qual a porta do servidor? ")

	udp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)
	
	print ('Para sair use CTRL+X\n')
	msg = str(input("[Me]: "))
	while msg != '\x18':
		msg = udp_pack(0, PORT, msg)
		udp.sendto(msg, dest)
		msg = str(input())
	udp.close()

if __name__ == "__main__":
	udp_client()