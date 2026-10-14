# QUESTION 4
# Combine two dicts, adding values for common keys

n = int(input("Enter the size of first dictionary here : "))
m = int(input("Enter the size of second dictionary here : "))

d1 = {}
d2 = {}

for i in range(0,n):
    key1 = int(input(f"Enter key {i+1} here : "))
    value1 = int(input(f"Enter value {i+1} here : "))
    d1[key1] = value1

for i in range(0,m):
    key2 = int(input(f"Enter key {i+1} here : "))
    value2 = int(input(f"Enter value {i+1} here : "))
    d2[key2] = value2

print("Dictionary 1 = ",d1)
print("Dictionary 2 = ",d2)

for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]

print(d1)