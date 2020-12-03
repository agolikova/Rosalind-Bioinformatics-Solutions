#Given: Positive integers n≤100 and m≤20
#Return: Total number of pairs of rabbits that will remain after n-th month if all rabbits live for m months
#Assumes each pair of rabbits reaches maturity in 1 month & produces a single pair of offspring (one male, one female) each subsequent month

def rabbitcalculator(n, m):
    """ Return total number of pairs of rabbits that will remain after the n-th month
    if all rabbits live for m months"""

    bunnies = [1, 1]
    months = 2
    count = []

    while months < n:
        if months < m:
            bunnies.append(bunnies[-2] + bunnies[-1])
        elif months == m or count == m + 1:
            bunnies.append(bunnies[-2] + bunnies[-1] - 1)
        else:
            bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(m + 1)])
        months += 1

    return bunnies[-1]

print(rabbitcalculator(93, 16))
