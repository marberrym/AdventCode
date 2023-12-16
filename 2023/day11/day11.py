f = open('input.txt', 'r');
puzzle_input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();


def check_column(galaxy_grid, col_idx):
    should_expand = True
    for row in galaxy_grid:
        if row[col_idx] == '.':
            continue
        else:
            should_expand = False
    return should_expand


def generate_row(num):
    row = []
    for _ in range(num): row.append('.')
    return row


def expand_galaxy(galaxy_grid):
    grid = galaxy_grid
    rows_to_insert = []
    cols_to_insert = []

    for row_idx, row in enumerate(grid):
        if all([x == '.' for x in row]): rows_to_insert.append(row_idx)

    for col_idx, col in enumerate(grid[0]):
        if col == '.':
            if check_column(grid, col_idx):
                cols_to_insert.append(col_idx)

    for idx in rows_to_insert:
        grid.insert(idx, generate_row(len(grid[0])))

    for idx in cols_to_insert:
        for row in grid:
            row.insert(idx, '.')

    return grid


def find_all_galaxy_coords(grid):
    coords = []
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col == "#":
                coords.append([row_idx, col_idx])
    return coords


def check_point(start, end):

    if (abs(end[0] - start[0]) == 1 and abs(end[1] - start[1]) == 0) or (end[0] == start[0] and end[1] == start[1

        or end[0] == start[0]) and (abs(end[1] - start[1]) == 1 or end[1] == start[1]):
    if (abs(end[0] - start[0]) == 1 or end[0] == start[0]) and (abs(end[1] - start[1]) == 1 or end[1] == start[1]):
        return True
    else:
        return False


def find_path(start, end):
    current = start.copy()
    steps = 0
    last_step_was_vertical = True

    while not check_point(current, end):
        print("CURRENT", current)
        print(check_point(current, end))

        vertical_diff = abs(current[0] - end[0])
        horizontal_diff = abs(current[1] - end[1])
        if vertical_diff > 1:
            if current[0] < end[0]:
                current[0] += 1
                steps += 1
            if current[0] > end[0]:
                current[0] -= 1
                steps += 1
            last_step_was_vertical = False
        elif horizontal_diff > 1:
            if current[1] < end[1]:
                current[1] += 1
                steps += 1
            if current[1] > end[1]:
                current[1] -= 1
                steps += 1
            last_step_was_vertical = True

    return steps


def get_coords_without_start(coords, start, completed_coords):
    return list(filter(lambda x: x != start and x not in completed_coords, coords))


def find_step_count_for_coord(start_coord, goal_coords):
    steps = 0
    for goal_coord in goal_coords:
        step_count = find_path(start_coord, goal_coord)
        print("Step count is...", step_count)
        steps += step_count
    return steps


def generate_paths(coords):
    paths = []
    completed_coords = []
    for coord in coords:
        paths.append({
            "start": coord,
            "goals": get_coords_without_start(coords, coord, completed_coords)
        })
        completed_coords.append(coord)

    return paths


def find_paths(coords):
    paths = generate_paths(coords)
    total_steps = 0

    for coord in paths:
        total_steps += find_step_count_for_coord(coord["start"], coord["goals"])

    print(total_steps)


def main(data):
    galaxy_grid = [list(x) for x in data]

    expanded_galaxy_grid = expand_galaxy(galaxy_grid)
    galaxy_coords = find_all_galaxy_coords(expanded_galaxy_grid)

    paths = find_paths(galaxy_coords)
    for row in expanded_galaxy_grid:
        print(row)

    print(galaxy_coords)


main(test)
