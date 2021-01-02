#Given: At most 50 DNA strings of approximately equal length, deriving from same strand of single linear chromosome
#Return: Shortest superstring containing all given strings (thus corresponding to a reconstructed chromosome)
#NB dataset guaranteed to satisfy following condition: there exists a unique way to reconstruct entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length

from Bio import SeqIO

def find_superstring(substrings, result = ""):
    """Returns shortest superstring containing all given substrings"""

    #Return superstring once all substrings have been removed from list and added to superstring
    if len(substrings) == 0:
        return result

    #pop() method removes item at given index from list & returns removed item
    #First substring goes into algorithm
    elif len(result) == 0:
        result = substrings.pop(0)
        return find_superstring(substrings, result)

    else:
        for i in range(len(substrings)): #Go through each substring one by one
            a = substrings[i]
            l = len(a)

            for p in range(int(l/2)):
                q = l - p #Know that reads will overlap by half their length or more

                if result.startswith(a[p:]): #Check if current superstring result starts with ending of substring a
                    substrings.pop(i) #If so, remove substring from list and merge to superstring
                    return find_superstring(substrings, a[:p] + result)

                if result.endswith(a[:q]): #Check if current superstring result ends with start of substring a
                    substrings.pop(i) #If so, remove substring from list and merge to superstring
                    return find_superstring(substrings, result + a[q:])

with open('../Files/rosalind_bio_LONG.txt', 'r') as myfile:
    sequences = []
    for record in SeqIO.parse(myfile, "fasta"):
        sequences.append(record.seq)

print(find_superstring(sequences))
