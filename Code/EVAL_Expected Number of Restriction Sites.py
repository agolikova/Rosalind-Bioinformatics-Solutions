#Given: Positive integer n (≤1,000,000), DNA string s of even length (≤10), array A of length (≤20) containing numbers between 0 and 1
#Return: Array B having same length as A, where B[i] represents expected number of times that s will appear as substring of random DNA string t of length n where t is formed with GC-content A[i]

def restriction_sites(length, dna, GC_array):
    """Prints array B where B[i] represents no. of times given dna string will appear as substring of random DNA string t of given length when t is formed with given GC content from GC_array[i]"""

    AT = 0
    GC = 0

    for nt in dna:
        if nt == "A" or nt == "T":
            AT += 1
        elif nt == "G" or nt == "C":
            GC += 1

    #Number of opportunities for finding dna in random dna string t is equal to given length - len(dna) + 1
    substring_slots = length - len(dna) + 1

    B = []

    for GC_value in GC_array:
        #Prob that randomly created dna seq with specific GC content will match given dna seq
        dna_prob = ((0.5 * GC_value)**GC) * ((0.5 * (1 - GC_value))**AT)

        #For overall prob of finding dna in t, add all individual probs of randomly forming dna with specified GC contents
        result = dna_prob * substring_slots
        B.append("%0.3f" % result)

    print(*B, sep=" ")

with open('../Files/rosalind_bio_EVAL.txt', 'r') as myfile:
    mylines = myfile.read().splitlines()
    n = int(mylines[0]) #Positive integer
    s = mylines[1] #DNA string
    A = [float (x) for x in mylines[2].split()] #Array of GC contents

restriction_sites(n, s, A)
