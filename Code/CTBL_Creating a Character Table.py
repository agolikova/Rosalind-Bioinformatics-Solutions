#Given: Unrooted binary tree T in Newick format for at most 200 taxa
#Return: Character table having same splits as the edge splits of T. Columns should encode taxa ordered lexicographically

from Bio import Phylo

def colour_clade(clade, root):
    for subclade in clade.clades:
        if not subclade.is_terminal():
            print_subtrees(subclade, root)
            colour_clade(subclade, root)

def print_subtrees(clade, root):
    array = ""

    all_nodes = set(root.get_terminals())
    coloured_nodes = set(clade.get_terminals())
    noncoloured_nodes = all_nodes - coloured_nodes

    on_tree = []
    off_tree = []

    for i in coloured_nodes:
        on_tree.append(i.name)
    for j in noncoloured_nodes:
        off_tree.append(j.name)
    for taxon in taxa:
        if taxon in on_tree:
            array += "1"
        elif taxon in off_tree:
            array += "0"

    print(array)

with open('../Files/rosalind_bio_CTBL.txt', 'r') as myfile:
    taxa = []
    tree = Phylo.read(myfile, "newick")

    for clade in tree.find_clades():
        if clade.name:
            taxa.append(clade.name)

    taxa = sorted(taxa)

root = tree.root
colour_clade(root, root)
