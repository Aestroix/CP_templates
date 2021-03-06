def lower_bound(li, num): 
	'''
	RETURNS AN INDEX IN THE SORTED ARRAY WHERE THE ELEMENT IS NOT LESS THAN
	THE GIVEN NUMBER
	'''
	answer = -1 # return -1 if all the elements are less than the number
	start = 0
	end = len(li)-1

	while(start <= end):
		middle = (end+start)//2
		if li[middle] >= num:
			answer = middle
			end = middle - 1
		else:
			start = middle + 1
	return answer 

li = list(map(int,input().split()))
li.sort() #sorted array is must
val = int(input("Enter the number:"))
ind = lower_bound(li,val)
print(ind)