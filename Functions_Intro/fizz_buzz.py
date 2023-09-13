
def fizz_buzz(number: int) -> str:
    """
    returns "fizz" if `number` divisible by 3
    returns "buzz" if `number` divisible by 5

    :param number: number to be checked
    :return: fizz, buzz, fizz buzz, or number
    """
    output = ""
    if number % 3 == 0 and number % 5 == 0:
        output = "fizz buzz"
    elif number % 3 == 0 and number % 5 != 0:
        output = "fizz"
    elif number % 5 == 0 and number % 3 != 0:
        output = "buzz"
    else:
        output = str(number)
    return output


print("Let's play Fizz Buzz")
print()
print("We will take turns to count to 100. Input 'fizz' if your number\n"
      "is divisible by 3, 'buzz' if your number is divisible by 5,\n"
      "'fizz buzz' if it is divisible by both 3 and 5, or the number itself.")
print()
print("I'll go first.")

count = 1
while count < 101:
    print(fizz_buzz(count))
    count += 1
    guess = input("")
    # guess = fizz_buzz(count)
    if guess != fizz_buzz(count):
        print("Bad luck! you got that wrong.")
        break
    else:
        count += 1
else:
    print("Well done! We made it to 100.")
