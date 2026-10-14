# QUESTION 1
# Merge two dictionaries into one

n = int(input("Enter size of dictionary 1 here : "))
m = int(input("Enter size of dictionary 2 here : "))

d1 = {}
d2 = {}

print("****FOR FIRST DICTIONARY****")
for i in range(0,n):
    key = int(input(f"Enter key {i+1} here : "))
    value = int(input(f"Enter value {i+1} here : "))
    d1[key] = value

print("****FOR SECOND DICTIONARY****")
for i in range(0,n):
    key1 = int(input(f"Enter key {i+1} here : "))
    value1 = int(input(f"Enter Value {i+1} here : "))
    d2[key1] = value1

print(f"First Dictionary = {d1}")
print(f"Second Dictionary = {d2}")


## The logical way
for i in d2:
    d1[i] = d2[i]

print(d1)

## The easy way
d1.update(d2)
print(d1)