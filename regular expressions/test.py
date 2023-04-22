#used to:
#   search for a specific string in a large amount of data
#   verify that a string has a proper format (Email, phone)
#   find a string and replace it with another string
#   format data into the proper form for importing for example

import re

if re.search("ape.", "The ape was at the apex"):
    print("There is an ape")
theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):
    locTuple = i.span()
    print(locTuple)
    print(theStr[locTuple[0]: locTuple[1]])