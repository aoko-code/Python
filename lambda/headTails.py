import random
hTList = []

for i in range(1, 101):
    hTList += random.choice(['H', 'T'])

print("Heads: ", hTList.count('H'))
print("Tails: ", hTList.count('T'))