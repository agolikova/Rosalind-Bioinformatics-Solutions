#Given: Collection of at most 10 symbols defining an ordered alphabet, and positive integer n
#Return: All strings of length n that can be formed from alphabet, ordered lexicographically
#NB alphabet order is based on the order in which the symbols are given

import itertools

def permcalculator(alphabet, n):
    """Prints all strings length n that can be formed from alphabet, ordered lexicographically"""

    #Use Cartesian product
    perms = itertools.product(alphabet, repeat=n)

    for counter, perm in enumerate(list(perms)):
        permutation = ''
        for item in perm:
            permutation += str(item)
        print(permutation)

    #Another solution not using enumerate function
    #for p in perms:
        #print(''.join(p))

permcalculator("ABCDEFG", 3)
