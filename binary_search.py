import time

def binary_search(lst, target):
	if len(lst) == 1 and target != lst[0]:
		return -1
	else:
		i = len(lst) // 2
		if target < lst[i]:
			#print(i)
			i = binary_search(lst[:i], target)
		elif target > lst[i]:
			#print(i)
			i = binary_search(lst[i:], target)
		elif target == lst[i]:
			#print(i)
			return i
		else:
			return -1
		return i


if __name__ == "__main__":
	lst = [1,3,4,5,6,7,8,9,10]
	target = 2
	print(binary_search(lst, target))

search_start = time.time()
call_search_function = binary_search(lst, target)
search_stop = time.time()
search_running_time = search_stop - search_start