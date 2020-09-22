def pref(li):
	'''
	returns a prefix sum array of given array
	example:

	if given a list: [1,2,3,4]
	returns:
					 [0,1,3,6,10]

	This algorithm is one of the most basic ones which is very useful for problems
	like LAZY-SUM, feel free to search tha too :^))
	'''
	pref_sum = [0]
	for i in li:
		pref_sum.append(pref_sum[-1] + i)
	return pref_sum

li = list(map(int,input().split())) # input a list of space separated integers
pref_sum_array = pref(li)
print(pref_sum_array)