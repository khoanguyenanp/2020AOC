import sys
sys.path.insert(1, './input/')
import input

geo_map = input.getDay3Input()
slope1 = [[3,1]]
slope2 = [[1,1], [3,1], [5,1], [7,1], [1,2]]
# print(geo_map)

def reMap(geo_map):
	res = []
	for row in geo_map:
		row_data = row + row
		res.append(row_data)
	return res

def countTree(geo_map, slope):
	cur_long = 0
	cur_lat = 0
	height = len(geo_map)
	width = len(geo_map[0])
	count = 0

	while cur_long < height:
		cur_lat += slope[0]
		cur_long += slope[1]
		if(cur_lat >= width):
			geo_map = reMap(geo_map)
			width = len(geo_map[0])
		if(cur_long < height and geo_map[cur_long][cur_lat] == "#"): count += 1

	return count

def getTreeProd(geo_map, slope_list):
	res = 1
	for slope in slope_list:
		tree = countTree(geo_map, slope)
		res = res * tree
	
	return res

res1 = getTreeProd(geo_map,slope1)
print(res1)

res2 = getTreeProd(geo_map, slope2)
print(res2)