class node():
	def __init__(self, name = "", data = "not a file!", owner = None, allowed = dict(), parent = None, filetype = "folder"):
		self.name = name
		self.data = data
		self.owner = owner
		self.allowed = allowed
		self.parent = parent
		self.filetype = filetype
		self.childs = []
	'''getters'''
	def getName(self):
		return self.name
	def getData(self):
		return self.data
	def getOwner(self):
		return self.owner
	def getAllowed(self):
		return self.allowed
	def getParent(self):
		return self.parent
	def getType(self):
		return self.filetype
	def getChildren(self):
		return self.childs
	'''setters'''
	def setName(self, newName, curOwner):
		if newName != "" and self.getOwner() == curOwner:
			self.name = newName
			return True
		return False
	def setData(self, newData, curOwner):
		if newData != "" and self.getOwner() == curOwner:
			self.data = newData
			return True
		return False
	def setAllowed(self, newAllowed, curOwner):
		if newAllowed != None and newAllowed[0] not in self.getAllowed() and self.getOwner() == curOwner:
			self.allowed[newAllowed[0]] = newAllowed[1]
			return True
		return False
	def setParent(self, newParent, curOwner):
		if newParent is not None and self.getOwner() == curOwner:
			self.parent = newParent
			return True
		return False
	def setChildren(self, newChild, curOwner):
		if newChild != None and newChild not in self.getChildren() and self.getOwner() == curOwner:
			self.childs.append(newChild)
			return True
		if newChild != None and newChild in self.getChildren() and self.getOwner() == curOwner:
			self.childs.remove(newChild)
			self.childs.append(newChild)
			return True
		return False
	'''deleters'''
	def resetAllowed(self, delAllowed, curOwner):
		if delAllowed != None and delAllowed[0] in self.getAllowed() and self.getOwner() == curOwner:
			del self.allowed[delAllowed[0]]
			return True
		return False
	def resetChildren(self, delChild, curOwner):
		if delChild != None and delChild in self.getChildren() and self.getOwner() == curOwner:
			self.childs.remove(delChild)
			return True
		return False
	'''comparisons'''
	def __lt__(self, other):
		if self.getType() == other.getType():
			return self.getName() < other.getName()
		elif self.getType() == "folder":
			return True
		return False
	def __le__(self, other):
		if self.getType() == other.getType():
			return self.getName() <= other.getName()
		elif self.getType() == "folder":
			return True
		return False
	def __eq__(self, other):
		if self.getType() == other.getType():
			return self.getName() == other.getName()
		return False
	def __ne__(self, other):
		if self.getType() == other.getType():
			return self.getName() != other.getName()
		return True
	def __gt__(self, other):
		if self.getType() == other.getType():
			return self.getName() > other.getName()
		elif self.getType() == "folder":
			return False
		return True
	def __ge__(self, other):
		if self.getType() == other.getType():
			return self.getName() >= other.getName()
		elif self.getType() == "folder":
			return False
		return True