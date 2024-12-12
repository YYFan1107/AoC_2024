def get_file_data(file_name):
    f = open(file_name)
    data = []
    for read in f:
        data.append(read.rstrip())
    return data

def check_levels(array):
    increasing = True
    decreasing = True
    for i in range(len(array) - 1):
        if array[i + 1] <= array[i]:
            increasing = False
        elif array[i + 1] >= array[i]:
            decreasing = False
    return increasing or decreasing

def check_difference(array):
    for i in range(len(array) - 1):
        differ = abs(array[i] - array[i + 1])
        if differ < 1 or differ > 3:
            return False
    return True

def calc_part1(array):
    safe = 0
    for nums in array:
        if check_levels(nums) and check_difference(nums):
            safe += 1
    return safe

def calc_part2(array):
    safe = 0
    for lists in array:
        if check_levels(lists) and check_difference(lists):
            safe += 1
            continue
        for i in range(len(lists)):
            new_list = lists.copy()
            new_list.pop(i)
            if check_levels(new_list) and check_difference(new_list):
                safe += 1
                break
    return safe

file_data = get_file_data("Day2Input.txt")
report = []

for x in file_data:
    split_num = x.split(" ")
    line = []
    for i in split_num:
        line.append(int(i))
    report.append(line)

print(calc_part1(report))
print(calc_part2(report))