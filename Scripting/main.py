import os
#getting the name of the user
name = os.getlogin()
print(name)
#processes
gid = os.getppid()
print(gid)
#current working dir
cdir = os.getcwd()
print(cdir)
