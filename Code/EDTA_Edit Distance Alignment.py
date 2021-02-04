#Given: 2 protein strings s and t
#Return: Edit distance dE(s,t) followed by two augmented strings s′ and t′ representing optimal alignment of s and t
#Edit distance = min no. of edit operations needed to transform s into t
#Edit operation = substitution, insertion, or deletion of a single symbol
#Optimal alignment = alignment minimizing total no. of edit operations required to transform one string into the other

from Bio import SeqIO

def match(a, b):
    """Returns 1 if two given arguments are equal, 0 if not"""

    if a == b:
        return 0
    return 1

def edit_distance_alignment(seq1, seq2):
    """Prints edit distance (Levenshtein distance) when given two protein strings,
    followed by 2 augmented strings representing optimal alignment of seq1 & seq2"""

    #Initialize matrix M with len (s) rows and len (t) columns
    M = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]

    for i in range(1, len(seq1) + 1):
        M[i][0] = i

    for i in range(1, len(seq2) + 1):
        M[0][i] = i

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if seq1[i - 1] == seq2[j - 1]:
                M[i][j] = M[i - 1][j - 1]
            else:
                M[i][j] = min(M[i - 1][j] + 1, M[i][j - 1] + 1, M[i - 1][j - 1] + 1)

    print(M[len(seq1)][len(seq2)])

    seq1_prim = ""
    seq2_prim = ""

    i = len(seq1)
    j = len(seq2)

    while i * j != 0:
        if M[i][j] == M[i - 1][j - 1] + match(seq1[i -1], seq2[j - 1]):
            seq1_prim = seq1[i - 1] + seq1_prim
            seq2_prim = seq2[j - 1] + seq2_prim
            i -= 1
            j -= 1

        #Use gap symbols '-' to encode insertion or deletion of symbol to which '-' is aligned
        elif i > 0 and M[i][j] == M[i - 1][j] + 1:
            seq1_prim = seq1[i - 1] + seq1_prim
            seq2_prim = "-" + seq2_prim
            i -= 1

        else:
            seq2_prim = seq2[j - 1] + seq2_prim
            seq1_prim = "-" + seq1_prim
            j -= 1

    print(seq1_prim)
    print(seq2_prim)

with open('../Files/rosalind_bio_EDTA.txt', 'r') as myfile:
    sequences = []
    for record in SeqIO.parse(myfile, "fasta"):
        sequences.append(str(record.seq))

s = sequences[0]
t = sequences[1]

edit_distance_alignment(s, t)
