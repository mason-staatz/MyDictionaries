infile = open("AI.txt", "r")


dict = {}

count = 0
for word in infile:
    for t in word.split():
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1

print(dict)
