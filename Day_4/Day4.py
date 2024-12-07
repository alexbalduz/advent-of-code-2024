with open('Day_4/day4-Input.txt', 'r') as file:
    puzzle_input = file.read().strip().splitlines()
    puzzle = [list(row) for row in puzzle_input]

# Part 1

def word_search2(grid):
    keyword = "XMAS"
    target_length = len(keyword)
    counter = 0
    rows = len(grid)
    cols = len(grid[0])
    def is_valid_direction(row, col, dr, dc):
        for i in range(target_length):
            r = row + i * dr
            c = col + i * dc
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != keyword[i]:
                return False
        return True
    for row in range(rows):
        for col in range(cols):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dr, dc in directions:
                if is_valid_direction(row, col, dr, dc):
                    counter += 1
    return counter

total = word_search2(puzzle)
print("🐍 File: Day_4/Day4.py | Line: 29 | undefined ~ total",total)

# Part 2

def word_search2(grid):
    counter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == 'A':
                diag_1 = f"{grid[row-1][col-1]}{grid[row+1][col+1]}"
                diag_2 = f"{grid[row-1][col+1]}{grid[row+1][col-1]}"

                if diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]:
                    counter += 1

    return counter


total = word_search2(puzzle)
print("🐍 File: Day_4/Day4.py | Line: 51 | undefined ~ total",total)