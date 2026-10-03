count = 1
while count <= 5:
    print(count)
    count += 1

# Output: 1  2  3  4  5


"""
PRACTICE QUESTION USING WHILE LOOPS
"""

# Separate each digit of a number and print on a new line


num = int(input("Enter your number : "))

while (num !=  0):
    print(num%10)
    num = num//10


# Accept a number and print its reverse


num = int(input("Enter your number: "))

reverse_num = 0

while (num != 0):
    rem = num%10
    num = num//10
    reverse_num = reverse_num*10 + rem

print(reverse_num)


# Check if a number is palindromic (equal to its reverse)

num = int(input("Enter your number: "))
temp_num = num
reverse_num = 0

while (num !=  0):
    rem = num%10
    num = num//10
    reverse_num = reverse_num*10 + rem


if (reverse_num == temp_num):
    print(f"{temp_num} is a palindromic number")
else:
    print(f"{temp_num} is not a palindromic number")
    

