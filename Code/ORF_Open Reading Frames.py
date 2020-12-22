#Given: DNA string s of length at most 1 kbp in FASTA format
#Return: Every distinct candidate protein string that can be translated from ORFs of s

from Bio.Seq import Seq
from Bio import SeqIO
import re

def find_ORFs(dna):
    """Finds & prints every distinct candidate protein string that can be translated from ORFs of given dna sequence"""

    #1 possible start codon, 3 possible stop codons
    pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
    forward_seq = dna
    reverse_seq = forward_seq.reverse_complement()
    sequences = []

    for orf in re.findall(pattern, str(forward_seq)):
        myorf = Seq(orf)
        protein = myorf.translate()
        if protein not in sequences:
            sequences.append(protein)

    for orf in re.findall(pattern, str(reverse_seq)):
        myorf = Seq(orf)
        protein = myorf.translate()
        if protein not in sequences:
            sequences.append(protein)

    for n, seq in enumerate(sequences):
        print(seq)

with open('../Files/rosalind_bio_ORF.txt', 'r') as myfile:
    for record in SeqIO.parse(myfile, "fasta"):
        sequence = record.seq

find_ORFs(sequence)

#testdna = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
#find_ORFs(testdna)
