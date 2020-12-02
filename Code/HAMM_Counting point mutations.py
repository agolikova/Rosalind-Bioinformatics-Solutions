#Given: Two DNA strings s and t of equal length
#Return: The Hamming distance dH(s,t)

def calcpoints(seq1, seq2):
    """Counts symbol substitutions between 2 strings (Hamming distance)"""

    count = 0
    
    for ind in range(len(seq1)):
        if seq1[ind] != seq2[ind]:
            count += 1
            
    return count

with open('../Files/rosalind_bio_HAMM.txt', 'r') as myfile:
    strands = myfile.read().splitlines()

s = strands[0]
t = strands[1]

print(calcpoints(s, t))
