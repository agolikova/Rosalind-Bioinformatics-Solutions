#Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format
#Return: One collection of indices of s in which the symbols of t appear as a subsequence of s (do not need to appear contiguously)

from Bio import SeqIO

def find_spliced_motif(dna, motif):
    """Prints indices of given dna seq at which nucleotides of given motif appear as a subsequence"""

    result = []
    index = 0

    #Starting with first base of motif, find first position where it occurs in test sequence [n]
    #For next base of motif, start search in test sequence at base just after last found [n + 1]

    for i in range(len(motif)):

        for j in range(index, len(dna)):
            index += 1

            if len(result) <= len(motif):

                if motif[i] == dna[j]:
                    result.append(index)
                    break

    print(*result, sep = " ")

with open('../Files/rosalind_bio_SSEQ.txt', 'r') as myfile:
    sequences = list(SeqIO.parse(myfile, "fasta"))
    s = sequences[0]
    t = sequences[1]

find_spliced_motif(s, t)

#TEST dna_seq = "ACGTACGTGACG"
#TEST motif = "GAT"
