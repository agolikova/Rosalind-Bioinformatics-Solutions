#Given: Collection of n (n≤10) GenBank entry IDs
#Return: Shortest of strings associated with IDs in FASTA format

#Use Entrez, data retrieval system offered by NCBI
from Bio import Entrez, SeqIO

def GenBank_entries(GenBank_IDs):
    """Returns shortest of the strings associated with given GenBank IDs in FASTA format"""

    Entrez.email = "example@test.com"

    #db parameter takes database to search, rettype parameter takes data format to be returned
    handle = Entrez.efetch(db = "nucleotide", id = GenBank_IDs, rettype = "fasta")
    records = list(SeqIO.parse(handle, "fasta"))

    #Find shortest seq & return in specified format
    shortest = min(records, key = lambda x: len(x.seq))
    return shortest.format("fasta")

with open('../Files/rosalind_frmt.txt', 'r') as myfile:
    IDs = myfile.read().strip().split()

print(GenBank_entries(IDs))
