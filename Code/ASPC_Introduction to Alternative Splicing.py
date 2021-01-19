#Given: Positive integers n and m with 0 ≤ m ≤ n ≤ 2000
#Return: Sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000

#Count total number of subsets having a fixed size k
#NB order of elements (exons) in set cannot be altered in this instance

from math import factorial

def count_subsets(n, m):
    """Returns sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000"""

    subsets = 0

    # C(n,k) = n! / (k! (n-k)!)

    for k in range(m, n+1):
        subsets += (factorial(n) // (factorial(k) * factorial(n-k)))

    result = subsets % 1000000

    return result

n = 1633 #Number of elements in set
m = 1251 #Sets could have a size between len(m) and len(n)

print(count_subsets(n, m))
