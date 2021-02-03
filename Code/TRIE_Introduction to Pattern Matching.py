#Given: List of at most 100 DNA strings, none of which is a prefix of another
#Return: Adjacency list corresponding to trie T for these patterns, in following format:
#If T has n nodes, first label root with 1 then label remaining nodes with integers 2 through n in any order
#Each edge of adjacency list of T will be encoded by triple containing: integer representing edge's parent node, integer representing edge's child node, symbol labelling edge

import itertools
from collections import defaultdict

class Trie:
    available = 1

    def __init__(self):
        self.label = str(Trie.available)

        #Can create new Trie objects using defaultdict
        #Works like normal dict but initialized with function that provides default value for nonexistent key
        #Will never raise KeyError
        self.child_nodes = defaultdict(Trie)

        Trie.available += 1

    def add_child(self, child):
        if not child: return

        #Shifts first character of word & delegates rest of word by recursion
        self.child_nodes[child[0]].add_child(child[1:])

    def print_trie(self):
        for char, child in self.child_nodes.items():
            print(self.label, child.label, char)
            child.print_trie()

T = Trie()

with open('../Files/rosalind_bio_TRIE.txt', 'r') as myfile:
    for s in myfile.read().split('\n'):
        T.add_child(s)

T.print_trie()
