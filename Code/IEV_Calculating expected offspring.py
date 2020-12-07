#Given: Six integers representing number of couples having the following genotypes:
    # 1. AA-AA
    # 2. AA-Aa
    # 3. AA-aa
    # 4. Aa-Aa
    # 5. Aa-aa
    # 6. aa-aa

#Return: Expected number of offspring displaying dominant phenotype in next generation
#Assume that every couple has exactly two offspring

def calc_offspring(gen1, gen2, gen3, gen4, gen5, gen6):
    """Returns expected number of offspring displaying dominant phenotype in the next generation"""

    offspring1 = gen1 * 2
    offspring2 = gen2 * 2
    offspring3 = gen3 * 2
    offspring4 = gen4 * 1.5
    offspring5 = gen5
    offspring6 = gen6 * 0

    totaloffspring = offspring1 + offspring2 + offspring3 + offspring4 + offspring5 + offspring6

    return totaloffspring

print(calc_offspring(17186, 18245, 17214, 18565, 17104, 19517))
