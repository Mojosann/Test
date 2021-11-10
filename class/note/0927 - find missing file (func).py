# [Find missing exr file]

def find_missing_file(input_list):
    num_list = []
    missing_list = []

    for item in input_list:
        num_list.append(int(item.split('.')[1]))

    num_list.sort()
    for num in range(num_list[0], num_list[-1]+1):
        if num not in num_list:
            missing_list.append(num)
            #print(num, 'missing!')

    return missing_list