# A-Z 65-90
# a-z 97-122

norm_string = input("enter a string for conversion in: ")
secret_string = ""
for char in norm_string:
    secret_string += str(ord(char) - 23)
print("secret message: ", secret_string)

norm_string = ""
for i in range (0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i + 1]
    norm_string += chr(int(char_code) + 23)
print("original message: ", norm_string)