# Sarah Smith
# Sandbox

import sys, os, re, pwd, grp, tempfile, token, inspect, keyword
from types import *


class Sandbox():

	def __init__(self,filename):
		self.filename = filename
		self.main(self.filename)

	def scanner(self,filename):

		validwords = []

		with open(filename, "r") as f:
			lines = f.read()
			word = re.split(r'\W+', lines)
			wordcounter = len(word)

			for i in range(0,wordcounter):
				if self.whitelisted(word[i]):
					validwords.append("true")
				else:
					validwords.append("false")

			if "false" in validwords:
				print "invalid content!"
			else:
				return True
					
					

	def whitelisted(self,word):
		# define whitelisted built-in keywords
		lexical_entries = ["and","elif","from","return","else","not","try","class","except","if","or","while","continue","import","in","print","def","finally","for","is","in","raise"]
		
		# define whitelisted built-in functions
		lexical_functions = ["set","iter","len","list","next","input","False", "True","None", "__import__","__package__","__name__","abs","all","any","ascii","bool","bytearray","bytes","dict","enumerate","float","help","str","sorted","range","sum","round","print","pow","object","sum","min","max","int"]

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
				print "illegally attempted function call: " + word
				return False
				sys.exit(0)

		elif word in dir(__builtins__):
			if word in lexical_functions:
				return True
			else:
				print "illegally attempted function call: " + word
				return False
				sys.exit(0)

		else:
			return True # non keywords

	def permissions(self):

		#temporary folder called Jail
		tempdir = tempfile.mkdtemp(suffix='JAIL')

		print tempdir
		

	def main(self,filename):
		if self.scanner(filename):
			execfile(filename)
		else:
			print "illegal content" 
			sys.exit(0)



obj = Sandbox(sys.argv[1])


