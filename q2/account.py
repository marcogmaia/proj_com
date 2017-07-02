class account():
	def __init__(self, user, password):
		self.user = user
		self.password = password
	'''getters'''
	def getUser(self):
		return self.user
	def getPass(self):
		return self.password
	'''setters'''
	def setUser(self, curAccount, newUser):
		if newUser != "" and self.getUser() == curAccount.getUser() and self.getPass() == curAccount.getPass():
			self.user = newUser
			return True
		return False
	def setPass(self, curUser, newPass):
		if newPass != "" and self.getUser() == curAccount.getUser() and self.getPass() == curAccount.getPass():
			self.password = newPass
			return True
		return False
	'''comparisons'''
	def __lt__(self, other):
		return self.getUser() < other.getUser()
	def __le__(self, other):
		return self.getUser() <= other.getUser()
	def __eq__(self, other):
		return self.getUser() == other.getUser()
	def __ne__(self, other):
		return self.getUser() != other.getUser()
	def __gt__(self, other):
		return self.getUser() > other.getUser()
	def __ge__(self, other):
		return self.getUser() >= other.getUser()