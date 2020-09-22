# target sum to make from the given numbers by changing the sign
# of numbers. Find the number of ways

li = [1,1,1,1,1]
target_sum = 3
n = len(li)
s = sum(li)
dp = [[-1 for j in range(s+1)] for i in range(n+1)]
def knapsack(li,sumi,s,n):
	if s == sumi:
		return 1
	if s < sumi:
		return 0
	if n == 0:
		return 0
	if dp[n][s] != -1:
		return dp[n][s]
	else:
		dp[n][s] = knapsack(li,sumi,s-2*li[n-1],n-1) + knapsack(li,sumi,s,n-1)
		return dp[n][s]
print(knapsack(li,target_sum,s,n))
