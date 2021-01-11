#Given: A positive integer n (n≤1000)
#Return: Value of B(n) modulo 1,000,000. B(n) denotes total number of distinct rooted binary trees on n labeled taxa

def double_factorial(n):
    """Returns double factorial !! of n"""

    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)

def count_unrooted_binary_trees(n):
    """Returns total number of distinct unrooted binary trees having n labeled leaves, modulo 1,000,000"""

    output = double_factorial(2 * n - 5) % 1000000
    return output

def count_rooted_binary_trees(n):
    """Returns total number of distinct rooted binary trees on n labeled taxa"""

    #Transform unrooted binary tree into rooted binary tree by inserting a node into any of its 2 * n - 3 edges
    output = (count_unrooted_binary_trees(n) * (2 * n - 3)) % 1000000

    return output

n = 949
print(count_rooted_binary_trees(n))
