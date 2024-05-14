'''
Binary representation of next number

Given a binary representation in the form of a string(s) of a number n, the task is to find a binary representation of n+1.

Example 1:

Input: s = "10"
Output: 11
Explanation: "10" is the binary 
representation of 2 and binary 
representation of 3 is "11"
'''

class Solution:
	def binaryNextNumber(self, s):
	    length=len(s)
	    
		if '0' not in s:
		    return '1'+'0'*length
		    
        i=-1
        s=list(s)
        
        while i>-length-1:
            if s[i]=='1':
                s[i]='0'
            elif s[i]=='0':
                s[i]='1'
                break
            i-=1
        i=0
        
        count=0
        while i<length:
            if s[i]=='0':
                count+=1
            else:
                break
            i+=1
        return ''.join(s[count:])
