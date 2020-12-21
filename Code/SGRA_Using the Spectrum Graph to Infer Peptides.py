#Given: List L (of length at most 100) containing positive real numbers
#Return: Longest protein string that matches the spectrum graph of L

import numpy as np

MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}

mass_aa_decimal2 = {round(value, 2): key for key, value in MONOISOTOPIC_MASS_TABLE.items()}

def get_graph(L):
    """Converts given list L of masses into graph & edges"""

    graph, edges = {}, {}

    for i in range(len(L)):
        graph[L[i]] = []

        for j in range(i, len(L)):
            aa = mass_aa_decimal2.get(round(L[j]-L[i], 2), 0)

            if aa:
               graph[L[i]].append(L[j])
               edges[(L[i],L[j])] = aa

    return graph, edges

def find_all_paths(graph, start, end, path=[]):
    """Returns all paths using given start & end of graph"""

    path = path +[start]

    if start == end:
        return [path]

    paths = []

    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

def get_peptide(l, graph, edges):
    """Returns longest protein string that matches spectrum graph of L"""

    all_peptide_paths = []

    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            all_paths = find_all_paths(graph, l[i], l[j], path=[])
            all_peptide_paths.extend(all_paths)

    output = []

    for peptide_paths in  all_peptide_paths:
        peptide = [""]

        for i in range(len(peptide_paths) - 1):
            aa = mass_aa_decimal2.get(round(peptide_paths[i+1] - peptide_paths[i], 2))
            peptide = [p+a for p in peptide for a in aa]

        output.extend(peptide)

    return output

with open('../Files/rosalind_bio_SGRA.txt') as myfile:
    masses = [float(mass) for mass in myfile.read().strip().split('\n')]

graph, edges = get_graph(masses)
peptides = get_peptide(masses, graph, edges)
longest_protein_string = max(peptides, key=len, default="")
print(longest_protein_string)
