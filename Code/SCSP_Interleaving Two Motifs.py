#Given: Two DNA strings s and t
#Return: A shortest common supersequence of s and t (longest non-contiguous collection of nt's shared by both seqs)

def lcs(s, t):
    """Returns longest common subsequence of 2 given sequences"""

    lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    for i, x in enumerate(s):
        for j, y in enumerate(t):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

    spliced_motif = ""
    x, y = len(s), len(t)

    while x * y != 0:
        if lengths[x][y] == lengths[x -1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            spliced_motif = s[x - 1] + spliced_motif
            x -= 1
            y -= 1

    return spliced_motif

#Add in nucleotides missing from each seq to find shortest common supersequence (scs)
def scs(s, t):
    """Returns shortest common supersequence of 2 given sequences"""

    subseq = lcs(s, t)
    superseq = ""
    i, j = 0, 0

    for nt in subseq:
        if i < len(s):
            while s[i] != nt:
                superseq += s[i]
                i += 1
            i += 1

        if j < len(t):
            while t[j] != nt:
                superseq += t[j]
                j += 1
            j += 1

        superseq += nt

    if i < len(s):
        superseq += s[i:]

    if j < len(t):
        superseq += t[j:]

    return superseq

with open('../Files/rosalind_bio_SCSP.txt', 'r') as myfile:
    mylines = myfile.read().splitlines()
    string1 = mylines[0]
    string2 = mylines[1]

print(scs(string1, string2))
