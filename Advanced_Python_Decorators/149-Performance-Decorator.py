# Performance Decorator
# Used to test how fast your code runs

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()  # returns current time in seconds
        result = fn(*args, **kwargs)
        t2 = time()  # returns current time in seconds
        print(f'Duration: {t2 - t1} s')
        return result
    return wrapper


@performance
def multiply_by2(num):
    return num * 2


print(multiply_by2(1))
# Output:
# Duration: 1.430511474609375e-06 s
# 2
