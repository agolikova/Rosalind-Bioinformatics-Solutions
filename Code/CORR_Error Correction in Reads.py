#Given: Collection of up to 1000 reads of equal length, some of which were generated with a single nt error
#Return: List of all corrections in form "[old read]->[new read]"

#NB following rules apply for each read s in dataset:
#1. s is correct if appears in dataset at least twice (normal or reverse complement)
#2. s is incorrect if appears only once and Hamming distance is 1 with respect to one of correct reads (normal or revc)

from Bio import SeqIO
from Bio.Seq import Seq

def hamming(seq1, seq2):
    """Returns Hamming distance between seq1 & seq2"""

    mutations = 0
    for index in range(len(seq1)):
        if seq1[index] != seq2[index]:
            mutations += 1
    return mutations

def correct_errors(sequences):
    """Prints list of sequences with corrected errors"""

    correct = []
    incorrect = []

    for i, j in enumerate(sequences):
        seq = Seq(j)
        rev_seq = seq.reverse_complement()

        for k in range(i + 1, len(sequences)):
            if seq == sequences[k] or rev_seq == sequences[k]:
                if seq not in correct and rev_seq not in correct:
                    correct.append(str(seq))
                    correct.append(str(rev_seq))

    for l in sequences:
        if l not in correct:
            incorrect.append(l)

    output = []

    for incorrect_seq in incorrect:
        for correct_seq in correct:
            if hamming(incorrect_seq, correct_seq) == 1:
                output.append(incorrect_seq + "->" + correct_seq)

    print(*output, sep="\n")

with open('../Files/rosalind_bio_CORR.txt', 'r') as myfile:
    dataset = []
    for record in SeqIO.parse(myfile, "fasta"):
        dataset.append(str(record.seq))

correct_errors(dataset)
