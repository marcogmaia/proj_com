import pickle
import bisect
import os

class dbNode():
	__nodeId = 1

	def __init__(self, owner, name, filetype, parent, data):
		self.__owner = owner
		self.name = name
		self.__filetype = filetype
		self.__parent = parent
		self.data = data
		self.__id = self.__genId()
		self.__childs = []

	def __genId(self):
		dbNode.__nodeId += 1
		return (dbNode.__nodeId - 1)

	def getOwner(self):
		return self.__owner

	def getName(self):
		return self.name

	def getType(self):
		return self.__filetype

	def getParent(self):
		return self.__parent

	def getData(self):
		return self.data

	def getId(self):
		return self.__id

	def getChilds(self):
		return self.__childs

	def setData(self, data):
		self.data = data

	def setName(self, name):
		self.name = name

	def addChild(self, newChild):
		pos = bisect.bisect(self.childs, newChild)
		if self.childs[pos-1] == newChild:
			print("caminho ja existe!")
			return -1
		else:
			bisect.insort(self.childs, newChild)
			return pos

	def updateChild(self, childId):
		return childId
		'''
		Preciso implementar isso pra poder terminar o addDir do dataBase
		'''
class dataBase():
	__staticId = 1

	def __genId(self):
		dataBase.__staticId += 1
		return (dataBase.__staticId - 1)

	def __makeDB(self, path):
		if not os.path.isdir(path):
			os.makedirs(path)
		else:
			print("database ja existe!")

	def __init__(self):
		self.id = self.__genId()
		self.userList = []
		self.content = []
		self.__makeDB(str(self.id))

	def createUser(self, user, password):
		users = [x[0] for x in self.userList]
		pos = bisect.bisect(users, user)

		if users[pos-1] == user:
			print("usuario ja existe!")
		else:
			key = [user, password]
			bisect.insort(self.userList, key)
	
	def createDir(self, name, owner):
		path = self.id+"/"+name
		if os.path.isdir(path):
			print("diretorio ja existe!")
		else:
			folders = [x for x in self.content if x.getType() == "folder"]
			tracer = []
			root = [name]

			while(root != root[-1].split("/", 1)):
				root = root[-1].split("/", 1)
				folders = [x for x in folders if (x.getType() == "folder" and x.getName() == root[0])]
				if len(folders) is not 0:
					tracer.append(folders[0])
					folders = folders[0].getChilds()

			path = root[0]
			parent = tracer[-1].getId()
			node = dbNode(owner, path, "folder", parent, "not a file!")
			'''
			Preciso adicionar os filhos recursivamente pra cima e atualizar a pasta raiz do content
			ou seja, adiciona o novo node na ultima pasta do tracer, depois atualizo essa nova pasta
			na penultima do tracer e assim sucessivamente até que eu chegue na pasta que está no 
			content, por fim essa pasta deve ser atualizada usando bisect.
			'''


	def createFile(self, name, data):
		path = self.id+"/"+name
		if os.path.isfile(path):
			print("arquivo ja existe!")
		else:
			node = dbNode(path, "file", self.id, data)