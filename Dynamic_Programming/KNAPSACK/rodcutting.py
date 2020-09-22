# cutting the rod into pieces such that the profit is maximum
# UNBOUNDED KNAPSACK coz we can repeat the pieces of rod as
# many times we want to








size = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]
n = len(size)
w = len(size) # THE SIZE OF THE ROD IS FIXED AT MAX LEN
dp = [[-1 for j in range(w+1)] for i in range(n+1)]
def knapsack(size,price,w,n):
	if w == 0 or n == 0: # if all the rod is consumed or size become empty  
		return 0 		 # while reached to end by any of the means
	if dp[n][w] != -1:
		return dp[n][w]
	else:
		if size[n-1] <= w:
			dp[n][w] = max(price[n-1] + knapsack(size,price,w-size[n-1],n), knapsack(size,price,w,n-1)) 
			''' unbounded knapsack case when if it is possible to use the element then it is not processed and if you have decided not to 
			take it then it is processed'''
		else:
			dp[n][w] = knapsack(size,price,w,n-1)
		return dp[n][w]
print(*size)
print(*price)	
print('The maximum profit is: ', knapsack(size,price,w,n))