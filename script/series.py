print('Hello from: ', __name__)


def fibonacci(n):
    """
    This fibonacci function starts with 0 and 1 and continues to add
    numbers in a list until reached limit.
    Recursion is implemented in the return statement.
    """
    if n in {0, 1}:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    This is a lucas function that instead of the fibonacci function it starts with 2
    and an 0 return 2 almost the same code beside 1 char changed.
    """
    if n in {0, 1}:
        if n == 0:
            return 2
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, zero=0, one=1):
    while one == 1 and zero == 0:
        return fibonacci(n)
    if one == 1 and zero == 2:
        return lucas(n)
