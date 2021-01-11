#Given: Positive integer n & an adjacency list (list of edges) corresponding to graph on n nodes that contains no cycles
#Return: Minimum number of edges that can be added to graph to produce a tree

#A tree of n nodes has n−1 edges
#Solution is computing (n−1) - number of edges already present in adjacency list

def complete_tree(nodes, adjacency_list):
    """Returns min no. of edges that can be added to graph consisting of edges in given adjacency list & n nodes to produce a tree"""

    existing_edges = []

    for edge in adjacency_list:
        existing_edges.append(edge)

    extra_edges = (nodes - 1) - len(existing_edges)

    return extra_edges

with open('../Files/rosalind_bio_TREE.txt', 'r') as myfile:
    lines = myfile.read().splitlines()
    n = int(lines[0])
    edges = lines[1:]

print(complete_tree(n, edges))
