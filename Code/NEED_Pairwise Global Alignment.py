#Given: 2 GenBank IDs
#Return: Maximum global alignment score between DNA strings associated with these IDs

#Use Entrez, data retrieval system offered by NCBI
#Instead of Bio.Align can use Bio.pairwise2, but runs much slower
from Bio import Entrez, SeqIO, Align

def max_alignment_score(GenBank_IDs):
    """Returns maximum global alignment score between DNA strings associated with given GenBank IDs"""

    Entrez.email = "example@test.com"

    #db parameter takes database to search, rettype parameter takes data format to be returned
    handle = Entrez.efetch(db = "nucleotide", id = GenBank_IDs, rettype = "fasta")
    records = list(SeqIO.parse(handle, "fasta"))

    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 5
    aligner.mismatch_score = -4
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -1

    alignments = aligner.align(records[0].seq, records[1].seq)
    print(alignments[0])

    score = aligner.score(records[0].seq, records[1].seq)
    return score

with open('../Files/rosalind_need.txt', 'r') as myfile:
    IDs = myfile.read().strip().split()

print(max_alignment_score(IDs))
