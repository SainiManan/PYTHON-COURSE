# QUESTION 5
# Check if the list is still sorted

n = int(input("Enter the number of elements in the list here : "))

lst = []

for i in range(0,n):
    a = int(input(f"Enter element {i+1} here : "))
    lst.append(a)

print(lst)

sorted = 0

for i in range(0,n-1):
    if (lst[i]>lst[i+1]):
        print("Your list is not sorted")
        break
    else:
        print("Your list is sorted")
        break



