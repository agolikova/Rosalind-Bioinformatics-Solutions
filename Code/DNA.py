#COUNTING DNA NUCLEOTIDES 
#Given: DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting respective number of times that symbols 'A', 'C', 'G', and 'T' occur in s.

def count_nt(file):
    """Return number of times that each nt appears in given DNA seq"""
    
    for line in myfile:
        for word in line.split():
            A = word.count('A')
            C = word.count('C')
            G = word.count('G')
            T = word.count('T')

    print(A, C, G, T)

myfile = open('../Files/rosalind_bio_DNA.txt', 'r')
count_nt(myfile)

myfile.close()
