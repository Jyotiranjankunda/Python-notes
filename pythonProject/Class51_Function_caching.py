# Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

# In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def func_sleep(n):
    time.sleep(3)
    return f"Executed for {n}"

# These 3 functions calls will take 3 sec each to execute
print(func_sleep(5))
print(func_sleep(10))
print(func_sleep(15))

# But these 3 again with same values won't execute again. As 5, 10, 15 are already in the cache, the function does not execute again. It returns the cached result immediately without sleeping or printing.
print(func_sleep(5))
print(func_sleep(10))
print(func_sleep(15))

# 20 is a new value for fun_sleep, so it will again take 3 secs.
print(func_sleep(20))