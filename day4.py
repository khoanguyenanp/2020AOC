import sys
import re
sys.path.insert(1, './input/')
import input

batch = input.getDay4Input()
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
byr = [1920,2002]
iyr = [2010,2020]
eyr = [2020,2030]
hgt_cm = [150,193]
hgt_in = [59,76]
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def isValidHgt(hgt):
	if 'cm' in hgt:
		rule = hgt_cm
		hgt = int(hgt.replace('cm',''))
	elif 'in' in hgt:
		rule = hgt_in
		hgt = int(hgt.replace('in',''))
	else:
		return False

	if (rule[0] <= hgt <= rule[1]): return True
	return False
	
def isValidHcl(hcl):
	if not hcl[0] == '#': return False
	if not len(hcl) == 7: return False
	hcl = hcl.replace('#','')
	ok = "0123456789abcdef"
	if not (all(c in ok for c in hcl)): return False
	return True

def getValidPassportCount(bactch, strict=False):
	valid = 0
	for passport in bactch:
		if strict:
			if not (all(elem in passport['fields']  for elem in req_fields)): continue
			if not (byr[0] <= int(passport['byr']) <= byr[1]): continue
			if not (iyr[0] <= int(passport['iyr']) <= iyr[1]): continue
			if not (eyr[0] <= int(passport['eyr']) <= eyr[1]): continue
			if not isValidHgt(passport['hgt']): continue
			if not isValidHcl(passport['hcl']): continue
			if not (len(passport['pid']) == 9 and passport['pid'].isdigit()): continue
			if not passport['ecl'] in ecl: continue
			valid += 1
		else :
			if (all(elem in passport['fields']  for elem in req_fields)): valid += 1
	return valid

res1 = getValidPassportCount(batch)
print(res1)

res2 = getValidPassportCount(batch, True)
print(res2)