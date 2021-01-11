#Given: A positive integer n (n≤1000)
#Return: Value of b(n) modulo 1,000,000. b(n) denotes total number of distinct unrooted binary trees having n labeled leaves
#NB number of distinct unrooted binary trees = 2n - 5!! (double factorial)

def count_unrooted_binary_trees(n):
    """Returns total number of distinct unrooted binary trees having n labeled leaves, modulo 1,000,000"""

    if n == 0 or n == 1:
        return 1
    else:
        return n * count_unrooted_binary_trees(n - 2)

n = 915

output = count_unrooted_binary_trees(2 * n - 5) % 1000000

print(output)
