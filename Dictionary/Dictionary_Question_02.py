# QUESTION 2
# Sum all values in a dictionary

d1 = {}

n = int(input("Enter the number of elements in a dictionary here : "))

for i in range(0,n):
    key = int(input(f"Enter key {i+1} here : "))
    value = int(input(f"Enter value {i+1} here : "))
    d1[key] = value

print("Entered dictionary is ",d1)

sum = 0

for i in d1:
    sum = sum + d1[i]

print(f"The sum of elements of the dictionary will be {sum}")