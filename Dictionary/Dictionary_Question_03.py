# QUESTION 3
# Count the frequency of each element in a list using a dictionary


lst = ["a","b","b","c","d","a"]

d = {}

for i in lst:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)