# Sarah Smith
# Sandbox

import sys, os, re, pwd, grp, tempfile, token, inspect, keyword
from types import *


class Sandbox():

	def __init__(self,filename):
		self.filename = filename
		self.scanner(filename)

	def scanner(self,filename):
		with open(filename, "r") as f:
			lines = f.read()
			word = re.split(r'\W+', lines)
			wordcounter = len(word)

			for i in range(0,wordcounter):
				self.whitelisted(word[i])

	def whitelisted(self,word):
		
		# define whitelisted built-in keywords
		lexical_entries = ["and","elif","from","return","else","not","try","class","except","if","or","while","continue","import","in","print","def","finally","for","is","raise"]
		
		lexical_functions = ["set","iter","len","list","next","input","False", "True","None", "__import__","__package__","__name__","abs","all","any","ascii","bool","bytearray","bytes","dict","enumerate","float","help","str","sorted","range","sum","round","print","pow","object","sum","min","max","int"]

		# First remove the integers, as they are allowed
		try:
			int(word)
			return True
		except ValueError:
			pass
		
		# if type(word) is IntType:
		# 	return True



		# Next try for keywords followed by functions
		if keyword.iskeyword(word):
			if word in lexical_entries:
				return True
			else:
				print "illegally attempted function call: " + word
				sys.exit(0)

		if word in dir(__builtins__):
			if word in lexical_functions:
				return True
			else:
				print "illegally attempted function call: " + word
				sys.exit(0)


		# return True

	def permissions(self):

		#temporary folder called Jail
		tempdir = tempfile.mkdtemp(suffix='JAIL')

		print tempdir
		

	# def main():
	# 	if scanner(sys.argv[1]):
	# 		permissions()
	# 		execfile(sys.argv[1])


	# # run main
	# if __name__ == "__main__":
	#     main()



obj = Sandbox(sys.argv[1])


