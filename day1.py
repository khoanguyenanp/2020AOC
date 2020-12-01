import numpy
import sys
sys.path.insert(1, './input/')
import input

expenses = input.getDay1Input()

def reportRepair(expenses, count=3, total=2020):
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

value = reportRepair(expenses, 2)
value = numpy.prod(value)
print value