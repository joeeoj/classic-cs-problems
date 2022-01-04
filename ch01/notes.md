> the term "classic computer science problems" is used here to mean "programming problems typically taught in an undergraduate computer science curriculum."

> Chapter 1 introduces...recursion, memoization, and bit manipulation...essential building blocks of other techniques explored in later chapters.

## fibonacci

Fibonacci sequence: a sequence of numbers such that any number, except for the first and second, is the sum of the previous two.

i.e. 0, 1, 1, 2, 3, 5, 8, 13, 21, etc.

To get any value in the sequence:

`fib(n) = fib(n - 1) + fib(n - 2)`


i.e. the 20th fib value = `fib(20 - 1) + fib(20 - 2)`

> **Remember, any problem that can be solved recursively can also be solved iteratively**
