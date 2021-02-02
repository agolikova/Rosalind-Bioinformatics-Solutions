#Given: 2 protein strings s and t
#Return: Maximum alignment score between s and t, using BLOSUM62 scoring matrix & linear gap penalty equal to 5

from Bio import SeqIO
from Bio.Align import substitution_matrices

#OPTION 1 using PairwiseAlignment class within Bio.Align module (much faster)

from Bio import Align

def max_alignment_score(seq1, seq2):
    """Calculate & return max alignment score between seq1 and seq2"""

    #Create aligner object which will store alignment parameters
    aligner = Align.PairwiseAligner()

    #Set parameters
    aligner.mode = "global"
    blosum62 = substitution_matrices.load("BLOSUM62")
    aligner.substitution_matrix = blosum62

    #Gap open penalty & gap extension penalty both set to -5 as using linear gap penalty equal to 5
    aligner.open_gap_score = -5
    aligner.extend_gap_score = -5

    #Calculate & print optimal alignment
    alignments = aligner.align(seq1, seq2)
    print(alignments[0])

    #Calculate & print alignment score
    score = aligner.score(seq1, seq2)
    return score

with open('../Files/rosalind_bio_GLOB.txt', 'r') as myfile:
    sequences = []
    for record in SeqIO.parse(myfile, "fasta"):
        sequences.append(record.seq)
    s = sequences[0]
    t = sequences[1]

print(max_alignment_score(s, t))

#OPTION 2 using Bio.pairwise2 module

from Bio import pairwise2

blosum62 = substitution_matrices.load("BLOSUM62")

def max_alignment_score(seq1, seq2):
    """Calculate & return max alignment score between seq1 and seq2"""

    #Alignment type is global
    #d parameter symbolises that a dictionary returns score of any pair of characters
    #s parameter symbolises that same open & extend gap penalties used for both seqs
    #Gap open penalty & gap extension penalty both set to -5 as using linear gap penalty equal to 5
    alignments = pairwise2.align.globalds(seq1, seq2, blosum62, -5, -5)

    #Method returns nice string printout of alignment
    return pairwise2.format_alignment(*alignments[0])

with open('../Files/rosalind_bio_GLOB.txt', 'r') as myfile:
    sequences = []
    for record in SeqIO.parse(myfile, "fasta"):
        sequences.append(record.seq)
    s = sequences[0]
    t = sequences[1]

print(max_alignment_score(s, t))
