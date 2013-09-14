# Sarah Smith
# Sandbox

import sys, os, re, pwd, grp, tempfile


def scanner(filename):
	with open(filename, "r") as f:
		lines = f.read()
		word = re.split(r'\W+', lines)
		wordcounter = len(word)
		for i in range(0,wordcounter):
			if blacklisted(word[i]):
				print "contains blacklisted contents"
				return False
				sys.exit(0)
		return True

def blacklisted(word):
	if word in ["cat","cd","cp","chmod","chroot", "eval", "exec","ftp", "grep","ls","mkdir","more","mv","ncftp","pwd","rm","rmdir","rsh","setenv","sort","tar","telnet"]:
		return True
	else:
		return False

def permissions():

	#temporary folder called Jail
	tempdir = tempfile.mkdtemp(suffix='JAIL')

	print tempdir



def main():
	if scanner(sys.argv[1]):
		permissions()
		execfile(sys.argv[1])




# run main
if __name__ == "__main__":
    main()


