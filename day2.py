import sys
sys.path.insert(1, './input/')
import input

passwords = input.getDay2Input()

def countValidPassword1(data):
	valid = 0
	for value in data:
		# Ex: {rule:[1,7], req: j, password: fhjsgd}
		req_char = value['req']
		count = value['password'].count(req_char)
		if(count >= value['rule'][0] and count <= value['rule'][1]): valid += 1

	return valid

def countValidPassword2(data):
	valid = 0
	for value in data:
		# Ex: {rule:[1,7], req: j, password: fhjsgd}
		count = 0
		req_char = value['req']
		password = value['password']
		first_pos = value['rule'][0] - 1
		second_pos = value['rule'][1] - 1
		if(password[first_pos] == req_char): count += 1
		if(password[second_pos] == req_char): count += 1
		if(count == 1): valid += 1
	return valid

valid_password1 = countValidPassword1(passwords)
print(valid_password1)

valid_password2 = countValidPassword2(passwords)
print(valid_password2)