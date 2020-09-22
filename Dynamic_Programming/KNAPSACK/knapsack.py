# To IDENTIFY THE DP PROBLEM IT HAS TWO PARTS:
# 1.) CHOICE       2.) OPTIMAL SOULUTION REQD.
# PARENT OF DP IS RECURSION 


# FOR A KNAPSACK: ITEMS HAVE A WEIGHT AND VALUE AND A FIXED BOUND IS GIVEN ON THE STORAGE OF THE BAG.
# IDENTIFYING THE MAX PROFIT OR MINIMUM SOMETHING...

#CHOICE DIAGRAM>>>>>>>>>>>>>
# WT:     1 3 4 5 
# VAL:    1 4 5 7
# W:      7

# Global declaration of dp matrix because here two parameters are changing: n and w
#SUPPOSE N AND W LIE IN THE RANGE 100 AND 100 RESPECTIVELY 



# IT IS KNOWN AS THE TOP-DOWN APPROACH


wt = [2,6,8,4,12,20]
val = [100,200,500,2900,10,1]
n = len(wt)
capacity = 10 # of knapsack 
dp = [[-1 for j in range(capacity+1)] for i in range(n+1)]
def knapsack(wt,val,w,n):
	if w == 0 or n == 0:
		return 0
	if dp[n][w] != -1:
		return dp[n][w]
	else:
		if wt[n-1] <= w:
			dp[n][w] = max( val[n-1] + knapsack(wt,val,w-wt[n-1], n-1), knapsack(wt,val,w,n-1))
			return dp[n][w]
		else:
			dp[n][w] = knapsack(wt,val,w,n-1)
			return dp[n][w]




print(knapsack(wt,val,capacity,n))

