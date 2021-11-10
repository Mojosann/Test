# [list practice]

# find age>18
# name: age, location

over18_list = []
for location, name_age in data_01.items():
    for name, age in name_age.items():
        if age>18:
            over18_list.append([name, age, location])

# live in Taipei and age > 40
tai_people_list = []
for name, age, location in over18_list:
    if location == 'Taipei' and age > 40:
        print('%s: %s(Taipei)' % (name, str(age)))
        tai_people_list.append([name, age])

print(len(over18_list))
print(len(tai_people_list))

# data_02
# age > 20

over20_list = []
for location, gender_age_name in data_02.items():
    for info in gender_age_name:
        if info['age'] > 20:
            over20_list.append([info['name'], info['age'], location])

for name, age, location in over20_list:
    print('%s: %s(%s)' % (name, str(age), location))

# live in Taichung & age > 30
chung_people_list = []
for name, age, location in over20_list:
    if location == 'Taichung' and age > 30:
        print('%s: %s(Taichung)' % (name, str(age)))
        chung_people_list.append([name, age])

print(len(over20_list))
print(len(chung_people_list))

# get missing number
number_list = [1, 2, 3, 4, 6, 7, 9]
missing_list = []
for num in range(number_list[0], number_list[-1]):
    if num not in number_list:
        missing_list.append(num)
print(missing_list)