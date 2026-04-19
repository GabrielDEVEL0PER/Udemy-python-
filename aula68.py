import sys

sys.setrecursionlimit(1004)

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))