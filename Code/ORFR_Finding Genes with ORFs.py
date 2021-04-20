#Given: DNA string s of length at most 1 kbp
#Return: Longest protein string that can be translated from an ORF of s

from Bio import SeqIO
from Bio.Seq import Seq
from re import finditer

def find_ORF(dna):
    """Returns longest protein string that can be translated from an ORF of given dna sequence"""

    proteins = []

    #Find all ORFs in dna seq, translate and add protein strings to list
    #Match.start (regex) returns index of start of matched substring
    for ORF in finditer('ATG', str(dna)):
        protein = dna[ORF.start():].translate(table = 1, stop_symbol = '', to_stop = True)
        proteins.append(str(protein))

    #Find all ORFs in complementary strand, translate and add protein strings to list
    rev_dna = dna.reverse_complement()
    for ORF in finditer('ATG', str(rev_dna)):
        protein = rev_dna[ORF.start():].translate(table = 1, stop_symbol = '', to_stop = True)
        proteins.append(str(protein))

    #Find & return longest protein string
    longest_protein = max(proteins, key = len)
    return longest_protein

with open('../Files/rosalind_orfr.txt', 'r') as myfile:
    s = Seq(myfile.readline().strip())

    print(find_ORF(s))
