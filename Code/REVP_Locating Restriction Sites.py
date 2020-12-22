#Given: DNA string of length at most 1 kbp in FASTA format
#Return: Position and length of every reverse palindrome in string having length between 4 and 12

from Bio import SeqIO

def find_restriction_sites(sequence):
    """Finds & prints position & length of every reverse palindrome in given sequence having length between 4 and 12"""

    forward_seq = str(sequence)
    reverse_seq = str(sequence.complement())

    for i in range(len(forward_seq)):
        for j in range(i, len(forward_seq)):
            m = forward_seq[i:j+1]
            rev_m = reverse_seq[i:j+1]

            if 4 <= len(m) <= 12:
                if m == rev_m[::-1]:
                    print(i+1, len(m))

with open('../Files/rosalind_bio_REVP.txt', 'r') as myfile:
    for record in SeqIO.parse(myfile, "fasta"):
        dna = record.seq

find_restriction_sites(dna)
