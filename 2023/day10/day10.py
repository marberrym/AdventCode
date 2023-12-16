f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

directional_map = {
    "valid_ups": ["|", "7", "F"],
    "valid_lefts": ["-", "L", "F"],
    "valid_downs": ["|", "L", "J"],
    "valid_rights": ["-", "7", "J"]
}

def find_starting_point(grid):
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col == "S":
                return [row_idx, col_idx]
            
def get_surrounding_cells(grid, row, col):
    up_cell = grid[row - 1][col].strip() if row > 0 else None
    down_cell = grid[row + 1][col].strip()  if row < len(grid) - 1 else None
    left_cell = grid[row][col - 1].strip()  if col > 0 else None
    right_cell = grid[row][col + 1].strip()  if col < len(grid[0]) - 1 else None
    return [up_cell, down_cell, left_cell, right_cell]
            
def travel_pipe(grid, row_start, col_start):
    # Check above
    visited_cells = []
    starting_point = [row_start, col_start]
    current_row = row_start
    current_col = col_start
    step_count = 0

    
    while [current_row, current_col] not in visited_cells:
        visited_cells.append([current_row, current_col])
        step_count += 1
        up_cell, down_cell, left_cell, right_cell = get_surrounding_cells(grid, current_row, current_col)

        print(f"Visited {current_row}, {current_col}")

        print(F"left cell follows {left_cell}")
        print([current_row, current_col - 1] in visited_cells)
        print(left_cell in directional_map["valid_lefts"])

        if up_cell in directional_map["valid_ups"] and [current_row - 1, current_col] not in visited_cells: current_row -= 1
        elif down_cell in directional_map["valid_downs"] and [current_row + 1, current_col] not in visited_cells: current_row += 1
        elif left_cell in directional_map["valid_lefts"] and [current_row, current_col - 1] not in visited_cells: current_col -= 1
        elif right_cell in directional_map["valid_rights"] and [current_row, current_col + 1] not in visited_cells: current_col += 1

        print(f"headed to {current_row}, {current_col}")
    
    for line in grid:
        print(line)

    print("Step count... ", step_count)
    print("Step count / 2...", int(step_count / 2))

def main(input):
    grid = [list(x) for x in input]
    row_start, col_start = find_starting_point(grid)

    print("Starting point is... ", row_start, col_start)

    travel_pipe(grid, row_start, col_start)

main(test)
