# Problem Description

# You are given a 1D integer array B containing A integers.

# Count the number of ways to split all the elements of the array into 3 contiguous parts so that the sum of elements in each part is the same.

# Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n])

#IDEA: find the sums 1/3 and 2/3 of total

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        for i in range(1,A):
            B[i] = B[i]+B[i-1]
        if B[A-1]%3 !=0 :
            return 0
        req_sum13 = B[A-1]//3
        count13 = 0
        ret = 0
        for i in range(A-1):
            if B[i] == 2*req_sum13:
                ret += count13
            if B[i] == req_sum13:
                count13 +=1
        return ret
            
                
                
                
