#Given: Genus name, followed by two dates in YYYY/M/D format
#Return: Number of Nucleotide GenBank entries for given genus that were published between dates specified

#Use Entrez, data retrieval system offered by NCBI
from Bio import Entrez

def GenBank_entries(genus, date1, date2):
    """Returns number of Nucleotide GenBank entries for given genus that were published between dates specified"""

    Entrez.email = "example@test.com"

    #Search NCBI nucleotide database
    terminology = Entrez.esearch(db="nucleotide", term=genus + '[Organism] AND ("' + date1 + '"[PDAT] : "' + date2 + '"[PDAT])')

    nucleotides = Entrez.read(terminology)

    return nucleotides['Count']

with open('../Files/rosalind_gbk.txt', 'r') as myfile:
    genus_name = myfile.readline().strip()
    start = myfile.readline().strip()
    end = myfile.readline().strip()

print(GenBank_entries(genus_name, start, end))
