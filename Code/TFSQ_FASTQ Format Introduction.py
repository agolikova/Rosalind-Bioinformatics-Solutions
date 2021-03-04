#Given: FASTQ file
#Return: Corresponding FASTA records

#OPTION 1
from Bio import SeqIO

def convert_format(input_file):
    """Converts given FASTQ file to FASTA format"""

    output_file = '../Files/rosalind_tfsq_output.txt'

    SeqIO.convert(input_file, 'fastq', output_file, 'fasta')

with open('../Files/rosalind_tfsq.txt', 'r') as myfile:
    convert_format(myfile)
   
#OPTION 2
from Bio import SeqIO
from io import StringIO #StringIO module used to create in-memory file-like object

def convert_format(input_file):
    """Converts given FASTQ file to FASTA format"""

    #Create initial object that will be treated like a file
    output_file = StringIO("")

    SeqIO.convert(input_file, 'fastq', output_file, 'fasta')

    #StringIO.getvalue() function returns entire content of file
    return output_file.getvalue()

with open('../Files/rosalind_tfsq.txt', 'r') as myfile:
    print(convert_format(myfile))
