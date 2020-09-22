#IN THE BOTTOM UP APPROACH THE BASE CONDITION IS CHANGED TO 
#THE INITIALISATION PROCESS IN DP TABLE 
# THE RECURSIVE FUNCTION CALL IS REPLACESD BY DIRECTLY ACCESSING THE 
# ELEMTNS OF THE DP TABLE

# IT IS KN0OW AS THE BOTTOM UP APPROACH


def knapsack(wt,val,w,n):
	dp = [[-1 for i in range(w+1)] for j in range(n+1)]
	for i in range(n+1):
		dp[i][0] = 0
	for j in range(w+1):
		dp[0][j] = 0   # the initialisation
	for i in range(1,n+1):
		for j in range(1,w+1):
			if wt[i-1] <= j:
				dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
			else:
				dp[i][j] = dp[i-1][j]
	for i in range(n+1):
		print(*dp[i])
	return dp[n][w]



wt = [2,6,8,4]
val = [500,2900,10,1]
capacity = 10
print(knapsack(wt,val,capacity,len(wt)))