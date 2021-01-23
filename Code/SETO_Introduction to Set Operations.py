#Given: Positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}
#Return: Six sets: A∪B, A∩B, A−B, B−A, A^c, and B^c (where set complements are taken with respect to {1,2,…,n})

def union(a, b):
    #return a | b
    return a.union(b)

def intersection(a, b):
    #return a & b
    return a.intersection(b)

def set_difference(a, b):
    return a - b

def set_complement(u, a):
    return u - a

with open('../Files/rosalind_bio_SETO.txt', 'r') as myfile:
    mylines = myfile.read().splitlines()

    n = int(mylines[0].rstrip())
    U = set(range(1, n + 1))
    A = set([int(x) for x in mylines[1].strip('{}').split(',')])
    B = set([int(x) for x in mylines[2].strip('{}').split(',')])

print(union(A, B))
print(intersection(A, B))
print(set_difference(A, B))
print(set_difference(B, A))
print(set_complement(U, A))
print(set_complement(U, B))
