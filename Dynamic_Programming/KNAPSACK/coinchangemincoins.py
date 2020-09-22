# FINDING THE MAXIMUM NUMBER OF coins TO FIND THE CHANGE OF THE COINS
# infinite number of coins are available
from sys import *
li = [1,3,4] #coin denomination
val = 6
n = len(li)
dp = [[-1 for j in range(val+1)] for i in range(n+1)]

def fn(li,n,val):
	if n == 0:
		return maxsize  #to find the minimum coins use maxsize to store the 
	if val == 0:		#upper limit reached when the list of coins become empty
		return 0
	if dp[n][val] != -1:
		return dp[n][val]
	else:
		if li[n-1] <= val:
			dp[n][val] = min(fn(li,n,val-li[n-1])+1,  fn(li,n-1,val))
		else:
			dp[n][val] = fn(li,n-1,val)
		return dp[n][val]

print('The min number of coins to make the change are: ',fn(li,n,val))

 


