#Given: Positive integer n≤50
#Return: Array A of len 2n in which A[k] represents common logarithm of probability that 2 diploid siblings share at least k of their 2n chromosomes

import math

def binomial(n, k, p):
    return (math.factorial(n) / math.factorial(k) / math.factorial(n-k)) * (p**k * (1-p)**(n-k))

def calcprob(n):
    """Returns array A in which A[k] represents common log of probability that 2 diploid siblings share at least k of their 2n chromosomes"""

    A = []

    for k in range(2 * n, -1, -1):
        A.append(binomial(n * 2, k, 0.5))

    A = [math.log10(sum(A[:i])) for i in range(2 * n, 0, -1)]

    print(' '.join([str(i) for i in A]))

with open('../Files/rosalind_bio_INDC.txt', 'r') as myfile:
    integer = int(myfile.readline().strip())

calcprob(integer)
