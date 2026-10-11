# Question 3
# Find the greatest element and print its index

n = int(input("Enter the number of elements in the list here : "))

lst = []

for i in range(0,n):
    a = int(input(f"Enter element {i} here : "))
    lst.append(a);

print(lst)

largest = float("-inf")

for i in range(0,n):
    if(lst[i]>largest):
        largest = lst[i]

print(f"The largest number in the given list is {largest}")