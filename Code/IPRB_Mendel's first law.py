#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms
#k individuals = homozygous dominant for a factor, m = heterozygous, n = homozygous recessive
#Return: Probability that two randomly selected mating organisms will produce individual possessing a dominant allele (and thus displaying dominant phenotype). Assume that any two organisms can mate

def calc_prob(k, m, n):
    """Return  probability that two randomly selected mating organisms will produce
    an individual possessing a dominant allele"""

    total = k + m + n

    nn = (n/total) * ((n-1)/(total-1))
    mm = (m/total) * ((m-1)/(total-1))
    nm = ((m/total) * (n/(total-1))) + ((n/total) * (m/(total-1)))

    #Calculate probability of offspring with recessive phenotype
    prob_recess = nn + mm*0.25 + nm*0.5

    #Subtract prob of recessive phenotype from 1 to get prob of dominant phenotype
    probability = 1 - prob_recess

    return probability

print(calc_prob(25, 15, 26))
