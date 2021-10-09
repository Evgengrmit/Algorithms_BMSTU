from functools import lru_cache
import time
import sys

sys.setrecursionlimit(10 ** 9)


@lru_cache(maxsize=10 ** 9)
def simple_binomial(k, n):
    if k > n:
        return 0
    if k > n // 2:
        k = n - k
    if k == 0 or k == n:
        return 1
    return simple_binomial(k, n - 1) + simple_binomial(k - 1, n - 1)


now = time.time()
print(simple_binomial(5000, 10000))
print(time.time() - now)
