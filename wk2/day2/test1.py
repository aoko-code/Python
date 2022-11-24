random_string = "    this is the message "
random_string= random_string.strip()
print(random_string)
print(random_string.capitalize())
print(random_string.upper())
print(random_string.lower())
a_list = ["random", "words", "here", "everyone", "look"]
print(" ".join(a_list))
a_list1 = random_string.split()
for i in a_list1:
    print(i)
print("how many is: ", random_string.count("is"))
print("where is string:", random_string.find("string"))