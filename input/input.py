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