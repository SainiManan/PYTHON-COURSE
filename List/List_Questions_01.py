# This program consists question from list in python

# QUESTION 1
# Print all positive and negative elements separately

n = int(input("Enter the number of elements in a list here : "))

lst = []

for i in range(0,n):
    a = int(input(f"Enter your element {i+1} here : "))
    lst.append(a);

print(lst)

postive_list = []
negative_list = []

for i in range(0,n):
    if(lst[i] > 0):
        postive_list.append(lst[i])
    elif(lst[i] < 0):
        negative_list.append(lst[i])


print("Positive elements list : ",postive_list)
print("Negative elements list : ",negative_list)