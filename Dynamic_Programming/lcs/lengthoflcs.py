# FINDING THE LENGTH OF LONGEST COMMON SUBSTRING
# GIVEN TWO STRINGS

x = 'i am karmanya'
y = 'abeghr'
n, m = len(x), len(y)
dp = [[-1 for j in range(m+1)] for i in range(n+1)]
def lcs(x,y,n,m):
	if n == 0 or m == 0:
		return 0
	if dp[n][m] != -1:
		return dp[n][m]
	else:
		if x[n-1] != y[m-1]:
			dp[n][m] = max(lcs(x,y,n-1,m), lcs(x,y,n,m-1))
		else:
			dp[n][m] = 1 + lcs(x,y,n-1,m-1)
		return dp[n][m]
length_of_longest_common_substring = lcs(x,y,n,m)
print('the answer is: ', length_of_longest_common_substring)
