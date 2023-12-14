f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();


def check_column(galaxy_grid, col_idx):
    should_expand = True
    for row in galaxy_grid:
        if row[col_idx] == '.': continue
        else: should_expand = False
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

def find_path(start, end):
    current = start
    steps = 0

    while current != end:
        if current[0] < end[0]:
            current[0] += 1
            steps += 1
        if current[0] > end[0]:
            current[0] -= 1
            steps += 1
        if current[1] < end[1]:
            current[1] += 1
            steps += 1
        if current[1] > end[1]:
            current[1] += 1
            steps += 1
    
    return steps


def find_paths(coords):
    paths = {}
    completed_coords = []
    coords_clone = coords
    for coord in coords:
        print("START WITH...", coord)
        coords_without_start_point = filter(lambda x: x != coord and x not in completed_coords, coords_clone)
        print("COORDS WITHOUT START...", list(coords_without_start_point))
        for goal_coord in list(coords_without_start_point):
            print(goal_coord)
            steps = find_path(coord, goal_coord)
            key = f"{coord[0]},{coord[1]}-{goal_coord[0]},{goal_coord[1]}"
            print(key)
            paths[key] = steps
            
        completed_coords.append(coord)

    print(paths)

    

def main(input):
    galaxy_grid = [list(x) for x in input]

    expanded_galaxy_grid = expand_galaxy(galaxy_grid)
    galaxy_coords = find_all_galaxy_coords(expanded_galaxy_grid)

    

    paths = find_paths(galaxy_coords)
    for row in expanded_galaxy_grid:
        print(row)

    print(galaxy_coords)

main(test)
