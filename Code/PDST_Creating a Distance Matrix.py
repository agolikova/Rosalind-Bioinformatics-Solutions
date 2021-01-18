#Given: Collection of n (n≤10) DNA strings of equal length in FASTA
#Return: Matrix D corresponding to p-distance on given strings
#P-distance = proportion of corresponding symbols that differ between 2 seqs

from Bio import SeqIO

def hamming(seq1, seq2):
    """Returns Hamming distance between 2 given dna sequences of same length"""

    mutations = 0

    for index in range(len(seq1)):
        if seq1[index] != seq2[index]:
            mutations += 1

    return mutations

def distance_matrix(sequences):
    """Prints distance matrix corresponding to p-distance on given collection of sequences of same length"""

    seq_len = len(sequences[0])

    for current_seq in sequences:
        distance = []

        for comp_seq in sequences:
            ham = hamming(current_seq, comp_seq)
            distance.append(str.format('{0:.5f}', ham/seq_len))

        print(*distance, sep=" ")

with open('../Files/rosalind_bio_PDST.txt', 'r') as myfile:
    data = []
    for record in SeqIO.parse(myfile, "fasta"):
        data.append(str(record.seq))

distance_matrix(data)
