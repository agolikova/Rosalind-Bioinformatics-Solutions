#Given: DNA string s
#Return: Failure array of s
#NB failure arrays are employed in the course of KMP algorithm to speed up motif finding in strings

from Bio import SeqIO

def create_failure_array(sequence):
    """Prints failure array of given sequence"""

    failure_array = [0] * len(sequence)
    k = 0

    for i in range(2, len(sequence) + 1):
        while k > 0 and sequence[k] != sequence[i - 1]:
            k = failure_array[k - 1]
        if sequence[k] == sequence[i - 1]:
            k += 1
        failure_array[i - 1] = k

    print(" ".join(map(str, failure_array)))

with open('../Files/rosalind_bio_KMP.txt', 'r') as myfile:
    record = SeqIO.read(myfile, "fasta")
    DNA = list(record.seq)

create_failure_array(DNA)
