try:
    myFile = open("mydata.txt", encoding="utf-8")
except FileNotFoundError as ex:
    print("The file was not found")
    print(ex.args)

else:
    print("File: ", myFile.read())
    myFile.close()

finally:
    print("Finished!! ")