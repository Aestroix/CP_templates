#approach is to check if the sums from 0 to n//2 are possible to 
#make from the given list of numbers and minimize the 
# range-2*s1 when s1 is maximum
li = [10,11,2,3,4,5,6,7,9]
n = len(li)
dp = [[-1 for j in range(sum(li)+1)] for i in range(n+1)]
s = sum(li)
check = []
def knapsack(li,n,s):
	if s == 0:
		return 1
	elif n==0:
		return 0
	if dp[n][s] != -1:
		return dp[n][s]
	else:
		if li[n-1] <= s:
			dp[n][s] = knapsack(li,n-1,s-li[n-1]) or knapsack(li,n-1,s)
		else:
			dp[n][s] = knapsack(li,n-1,s)
		return dp[n][s]

for i in range(s//2 + 1):
	if knapsack(li,n,i) == 1:
		check.append(i)
print(s - 2*check[-1])







