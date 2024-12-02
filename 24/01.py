with open("inputs/input01.txt") as inputfile:
    data = inputfile.read().split('\n')

data = [d.split() for d in data]

left = sorted([int(a) for a, _ in data])
right = sorted([int(b) for _, b in data])

distance = 0
for i in range(len(left)):
    left_num = left[i]
    right_num = right[i]
    if left_num > right_num:
        distance += left_num - right_num
    else:
        distance += right_num - left_num

print(f"The distance is {distance}")
