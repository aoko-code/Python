import os
with open("mdata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("hello there\nthis is a file\n And am writing in it")

with open("mdata.txt", encoding="utf-8") as myFile:

    print(myFile.read())

print(myFile.closed)
print(myFile.name)
print(myFile.mode)

os.rename('mdata.txt', 'maydata.txt')
os.remove("maydata.txt")
os.mkdir('mydir')
os.chdir('mydir')
print('current directory: ', os.getcwd())
