# [string intro]

message = 'string'
print(message)

message3 = 'asdf \'asdf\' lasd'
message4 = 'Hello,\rthis is \'TWR\' TD school.'
print(message4)

message5 = 'Hello,\nthis is \'TWR\' TD school.'
print(message5)

file_path = 'D:\temp\twr\school'
print(file_path)

message6 = 'Hello, this is "TWR" TD school.'
print(message)

message = message6.upper()
print(message.upper())
print(message.lower())
print(message.replace('school', 'academy'))

print(message6.upper().replace('SCHOOL', 'academy'))

if 'TWR' in message:
	print(message.replace('TWR', 'twr'))

message1 = 'Hello.'
message2 = 'This is "TWR" TD school.'

message = message1 + " " + message2
print(message)

message = 'HOLA' + " " + message2
print(message1 *3)

name = 'Anna'
age = 6

message = message1 + ' ' + name + '. ' +message2 + str(age) + message3
print(message)

test_list = [1, 2, 3, 4, '5', '6', '7', '8']
print(test_list)

task_path = 'Z:/twr/sq0010/sh0010/lighting'
driver_path = task_path[:3]
print(driver_path)

if task_path[1] == ':':
	print("windows drive...")
