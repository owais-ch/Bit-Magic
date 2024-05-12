'''
Party of Couples (GFG)

You are given an integer array arr[] of size n, representing n number of people in a party, each person is denoted by an integer. Couples are represented by the same number ie: two people have the same integer value, it means they are a couple. Find out the only single person in the party of couples.

NOTE: It is guarantee that there exist only one single person in the party.

Example 1:

Input: 
n = 5
arr = {1, 2, 3, 2, 1}
Output: 
3
Explaination: Only the number 3 is single.
'''
class Solution:
    def findSingle(self, n, arr):
        for i in range(n):
            if i==0:
                value=arr[i]
            else:
                value=value^arr[i]
        return value
