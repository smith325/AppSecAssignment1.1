# Sarah Smith
# Sandbox

import sys, os, re, pwd, grp, tempfile, token, inspect, keyword, ast
from types import *


class Sandbox():

	def __init__(self,filename):
		self.filename = filename
		self.main(self.filename)

	def scanner(self,filename):
		with open(filename, "r") as f:
			lines = f.read()
			tree = ast.parse(lines)
			return self.traverser(tree)

	def traverser(self,node):
		print "node: "+node.__class__.__name__

		if node.__class__ == ast.Name:
			if not self.whitelisted(node.id):
				return False

		for entry in ast.iter_fields(node):
			print entry
		
		children = ast.iter_child_nodes(node)
		for child in children:
			if not self.traverser(child):
				return False
		
		return True

	def whitelisted(self,word):
		# define whitelisted built-in keywords
		lexical_entries = ["pass","as","with","and","elif","from","return","else","not","try","class","except","if","or","while","continue","import","in","print","def","finally","for","is","in","raise"]
		
		# define whitelisted built-in functions
		lexical_functions = ["ValueError","open","set","iter","len","list","next","input","False", "True","None", "__import__","__package__","__name__","abs","all","any","ascii","bool","bytearray","bytes","dict","enumerate","float","help","str","sorted","range","sum","round","print","pow","object","sum","min","max","int"]

		# First remove the integers, as they are allowed

		try:
			int(word)
			return True
		except ValueError:
			pass


		# Next try for keywords followed by functions
		if keyword.iskeyword(word):
			if word in lexical_entries:
				return True
			else:
				print "illegally attempted keyword call: " + word
				return False
		elif word in dir(__builtins__):
			if word in lexical_functions:
				return True
			else:
				print "illegally attempted function call: " + word
				return False
		else:
			return True # non keywords

	def permissions(self):

		#temporary folder called Jail
		tempdir = tempfile.mkdtemp(suffix='JAIL')
		print tempdir

		

	def main(self,filename):
		if self.scanner(filename):
			self.permissions()
			execfile(filename)
		else:
			print "invalid content!" 
			sys.exit(0)



obj = Sandbox(sys.argv[1])


