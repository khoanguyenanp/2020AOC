import sys
sys.path.insert(1, './input/')
import input

def isNumberValid(number, checklist):
	i=0

	list_len = len(checklist)
	valid = False
	while i<list_len:
		need_value = number - checklist[i]
		i += 1
		if need_value == checklist[i-1]:
			continue
		elif need_value in checklist[i:list_len]:
			valid = True
			i = list_len

	return valid

def getInvalidNumber(checklist, count=25):
	i=count
	value = 0
	while i<len(checklist):
		start = i - count
		value = checklist[i]
		if isNumberValid(value, checklist[start:i]):
			i+=1
		else:
			i=len(checklist)
	return value

def getContiguousSet(checklist, count=25):
	number = getInvalidNumber(checklist, count)
	i = 0
	list_len = len(checklist)
	contiguous_set = []
	while i < list_len:
		finish = False
		contiguous_set = []
		sub_list = checklist[i:list_len]
		for value in sub_list:
			contiguous_set.append(value)
			total = sum(contiguous_set)
			if(total == number):
				finish = True
				break
			elif(total > number):
				break
		if finish:
			i = list_len
		else:
			i +=1
	return contiguous_set

def findEncryptionWeakness(checklist, count = 25):
	contiguous_set = getContiguousSet(checklist, count)
	contiguous_set = sorted(contiguous_set)
	min_val = contiguous_set[0]
	max_val = contiguous_set[(len(contiguous_set)-1)]

	return min_val + max_val
res1 = getInvalidNumber(input.getDay9Input(), 25)
print(res1)
res2 = findEncryptionWeakness(input.getDay9Input(),25)
print(res2)