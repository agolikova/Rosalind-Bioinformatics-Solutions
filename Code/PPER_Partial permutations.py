#Given: Positive integers n and k such that 100 ≥ n > 0 and 10 ≥ k > 0
#Return: Total number of partial permutations P(n,k), modulo 1,000,000

def permcalculator(n, k):
    """Returns total number of partial permutations o given integers P(n,k), modulo 1,000,000"""

    #FASTER VARIANT
    #Count the number of choices there are in choosing k numbers out of the set (1,2,3,...,n)
    #For first choice, there are n numbers to choose from. Second choice, n - 1 numbers left
    #Process continues until kth choice made
    #Each choice is independent of the next, so can multiply choices at each step
    partial_perm = 1

    for i in range(k):
        partial_perm *= (n - i)

    total = partial_perm % 1000000

    return total

    #SLOWER VARIANT
    #count = 0
    #for perm in itertools.permutations(range(1, n+1), k):
        #count += 1
    #total = count % 1000000
    #return total

print(permcalculator(100, 8))
