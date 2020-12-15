#Given: List L of n (n≤100) positive real numbers
#Return: Protein string of length n−1 whose prefix spectrum is equal to L

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

def inferring_protein(dataset):
    """Returns protein string whose prefix spectrum is equal to dataset"""

    L = [float(line) for line in dataset]

    aa_masses = []

    for i in range(len(L) - 1):
        aa_mass = round(L[i + 1] - L[i], 4)
        aa_masses.append(aa_mass)

    rounded_mass_table = {}

    for key, value in MONOISOTOPIC_MASS_TABLE.items():
        rounded_mass_table[round(value, 4)] = key

    protein_string = ""

    for mass in aa_masses:
        protein_string += rounded_mass_table[mass]

    return protein_string

with open('../Files/rosalind_bio_SPEC.txt', 'r') as myfile:
    print(inferring_protein(myfile))
