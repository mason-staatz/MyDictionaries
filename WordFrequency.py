import re

infile = open("AI.txt", "r")


dict = {}


for word in infile:
    ret = re.sub("[^A-Za-z0-9 ]+", "", word)
    word1 = ret.split()
    for t in word1:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1

print(dict)
