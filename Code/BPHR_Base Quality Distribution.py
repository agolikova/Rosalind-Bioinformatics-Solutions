#Given: FASTQ file, quality threshold q
#Return: Number of positions where mean base quality falls below given threshold

from Bio import SeqIO

def base_quality(records, threshold):
    """Returns number of positions where mean base quality of records falls below given threshold"""

    count = 0

    qualities = []

    #letter_annotations = restricted dict containing annotation (quality in this case) per letter/symbol
    for record in records:
        quality =  record.letter_annotations["phred_quality"]
        qualities.append(quality)

    for i in range(len(qualities[0])):
        if sum([q[i] for q in qualities]) / len(qualities) < threshold:
            count += 1

    return count

with open('../Files/rosalind_bphr.txt', 'r') as myfile:
    q = int(myfile.readline())
    sequences = list(SeqIO.parse(myfile, "fastq"))

print(base_quality(sequences, q))
