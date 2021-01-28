#Given: DNA string s with $ appended, a positive integer k, and a list of edges defining suffix tree T(s)
#Each edge represented by 4 components: label of its parent node in T(s); label of its child node in T(s); location of substring t of s∗ assigned to edge; length of t
#Return: Longest substring of s that occurs at least k times in s

class Node:
    def __init__(self, lab):
        self.f = self.t = 0
        self.s = set()
        self.lab = lab

    def __repr__(self):
        return '%s(f=%s, t=%s, s=%s)' % tuple(map(str, (self.lab, self.f, self.t, self.s)))

def longest_substring(r, l):
    """Returns longest repeating substring of given seq"""

    global longest_length, longest_string
    substring = 0

    if r.t == len(dna_string):
        return 1

    str_collection.append((r.f, r.t))

    for son in r.s:
        substring += longest_substring(son, 1 + r.t - r.f)

    if substring >= k and l + r.t - r.f > longest_length:
        longest_string = list(str_collection)
        longest_length = l + r.t - r.f

    str_collection.pop()

    return substring

sons = set()
nodes = {}
longest_length = 0
longest_string = []
str_collection = []

with open('../Files/rosalind_bio_LREP.txt', 'r') as myfile:
    dna_string = myfile.readline().strip()
    k = int(myfile.readline().strip())

    for x in map(str.strip, myfile.readlines()):
        a, b, location, t_len = x.split()

        node_a = nodes.setdefault(a, Node(a))
        node_b = nodes.setdefault(b, Node(b))
        node_b.f = int(location) - 1
        node_b.t = int(location) + int(t_len) - 1

        node_a.s.add(node_b)
        sons.add(node_b)

    root = (set(nodes.values()) - sons).pop()

longest_substring(root, 0)

print(''.join(dna_string[i:j] for (i, j) in longest_string))
