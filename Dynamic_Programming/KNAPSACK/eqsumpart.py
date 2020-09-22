# TD APPROACH FOR CHECKING FOR EQUAL SUM PARTITION
dp = [[-1 for i in range(23)] for j in range(5)]
def knapsack(li,sumi,sumsofar,n):
	if sumsofar == (sumi-sumsofar):
		return 1
	if n < 1:
		return 0
	if dp[n][sumsofar] != -1:
		return dp[n][sumsofar]
	else:
		dp[n][sumsofar] = (knapsack(li,sumi,sumsofar+li[n-1],n-1) 
				or knapsack(li,sumi,sumsofar,n-1))
		return dp[n][sumsofar]


li = [1,5,11,5]
if sum(li)&1: #in case of odd there is no way of dividing
	print("no")
else:
	if(knapsack(li,sum(li),0,4)):
		print('yes')
	else:
		print('no')



# ANOTHER METHOD IS THAT YOU CONVERT IT INTO TARGET SUM PARTITION OF 
# THE TARGET SUM == HALF THE VALUE OF TOTAL SUM
