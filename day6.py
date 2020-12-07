import sys
sys.path.insert(1, './input/')
import input

answers = input.getDay6Input()

# helper
def deDup(string):
	res = ''
	for char in string:
		if not char in res: res += char
	return res

# Part 1
def getYesCountByGroup(group):
	answer = ''.join([str(elem) for elem in group])
	answer = deDup(answer)
	return len(answer)

def getTotalYesCount(answers):
	total = 0
	for value in answers:
		count = getYesCountByGroup(value)
		total += count
	
	return total

# Part 2
def getYesCountByGroup2(group):
	people = len(group)
	people_answers = {}
	count = 0
	for answer in group:
		answer = deDup(answer)
		for char in answer:
			if char in people_answers:
				people_answers[char] += 1
			else:
				people_answers[char] = 1
	for key in people_answers:
		if(people_answers[key] == people): count += 1

	return count


def getTotalYesCount2(answers):
	total = 0
	for value in answers:
		count = getYesCountByGroup2(value)
		total += count
	
	return total

res1 = getTotalYesCount(answers)
print(res1)

res2 = getTotalYesCount2(answers)
print(res2)