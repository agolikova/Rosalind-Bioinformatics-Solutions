#Given: Array A for which A[k] represents proportion of homozygous recessive individuals for k-th Mendelian factor in a diploid population. Assume that population is in genetic equilibrium for all factors
#Return: Array B having same length as A in which B[k] represents probability that a randomly selected individual carries at least one copy of recessive allele for k-th factor

from math import sqrt

with open('../Files/rosalind_bio_AFRQ.txt', 'r') as myfile:
    A = map(float, myfile.read().strip().split())

B = [2 * sqrt(i) - i for i in A]
print(' '.join(map(str, B)))
