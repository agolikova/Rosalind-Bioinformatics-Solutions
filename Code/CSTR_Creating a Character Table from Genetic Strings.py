#Given: A collection of at most 100 characterizable DNA strings
#Return: A character table for which each nontrivial character encodes symbol choice at a single position of strings

def get_character_table(dna_strings):
    """Prints character table from given list of genetic strings"""

    string1 = dna_strings[0]

    for i in range(len(string1)):
        count0 = 0
        count1 = 0
        output = ""

        for seq in dna_strings:
            if string1[i] == seq[i]:
                count1 += 1
                output += "1"
            else:
                count0 += 1
                output += "0"

        #Character table should not encode trivial characters
        if count1 > 1 and count0 > 1:
            print(output)

with open('../Files/rosalind_bio_CSTR.txt', 'r') as myfile:
    sequences = []
    for line in myfile:
        sequences.append(line.strip())

get_character_table(sequences)
