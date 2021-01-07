#Given: DNA string s of length at most 100 bp and array A containing at most 20 numbers between 0 and 1
#Return: Array B having same length as A in which B[k] represents common logarithm of probability that a random string constructed with GC-content found in A[k] will match s exactly

import math

def random_strings(sequence, GC_array):
    """Prints array which represents common log of probabilities that random string constructed with GC contents in given array will match given seq exactly"""

    AT = 0
    GC = 0

    for nt in sequence:
        if nt == "A" or nt == "T":
            AT += 1
        elif nt == "G" or nt == "C":
            GC += 1

    probabilities = []

    #Calculate probability of G = probability of C = %GC/2
    #Calculate probability of A = probability of T = (1-%GC)/2

    #For each consecutive base in provided sequence:
    #1. Convert total probability to logarithm using math.log(probability, base=10)
    #2. Total probability to be multiplied by probability of specifically that base

    for i in range(len(GC_array)):
        prob = (AT * math.log10((1 - GC_array[i])/2)) + (GC * math.log10(GC_array[i]/2))

        probabilities.append('%0.3f' % prob)

    print(*probabilities, sep= " ")

with open('../Files/rosalind_bio_PROB.txt', 'r') as myfile:
    data = myfile.read().splitlines()
    seq = data[0]
    array = data[1].split()
    GC = [float(x) for x in array]

random_strings(seq, GC)
