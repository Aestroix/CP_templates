# LENGTH OF LONGEST COMMON SUBSTRING
x = 'eekgeeks...geek'
y = 'geeks'
n = len(x)
m = len(y)
result = 0
def lcstr(x,y,n,m,cnt):
	if n==0 or m==0:
		return cnt
	if x[n-1] == y[m-1]:
		cnt = lcstr(x,y,n-1,m-1,cnt+1)
	else:
		cnt = max(cnt,lcstr(x,y,n,m-1,0),lcstr(x,y,n-1,m,0))
	return cnt
print('LENGTH OF LONGEST COMMON SUBSTRING IS:',lcstr(x,y,n,m,0))
