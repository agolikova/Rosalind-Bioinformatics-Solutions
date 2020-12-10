#Given: A protein string of length at most 1000 aa
#Return: Total possible number of diff RNA strings from which protein could have been translated, modulo 1,000,000

RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def codon_frequencies():
    """Returns number of codons that encode each amino acid"""

    frequencies = {}

    for codon, aa in RNA_CODON_TABLE.items():
        if aa not in frequencies:
            frequencies[aa] = 0
        frequencies[aa] += 1

    return frequencies

def possible_RNA_strings(protein_seq):
    """Returns number of possible RNA strings from which given protein seq could have been translated"""

    function = codon_frequencies()

    #For every possible sequence that encodes given protein, there are three possible stop codons
    #Total amount of possible seqs is 3* number of codons that each aa in protein could be encoded by

    n = function['Stop']
    # n = 3

    for amino_acid in protein_seq:
        n *= function[amino_acid]

    return n % 1000000

with open('../Files/rosalind_bio_MRNA.txt', 'r') as myfile:
    my_protein_seq = myfile.read().strip()

print(possible_RNA_strings(my_protein_seq))
