def multiply(x: float, y: float) -> float:
    """
    Multiply the two given parameters together.

    :param x: First parameter
    :param y: Second parameter
    :return: The result of the multiplication
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Return `True` if inputted string is a palindrome.

    :param string: The string to check.
    :return: `True` if palindrome, `False` if not palindrome
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string: str) -> bool:
    """
    Return `True` if inputted string is a palindromic sentence,
    not including non-alphabetic characters, eg. spaces.

    :param string: Sentence to be checked
    :return: `True` if palindrome, `False` if not palindrome
    """
    alphanumeric_only = "".join(char for char in string if char.isalpha())
    # return alphanumeric_only[::-1].casefold() == alphanumeric_only.casefold()
    return is_palindrome(alphanumeric_only)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence()
