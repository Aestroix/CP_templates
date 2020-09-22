# FINDING THE MAXIMUM NUMBER OF WAYS TO FIND THE CHANGE OF THE COINS
# infinite number of coins are available

li = [1,2,3] #coin denomination
val = 4
n = len(li)
dp = [[-1 for j in range(val+1)] for i in range(n+1)]

def fn(li,n,val):
	if val == 0:
		return 1
	if n == 0:
		return 0
	if dp[n][val] != -1:
		return dp[n][val]
	else:
		if li[n-1] <= val:
			dp[n][val] = fn(li,n,val-li[n-1]) + fn(li,n-1,val)
		else:
			dp[n][val] = fn(li,n-1,val)
		return dp[n][val]

print('The number of ways to make the change are: ',fn(li,n,val))

 


