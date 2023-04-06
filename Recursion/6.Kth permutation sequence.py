"""
1. We take the factorial of the given n as well as store the values from 1 to n in some data structure say a list.
2. Initialise an empty string to add the nums of the discovered kth permutation one by one.
3. Since we use 0-based indexing we do, k-=1.

Ex: if n = 4, arr = [1,2,3,4], k = 16(given 17), fact = 24(but here assuming we already fixed first number we get fact = 6)
    fixing 1 --> [2,3,4] --> 3! = 6 ------ [0,5]
    fixing 2 --> [1,3,4] --> 3!            [6 to 11]
    fixing 2 --> [1,3,4] --> 3!            [11 to 17]
    fixing 4 --> [1,2,3] --> 3!
                   total --> 24
    so we add our first no 3 to the string becoz arr[16//6] is arr[2] which is 3.
    we remove that element.
    to update k, we do k = 16%6 so we get to know that now we have to find the 4th sequence after fixing 2.
    to update fact,  we do fact = 6//3 (3 is after popping)
In this way we go on adding the next num to the res that is to be fixed to produce kth permutation.
"""

# Time Complexity: O(N) * O(N) = O(N^2)

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = []
        fact = 1
        for i in range(1, n):
            fact = fact*i
            arr.append(i)
        arr.append(n)
        string = ''
        k -= 1
        while True:
            string += str(arr[k//fact])
            arr.pop(k//fact)
            if len(arr) == 0:
                break
            k %= fact
            fact //= len(arr)
        return string
