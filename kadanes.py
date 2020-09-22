def kadane(li): 
	'''
	maximum sum contiguous subarray

	returns the maximum sum of contiguous subarray

	subarray is obtained by deleting some elements from the start and the end
	'''
	sum_so_far = 0
	current_sum = 0
	for elem in li:
		current_sum += elem
		if current_sum < 0:
			current_sum = 0
		else:
			sum_so_far = max(sum_so_far,current_sum)
	return sum_so_far

li = list(map(int,input().split())) #enter space separated numbers
max_sum_subarray = kadane(li)
print(max_sum_subarray)