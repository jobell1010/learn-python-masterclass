def sum_numbers(*x: float) -> float:
    """
    Calculate the sum of all numbers passed as arguments.
    :param: numbers to be added
    :return: answer after adding
    """
    print(x)
    answer = 0
    for i in x:
        answer += i
    return answer


print(sum_numbers(12.5, 3.147, 98.1))