#Given: Positive integers N (N ≤ 7), m (m ≤ 2N), g (g ≤ 6) and k (k ≤ 2N)
#Return: Probability that in population of N diploid individuals initially possessing m copies of dominant allele, will observe after g generations at least k copies of recessive allele. Assume Wright-Fisher model

from scipy.special import comb

def WrightFisher(N, m, g, k):
    """Given population of N diploid individuals initially possessing m copies of dominant allele, returns prob that after g generations will observe at least k copies of recessive allele"""

    p = m / (2 * N) #Dominant allele
    q = 1 - p #Recessive allele

    #Probability of exactly i copies of recessive allele in 1st generation
    prob = [comb(2 * N, i) * (q ** (i)) * (p ** (2 * N - i)) for i in range(1, 2 * N + 1)]

    #Probability of exactly t copies of recessive allele in next generation
    for gen in range(1, g):
        gen_prob = []

        #Probability of exactly t copies of recessive allele in "gen" generation
        for t in range(1, 2 * N + 1):
            prob_t = [comb(2 * N, t) * ((i / (2 * N)) ** (t)) * ((1 - (i / (2 * N))) ** (2 * N - t)) for i in range(1, 2 * N + 1)]
            gen_prob.append(sum([prob_t[j] * prob[j] for j in range(2 * N)]))

        prob = gen_prob

    output = sum(prob[k - 1:])
    return output

with open('../Files/rosalind_bio_WFMD.txt', 'r') as myfile:
    N, m, g, k = map(int, myfile.readline().strip().split())
    print(WrightFisher(N, m, g, k))
