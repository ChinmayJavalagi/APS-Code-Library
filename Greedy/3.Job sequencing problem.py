"""
1. Sort the Jobs in decreasing order of profit.
2. Create a visited array of length n to keep track of which jobs we have considered.

The thought process here is to iterate over the sorted Jobs and assign it to the maximum deadline possible, suppose if deadline of profit 40 is 4 then we assign it to 4 instead of any other day so that we can save left out days for other job deadlines which might be less than 4.

4. Iterate from beginning to consider jobs, then iterate from backwards(i.e. from deadline to 1) check if not visited, cnt_jobs++, profit+=job.profit and make it as visited and break the loop.
5. if visited, then go on checking the previous index if any space is there.
"""


#Time Complexity: O(N log N) + O(N*M)
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key = lambda x:x.profit, reverse = True)
       
        jobIds = [-1]*(n+1)
        jobProfit, countJobs = 0, 0
        for i in range(n):
            for j in range(Jobs[i].deadline, 0, -1):
                if jobIds[j] == -1:
                    countJobs+=1
                    jobProfit+=Jobs[i].profit
                    jobIds[j] = 1
                    break
                
                
        return countJobs, jobProfit    
