# QUESTION 2
# Find the mean (average) of all list elements

n = int(input("Enter the number of elements in a list here : "))

lst = []

for i in range(0,n):
    a = int(input(f"Enter element {i+1} here : "))
    lst.append(a)

print(f"The entered list is {lst}")

val = 0;

for i in range(0,n):
    val = val + lst[i];

mean = val/n;

print("The mean of given list is ",mean)