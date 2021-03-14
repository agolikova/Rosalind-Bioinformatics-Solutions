#Given: A quality threshold, along with FASTQ entries for multiple reads
#Return: Number of reads whose average quality is below threshold

from Bio import SeqIO

def below_threshold(reads, threshold):
    """Returns number of reads whose average quality is below given threshold"""

    count = 0

    for read in reads:
        quality = read.letter_annotations["phred_quality"]
        avg_quality = sum(quality)/len(quality)

        if avg_quality < threshold:
            count += 1

    return count

with open('../Files/rosalind_phre.txt', 'r') as myfile:
    quality_threshold = int(myfile.readline())
    fastq_entries = SeqIO.parse(myfile, "fastq")

    print(below_threshold(fastq_entries, quality_threshold))
