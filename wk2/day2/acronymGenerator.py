org_string = input("convert to Acronym: ")
org_string = org_string.upper()
list_of_words = org_string.split()

for word in list_of_words:
    print(word[0], end="")

print()