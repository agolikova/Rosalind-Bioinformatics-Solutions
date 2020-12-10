#Given: Positive integer n ≤ 7
#Return: Total number of permutations of length n, followed by list of all permutations

import math
import itertools

def permcalculator(n):
    """Prints total number of permutations of length n, followed by list of all permutations"""

    #Factorial is the product of all positive integers less than or equal to n
    print(math.factorial(n))

    perms = itertools.permutations(list(range(1, n+1)))

    for counter, perm in enumerate(list(perms)):
        permutation = ''
        for item in perm:
            permutation += str(item) + ' '
        print(permutation)

permcalculator(3)
