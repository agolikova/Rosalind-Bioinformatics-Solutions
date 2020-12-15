#Given: List L containing 2n+3 positive real numbers
#First number in L = parent mass of peptide P, all other numbers represent masses of b-ions & y-ions of P
#Return: Protein string t whose t-prefix & t-suffix weights correspond to non-parent mass values of L

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

def inferring_peptide(parent, ions):
    """Returns protein string whose prefix and suffix weights correspond to non-parent mass values given"""

    pairs = []
    index = 0
    peptide = ''

    while index < len(ions) / 2:
        closest_partner = 0
        distance = 400

        for ion in ions:
            if abs(parent - ions[index] - ion) < distance:
                closest_partner = ion
                distance = abs(parent - ions[index] - ion)

        pairs.append((ions[index], closest_partner))
        index += 1

    index = 0

    while index < len(ions) / 2 - 1:
        nearest_candidate = None

        for candidate in MONOISOTOPIC_MASS_TABLE.keys():
            if round(abs(pairs[index + 1][0] - pairs[index][0] - MONOISOTOPIC_MASS_TABLE[candidate]), 3) == 0:
                nearest_candidate = candidate

        if not nearest_candidate:
            pairs[index + 1] = (pairs[index + 1][1], pairs[index + 1][0])
            pairs.sort()

            index = 0
            peptide = ''

        else:
            peptide = ''.join([peptide, nearest_candidate])
            index += 1

    return peptide

with open('../Files/rosalind_bio_FULL.txt') as myfile:
    parent_weight = float(myfile.readline().strip())
    data = []

    for line in myfile:
        data.append(float(line.strip()))

print(inferring_peptide(parent_weight, data))
