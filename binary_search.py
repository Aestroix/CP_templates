def binary_search(li, val, lb, ub): 
	'''
	li: stores the list of numbers to search upon in ascending order
	val: value to be searched for
	lb: starting index
	ub: ending index

	This function searches for the val in li and return
	0: if the value is not present
	1: if the value is present
	'''
	ans = 0
	while(lb <= ub):
		mid = (lb+ub)//2
		#print(mid, li[mid])
		if li[mid] > val:
			ub = mid-1
		elif val > li[mid]:
			lb = mid + 1
		else:
			ans = 1
			break
	return ans

li = list(map(int,input().split())) # enter the list of numbers
li.sort() #sorting the list
val = int(input("Enter the value to be searched for:"))
if binary_search(li,val,0,len(li)-1):
	print("the entered value is present in the list of numbers.")
else:
	print("The entered value is not present in the list of numbers.")

'''
The code works with the time complexity O(log(n)) where n is the length of list

'''