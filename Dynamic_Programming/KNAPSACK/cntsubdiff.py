#COUNTING THE NUMBER OF SUBSETS HAVING THE GIVEN DIFFERENCE
'''
approach is tha when I prepared the array havving the possible 
subset sums and now, I will count the sums making the given difference
'''

li = [10,11,2,3,4,5,6,7,2]
n = len(li)
dp = [[-1 for j in range(sum(li)+1)] for i in range(n+1)]
s = sum(li)
check_diff = 2
check = {}
def knapsack(li,s,n):
	if s == 0:
		return 1
	if n == 0:
		return 0
	if dp[n][s] != -1:
		return dp[n][s]
	else:
		if li[n-1] <= s:
			dp[n][s] = knapsack(li,s-li[n-1],n-1) + knapsack(li,s,n-1)
		else:
			dp[n][s] = knapsack(li,s,n-1)
		return dp[n][s]
cnt = 0
ans = 0
for i in range(s//2+1):
	cnt = knapsack(li,i,n)
	if cnt:
		check.setdefault(i,cnt)
		#print(s,check_diff,2*i,check[i])
		if s - 2*i == check_diff:
			ans += check[i]
print(check)
print(ans)