def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def calc_part1(list1, list2):
    distance = 0
    for left, right in zip(list1, list2):
        distance += abs(left - right)
    return distance

def calc_part2(list1, list2):
    sim = 0
    count = 0
    for i in list1:
        for j in list2:
            if i == j:
                count += 1
        sim += i * count
        count = 0
    return sim

file_data = get_file_data("Day1Input.txt")
left_list = []
right_list = []

for x in file_data:
    split_num = x.split("   ")
    left_list.append(int(split_num[0]))
    right_list.append(int(split_num[1]))

left_list.sort()
right_list.sort()

print(calc_part1(left_list, right_list))
print(calc_part2(left_list, right_list))