#Given: Positive integer n
#Return: Number of internal nodes of any unrooted binary tree having n leaves
#In other words, calculate the number of phylogenetic ancestors in the tree

#An unrooted binary tree having n leaves has n - 2 internal nodes
#This is because each node in an unrooted binary tree can have degree 1 (leaf) or 3 (internal node)
#So all internal nodes except the 2 outer ones will be connected to 2 other internal nodes and 1 leaf
#And 2 internal nodes on the ends will be connected to 1 internal node and 2 leaves

def calc_internal_nodes(n):
    """Returns number of internal nodes of unrooted binary tree having n number of leaves"""

    internal_nodes = n - 2
    return internal_nodes

print(calc_internal_nodes(117))
