'''
Longest Consecutive 1's (GFG)

Given a number N. Find the length of the longest consecutive 1s in its binary representation.

Example 1:

Input: N = 14
Output: 3
Explanation: 
Binary representation of 14 is 
1110, in which 111 is the longest 
consecutive set bits of length is 3.
Example 2:

Input: N = 222
Output: 4
Explanation: 
Binary representation of 222 is 
11011110, in which 1111 is the 
longest consecutive set bits of length 4. 
'''


class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        maximum=0
        total=0
        
        while N>0:
            if N&1==1:
                total+=1
            else:
                maximum=max(maximum,total)
                total=0
            N=N>>1
            
        if total>0:
            maximum=max(maximum,total)
            
        return maximum
