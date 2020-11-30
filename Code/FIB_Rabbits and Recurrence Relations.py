#Given: Positive integers n≤40 and  k≤5
#Return: Total number of rabbit pairs that will be present after n months
#Begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs

def rabbitcalculator(n, k):
    """Returns total number of rabbit pairs that will be present after n months"""

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rabbitcalculator(n - 1, k) + k * rabbitcalculator(n - 2, k)

print(rabbitcalculator(34, 2))
