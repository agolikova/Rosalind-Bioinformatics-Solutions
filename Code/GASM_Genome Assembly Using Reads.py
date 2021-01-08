#Given: Collection S of (error-free) reads of equal length. In this dataset, de Bruijn graph consists of exactly two directed cycles
#Return: A cyclic superstring of minimal length containing every read or its reverse complement

from Bio.Seq import Seq

def get_cyclic_superstring(kmers):
	"""Returns cyclic superstring of min length containing every given kmer/its reverse complement"""

	#Iterate over k values until the one which gives 2 directed cycles is found
	for kval in range(1, len(kmers[0])):

		#Construct de Bruijn Graph
		DBG_edge_elements = set()

		for kmer in kmers:
			for i in range(kval):
				DBG_edge_elements.add(kmer[i:len(kmer) + i - kval + 1])
				DBG_edge_elements.add(str((Seq(kmer[i:len(kmer) - kval + i + 1])).reverse_complement()))

		#Create edges of graph
		k = len(list(DBG_edge_elements)[0])
		edge = lambda element: [element[0:k-1], element[1:k]]
		DBG_edges = [edge(element) for element in DBG_edge_elements]

		#Construct cyclic superstrings from edges
		cyclics = []

		for repeat in range(2):
			temp_kmer = DBG_edges.pop(0)
			cyclic = temp_kmer[0][-1]

			while temp_kmer[1] in [item[0] for item in DBG_edges]:
				cyclic += temp_kmer[1][-1]
				[index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp_kmer[1]]
				temp_kmer = DBG_edges.pop(index)

			cyclics.append(cyclic)

		#Break if two directed cycles have been found
		if len(DBG_edges) == 0:
			break

	#Return cyclic superstring
	return cyclics[0]

with open('../Files/rosalind_bio_GASM.txt', 'r') as myfile:
	reads = [line.strip() for line in myfile.readlines()]

print(get_cyclic_superstring(reads))
