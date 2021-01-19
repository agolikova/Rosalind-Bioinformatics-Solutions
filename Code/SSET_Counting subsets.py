#Given: Positive integer n (n≤1000)
#Return: Total number of subsets of {1,2,…,n} modulo 1,000,000

def count_subsets(n):
    """Returns total number of subsets of {1,2,…,n} modulo 1,000,000"""

    #A set with n elements has 2 ** n subsets
    result = pow(2, n, 1000000) #3rd parameter is optional modulus
    #Alternative: result = (2 ** n) % 1000000

    return result

#n = int(input("Enter n: "))
n = 953

print(count_subsets(n))
