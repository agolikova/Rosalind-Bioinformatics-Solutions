#Given: RNA string s having same number of occurrences of 'A' as 'U' and same number of occurrences of 'C' as 'G'
#Return: Total possible number of perfect matchings of basepair edges in bonding graph of s

from math import factorial
from Bio import SeqIO

def perfect_matchings(sequence):
    """Returns total possible number of perfect matchings of bp edges in bonding graph of given RNA sequence"""

    #Two separate complete bipartite graphs, one for AU bonding and one for GC bonding
    #Can describe number of perfect matchings for each graph, if n1 = nr of A's and n2 = nr of G's, as n1! and n2!
    AU = 0
    GC = 0

    for nt in sequence:
        if nt == "A":
            AU += 1
        elif nt == "G":
            GC += 1

    #Total amount of perfect matchings for two graphs combined = n1! * n2!
    matchings = factorial(AU) * factorial(GC)

    return matchings

with open('../Files/rosalind_bio_PMCH.txt', 'r') as myfile:
    for record in SeqIO.parse(myfile, "fasta"):
        rna = str(record.seq)

print(perfect_matchings(rna))
