#Given: 2 protein strings s and t
#Return: Edit distance dE(s,t)
#Edit distance = min no. of edit operations needed to transform s into t
#Edit operation = substitution, insertion, or deletion of a single symbol

from Bio import SeqIO

def edit_distance(seq1, seq2):
    """Returns edit distance (Levenshtein distance) when given 2 protein strings"""

    #Use Wagner-Fischer dynamic programming algorithm
    current = list(range(len(seq1) + 1))

    for j, y in enumerate(seq2):
        last, current = current, [j + 1]

        for i, x in enumerate(seq1):
            current.append(last[i] if y == x else min([last[i + 1], last[i], current[-1]]) + 1)

    return current[-1]

with open('../Files/rosalind_bio_EDIT.txt', 'r') as myfile:
    sequences = []
    for record in SeqIO.parse(myfile, "fasta"):
        sequences.append(str(record.seq))

s = sequences[0]
t = sequences[1]

print(edit_distance(s, t))
