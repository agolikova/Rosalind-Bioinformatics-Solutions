#Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4)
#Return: All strings of length at most n formed from A, ordered lexicographically
#NB alphabet order is based on order in which symbols are given

import itertools

def permcalculator(alphabet, n):
    """Prints all strings length at most n that can be formed from given alphabet, ordered lexicographically"""

    perms = []

    #Put creation of permutations into for loop in order to get all different lengths
    for i in range(1, n+1):
        perms.append(list(map(''.join, (itertools.product(alphabet, repeat=i)))))

    #Chain function used for treating consecutive sequences as a single sequence
    #E.g for "DNA" returns ['D', 'N', 'A', 'DD', 'DN', 'DA', 'ND', 'NN'... etc]
    permutations = list(itertools.chain(*perms))

    #lambda argument: expression
    #key returns index of letter in custom alphabet
    sorted_perms = sorted(permutations, key = lambda word: [alphabet.index(c) for c in word])

    print(*sorted_perms, sep= "\n")

permcalculator("ZNYVDTHSLXWU", 3)
