def factorial(x: int):
    """
    Calculate the factorial of a given number.
    :param: Integer that you want to find the factorial of
    :return: Value of x!
    """
    answer = 1
    if x == 0:
        return answer
    else:
        for y in range(1, x + 1):
            answer = answer * y
        return answer


for i in range(0, 36):
    print(factorial(i))
