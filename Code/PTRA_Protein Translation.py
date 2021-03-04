#Given: DNA string s of length at most 10 kbp, and protein string translated by s
#Return: Index of genetic code variant (codon table) used for translation
#NB List of genetic code variants along with indexes representing these codes found here: http://www.bioinformatics.org/JaMBW/2/3/TranslationTables.html

from Bio.Seq import Seq

def genetic_code_variant(dna, protein):
    """Returns index of genetic code variant (codon table) used for translation"""

    table_indexes = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]

    for index in table_indexes:
        if dna.translate(table = index, stop_symbol = "") == protein:
            return index

with open('../Files/rosalind_ptra.txt', 'r') as myfile:
    s = Seq(myfile.readline().strip())
    translation = myfile.readline().strip()

print(genetic_code_variant(s, translation))
