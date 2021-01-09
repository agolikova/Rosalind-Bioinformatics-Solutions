#Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp)
#Return: The transition/transversion ratio R(s1,s2)
#Transitions = C ↔ T or A ↔ G, transversions = all other substitutions

from Bio import SeqIO

def calcratio(strandA, strandB):
    """Returns transition/transversion ratio of 2 given strands"""

    count_transitions = 0
    count_transversions = 0

    for ind in range(len(strandA)):
        if strandA[ind] != strandB[ind]:
            if strandA[ind] == "A" and strandB[ind] == "G":
                count_transitions += 1
            elif strandA[ind] == "G" and strandB[ind] == "A":
                count_transitions += 1
            elif strandA[ind] == "C" and strandB[ind] == "T":
                count_transitions += 1
            elif strandA[ind] == "T" and strandB[ind] == "C":
                count_transitions += 1
            else:
                count_transversions += 1

    ratio = count_transitions / count_transversions

    return ratio

with open('../Files/rosalind_bio_TRAN.txt', 'r') as myfile:
    strands = list(SeqIO.parse(myfile, "fasta"))
    s1 = strands[0]
    s2 = strands[1]

print(calcratio(s1, s2))
