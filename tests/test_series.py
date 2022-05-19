from script.series import fibonacci, lucas, sum_series


# print('Hello from: ', __name__)


# FIBONACCI TEST
def test_fib_zero():
    assert fibonacci(0) == 0


def test_fib_one():
    assert fibonacci(1) == 1


def test_fib_two():
    assert fibonacci(2) == 1


def test_fib_five():
    assert fibonacci(5) == 5


def test_fib_nine():
    assert fibonacci(9) == 34


# LUCAS TEST
def test_lucas_zero():
    assert lucas(0) == 2


def test_lucas_one():
    assert lucas(1) == 1


def test_lucas_two():
    assert lucas(2) == 3


def test_lucas_seven():
    assert lucas(7) == 29


def test_lucas_thirty_one():
    assert lucas(31) == 3010349


# Sum test
def test_sum_series_fibonacci_zero():
    assert sum_series(0) == 0


def test_sum_series_fibonacci_one():
    assert sum_series(1) == 1


def test_sum_series_fibonacci_nine():
    assert sum_series(9) == 34


def test_sum_series_lucas_zero():
    assert sum_series(0, 2, 1) == 2


def test_sum_series_lucas_one():
    assert sum_series(1, 2, 1) == 1


def test_sum_series_lucas_thirty_one():
    assert sum_series(31, 2, 1) == 3010349
