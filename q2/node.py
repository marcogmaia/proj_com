class node():
	def __init__(self, name = "", data = "not a file!", owner = [], allowed = set(), parent = "", filetype = "folder"):
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
		if newName is not "" and self.getOwner() is curOwner:
			self.name = newName
			return True
		return False
	def setData(self, newData, curOwner):
		if newData is not "" and self.getOwner() is curOwner:
			self.data = newData
			return True
		return False
	def setOwner(self, curOwner, newOwner):
		if newOnwer is not None and self.getOwner() is curOwner:
			self.owner = newOwner
			return True
		return False
	def setAllowed(self, newAllowed, curOwner):
		if newAllowed is not None and self.getOwner() is curOwner:
			self.allowed.add(newAllowed)
			return True
		return False
	def setParent(self, newParent, curOwner):
		if newParent is not None and self.getOwner() is curOwner:
			self.parent = newParent
			return True
		return False
	def setChildren(self, newChild, curOwner):
		if newChild is not None and newChild not in self.getChildren() and self.getOwner() is curOwner:
			self.childs.append(newChild)
			return True
		if newChild is not None and newChild in self.getChildren() and self.getOwner() is curOwner:
			self.childs.remove(newChild)
			self.childs.append(newChild)
			return True
		return False
	'''deleters'''
	def resetAllowed(self, delAllowed, curOwner):
		if delAllowed is not None and delAllowed in self.getAllowed() and self.getOwner() is curOwner:
			self.allowed.discard(delAllowed)
			return True
		return False
	def resetChildren(self, delChild, curOwner):
		if delChild is not None and delChild in self.getChildren() and self.getOwner() is curOwner:
			self.childs.remove(delChild)
			return True
		return False
	'''comparisons'''
	def __lt__(self, other):
		if self.getType() is other.getType():
			return self.getName() < other.getName()
		elif self.getType() is "folder":
			return True
		return False
	def __le__(self, other):
		if self.getType() is other.getType():
			return self.getName() <= other.getName()
		elif self.getType() is "folder":
			return True
		return False
	def __eq__(self, other):
		if self.getType() is other.getType():
			return self.getName() == other.getName()
		return False
	def __ne__(self, other):
		if self.getType() is other.getType():
			return self.getName() != other.getName()
		return True
	def __gt__(self, other):
		if self.getType() is other.getType():
			return self.getName() > other.getName()
		elif self.getType() is "folder":
			return False
		return True
	def __ge__(self, other):
		if self.getType() is other.getType():
			return self.getName() >= other.getName()
		elif self.getType() is "folder":
			return False
		return True