import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that the user will see, when
         they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("I'm sorry, but that is not a valid option")


highest = 10
answer = random.randint(1, highest)
# print(answer)   #todo: remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
print("Entering 0 will terminate the program")
guess = get_integer(": ")

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
        guess = get_integer(": ")

    if guess == answer:
        print("Well done you guessed it!")
# else:
#     print("Sorry, you have not guessed correctly")
