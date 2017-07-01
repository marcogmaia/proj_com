import account
import node
import os

class database():
	def __init__(self, name, admin):
		self.accounts = []
		self.root = node(name, owner = admin)
		os.makedirs(root)