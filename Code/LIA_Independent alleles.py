#Given: Two positive integers k (k≤7) and N (N≤2**k). First organism has genotype AaBb.
#Each following organism in same family tree always mates with organism having genotype Aa Bb & has 2 children.
#Return: Probability that at least N Aa Bb organisms will belong to k-th generation. Assume Mendel's 2nd law.

import math

def calc_prob(k, N):
    """Returns probability that at least N Aa Bb organisms will belong to k-th generation"""

    P = 2 ** k  # Population of P = k²
    probability = 0

    for i in range(N, P+1):
        #Use binomial distribution
        prob = (math.factorial(P))/ (math.factorial(i) * math.factorial(P-i)) * (0.25**i) * (0.75**(P-i))
        probability += prob

    return probability

k = 5 #k-th generation
N = 8 #Number of Aa Bb organisms that will belong to k-th generation

print(calc_prob(k, N))
