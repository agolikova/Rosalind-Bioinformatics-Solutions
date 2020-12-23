#Given: DNA string s and a collection of substrings of s acting as introns. All strings given in FASTA format
#Return: Protein string resulting from transcribing and translating exons of s

from Bio.Seq import Seq
from Bio import SeqIO

def splice_RNA(dna, introns):
    """Returns protein string resulting from splicing introns from given DNA & translating RNA"""

    for intron in introns:
        dna = dna.replace(str(intron.seq), "")

    protein = Seq(dna).translate(to_stop=True)

    return protein

with open('../Files/rosalind_bio_SPLC.txt', 'r') as myfile:
    dataset = list(SeqIO.parse(myfile, "fasta"))
    test_dna = str(dataset[0].seq)
    test_introns = dataset[1:]

print(splice_RNA(test_dna, test_introns))
