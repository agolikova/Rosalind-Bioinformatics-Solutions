#Given: DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting respective number of times that symbols 'A', 'C', 'G', and 'T' occur in s.

from Bio.Seq import Seq

def count_nt(dna):
    """Return number of times that each nt appears in given DNA seq"""

    A = dna.count("A")
    C = dna.count("C")
    G = dna.count("G")
    T = dna.count("T")

    print(A, C, G, T)

with open('../Files/rosalind_ini.txt', 'r') as myfile:
    my_seq = Seq(myfile.readline().strip())

count_nt(my_seq)
