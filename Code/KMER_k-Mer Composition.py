#Given: DNA string s in FASTA format
#Return: 4-mer composition of s

#k-mer composition of s can be represented by array A for which A[m] denotes number of times mth k-mer (with respect to lexicographic order) appears in s
#Requires O(n) time where n is length of DNA string

#e.g. all possible k-mers of ACGT are AAAA, AAAC, AAAG, AAAT ... TTTT
#Regardless of given seq, possible 4-mers always same for DNA

from Bio import SeqIO
import itertools
import re

def kmer_composition(sequence):
    """Prints array representing 4-mer composition of given DNA sequence"""

    #Generate list of all possible 4-mers in lexicographical order
    nucleotides = "ACGT"
    permutations = itertools.product(nucleotides, repeat=4)

    kmers = []

    for i, j in enumerate(list(permutations)):
        kmer = ""
        for item in j:
            kmer += str(item)
        kmers.append(kmer)

    #Use regex to find all occurrences of k-mers in sequences
    #Use ?= in pattern to include overlapping k-mers
    #Return results in array A

    A = []

    for k in kmers:
        occurrence = 0
        pattern = re.compile(r'(?=(' + k + '))')

        for l in re.findall(pattern, str(sequence)):
            occurrence += 1

        A.append(occurrence)

    print(*A, sep=" ")

with open('../Files/rosalind_bio_KMER.txt', 'r') as myfile:
    record = SeqIO.read(myfile, "fasta")
    DNA = record.seq

kmer_composition(DNA)
