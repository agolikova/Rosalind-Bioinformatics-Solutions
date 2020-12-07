#Given: A collection of up to 1000 (possibly repeating) DNA strings of equal length, corresponding to a set S of (k+1)-mers
#Return: Adjacency list corresponding to the de Bruijn graph corresponding to S∪S^rc

from Bio.Seq import Seq

def get_reverse_complement(dna):
    """Returns reverse complement of dna sequence"""

    seq = Seq(dna)
    rev_seq = seq.reverse_complement()
    return str(rev_seq)

def get_adjacency_list(sequences):
    """Prints adjacency list corresponding to de Bruijn graph representing overlapping strings in given sequences"""

    S = set()

    for i in sequences:
        if i not in S:
            S.add(i)

        C = get_reverse_complement(i)
        if C not in S:
            S.add(C)

    #Print adjacency list in format specified
    for j in S:
        print("(" + j[:-1] + ", " + j[1:] + ")")

with open('../Files/rosalind_bio_DBRU.txt', 'r') as myfile:
    data = []
    for line in myfile:
        data.append(line.strip())

get_adjacency_list(data)
