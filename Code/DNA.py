myfile = open('../Files/rosalind_bio_DNA.txt', 'r')

for line in myfile:
    for word in line.split():
        A = word.count('A')
        G = word.count('G')
        C = word.count('C')
        T = word.count('T')

print(A, C, G, T)

myfile.close()
