class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Say f[i] is the final cost to climb to the top from step i. 
        # Then f[i] = cost[i] + min(f[i+1], f[i+2])
        dp = list()
        dp.append(cost[0])
        dp.append(cost[1])
        for i in range(2,len(cost)):
            dp.append(min(dp[i-1],dp[i-2]) + cost[i])
        
        return min(dp[len(cost)-1], dp[len(cost)-2]) 

s = Solution()
test = [1,100,1,1,1,100,1,1,100,1]
r1=s.minCostClimbingStairs(test)
test1 = [10,15,20]
r2 = s.minCostClimbingStairs(test1)
print((r1,r2)) 