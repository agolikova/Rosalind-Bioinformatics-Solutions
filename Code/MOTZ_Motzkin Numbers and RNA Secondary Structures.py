#Given: RNA string s
#Return: Total number of non-crossing matchings of basepair edges in bonding graph of s, modulo 1,000,000

from Bio import SeqIO

#Set up initial dictionary for matchings
matchings = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
noncross_dict = {}

def calc_motzkin(seq):
    """Returns number of non-crossing matchings of bp edges in bonding graph of given RNA sequence, modulo 1,000,000"""

    #Only one possible way to match if len = 0 or 1
    if len(seq) <= 1:
        return 1

    else:
        #If seq not in dict, calc value, add to dict and return it
        #To save time, use memoization to store Motzkin number once it has been calculated
        if seq not in noncross_dict:
            temp = []

            for nt in range(1, len(seq)):
                if seq[0] == matchings[seq[nt]]:
                    temp.append([seq[1:nt], seq[nt+1:]])

            noncross_dict[seq] = (sum([calc_motzkin(subint[0]) * calc_motzkin(subint[1]) for subint in temp]) + calc_motzkin(seq[1:])) % 1000000

        return noncross_dict[seq]

with open('../Files/rosalind_bio_MOTZ.txt', 'r') as myfile:
    record = SeqIO.read(myfile, "fasta")
    RNA = str(record.seq)

print(calc_motzkin(RNA))
