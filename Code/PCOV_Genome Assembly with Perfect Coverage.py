#Given: A collection of (error-free) DNA k-mers (k≤50) taken from same strand of a circular chromosome
#In this dataset, all k-mers from this strand of chromosome are present, and their de Bruijn graph consists of exactly one simple cycle
#Return: A cyclic superstring of minimal length containing the reads (thus corresponding to a candidate cyclic chromosome)

def get_superstring(kmers):
    """Returns cyclic superstring of minimal length containing the given kmers"""

    #Construct de Bruijn graph
    DBG = set()
    for kmer in kmers:
        DBG.add(kmer)

    #Create graph edges
    k = len(kmers[0])
    edge = lambda element: [element[0:k-1], element[1:k]]
    DBG_edges = [edge(element) for element in DBG]

    #Construct cyclic superstring from edges
    temp = DBG_edges.pop(0)
    superstring = temp[0][-1]

    while DBG_edges:
        superstring += temp[1][-1]
        [index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp[1]]
        temp = DBG_edges.pop(index)

    return superstring

with open('../Files/rosalind_bio_PCOV.txt', 'r') as myfile:
    sequences = []
    for line in myfile:
        sequences.append(line.strip())

print(get_superstring(sequences))
