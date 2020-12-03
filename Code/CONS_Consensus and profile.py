#Given: A collection of at most 10 DNA strings of equal length
#Return: A consensus string and profile matrix for the collection

from Bio import SeqIO

with open('../Files/rosalind_bio_CONS.txt', 'r') as myfile:
    data = []
    for record in SeqIO.parse(myfile, "fasta"):
        sequence = []
        for nt in record.seq:
            sequence.append(nt)
        data.append(sequence) #Add each nested sequence list to list of all sequences

import numpy

def profile_matrix(sequences):
    """Prints profile matrix & consensus string for given collection of sequences"""

    # numpy.zeros returns a new array of given shape and type, filled with zeros
    # Optional parameters: shape (no. columns, no. rows), data type (dtype)
    profile = numpy.zeros((4, len(sequences[0])), dtype=numpy.int)

    # Iterate over each nt in each seq & count no. of times they occur at specific position
    # Add results to profile matrix
    for num, seq in enumerate(sequences):
        for col, nt in enumerate(seq):
            if nt == "A":
                profile[0][col] += 1
            elif nt == "C":
                profile[1][col] += 1
            elif nt == "G":
                profile[2][col] += 1
            elif nt == "T":
                profile[3][col] += 1

    #Evaluate profile matrix & create consensus sequence
    consensus = ""

    for A, C, G, T in zip(profile[0], profile[1], profile[2], profile[3]):
        if A >= C and A >= G and A >= T:
            consensus += "A"
        elif C >= A and C >= G and C >= T:
            consensus += "C"
        elif G >= A and G >= C and G >= T:
            consensus += "G"
        elif T >= A and T >= C and T >= G:
            consensus += "T"

    #Print consensus sequence & profile matrix in specified format
    #Use .join to get rid of () in matrix that is otherwise printed

    print(consensus)

    print("A: " + " ".join(str(num) for num in profile[0]))
    print("C: " + " ".join(str(num) for num in profile[1]))
    print("G: " + " ".join(str(num) for num in profile[2]))
    print("T: " + " ".join(str(num) for num in profile[3]))

profile_matrix(data)
