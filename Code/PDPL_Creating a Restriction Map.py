#Given: Multiset L containing positive integers which are differences between a set of numbers
#Return: Set X containing n non-negative integers such that ΔX = L
#Need to recreate a set which will generate the multiset when the diffs between the elements are calculated

from math import sqrt

def restriction_map(multiset):
    """Prints set containing non-negative integers such that ΔX = given multiset"""

    #Calculate how many elements needed in multiset
    n = int(0.5 + 0.5 * sqrt(8.0 * len(multiset) + 1))

    #Start with position of 0
    x = [0]

    #Largest value in multiset must be furthest element from 0
    x.append(max(multiset))
    multiset.remove(x[1])

    #Other values in multiset come from ΔX (delta X)
    deltaset = set(multiset)

    for i in deltaset:

        #See if each diff for candidate value is in list of diffs
        if sum([(abs(i - j) in multiset) for j in x]) == len(x):

            #Remove diffs already found
            for j in x:
                multiset.remove(abs(i - j))

            x.append(i)

            if len(x) == n:
                break

    x.sort()

    print(' '.join(map(str, x)))

with open('../Files/rosalind_bio_PDPL.txt', 'r') as myfile:
    L = list(map(int, myfile.read().strip().split()))

restriction_map(L)
