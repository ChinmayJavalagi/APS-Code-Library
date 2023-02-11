import math

n = int(input())
arr = [[int(input()) for x in range(n)] for y in range(n)]
dp = [math.inf]*2**n
dp[0] = 0

for mask in range(0,2**n-1):
    print("mask",mask)
    x = bin(mask).count('1')
    print("x",x)
    for j in range(n):
        print("j",j)
        if not mask&(1<<j):
            dp[mask|1<<j] = min(dp[mask|1<<j], dp[mask]+arr[x][j])
            print(dp)
            
print(dp)