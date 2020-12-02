#Given: At most 10 DNA strings in FASTA format
#Return: ID of string having highest GC-content, followed by GC-content of that string

myfile = open('../Files/rosalind_bio_GC.txt', 'r')

#OPTION 1
from Bio import SeqIO
from Bio.SeqUtils import GC

def calc_GC_content(file):
    """Returns ID & GC content of string having highest GC content in file given"""

    GCcount = 0
    GCname = ""

    for record in SeqIO.parse(file, "fasta"):
        if GCcount < GC(record.seq):
            GCcount = GC(record.seq)
            GCname = record.id

    print(GCname)
    print(GCcount)

calc_GC_content(myfile)

myfile.close()

#OPTION 2
data = ''.join([x.strip('\r\n') for x in myfile.readlines()]).split('>Rosalind_')
del data[0]

def calc_GC_content(sequences):
    """Returns ID & GC content of string having highest GC content in file given"""

    dictio = {}

    for seq in sequences:
        countCG = 0
        totalcount = 0
        nucleotides = str(seq[4:])
        stringID = str(seq[:4])

        for nt in nucleotides:
            totalcount += 1
            if nt == 'C' or nt == 'G':
                countCG += 1

        dictio[stringID] = (countCG/totalcount) * 100.000

    maxi = max(dictio, key=dictio.get)

    print('>Rosalind_'+str(maxi)+'\n'+("{0:.6f}".format(round(dictio[maxi],6))))

calc_GC_content(data)

myfile.close()

