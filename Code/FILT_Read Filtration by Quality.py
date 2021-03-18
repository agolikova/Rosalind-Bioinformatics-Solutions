#Given: Quality threshold value q, percentage of bases p, set of FASTQ entries
#Return: Number of reads in filtered FASTQ entries

from Bio import SeqIO

def filter_reads(reads, threshold, percentage):
    """Returns number of reads in filtered FASTQ entries"""

    count = 0

    for read in reads:

        #letter_annotations = restricted dict containing annotation (quality in this case) per letter/symbol
        qualities = read.letter_annotations["phred_quality"]

        passes = 0

        for letter_quality in qualities:
            if letter_quality >= threshold:
                passes += 1

        if (passes/len(qualities)) * 100 >= percentage:
            count += 1

    return count

with open('../Files/rosalind_filt.txt', 'r') as myfile:
    q, p = [int(num) for num in myfile.readline().split()]
    fastq_entries = SeqIO.parse(myfile, "fastq")

    print(filter_reads(fastq_entries, q, p))
