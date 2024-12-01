with open('Day_1/day1-Input.txt', 'r', encoding='utf-8') as file:
    column1 = []
    column2 = []

    for line in file:
        info = line.strip().split()
        if len(info) >= 2:
            column1.append(info[0])
            column2.append(info[1])

# Part 1
sortedColumn1 = []
sortedColumn2 = []
sortedColumn1 = sorted(column1)
sortedColumn2 = sorted(column2)

distance = 0

for i in range(len(sortedColumn1)):
    distance += abs(int(sortedColumn1[i]) - int(sortedColumn2[i]))

print("🐍 File: Day_1/Day1.py | Line: 21 | undefined ~ distance",distance)

# Part 2
similarity_score = 0

for number in sortedColumn1:
    count = sortedColumn2.count(number)
    similarity_score += int(number) * count

print("🐍 File: Day_1/Day1.py | Line: 29 | undefined ~ similarity_score",similarity_score)