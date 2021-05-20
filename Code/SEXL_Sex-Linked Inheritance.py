#Given: Array A of len n for which A[k] represents proportion of males in population exhibiting k-th of n total recessive X-linked genes. Assume population is in genetic equilibrium for all n genes
#Return: Array B of length n in which B[k] equals probability that a randomly selected female will be a carrier for k-th gene

from math import sqrt

with open('../Files/rosalind_bio_SEXL.txt', 'r') as myfile:
    A = map(float, myfile.read().strip().split())

B = [2 * (i - i ** 2) for i in A]
print(' '.join(map(str, B)))
