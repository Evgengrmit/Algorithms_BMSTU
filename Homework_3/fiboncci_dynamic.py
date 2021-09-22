from functools import lru_cache


def fib_tab(n):
    sequence = [0 for _ in range(n + 1)]
    sequence[0] = 0
    sequence[1] = 1

    for i in range(2, n + 1):
        sequence[i] = sequence[i - 1] + sequence[i - 2]

    return sequence[n]


memoized = {}


def fib_mem(n):
    if n in memoized:
        return memoized[n]
    if n <= 2:
        memoized[n] = 1
    else:
        memoized[n] = fib_mem(n - 1) + fib_mem(n - 2)
    return memoized[n]


@lru_cache(maxsize=1000)
def fib_dec(n):
    if n <= 2:
        return 1
    else:
        return fib_dec(n-1) +fib_dec(n-2)


print(fib_tab(10))
print(fib_mem(10))
print(fib_dec(10))