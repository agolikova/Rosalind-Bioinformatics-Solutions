#Given: Two DNA strings s and t
#Return: All locations of t as a substring of s (use 1-based numbering)

with open('../Files/rosalind_bio_SUBS.txt', 'r') as myfile:
    mylines = myfile.read().splitlines()
    mainstring = mylines[0]
    substring = mylines[1]
    
#OPTION 1
from Bio import motifs
from Bio.Seq import Seq

def findmotif(s, t):
    """Prints all locations of s as a substring of t using 1-based numbering"""

    target_seq = Seq(s)
    motif = motifs.create([Seq(t)])

    for pos, seq in motif.instances.search(target_seq):
        print(str(pos + 1), end = " ")

findmotif(mainstring, substring)

#OPTION 2
def findmotif(s, t):
    """Returns all locations of s as a substring of t using 1-based numbering"""

    count = s.find(t) #.find() returns index of first occurence of t in s
    locations = ""

    while count != -1:
        locations += " " + str(count + 1)
        count = s.find(t, count + 1)

    return locations

print(findmotif(mainstring, substring))

#OPTION 3
def findmotif(s, t):
    """Returns all locations of s as a substring of t using 1-based numbering"""

    locations = ""

    for i in range(len(s)):
        if s[i:].startswith(t):
            locations += " " + str(i + 1)

    return locations

print(findmotif(mainstring, substring))
