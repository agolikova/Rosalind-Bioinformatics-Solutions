#Given: Rooted binary tree T in Newick format encoding individual's pedigree for Mendelian factor whose alleles are A (dominant) & a (recessive)
#Return: 3 numbers between 0 and 1, corresponding to respective probabilities that individual at root of T will exhibit "AA", "Aa" & "aa" genotypes

#Create dict of probabilities of "AA", "Aa" & "aa" genotypes from ancestors
prob_dict ={
            ("AA", "AA"): (1.0, 0.0, 0.0),
            ("AA", "Aa"): (0.5, 0.5, 0.0),
            ("AA", "aa"): (0.0, 1.0, 0.0),
            ("Aa", "AA"): (0.5, 0.5, 0.0),
            ("Aa", "Aa"): (0.25, 0.5, 0.25),
            ("Aa", "aa"): (0.0, 0.5, 0.5),
            ("aa", "AA"): (0.0, 1.0, 0.0),
            ("aa", "Aa"): (0.0, 0.5, 0.5),
            ("aa", "aa"): (0.0, 0.0, 1.0)
            }

#Calculate offspring genotype probability
def calc_prob(ancestor1, ancestor2):
    p = {"AA":0.0, "Aa":0.0, "aa":0.0}

    for k1, v1 in ancestor1.items():
        for k2, v2 in ancestor2.items():
            p["AA"] += v1 * v2 * prob_dict[(k1,k2)][0]
            p["Aa"] += v1 * v2 * prob_dict[(k1,k2)][1]
            p["aa"] += v1 * v2 * prob_dict[(k1,k2)][2]

    return p

AA = {"AA":1.0, "Aa":0.0, "aa":0.0}
Aa = {"AA":0.0, "Aa":1.0, "aa":0.0}
aa = {"AA":0.0, "Aa":0.0, "aa":1.0}

with open('../Files/rosalind_bio_MEND.txt', 'r') as myfile:
    T = myfile.readline().strip()
    T = T.replace(";", "").replace("(", "calc_prob(")

    print(eval(T))
