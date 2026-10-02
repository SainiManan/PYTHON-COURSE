import random

num = random.randint(1,100)
print(num)

guess = int(input("Enter your guess: "))

while (guess != num):
    if (guess >= num + 30  or  guess <= num - 30):
        print("Too far away") 
    elif (guess >= num + 20  or  guess <= num - 20):
        print("Getting close")
    elif (guess >= num + 10  or  guess <= num - 10):
        print("That's close mate")
    elif (guess >= num + 5  or  guess <= num - 5):
        print("TOOOOO CLOSEEEE")
    elif (guess >= num + 3  or  guess <= num - 3):
        print("SEriously . how did you miss it!!!!!!")
    elif (guess >= num + 1  or  guess <= num - 1):
        print("How can you be so close and still miss man @!@*")
    guess = int(input("Enter your guess: "))


print("You guessed it right !!!")


## Took a little help from chat gpt (did like 95% by myself)






    
