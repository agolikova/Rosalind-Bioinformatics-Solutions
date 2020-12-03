#Given: Positive integer n, collection of n protein strings, multiset R of positive numbers (corresponding to complete spectrum of unknown protein string)
#Return: Maximum multiplicity of R⊖S[sk] taken over all strings sk, followed by string sk for which this maximum multiplicity occurs

MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}

def protein_weight(protein):
    """Returns weight of given protein string"""

    weight = sum(MONOISOTOPIC_MASS_TABLE[aa] for aa in protein)
    return round(weight, 5)

def get_multiplicity(string, multiset):
    """Calculates weight of each prefix/suffix & checks if they correspond to any given weight in multiset.
    Returns multiplicity count for given string."""

    multiplicity = 0

    for i in range(len(string) + 1):
        prefix = string[:i]
        suffix = string[i:]

        if protein_weight(prefix) in multiset or protein_weight(suffix) in multiset:
            multiplicity += 1

    return multiplicity

def get_max_multiplicity(protein_strings):
    """Prints max multiplicity over all protein strings & string over which this occurs"""

    max_multiplicity = 0
    result_string = ""

    for prot in protein_strings:
        m = get_multiplicity(prot, complete_spectrum)

        if m > max_multiplicity:
            max_multiplicity = m
            result_string = prot

    print(max_multiplicity)
    print(result_string)

with open('../Files/rosalind_bio_PRSM.txt', 'r') as myfile:
    n = int(myfile.readline().strip())

    my_proteins = []
    for i in range(n):
        my_proteins.append(myfile.readline().strip())

    complete_spectrum = set([float(j) for j in myfile.readlines()])

get_max_multiplicity(my_proteins)
