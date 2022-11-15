# LeetCode 70 Climb stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climb(n):
    prev = 0
    curr = 1
    for _ in range(n):
        x = prev + curr
        prev = curr
        curr = x
    return x

