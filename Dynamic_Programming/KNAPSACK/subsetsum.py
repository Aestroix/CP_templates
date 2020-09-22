# BOTTOM-UP WITH MEMOIZATION
# TRY MAKING THE DP ARRAY WITH CONSIDERATION THAT SUM AND LEN START FROM 0

# CHECK IF THE SUBSET IS PRESENT HAVING THE TARGETED SUM
dp = [[-1 for j in range(12)] for i in range(6)]
def knapsack(li,s,n):
	for j in range(s+1):
		dp[0][j] = 0 # when there is no element is the array to make the sum
	for i in range(n+1):
		dp[i][0] = 1 # s is 0 will always be yes null subarray selection
	for i in range(1,n+1):
		for j in range(1,s+1):
			if li[i-1] <= j:
				dp[i][j] = dp[i-1][j - li[i-1]] or dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j] 
	for i in range(n):
		print(*dp[i])
	return dp[n][s]

li = [2,3,7,8,10]
target_sum_present = 11
if knapsack(li,target_sum_present,5):
	print('yes')
else:
	print('no')