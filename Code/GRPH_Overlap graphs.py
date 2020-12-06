#Given: A collection of DNA strings in FASTA format
#Return: Adjacency list, where each row of list contains two node labels corresponding to a unique edge
#NB: k length = 3 (len of suffix of one seq/prefix of another seq that must match)

from Bio import SeqIO

mydata = {}

with open('../Files/rosalind_bio_GRPH.txt', 'r') as myfile:
    for record in SeqIO.parse(myfile, "fasta"):
        mydata[record.id] = str(record.seq)

def is_k_overlap(s1, s2, k):
    """Checks whether a string s1 has a k-suffix matching the k-prefix of a string s2"""

    return s1[-k:] == s2[:k]

import itertools

def k_edges(data, k):
    """Looks at all combinations of DNA sequences to find those that match, returns adjacency list"""

    edges = []

    for u,v in itertools.combinations(data, 2):
        u_dna, v_dna = data[u], data[v]

        if is_k_overlap(u_dna, v_dna, k):
            edges.append((u + " " + v))

        if is_k_overlap(v_dna, u_dna, k):
            edges.append((v + " " + u))

    return edges

#Use * to print list without [] and sep= to separate elements with \n instead of ,
print(*k_edges(mydata, 3), sep="\n")
