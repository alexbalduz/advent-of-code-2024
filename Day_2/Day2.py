with open('Day_2/day2-Input.txt', 'r', encoding='utf-8') as file:
    sequence = []
    for line in file:
        info = line.strip().split()
        sequence.append(info)

def is_safe(sublist):
    is_sorted = all(int(sublist[i]) < int(sublist[i + 1]) for i in range(len(sublist) - 1)) or \
                all(int(sublist[i]) > int(sublist[i + 1]) for i in range(len(sublist) - 1))

    if not is_sorted:
        return False

    return all(1 <= abs(int(sublist[i]) - int(sublist[i + 1])) <= 3 for i in range(len(sublist) - 1))

# Part 1
safe_counter = 0

for sublist in sequence:
    if len(sublist) <= 1:
        safe_counter += 1
        continue

    if is_safe(sublist):
        safe_counter += 1

print("🐍 File: Day_2/Day2.py | Line: 20 | undefined ~ safe_counter",safe_counter)

# Part 2
safe_counter = 0

for sublist in sequence:
    if len(sublist) <= 1:
        safe_counter += 1
        continue

    if is_safe(sublist):
        safe_counter += 1
        continue

    for i in range(len(sublist)):
        modified_sublist = sublist[:i] + sublist[i + 1:]

        if is_safe(modified_sublist):
            safe_counter += 1
            break

print("🐍 File: Day_2/Day2.py | Line: 20 | undefined ~ safe_counter", safe_counter)
