#Given: DNA string s of length at most 1000 bp
#Return: The reverse complement of s

myfile = open('../Files/rosalind_bio_REVC.txt', 'r')
myfile = myfile.read()

def revc(dna):
    """Return reverse complement of given DNA strand"""

    cstrand = ""

    for base in dna:
        if base == "A":
            cstrand = "T" + cstrand
        elif base == "T":
            cstrand = "A" + cstrand
        elif base == "C":
            cstrand = "G" + cstrand
        elif base == "G":
            cstrand = "C" + cstrand

    return cstrand

print(revc(myfile))
