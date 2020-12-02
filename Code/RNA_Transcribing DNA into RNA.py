#Given: DNA string t having length at most 1000 nt
#Return: Transcribed RNA string of t

myfile = open('../Files/rosalind_bio_RNA.txt', 'r')

#OPTION 1
from Bio.Seq import Seq

def transcription(file):
    dna = Seq(file.read())
    rna = dna.transcribe()
    return rna

print(transcription(myfile))

myfile.close()

#OPTION 2
myfile = myfile.read()

def transcription(file):
    return file.replace("T", "U")

print(transcription(myfile))

#OPTION 3
myfile = myfile.read()

def transcription(file):
    finalRNA = ""

    for n in myfile:
        if n == "T":
            n = "U"
        finalRNA = finalRNA + n

    return finalRNA

print(transcription(myfile))
