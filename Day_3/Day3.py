import re

with open('Day_3/day3-Input.txt') as file:
    puzzle = file.readlines()
    puzzle = "".join(puzzle).replace('\n', "")

# Part 1

pattern_mul = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern_mul, puzzle)

total_sum1 = 0

for match in matches:
    total_sum1 += int(match[0]) * int(match[1])

print("🐍 File: Day_3/Day3.py | Line: 17 | undefined ~ sum",total_sum1)

# Part 2

patternDisable = r"don't\(\).*?do\(\)"
puzzle = re.sub(patternDisable, "", puzzle)
matches = re.findall(pattern_mul, puzzle)

total_sum2 = 0

for match in matches:
    total_sum2 += int(match[0]) * int(match[1])

print("🐍 File: Day_3/Day3.py | Line: 29 | undefined ~ total_sum2",total_sum2)