#Given: FASTQ file, quality cut-off value q, Phred33 quality score assumed
#Return: FASTQ file trimmed from both ends (with leading & trailing bases with quality lower than q removed)

from Bio import SeqIO

def filter_reads(reads, threshold):
    """Returns FASTQ entry trimmed from both ends using given quality threshold"""

    for read in reads:

        #letter_annotations = restricted dict containing annotation (quality in this case) per letter/symbol
        quality = read.letter_annotations["phred_quality"]

        start, end = 0, len(quality)

        while quality[start] < threshold:
            start += 1

        while quality[end - 1] < threshold:
            end -= 1

        print(read[start:end].format("fastq"))

with open('../Files/rosalind_bfil.txt', 'r') as myfile:
    q = int(myfile.readline().strip())
    fastq_entries = SeqIO.parse(myfile, "fastq")

    filter_reads(fastq_entries, q)
