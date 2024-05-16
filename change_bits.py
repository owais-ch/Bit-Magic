'''
Change Bits (GFG)
Given a number N, complete the following tasks,
Task 1. Generate a new number from N by changing the zeroes in the binary representation of N to 1.
Task  2. Find the difference between N and the newly generated number.

Example 1:

Input: N = 8 
Output: 7 15
Explanation:
There are 3 zeroes in binary representation
of 8. Changing them to 1 will give 15.
Difference between these two is 7.

Example 2:
Input: N = 6 
Output: 1 7
Explanation:
There is 1 zero in binary representation
of 6. Changing it to 1 will give 7.
Difference between these two is 1.
'''
import math

class Solution:
    def changeBits(self, N):
        length=int(math.log(N,2))
        
        new_num=0
        prev=N
        while N>0:
            new_num+=2**(length)
            length=length-1
            N=N>>1
        
        return (new_num-prev),new_num
