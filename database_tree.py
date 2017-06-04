import os
import bisect

class account():
	__sudoPass = 65535

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.__privilege = 'user'

	def __lt__(self, other):
		return self.username < other.username
	def __le__(self, other):
		return self.username <= other.username
	def __eq__(self, other):
		return (self.username == other.username and self.password == other.password)
	def __ne__(self, other):
		return self.username != other.username
	def __gt__(self, other):
		return self.username > other.username
	def __ge__(self, other):
		return self.username >= other.username

	def changePrivilege(self, sudoPass, newPriv):
		if account.__sudoPass == sudoPass:
			self.__privilege = newPriv
			return 1
		else:
			return -1

	def changePassword(self, oldPass, newPass):
		if self.password == oldPass:
			self.password = newPass
			return 1
		else:
			return -1

	def getUsername(self):
		return self.username

	def getPassword(self):
		return self.password

class dbNode():
	def __init__(self, onwer, name, filetype, data):
		self.onwer = onwer
		self.name = name
		self.filetype = filetype
		self.data = data
		self.__children = []
		self.__allowed_see = []
		self.__allowed_edit = []
		if filetype == 'folder':
			self.__makedir(name)

	def __lt__(self, other):
		return self.name < other.name
	def __le__(self, other):
		return self.name <= other.name
	def __eq__(self, other):
		return (self.name == other.name and self.filetype == other.filetype)
	def __ne__(self, other):
		return (self.name != other.name and self.filetype != other.filetype)
	def __gt__(self, other):
		return self.name > other.name
	def __ge__(self, other):
		return self.name >= other.name

	def __getChildren(self):
		return self.__children

	def __getAllowedSee(self):
		return self.__allowed_see

	def __getAllowedEdit(self):
		return self.__allowed_edit

	def __makedir(self, path):
		if not os.path.isdir(path):
			os.makedirs(path)
		else:
			print("Pasta ja existe!\n")

	def getChildrenNames(self):
		return [x.name for x in self.__getChildren()]

	def getOnwer(self):
		return self.onwer

	def getName(self):
		return self.name

	def getFiletype(self):
		return self.filetype

	def getData(self):
		return self.data

	def addChildren(self, onwer, path, filetype, data):
		currentChildrens = [x.getName() for x in self.__getChildren()]
		pos = bisect.bisect(currentChildrens, path[0])
		if len(currentChildrens) == 0 or currentChildrens[pos-1] != path[0]:
			bisect.insort(self.__children, dbNode(onwer, path[0], filetype, data))
			if len(path) > 1:
				del path[0]
				return self.__children[pos].addChildren(onwer, path, filetype, data)
			else:
				return 1
		else:
			return 0

	def deleteChildren(self, user, childrenName):
		return NotImplemented