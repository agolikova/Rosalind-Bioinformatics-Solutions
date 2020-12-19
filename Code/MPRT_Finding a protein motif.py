#Given: At most 15 UniProt Protein Database access IDs
#Return: For each protein possessing N-glycosylation motif, output its given access ID followed by list of locations in protein string where motif can be found

#N-glycosylation motif: N{P}[ST]{P}
#[] = either/or, {} = any except

from urllib.request import urlopen #module for fetching URLs
from Bio import SeqIO
import re #regular expression operations module

def find_motif(UniProt_ID_list):
    """Prints any IDs in given list that contain N-glocyslation motif, as well as list of locations where motif found in each protein string"""

    for i in range(len(UniProt_ID_list)):
        # Gather FASTA seq data for each seq ID
        URL = 'http://www.uniprot.org/uniprot/'+ UniProt_ID_list[i] + '.fasta'
        data = urlopen(URL)

        #.decode used to convert from str to unicode (utf-8), ignoring any errors raised
        fasta = data.read().decode('utf-8', 'ignore')

        #Write to FASTA file
        with open('seq_file.fasta', 'a') as text_file:
            text_file.write(fasta)

    #Search FASTA sequences for N-glycosylation motif, ?= used to include overlapping motifs
    handle = open('seq_file.fasta', 'r')
    motifs = re.compile(r'(?=(N[^P][ST][^P]))')
    count = 0

    for record in SeqIO.parse(handle, 'fasta'):
        sequence = record.seq
        locations = []
        for m in re.finditer(motifs, str(sequence)):
            locations.append(m.start() + 1)

        #Print indexes where motif found (if any)
        if len(locations) > 0:
            print(UniProt_ID_list[count])
            print(' '.join(map(str, locations)))

        count += 1

with open('../Files/rosalind_bio_MPRT.txt', 'r') as myfile:
    IDs = []
    for line in myfile:
        IDs.append(line.strip())

find_motif(IDs)
