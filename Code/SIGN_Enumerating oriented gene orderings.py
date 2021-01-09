#Given: A positive integer n≤6
#Return: Total number of signed permutations of length n, followed by a list of all such permutations (in any order)
#NB signed permutations can have + or - signs (omit + when printing)

import itertools

def permcalculator(n):
    """Returns total no. of signed permutations of given length n, followed by list of all permutations"""

    permutation = []
    count = 0

    #Create list of all possible permutations of +ve integers up to n (1, 2, 3)
    for i in itertools.permutations(list(range(1, n + 1))):

        #Create list of all possible +ve & -ve outcomes at each of the 3 positions
        for j in itertools.product([-1, 1], repeat=len(list(range(1, n + 1)))):

            #Multiply list 1 by all possible variants of list 2
            #zip function generates tuples containing parallel elements from each iterable
            perm = [a * sign for a, sign in zip(i, j)]

            permutation.append(perm)
            count += 1

    print(count)

    for i in range(len(permutation)):
        print(*permutation[i]) #Use * to print lists without []

permcalculator(3)
