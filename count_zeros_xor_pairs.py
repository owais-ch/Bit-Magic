'''
Given an array A[] of size N. Find the number of pairs (i, j) such that
Ai XOR Aj = 0, and 1 ≤ i < j ≤ N.

Example 1:

â€‹Input : arr[ ] = {1, 3, 4, 1, 4}
Output : 2
Explanation:
Index( 0, 3 ) and (2 , 4 ) are only pairs 
whose xors is zero so count is 2.

â€‹Example 2:

Input : arr[ ] = {2, 2, 2} 
Output :  3
'''
import math

def calculate (arr, n) : 
    arr.sort()
    
    total=0
    count=1
    
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            if count>1:
                total+=(math.factorial(count)//(math.factorial(count-2)*math.factorial(2)))
            count=1
            
    if count>1:
        total+=(math.factorial(count)//(math.factorial(count-2)*math.factorial(2)))
        
    return total
