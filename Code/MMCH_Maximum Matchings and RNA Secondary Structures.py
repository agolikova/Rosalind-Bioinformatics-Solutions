#Given: RNA string s, NOT having same number of occurrences of 'A' as 'U' or same number of occurrences of 'C' as 'G'
#Return: Total possible number of maximum matchings of basepair edges in bonding graph of s

from math import factorial
from Bio import SeqIO

#Two separate complete graphs, one for AU bonding and one for GC bonding
#Can describe number of perfect matchings for each graph, if n1 = nr of A's and n2 = nr of G's, as n1! and n2!
#Total amount of perfect matchings for two graphs combined = n1! * n2!

def nPr(n, r):
    """Returns total no. of possible combinations of 2 nucleotides using given number of occurrences"""

    #n = nt with more occurrences
    #r = nt with fewer occurrences

    return factorial(n)//factorial(n-r)

def max_matchings(sequence):
    """Returns total possible number of maximum matchings of basepair edges in bonding graph of given sequence"""

    AU = []
    for nt in "AU":
        AU.append(sequence.count(nt))

    GC = []
    for nt in "GC":
        GC.append(sequence.count(nt))

    #1st A can pair with any U - once that pairing has been made, that pair of bases can be removed from pool and 2nd A can pair with any remaining U
    #Iterative process can continue until last remaining U/A has been paired & there is excess of As or Us left over
    #Factorial-style combination problem

    #Multiply no. of AU combos by no. of GC combos to get final solution
    matchings = nPr(max(AU), min(AU)) * nPr(max(GC), min(GC))

    return int(matchings)

with open('../Files/rosalind_bio_MMCH.txt', 'r') as myfile:
    record = SeqIO.read(myfile, "fasta")
    rna = str(record.seq)

print(max_matchings(rna))
