#Given: Two DNA strings s and t in FASTA format
#Return: A longest common subsequence of s and t (longest non-contiguous collection of nucleotides shared by both seqs)

from Bio import SeqIO

def longest_common_subsequence(seq1, seq2):
    """Prints longest common subsequence of 2 given seqs"""

    cur = [''] * (len(seq2) + 1)

    for x in seq1:
        last, cur = cur, ['']

        for i, y in enumerate(seq2):
            cur.append(last[i] + x if x == y else max(last[i+1], cur[-1], key=len))

    print(cur[-1])

with open('../Files/rosalind_bio_LCSQ2.txt', 'r') as myfile:
    sequences = []

    for record in SeqIO.parse(myfile, "fasta"):
        sequences.append(str(record.seq))

    s = sequences[0]
    t = sequences[1]

longest_common_subsequence(s, t)
