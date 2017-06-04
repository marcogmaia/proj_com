import database_tree as db
import bisect
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

accounts = []
idle = db.account('idle', 0)
sudo = db.account('sudo', 65535)
sudo.changePrivilege(65535, 'admin')
bisect.insort(accounts, sudo)
root = db.dbNode(sudo, 'root', 'folder', 'not a file!')
logged = idle
directory = 0

while 1:
	cls()
	curUsers = [x.getUsername() for x in accounts]
	menu = "1 - Create User\n2 - Change Password\n3 - Create Folder\n4 - Delete Folder\n5 - Upload File\n6 - Download File\n7 - Delete File\n8 - Login\n9 - Logout\n"
	opt = str(input(menu))
	if opt == '1':
		cls()
		usr = str(input("Digite nome de usuario desejado: "))
		while usr in curUsers:
			usr = str(input("Nome ja existe, tente outro nome: "))
		
		pass1 = 0; pass2 = 1
		while pass1 != pass2:
			pass1 = input("Digite a senha desejada: ")
			pass2 = input("Confirme a senha desejada: ")
			if pass1 != pass2:
				print("Senhas nao conferem!\n")

		newusr = db.account(usr, pass1)
		bisect.insort(accounts, newusr)
	
	elif opt == '2':
		cls()
		if logged == idle:
			print("Voce precisa estar logado!\n")
		else:
			usr = logged.getUsername()

			pass1 = 0; pass2 = 1
			while pass1 != pass2:
				pass1 = input("Digite a senha antiga: ")
				pass2 = input("Confirme a senha antiga: ")
				if pass1 == pass2 and db.account(usr, pass1):
					if db.account(usr, pass1) in accounts:
						pos = bisect.bisect(accounts, db.account(usr, pass1))
						newpass = input("Digite a nova senha: ")
						suss = accounts[pos-1].changePassword(pass1, newpass)
						if suss == 1:
							print("Senha alterada")
						if suss == -1:
							print("Senha antiga incorreta!\n")
							pass1 = 'err'

				else:
					print("Senhas nao conferem!\n")

	elif opt == '3':
		cls()
		if logged == idle:
			print("Voce precisa estar logado!\n")
		else:
			path = str(input("Digite o caminho da pasta que você deseja criar: "))
			path = path.split("/")
			while path[0] == '':
				del path[0]
			if root.addChildren(logged, path, 'folder', 'not a file!') == 1:
				print("Pasta criada!\n")
			else:
				print("Pasta ja existe!\n")


	elif opt == '8':
		cls()
		while True:
			usr = str(input("Digite o nome de usuario: "))
			password = input("Digite a senha: ")
			if db.account(usr, password) in accounts:
				logged = db.account(usr, password)
				break
			else:
				print("Usuario e/ou senha incorretos\n")

	elif opt == '9':
		cls()
		sure = str(input("Voce tem certeza que deseja sair? S/N\n"))
		while sure != 'N':
			if sure == 'S':
				logged = idle
				print("Deslogado com sucesso!\n")
				sure = 'N'
			else:
				sure = str(input("Opcao invalida! Digite S ou N\n"))