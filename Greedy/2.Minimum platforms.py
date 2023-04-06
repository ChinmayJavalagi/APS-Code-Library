"""
1. Sort both arr and dep.
2. Keep two indexes i=1 and j=0, for arr and dep respectively. Iterate through the arrays,
      if a train arrives before a train leaves(arr[i]<=dep[j]), then we need a new platform so cnt++ and i++ to check for arrival time of next train.
      if not then we decrease the cnt-- and j++ to check the departure of next train with arrival of another train.
3. Keep track of the maximum platforms requried using a variable maxi.
4. Return maxi

"""

#Time Complexity: O(nlogn)

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        
        maxi = 1
        cnt = 1
        i,j = 1,0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                cnt+=1
                i+=1
            else:
                cnt-=1
                j+=1
            maxi = max(maxi, cnt)
            
        return maxi
