# DAY 1
def transform(value):
    res = value.replace("\n", '')
    return int(res)

def getDay1Input():
    with open('./input/day1_input.txt', 'r') as f:
        lines = f.readlines()
    return list(map(transform, lines))


# DAY 2
def transformDay2Input(value):
	value = value.split(' ')
	rule = value[0].split('-')
	min_count = int(rule[0])
	max_count = int(rule[1])
	res = {
		'rule': [int(rule[0]), int(rule[1])],
		'req': value[1].replace(':',''),
		'password': value[2]
	}
	return res

def getDay2Input():
	with open('./input/day2_input.txt', 'r') as f:
		lines = f.read().splitlines()
	return list(map(transformDay2Input, lines))

# DAY 3
def getDay3Input():
	with open('./input/day3_input.txt', 'r') as f:
		lines = f.read().splitlines()
	return list(lines)

# DAY 4
def getDay4Input():
	with open('./input/day4_input.txt', 'r') as f:
		lines = f.read().splitlines()
		lines.append('')
	res=[]
	passport={'fields':[]}
	for data in lines:
		if(data == ''):
			res.append(passport)
			passport={'fields':[]}
			continue
		else:
			fields = data.split(' ')
			for field in fields:
				info = field.split(':')
				passport[info[0]] = info[1]
				passport['fields'].append(info[0])
	return res

# DAY 5
def getDay5Input():	
	with open('./input/day5_input.txt', 'r') as f:
		lines = f.read().splitlines()
	return list(lines)