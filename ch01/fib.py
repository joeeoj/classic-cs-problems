from functools import lru_cache
from typing import Dict


def fib_fail(n: int) -> int:
    """doesn't work because it's missing the base case"""
    return fib_fail(n - 1) + fib_fail(n - 2)


def fib_success(n: int) -> int:
    """takes care of 0 and 1 base cases that don't follow the rest of the pattern"""
    if n < 2:
        return n
    return fib_success(n - 2) + fib_success(n - 1)


# includes first two bases cases
memo: Dict[int, int] = {0: 0, 1: 1}

def fib_memo(n: int) -> int:
    """uses memoization to store intermediate results to avoid exponential recomputation"""
    if n not in memo:
        memo[n] = fib_memo(n - 2) + fib_memo(n - 1)
    return memo[n]


@lru_cache(maxsize=None)  # maxsize=None means no limit to cache size
def fib_memo_improved(n: int) -> int:
    if n < 2:
        return n
    return fib_memo_improved(n - 2) + fib_memo_improved(n - 1)



def fib_non_recursive(n: int) -> int:
    if n == 0:
        return 0

    last, nxt = 0, 1
    for _ in range(1, n):
        last, nxt = nxt, last + nxt
    return nxt
