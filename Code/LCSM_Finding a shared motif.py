#Given: A collection of k DNA strings of length at most 1 kbp each in FASTA format
#Return: A longest common substring of the collection

from Bio import SeqIO

def common_motif(sequences):
    """Returns longest common motif present in all given sequences"""

    #Sort sequences (shortest first). Alternatively use sequences.sort()
    sorted_sequences = sorted(sequences, key=len)
    short_seq = sorted_sequences[0]
    comp_seq = sorted_sequences[1:]

    motif = ""

    #Iterate over all possible motifs in shortest seq, test if they are also present in all other sequences

    for i in range(len(short_seq)):
        for j in range(i, len(short_seq)):
            m = short_seq[i:j + 1]
            found = False

            for sequ in comp_seq:
                if m in sequ:
                    found = True
                else:
                    found = False
                    break

            if found and len(m) > len(motif):
                motif = m

    return motif

with open('../Files/rosalind_bio_LCSM.txt', 'r') as myfile:
    data = []
    for record in SeqIO.parse(myfile, "fasta"):
        data.append(str(record.seq))

print(common_motif(data))
