#Given: A protein string P of length at most 1000 aa
#Return: Total weight of P

#OPTION 1
from Bio import Seq
from Bio.SeqUtils import molecular_weight

def calc_mass(protein_string):
    """Returns total weight of given protein string using monoisotopic mass table"""

    #Remove mass of single water molecule as considering peptides excised from middle of protein
    total_mass = molecular_weight(protein_string, "protein", monoisotopic=True) - 18.01056

    return total_mass

with open('../Files/rosalind_bio_PRTM.txt', 'r') as myfile:
    myfile = myfile.read().strip()

print(calc_mass(myfile))

#testdataset = "SKADYEK"

#OPTION 2
MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}

def calc_mass(protein_string):
    """Returns total weight of given protein string using monoisotopic mass table"""

    total_mass = 0

    for amino_acid in protein_string:
        ind_mass = MONOISOTOPIC_MASS_TABLE[amino_acid]
        total_mass += ind_mass
    #Considering peptides excised from middle of protein - no H2O mass added

    return total_mass

with open('../Files/rosalind_bio_PRTM.txt', 'r') as myfile:
    myfile = myfile.read().strip()

print(calc_mass(myfile))

#testdataset = "SKADYEK"
