"""
------RANGE FUNCTION------
range(stop)             # 0 up to stop-1
range(start, stop)      # start up to stop-1
range(start, stop, step)# start, jumping by step
"""
"""print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(1,6)))       # [1, 2, 3, 4, 5]
print(list(range(0,10,2)))"""   # [0, 2, 4, 6, 8]


"""for i in range(0,21,5):
    print(i)


for i in range(5,51,5):
    print(i)"""

# We can also take input from the user

"""n = int(input("ENTER A NUMBER FOR MULTIPLICATON TABLE: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

x = "TIGGLY"
char = int(input("Enter the length:"))
for i in range(0,char):
    print(x[i])"""

# Print "Hello World" n times

"""n = int(input("Enter the number of times you want to print: "))
word = str(input("write the word you wannna type: "))

for i in range(0,n):
    print(word)"""

# Print natural numbers from 1 to n

"""n = int(input("Enter the nth term: "))

for i in range(1,n+1):
    print(i)"""

# Reverse for loop — print n down to 1

"""n = int(input("Enter the first term: "))

for i in range(n,0,-1):
    print(i)"""

# Print the multiplication table of a number

"""n = int(input("Enter your number: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")"""

# Sum of first n natural numbers

"""n = int(input("Enter your natural number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i

print(sum)"""

# Factorial of a number

"""n = int(input("Enter your number: "))
factorial = 1

for i in range(n,0,-1):
    factorial = factorial*i

print(factorial)"""

# Print sum of all even and odd numbers in a range separately

"""n = int(input("Enter the nth term: "))
even_sum = 0
odd_sum = 0

for i in range(1,n+1):
    if i%2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print(even_sum)"""

# Print all factors of a number
"""
n = int(input("Enter the number: "))

for i in range(1,n+1):
    if (n%i == 0):
        print(i)
"""
# Check if a number is perfect (sum of factors = the number itself)

"""n = int(input("Enter your number: "))
factor_sum = 0

for i in range(1,n):
    if (n%i == 0):
        factor_sum = factor_sum + i

if factor_sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")"""

# Check if a number is prime
"""
n = int(input("Enter your number: "))

for i in range(2,n):
    if (n%i == 0):
        print("The number is not a prime number")
        break;
    elif (n%i != 0):
        print("The number is a prime number")
        break;

if (n == 2):
    print("The number is a prime number")"""

# Reverse a string without using built-in functions

"""
char = str(input("Enter your word here: "))
reverse_char = ""

for i in range(0,len(char)):
    reverse_char = reverse_char + char[len(char)-1-i]

print(reverse_char)
"""

# Check if a string is a palindrome
"""
char = str(input("Enter your word here: "))
reverse_char = ""

for i in range(0,len(char)):
    reverse_char = reverse_char + char[len(char)-1-i]

if reverse_char == char:
    print("The word is a pallandrome")
else:
    print("The word is not a pallandrome")
"""

# Count letters, digits, and special symbols in a string


word = str(input("Enter your word here: "))
digits = 0
letter = 0
special_symbols = 0

for i in range(0,len(word)):
    if (word[i]>='0' and word[i]<='9'):
        digits = digits + 1
    elif (word[i]>='a' and word[i]<='z'):
        letter = letter + 1
    elif (word[i]>='A' and word[i]<='Z'):
        letter = letter + 1
    else:
        special_symbols = special_symbols + 1


print(f"There are {digits} digits in the word {word}")
print(f"There are {letter} letters in the word {word}")
print(f"There are {special_symbols} special symbols in the word {word}")

