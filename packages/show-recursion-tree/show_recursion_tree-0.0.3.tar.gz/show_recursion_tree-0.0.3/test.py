
from src.show_recursion_tree import show_recursion_tree

@show_recursion_tree
def f(n):
    if n <= 2:
        return 1
    
    return f(n-2) + f(n-1)

f(5)