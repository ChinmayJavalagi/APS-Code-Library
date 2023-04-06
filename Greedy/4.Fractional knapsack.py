"""
1. Sort the array according to value/weight ratio in decreasing order.
2. Iterate and go on adding the values till the weight remaining in the knapsack is less than arr.weight.
3. Add the remaining value by calculating (W/arr[i].weight)*arr[i].value and return res
"""

#Time Complexity: O(n log n + n)


class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        arr.sort(key = lambda x : x.value/x.weight, reverse = True)
        res, cur_W = 0,W
        for i in range(n):
            if arr[i].weight <= W:
                W -= arr[i].weight
                res += arr[i].value 
            else:
                res += (W/arr[i].weight)*arr[i].value
                return res
        return res
