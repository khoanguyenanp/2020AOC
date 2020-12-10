import sys
sys.path.insert(1, './input/')
import input

def getAdapterCount(data):
	res = {
		'1_jolt': 0,
		'2_jolt': 0,
		'3_jolt': 0
	}
	current = data[0]
	i=1
	while i<len(data):
		value = data[i]
		if current+1==value:
			res['1_jolt'] += 1
		elif current+2==value:
			res['2_jolt'] += 1
		elif current+3==value:
			res['3_jolt'] += 1
		else:
			i=len(data)
			res = {}
		i+=1
		current = value
	return res

# res1 = getAdapterCount(input.getDay10Input())
# print(res1['1_jolt'] * res1['3_jolt'])


# Bad Attempt, run forever
def getComboCount(data):
	combo = {
		'0': [0]
	}
	
	current = 0
	# print(data)
	i = 0
	while i < len(data)-1:
		current = data[i]
		i+=1
		possible_value = findPossibleValue(data[i:], current)
		old_combo = findOldComboKey(current, combo)
		combo = deleteOldCombo(combo,old_combo)
		new_combo = createNewCombo(possible_value, old_combo)
		combo.update(new_combo)
	return combo

def findPossibleValue(data, number):
	i = 0
	target = number + 3
	res = []
	while i<len(data):
		if data[i] <= target:
			res.append(data[i])
			i+=1
		else:
			i = len(data)
	return res


def findOldComboKey(number, data):
	res = {}
	for key in data:
		if data[key][-1] == number:
			res[key] = data[key]
	return res

def deleteOldCombo(data, old_data):
	for key in old_data:
		del data[key]
	return data

def createNewCombo(value, combo):
	res = {}
	for number in value:
		for key in combo:
			new_key = key + str(number)
			new_combo = combo[key][0:]
			new_combo.append(number)
			res[new_key] = new_combo
	return res

# # Second Attempt
# def getComboCount2(data, combo):



res2 = getComboCount(input.getDay10Input())
print(len(res2))
# test= {'test':1, 'here':2}
# del test['test']
# del test['here']
# print test