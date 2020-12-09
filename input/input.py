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

# DAY 6
def getDay6Input():
	with open('./input/day6_input.txt', 'r') as f:
		lines = f.read().splitlines()
		lines.append('')
	res=[]
	group=[]
	for data in lines:
		if(data == ''):
			if(len(group)>0): res.append(group)
			group=[]
		else:
			group.append(data)
	return res

# DAY 7
def getDay7Input():
	with open('./input/day7_input.txt', 'r') as f:
		lines = f.read().splitlines()
	res={}
	bag={}
	for data in lines:
		bag = {}
		data = data.split('contain')
		bag_name = data[0].replace('bags', '').strip()
		bag = {
			'color': bag_name,
			'contains': [],
			'details': {}
		}
		contains = data[1].split(',')
		for contain in contains:
			if (contain.strip().replace('.','') == 'no other bags'):
				pass
			else:
				contain = contain.replace('bags.','').replace('bags','').replace('bag.', '').replace('bag','').strip()
				contain = contain.split(' ')
				count = contain[0]
				contain.remove(count)
				bag_color = ' '.join([str(elem) for elem in contain])
				bag['contains'].append(bag_color)
				bag['details'][bag_color] = count
		
		res[bag_name] = bag

	return res

# DAY 8 
def getDay8Input():
	with open('./input/day8_input.txt', 'r') as f:
		lines = f.read().splitlines()
	res = []
	for line in lines:
		instruction = {}
		line = line.split(' ')
		instruction = {
			'action': line[0],
			'value': int(line[1]),
			'execute': 0
		}
		res.append(instruction)
	return res

# DAY 9
def getDay9Input():
	with open('./input/day9_input.txt', 'r') as f:
		lines = f.read().splitlines()
	return list(map(int, lines))