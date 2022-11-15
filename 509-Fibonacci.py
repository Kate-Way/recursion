# 509 Fibonacci number
#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number
# is the sum of the two preceding ones, starting from 0 and 1. That is, F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        first_sum = 0
        second_sum = 1
        for i in range(1,n-1):
            x = first_sum + second_sum
            first_sum = second_sum
            second_sum = x
    return x


