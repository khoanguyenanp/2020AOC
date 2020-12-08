import sys
sys.path.insert(1, './input/')
import input

puzzle = input.getDay7Input()

# Part 1
def getBagsCount(bags_puzzle, search='shiny gold'):
	count = 0
	for bag in bags_puzzle:
		bag_data = bags_puzzle[bag]
		if(isBagContain(bag_data, search)):
			count += 1
		else:
			for contain_bag in bag_data['contains']:
				if(isBagContain(bags_puzzle[contain_bag], search)):
					count +=1
					break

	return count

def isBagContain(bag_data, search='shiny_gold'):
	if search in bag_data['contains']: 
		return True
	else:
		for contain_bag in bag_data['contains']:
			if(isBagContain(puzzle[contain_bag], search)):
				return True
		return False

# Part 2
def getContainBagsCount(bag_puzzle, search='shiny gold'):
	count = 0
	bags_details = bag_puzzle[search]['details']
	
	for bag_color in bags_details:
		bag_count = int(bags_details[bag_color])
		count += int(bags_details[bag_color])
		contain_count = getContainBagsCount(bag_puzzle, bag_color)
		contain_count = bag_count * contain_count
		count += contain_count
	return count


# res1 = getBagsCount(puzzle)
# print(res1)
res2 = getContainBagsCount(puzzle)
print(res2)