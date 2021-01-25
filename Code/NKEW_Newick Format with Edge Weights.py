#Given: Collection of n weighted trees in Newick format, with each tree containing at most 200 nodes. Each tree Tk is followed by a pair of nodes xk and yk in Tk
#Return: Collection of n numbers, for which kth number represents distance between xk and yk in Tk

import sys
from Bio import Phylo
import io

def calc_newick(dataset):
    """Returns Newick distance between specified pairs of nodes in given weighted trees"""

    #Use Phylo distance function from Bio.Phylo.BaseTree module
    for i, line in dataset:
        x, y = line.split()
        tree = Phylo.read(io.StringIO(i), 'newick')
        sys.stdout.write('%s' % round(tree.distance(x, y)) + ' ')

    sys.stdout.write('\n')

with open('../Files/rosalind_bio_NKEW.txt', 'r') as myfile:
    pairs = [i.split('\n') for i in myfile.read().strip().split('\n\n')] #'\n\n' = double new line

calc_newick(pairs)
