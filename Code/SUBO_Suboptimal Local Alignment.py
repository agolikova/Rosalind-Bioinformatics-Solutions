#Given: Two DNA strings s and t in FASTA format that share some short inexact repeat r of 32-40 bp
#By "inexact", meant that r may appear with slight modifications (each repeat differing by ≤3 changes/indels)
#Return: Total number of occurrences of r as substring of s, followed by  total number of occurrences of r as substring of t

#Use this tool to identify shared repeat: https://fasta.bioch.virginia.edu/fasta_www2/fasta_www.cgi
#Gap open penalty set to -60
#Gap extend penalty set to -30
#Identify repeat of 32-40 bp with highest % match
#Save repeat seq as "rosalind_subo_repeat.txt"

#Use Hamming distance to count no. of times repeat occurs in s & t, with each occurrence differing by <= 3 changes

from Bio import SeqIO

def hamming(seq1, seq2):
    """Counts symbol substitutions between 2 strings (Hamming distance)"""

    count = 0

    for ind in range(len(seq1)):
        if seq1[ind] != seq2[ind]:
            count += 1

    return count

def subo(dna, repeat):
    "Returns number of occurrences of repeat in dna, with Hamming distance <= 3"

    total = 0

    for i in range(0, len(dna) - len(repeat)):
        dna_range = dna[i:i+len(repeat)]
        hamm = hamming(dna_range, repeat)

        if hamm <= 3:
            total += 1

    return total

with open('../Files/rosalind_subo.txt', 'r') as myfile:
    sequences = list(SeqIO.parse(myfile, "fasta"))
    s = sequences[0].seq
    t = sequences[1].seq

with open('../Files/rosalind_subo_repeat.txt', 'r') as myfile:
    r = myfile.read().strip()

print(subo(s, r), subo(t, r))
