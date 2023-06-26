import random

highest = 10
answer = random.randint(1, highest)
# print(answer)   #todo: remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
print("Entering 0 will terminate the program")
guess = int(input())

if guess == answer:
    print("You got it first time!")
else:
    while guess != answer:
        if guess == 0:
            print("Goodbye! Better luck next time.")
            break
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        guess = int(input())

    if guess == answer:
        print("Well done you guessed it!")
# else:
#     print("Sorry, you have not guessed correctly")
