#Given: Collection of n (n≤10) DNA strings
#Return: Number of given strings that match their reverse complements

from Bio import SeqIO

def match_reverse_comp(dna):
    """Returns number of given dna strings that match their reverse complements"""

    count = 0

    for record in dna:
        if record.seq == record.seq.reverse_complement():
            count += 1

    return count

with open('../Files/rosalind_rvco.txt', 'r') as myfile:
    dna_collection = SeqIO.parse(myfile, "fasta")
    print(match_reverse_comp(dna_collection))
