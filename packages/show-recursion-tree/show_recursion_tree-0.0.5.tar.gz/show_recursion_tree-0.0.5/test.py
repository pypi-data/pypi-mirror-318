
from src.show_recursion_tree import show_recursion_tree

@show_recursion_tree
def fib(n: int, d={}) -> int:
    if n == 0 or n == 1:
        return 1
    
    if n-2 not in d:
        d[n-2] = fib(n-2, d=d)
    if n-1 not in d:
        d[n-1] = fib(n-1, d=d)

    return d[n-2] + d[n-2]

fib(5)