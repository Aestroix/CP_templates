dp = [[-1 for i in range(12)] for j in range(6)]
def knapsack(li,s,n):
	if s == 0: #when the sum is 0 the subset null is the answer
		dp[n][s] = 1
		return 1
	elif n == 0 and s != 0:
		dp[n][s] = 0 #when the size is zero never possible to find the sum
		return 0
	else:
		if dp[n][s] != -1:
			return dp[n][s]
		else:
			if li[n-1] <= s:
				dp[n][s] = dp[n-1][s-li[n-1]] or dp[n-1][s]
			else:
				dp[n][s] = dp[n-1][s] #element big not taken
			return dp[n][s]

li = [2,3,7,8,10]
target_sum_present = 11
if knapsack(li,target_sum_present,5):
	print('yes')
else:
	print('no')		