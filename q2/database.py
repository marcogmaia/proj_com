import node
import os

class database():
	def __init__(self, name, admin):
		self.root = node(name = name, owner = admin)
		self.acc_list = dict()
		self.admin = admin
		try:
			os.makedirs("root-"+name)
		except OSError:
			print("DB "+name+" already exists!")
		os.chdir("root-"+name)
	'''getters'''
	def getRoot(self):
		return self.root
	def getAccountList(self):
		return self.acc_list
	def getAdmin(self):
		return self.admin
	'''setters'''
	def setAccount(self, newAccount):
		if newAccount is not None:
			self.acc_list.add(newAccount)
			return True
		return False
	'''functions'''
	def createFolder(self, onwer, path):
		if owner[0] not in self.getAccountList():
			return False
		if os.path.isdir(path):
			return False

		begin = path.split("/", 1)[0]
		if os.path.isdir(begin):
			usr = [x.getOwner() for x in self.getRoot().getChildren() if x.getName() == begin]
			if usr != owner:
				return False

		os.makedirs(path)
		token = path.split("/")
		if len(token) == 1:
			newChild = node(name = token.pop(), owner = onwer, parent = self.root)
			return True

		newChild = node(name = token.pop(), owner = onwer)
		while len(token) > 0:
			folder = node(name = token.pop(), owner = owner)
			newChild.setParent(folder, owner)
			folder.setChildren(newChild, owner)
			newChild.setParent(folder, owner)


		self.root.setChildren(folder, admin)