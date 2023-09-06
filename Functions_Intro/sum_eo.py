def sum_eo(n, t):
    value = 0
    if t == 'e':
        for i in range(0, n, 2):
            value += i
        return value
    elif t == 'o':
        for i in range(1, n, 2):
            value += i
        return value
    value = -1
    return value


print(sum_eo(7, 'spam'))
