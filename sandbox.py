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
	# make sure to copy input files countdown.py and fibonacci.py to the /tmp/sandbox/ path
	#define the location of 'mytemp' parent folder relative to the system temp
	
	# sysTemp = tempfile.gettempdir()
	# myTemp = os.path.join(sysTemp,'jail')

	#You must make sure myTemp exists
	# if not os.path.exists(myTemp):
	#     os.makedirs(myTemp)

	#now make your temporary sub folder
	tempdir = tempfile.mkdtemp(suffix='JAIL')

	print tempdir

	# print "checking permissions"
	# path = "/tmp/sandbox/"
	# os.chdir(path)

	# uid = pwd.getpwnam("nobody").pw_uid
	# gid = grp.getgrnam("nogroup").gr_gids
	# os.chown(path, uid, gid)



def main():
	if scanner(sys.argv[1]):
		permissions()
		execfile(sys.argv[1])




# run main
if __name__ == "__main__":
    main()


