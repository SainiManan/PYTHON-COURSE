import math

print("******This is a basic calculator created using if else statements and by importing math module in python******")

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))

print("1. Basic arithmetic operations (=,-,*,/)")
print("2. Additional Mathematical Functions (LCM - Least Common Multiple , GCD = Greatest Common Divisor)")
operator = str(input("Enter your operator from the above options: "))

if (operator == '+'):
    print(f"The Sum of {a} and {b} will be",a+b)
elif (operator == '-'):
    print(f"The Difference of {a} and {b} will be",a-b)
elif (operator == '*'):
    print(f"The Product of {a} and {b} will be",a*b)
elif (operator == '/'):
    if (b != 0):
        print(f"The Division of {a} and {b} will be",a/b)
    else:
        print("Denominator should not be equal to zero !!")
elif (operator == 'LCM' or operator == 'lcm'):
    print(f"The Least Common Multiple of {a} and {b} will be",math.lcm(a,b))
elif (operator == 'GCD' or operator == 'gcd'):
    print(f"The Greatest Common Divisor of {a} and {b} will be",math.gcd(a,b))
else:
    print("Please enter a valid operator/function given above (+,-,*,/,lcm,gcd)")


#Done the whole thing by myself
        



