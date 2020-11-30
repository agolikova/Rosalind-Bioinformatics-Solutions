#COUNTING DNA NUCLEOTIDES 
#Given: DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting respective number of times that symbols 'A', 'C', 'G', and 'T' occur in s.

myfile = open('../Files/rosalind_bio_DNA.txt', 'r')

for line in myfile:
    for word in line.split():
        A = word.count('A')
        G = word.count('G')
        C = word.count('C')
        T = word.count('T')

print(A, C, G, T)

myfile.close()
