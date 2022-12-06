import os
with open("mydata.txt", encoding="utf-8") as myFile:
    lineNum = 1
    while True:
        line = myFile.readline()

        if not line:
            break
        wordList = line.split()

        print("Number of words : ", len(wordList))

        charCount = 0
        for word in wordList:
            for char in word:
                charCount += 1
        
        avgNumChars = charCount/len(wordList)
        print("Average word length: {:.2}".format(avgNumChars))
        print("line", lineNum," : ", line, end="")
        lineNum +=1