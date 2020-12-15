#Given: Two multisets of positive real numbers S1 and S2. The size of each multiset is at most 200
#NB Multisets represent simplified mass spec taken from 2 peptides
#Return: Largest multiplicity of S1⊖S2, as well as absolute value of number x maximizing (S1⊖S2)(x)

from collections import Counter

def minkowski_diff(set1, set2):
    """Prints number that occurs most frequently in multiset formed by set1 ⊖ set2, and its frequency"""

    differences = []

    for i in set1:
        for j in set2:
            diff = round(i - j, 5)
            differences.append(diff)

    #Returns list of most common element and its count
    mylist = Counter(differences).most_common(1)

    print(mylist[0][1]) #Prints largest multiplicity (frequency)
    print(mylist[0][0]) #Prints absolute value
    #NB mylist[0] returns correct answer with both number & freq, but not in order requested by problem

with open('../Files/rosalind_bio_CONV.txt', 'r') as myfile:
    multisets = []
    for line in myfile:
        multisets.append(line.strip())

S1 = [float(x) for x in multisets[0].split()]
S2 = [float(x) for x in multisets[1].split()]

minkowski_diff(S1, S2)
