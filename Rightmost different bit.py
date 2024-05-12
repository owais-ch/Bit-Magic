'''
Rightmost different bit
Given two numbers M and N. The task is to find the position of the rightmost different bit in the binary representation of numbers. If both M and N are the same then return -1 in this case.

Example 1: 

Input: 
M = 11, N = 9
Output: 
2
Explanation: 
Binary representation of the given numbers are: 1011 and 1001, 2nd bit from right is different.
'''
class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        position=1
        
        while m>0 or n>0:
            
            if m&1!=n&1:
                return position
            position+=1
            if m>0:
                m=m>>1
            if n>0:
                n=n>>1
        

        return -1
