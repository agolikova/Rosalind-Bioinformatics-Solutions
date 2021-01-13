#Given: RNA string s having same number of occurrences of 'A' as 'U' & same number of occurrences of 'C' as 'G'
#Return: Total number of non-crossing perfect matchings of basepair edges in bonding graph of s, modulo 1,000,000

from Bio import SeqIO

#Set up initial dictionary for number of matches for the sequence
cache = {'': 1, 'A': 0, 'C': 0, 'G': 0, 'U': 0, 'AA': 0, 'AC': 0, 'AG': 0, 'AU': 1, 'CA': 0, 'CC': 0,
         'CG': 1, 'CU': 0, 'GA': 0, 'GC': 1, 'GG': 0, 'GU': 0, 'UA': 1, 'UC': 0, 'UG': 0, 'UU': 0}

def countRNAstructures(sequence):
    """Returns total number of non-crossing perfect matchings of basepair edges in bonding graph of given seq, modulo 1,000,000"""

    if sequence not in cache:
        temp = []

        #Use recursion, iterate in jumps of 2 to speed up program
        for nt in range(1, len(sequence), 2):

            #Multiply first half of string * first nt and last nt of first half * second half
            #This combines no. of non-crossing perfect matches from subproblems
            temp.append(countRNAstructures(sequence[1:nt]) * cache[sequence[0] + sequence[nt]] * countRNAstructures(sequence[nt+1:]))

        #Use memoization to speed up program by storing result of function call & returning cached result when same input occurs
        cache[sequence] = sum(temp)

    #Output comes from dynamically generated dictionary
    return cache[sequence]

with open('../Files/rosalind_bio_CAT.txt', 'r') as myfile:
    record = SeqIO.read(myfile, "fasta")
    RNA = str(record.seq)

print(countRNAstructures(RNA) % 1000000)
