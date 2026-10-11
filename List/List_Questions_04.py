# QUESTION 4
# Find the second greatest element in a list

n = int(input("Enter number of elements in the list here : "))

lst = []

for i in range(0,n):
    a = int(input(f"Enter element {i+1} here : "))
    lst.append(a)

print(lst)

largest = lst[0]

for i in range(0,n):
    if(lst[i]>largest):
        largest = lst[i]

second_largest = lst[0]

for i in range(0,n):
    if(lst[i]>second_largest and lst[i] != largest):
        second_largest = lst[i]


print(f"The largest element in the list is {largest}")
print(f"The second largest element in the list is {second_largest}")