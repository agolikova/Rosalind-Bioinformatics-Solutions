#Given: DNA string s of length at most 1000 bp
#Return: The reverse complement of s

with open('../Files/rosalind_bio_REVC.txt', 'r') as myfile:
    mydna = myfile.read()
   
#OPTION 1
from Bio.Seq import Seq

def revc(sequence):
    """Return reverse complement of given DNA strand"""

    dna = Seq(sequence)
    cstrand = dna.reverse_complement()

    return cstrand

print(revc(mydna))

#OPTION2
def revc(dna):
    """Return reverse complement of given DNA strand"""

    cstrand = ""

    for base in dna:
        if base == "A":
            cstrand = "T" + cstrand
        elif base == "T":
            cstrand = "A" + cstrand
        elif base == "C":
            cstrand = "G" + cstrand
        elif base == "G":
            cstrand = "C" + cstrand

    return cstrand

print(revc(mydna))
