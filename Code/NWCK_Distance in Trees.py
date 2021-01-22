#Given: Collection of n trees in Newick format, with each tree containing at most 200 nodes. Each tree Tk is followed by a pair of nodes xk and yk in Tk.
#Return: Collection of n positive integers, for which kth integer represents distance between xk and yk in Tk

import sys
from Bio import Phylo
import io

def newick(dataset):
    """Returns Newick distance between specified pairs of nodes in given trees"""

    #Assign branch len 1 to all branches
    #Use Phylo distance function from Bio.Phylo.BaseTree module

    for i, line in dataset:
        x, y = line.split()
        tree = Phylo.read(io.StringIO(i), 'newick')
        clades = tree.find_clades()

        for clade in clades:
            clade.branch_length = 1

        sys.stdout.write('%s' % tree.distance(x, y) + ' ')

    sys.stdout.write('\n')

with open('../Files/rosalind_bio_NWCK.txt', 'r') as myfile:
    data = [i.split('\n') for i in myfile.read().strip().split('\n\n')] #'\n\n' = double new line

newick(data)
