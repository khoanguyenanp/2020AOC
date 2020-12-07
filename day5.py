import numpy
import sys
sys.path.insert(1, './input/')
import input

boarding_passes = input.getDay5Input()

def transformSeatId(boarding_pass):
	dic = {
		'B': 'upper',
		'F': 'lower',
		'R': 'upper',
		'L': 'lower'
	}

	i =	0
	rows = [0,127]
	columns = [0,7]
	while i<7:
		location = dic[boarding_pass[i]]
		rows = getRange(location, rows)
		i+=1 
	row = rows[0]
	while i<len(boarding_pass):
		location = dic[boarding_pass[i]]
		columns = getRange(location, columns)
		i+=1
	columns = columns[0]

	seat_id = row * 8 + columns

	return seat_id

def getRange(location,data):
	data = range(data[0],data[1]+1)
	half = len(data)/2

	if(location == 'upper'):
		start = data[half]
		end_index = len(data)-1
		end = data[end_index]
	elif(location == 'lower'):
		start = data[0]
		end_index = half-1
		end = data[end_index]
	return [start,end]


def getSeatIdList(boarding_passes):
	seat_ids = list()

	for data in boarding_passes:
		seat_ids.append(transformSeatId(data))

	return sorted(seat_ids, reverse = True)

def getMissingSeatId(boarding_passes):
	seat_ids = getSeatIdList(boarding_passes)
	i=0
	while i<len(seat_ids):
		if((i+1 < len(seat_ids)) and ((seat_ids[i]-2) == seat_ids[i+1])):
			seat_id = seat_ids[i] - 1
			i = len(seat_ids)
		i+=1
	return seat_id

res1 = getSeatIdList(boarding_passes)
print(res1[0])
res2 = getMissingSeatId(boarding_passes)
print(res2)