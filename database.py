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
		pos = bisect.bisect(self.__childs, newChild)
		if self.__childs[pos-1] == newChild:
			print("caminho ja existe!")
			return -1
		else:
			bisect.insort(self.__childs, newChild)
			return pos

	def updateChild(self, child):
		oldChild = [x for x in self.getChilds() if x.getId() == child.getId()]
		del self.__childs[bisect.bisect(self.__childs, oldChild) - 1]
		bisect.insort(self.__childs, child)
		return childId

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
			if len(tracer) > 0:
				parent = tracer[-1].getId()
			else:
				parent = self.id
			node = dbNode(owner, path, "folder", parent, "not a file!")
			

			if len(tracer) == 0:
				pos = bisect.bisect(self.content, node)
				if self.content[pos-1] == node:
					print("caminho ja existe!")
				else:
					bisect.insort(self.content, node)
			else:
				tail = tracer.pop()
				tail.addChild(node)
				while len(tracer) > 0:
					tail = tracer.pop()

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