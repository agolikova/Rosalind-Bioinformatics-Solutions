#Given: RNA string s
#Return: Total number of noncrossing matchings of basepair edges in bonding graph of s, modulo 1,000,000

#Set up initial dictionary for matchings
matchings = {'A':'U', 'U':'AG', 'C':'G', 'G':'CU'}

wobble_dict = {}

def wobble_bonding(seq):
    """Returns number of noncrossing bonding graphs for a given RNA sequence
    Includes wobble base pairing between G and U
    To pair, bases must be separated by at least 4 other bases"""

    #Only one possible way to match if len = 0 or 1
    if len(seq) <= 1:
        return 1

    else:
        #If seq not in dict, calc value, add to dict and return it
        #To save time, use memoization to store result once it has been calculated
        if seq not in wobble_dict:
            temp = []

            for nt in range(4, len(seq)):
                if seq[0] in matchings[seq[nt]]:
                    temp.append([seq[1:nt], seq[nt+1:]])

            wobble_dict[seq] = (sum([wobble_bonding(subint[0]) * wobble_bonding(subint[1]) for subint in temp]) + wobble_bonding(seq[1:]))

        return wobble_dict[seq]

with open('../Files/rosalind_bio_RNAS.txt', 'r') as myfile:
    RNA = myfile.read().rstrip()

print(wobble_bonding(RNA))
