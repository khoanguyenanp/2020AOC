import sys
sys.path.insert(1, './input/')
import input

ops = {
		'+': lambda x, y: x + y,
		'-': lambda x, y: x - y
	}

def getAccBeforeRepeat(data):
	acc = 0

	i = 0
	while 0 <= i < len(data):
		if data[i]['execute'] > 0:
			i = -1
		else:
			op = data[i]['op']
			value = data[i]['value']
			data[i]['execute'] += 1
			if(data[i]['action'] == 'nop'):
				i +=1
			elif(data[i]['action'] == 'acc'):
				acc = ops[op](acc, value)
				i +=1
			elif(data[i]['action'] == 'jmp'):
				i = ops[op](i, value)
	return acc

def isValidInstruction(data):
	i=0
	valid=False
	while 0 <= i < len(data):
		if data[i]['execute'] > 0:
			i = -1
		else:
			op = data[i]['op']
			value = data[i]['value']
			data[i]['execute'] += 1
			if(data[i]['action'] == 'nop' or data[i]['action'] == 'acc'):
				i += 1
			elif(data[i]['action'] == 'jmp'):
				i = ops[op](i, value)
			else:
				i += 1
	if(i == len(data)): valid = True
	return valid

def getCorrectAcc(data):

	swap = {
		'nop': 'jmp',
		'jmp': 'nop'
	}
	i=0
	while i<len(data):
		instruction = data[i]
		if(instruction['action'] == 'nop' and instruction['value']==0):
			i +=1
		elif(instruction['action'] == 'nop' or instruction['action'] == 'jmp'):
			org_action = instruction['action']
			tmp_instruction = input.getDay8Input()
			tmp_instruction[i]['action'] = swap[org_action]
			if isValidInstruction(tmp_instruction):
				data[i]['action'] = swap[org_action]
				i = len(data)
			else:
				i +=1
		else:
			i +=1
	
	acc = getAccBeforeRepeat(data)
	return acc

res1 = getAccBeforeRepeat(input.getDay8Input())
print(res1)

res2 = getCorrectAcc(input.getDay8Input())
print(res2)