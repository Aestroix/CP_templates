# COUNT OF SUNSETS HAVING THE TARGET SUM
# TD APPROACH

def knapsack(li,ts,n,s,dp):
	if s == ts:
		dp[n][s] = 1
		return 1
	if n == 0 and ts!= 0:
		dp[n][s] = 0
		return 0
	if dp[n][s] != -1:
		return dp[n][s]
	else:
		if li[n-1] <= ts:
			dp[n][s] = knapsack(li,ts,n-1,s + li[n-1],dp) + knapsack(li,ts,n-1,s,dp)
		else:
			dp[n][s] = knapsack(li,ts,n-1,s,dp)
		return dp[n][s]





li = [2,3,5,6,8,10]
n = 6
targetsum = 10
dp = [[-1 for j in range(sum(li)+1)] for i in range(len(li)+1)]
print(knapsack(li,targetsum,n,0,dp))