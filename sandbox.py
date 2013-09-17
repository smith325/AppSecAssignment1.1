# Sarah Smith
# Sandbox

import sys, os, subprocess, re, pwd, grp, tempfile, token, inspect, keyword, ast
from types import *


class Sandbox():

	def __init__(self,filename):
		self.filename = filename
		self.lexical_entries=["pass","as","with","and","elif","from","return","else","not","try","class","except","if","or","while",
		"continue","import","in","print","def","finally","for","is","in","raise"]
		self.lexical_functions = ["hasattr","isinstance","getattr","tuple","compile","execfile","globals","type","dir","ValueError","open","set","iter","len","list","next","input","False", 
		"True","None", "__import__","__package__","__name__","abs","all","any","bool","bytearray","bytes","dict","enumerate","float","help","str","sorted","range","sum","round","print","pow","object","sum","min","max","int"]

		self.main(self.filename)

	def scanner(self,filename):
		print "begin parsing "+filename
		with open(filename, "r") as f:
			lines = f.read()
			tree = ast.parse(lines)
			return self.traverser(tree)

	def traverser(self,node):
		if node.__class__ == ast.Name:
			if not self.whitelisted(node.id):
				return False
		
		children = ast.iter_child_nodes(node)
		for child in children:
			if not self.traverser(child):
				return False
		
		return True

	def whitelisted(self,word):
		# define whitelisted built-in keywords
	
		# First remove the integers, as they are allowed

		try:
			int(word)
			return True
		except ValueError:
			pass


		# Next try for keywords followed by functions
		if keyword.iskeyword(word):
			if word in self.lexical_entries:
				return True
			else:
				print "illegally attempted keyword call: " + word
				return False
		elif word in dir(__builtins__):
			if word in self.lexical_functions:
				return True
			else:
				print "illegally attempted function call: " + word
				return False
		else:
			return True # non keywords

	def permissions(self):

		#temporary folder called Jail
		# tempdir = tempfile.mkdtemp(suffix='JAIL')
		# os.chroot(tempdir)
		# print tempdir


		current_uid = pwd.getpwnam("nobody").pw_uid
		current_gid = grp.getgrnam("nogroup").gr_gid

		# os.setgroups([])

		os.setgid(current_gid)
		os.setuid(current_uid)

		old_umask = os.umask(077)

	def decrease_permissions(self):
		os.setuid = pwd.getpwnam("nobody").pw_uid
		os.setgid = grp.getgrnam("nogroup").gr_gid

	def main(self,filename):
		if self.scanner(filename):
			# self.permissions()
			builtins_dict = {}

			for key in dir(__builtins__):
				if key not in self.lexical_functions:
					if hasattr(__builtins__,'__dict__'):
						__builtins__.__dict__[key] = None

			# remove executing file from args
			if len(sys.argv) > 1:
				sys.argv.pop(0) 
			
			execfile(filename,builtins_dict,builtins_dict)

		else:
			print "invalid content!" 
			sys.exit(0)



obj = Sandbox(sys.argv[1])


