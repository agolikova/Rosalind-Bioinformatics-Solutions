#Given: Positive integer n≤10000 followed by a permutation π of length n
#Return: Longest increasing subsequence of π, followed by a longest decreasing subsequence of π
#NB a subsequence of a permutation is a collection of elements of the permutation in the order that they appear, not necessarily contiguously 

def subsequence(seq):
    """Returns longest increasing subsequence of given seq"""

    P = [None] * len(seq) #list: P[i] points to M[j], where i is index of seq ie. point to previous element of subs
    M = [None] * len(seq) #list: M[j-1] will point to index of seq that holds smallest value that could be used to build incr subs

    #At least one element in list, so at least an increasing subsequence of len 1 (first element)
    L = 1 #number: gets updated while looping & marks len of longest incr subs found up until that point
    M[0] = 0

    #Loop over seq starting from second element
    for i in range(1, len(seq)):

        #Binary search: want largest j <= L such that seq[M[j]] < seq[i]
        #Want lower bound at end of search process
        low = 0
        high = L

        #Manually check upper bound value as not checked in binary search
        if seq[M[high - 1]] < seq[i]:
            j = high

        #Actual binary search loop
        else:
            while high - low > 1:
                mid = (high + low) // 2

                if seq[M[mid -1]] < seq[i]:
                    low = mid
                else:
                    high = mid

            j = low #sets default value to 0

        P[i] = M[j - 1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)

    result = []
    pos = M[L - 1]

    for k in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]

with open('../Files/rosalind_bio_LGIS.txt', 'r') as myfile:
    mylines = myfile.read().splitlines()
    n = int(mylines[0])
    permutation = [int (x) for x in mylines[1].split()]

incr = subsequence(permutation)

#To get the longest decreasing subsequence, revert the values, call the function, then revert the values again
decr = subsequence(permutation[::-1])[::-1]

print(*incr)
print(*decr)
