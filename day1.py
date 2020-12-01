import numpy
import sys
sys.path.insert(1, './input/')
import input

expense = input.getDay1Input()

def convert(value):
	if isinstance(value, list): return value
	res = value.split("+")
	return list(map(int, res))

def reportRepair(expense, count=3, total=2020):
	# Turn string to array
	expenses = convert(expense)

	needs = list()
	res = list()
	# Get array of value needed for total
	for value in expenses:
		needs.append(total-value)

		if(count > 2):
			need_values = reportRepair(expense, count-1, total-value)
			if need_values: 
				need_values.append(value)
				res = need_values

	# Find the value needed
	if not res: res = list(set(expenses) & set(needs))

	return res

value = reportRepair(expense, 2)
value = numpy.prod(value)
print value