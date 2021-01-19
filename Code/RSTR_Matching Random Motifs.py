#Given: Positive integer N, a number x, and a DNA string s
#Return: Probability that if N random DNA strings having same length as s are constructed with GC-content x, at least one of those strings will equal s

def calc_prob(number_of_strings, GC_content, DNA):
    """Returns probability that if given number of random DNA strings having same length as given DNA seq are constructed with given GC-content, at least one of those strings will equal the DNA seq"""

    AT = 0
    GC = 0

    for nt in DNA:
        if nt == "A" or nt == "T":
            AT += 1
        elif nt == "G" or nt == "C":
            GC += 1

    #P(at least 1 match of s) = 1 − P(no matches out of N strings) = 1 − [1 - P_no_match]^N

    P_no_match = (((1 - GC_content)/2) **AT) * ((GC_content/2) **GC)
    prob = 1 - (1-P_no_match) **number_of_strings

    print("%0.3f" %prob)

N = 89314
x = 0.546363
s = "TGCCTCTAC"

calc_prob(N, x, s)
