#Given: RNA string s corresponding to strand of mRNA
#Return: Protein string encoded by  s

#OPTION 1
from Bio.Seq import Seq

with open('../Files/rosalind_bio_PROT.txt', 'r') as myfile:
    my_rna = Seq(myfile.read())

def translation(rna):
    """Returns protein string encoded by mRNA given"""

    protein = rna.translate()
    return protein

print(translation(my_rna))

#OPTION 2
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

def protein_string(mrna):
    """Returns protein string encoded by mRNA given"""

    output = ''

    for i in range(0, len(mrna), 3):
        symbol = RNA_CODON_TABLE[mrna[i:i+3]]
        if symbol == 'Stop':
            break
        output += symbol

    return output

with open('../Files/rosalind_bio_PROT.txt', 'r') as myfile:
    my_rna = myfile.read()

print(protein_string(my_rna))
