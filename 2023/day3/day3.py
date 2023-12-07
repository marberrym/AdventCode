f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def prep_board(input):
    engine_board = []
    for row in input:
        engine_board.append(list(row))
    return engine_board

# Part 1 functions
def check_if_symbol(char):
    numeric = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    if (char not in numeric):
        return True
    else:
        return False

def check_for_adjacent_symbols(engine_matrix, row_idx, char_idx):
    prev_row = row_idx - 1
    next_row = row_idx + 1
    prev_char = char_idx - 1
    next_char = char_idx + 1

    # If it's not the first row, check previous row
    if (row_idx > 0):
        if char_idx > 0 and check_if_symbol(engine_matrix[prev_row][prev_char]):
            return True
        if check_if_symbol(engine_matrix[prev_row][char_idx]):
            return True
        if char_idx < (len(engine_matrix[row_idx]) - 1) and check_if_symbol(engine_matrix[prev_row][next_char]):
            return True
    
    # If it's not the first char, check previous char
    if (char_idx > 0):
        if not(engine_matrix[row_idx][prev_char].isnumeric()) and check_if_symbol(engine_matrix[row_idx][prev_char]):
            return True
        
    # If it's not the last char, check next char
    if char_idx < (len(engine_matrix[row_idx]) - 1):
        if not(engine_matrix[row_idx][next_char].isnumeric()) and check_if_symbol(engine_matrix[row_idx][next_char]):
            return True
        
    # If it's not the last row, check the next row
    if (row_idx < (len(engine_matrix) - 1)):
        if char_idx > 0 and check_if_symbol(engine_matrix[next_row][prev_char]):
            return True
        if check_if_symbol(engine_matrix[next_row][char_idx]):
            return True
        if char_idx < (len(engine_matrix[row_idx]) - 1) and check_if_symbol(engine_matrix[next_row][next_char]):
            return True
    
    return False

def find_number_start(engine_matrix, row_idx, char_idx):
    if char_idx > 0:
        if engine_matrix[row_idx][char_idx - 1].isnumeric():
            return find_number_start(engine_matrix, row_idx, char_idx - 1)
        else:
            return char_idx
    
    return char_idx
    
    
def find_number_end(engine_matrix, row_idx, char_idx):
    if char_idx < (len(engine_matrix[row_idx]) - 1):
        if engine_matrix[row_idx][char_idx + 1].isnumeric():
            return find_number_end(engine_matrix, row_idx, char_idx + 1)
        else:
            return char_idx
    
    return char_idx
        
def get_all_numeric_indexes(row):
    numeric_indexes = {}
    for char_idx, char in enumerate(row):
        if char.isnumeric():
            numeric_indexes[char_idx] = char
    return numeric_indexes

def get_all_valid_numeric_indexes(engine_matrix, row_idx, numeric_indexes):
    valid_numeric_indexes = {}
    for char_idx in numeric_indexes:
        if check_for_adjacent_symbols(engine_matrix, row_idx, char_idx):
            valid_numeric_indexes[char_idx] = numeric_indexes[char_idx]
    return valid_numeric_indexes

def get_all_valid_number_coordinates(engine_matrix, row_idx, valid_numeric_indexes):
    valid_number_coordinates = []
    for char_idx in valid_numeric_indexes:
        number_coords = [find_number_start(engine_matrix, row_idx, char_idx), find_number_end(engine_matrix, row_idx, char_idx)]
        if number_coords not in valid_number_coordinates:
            valid_number_coordinates.append(number_coords)
    return valid_number_coordinates

# Part 2 functions:
def check_for_number(char):
    if char.isnumeric():
        return True
    return False

def get_adjacent_coords(coord):
    return {
        'row_idx': coord[0],
        'char_idx': coord[1],
        'prev_row': coord[0] - 1,
        'next_row': coord[0] + 1,
        'prev_char': coord[1] - 1,
        'next_char': coord[1] + 1
    }

def find_whole_number(engine_matrix, row_idx, char_idx):
    number = ''
    start_idx = find_number_start(engine_matrix, row_idx, char_idx)
    end_idx = find_number_end(engine_matrix, row_idx, char_idx)
    indexes = range(start_idx, end_idx + 1)
    for d in indexes:
        number += engine_matrix[row_idx][d]
    return number

def verify_gear_coords(engine_matrix, potential_gear_coords):
    gear_power_numbers = []
    for coord in potential_gear_coords:
        adjacent_coords = get_adjacent_coords(coord)
        row_idx, char_idx, prev_row, next_row, prev_char, next_char = adjacent_coords['row_idx'], adjacent_coords['char_idx'], adjacent_coords['prev_row'], adjacent_coords['next_row'], adjacent_coords['prev_char'], adjacent_coords['next_char']

        adjacent_numbers = 0
        
        first_gear = None
        # If it's not the first row, check previous row
        if (row_idx > 0):
            if char_idx > 0 and check_for_number(engine_matrix[prev_row][prev_char]):
                if not(check_for_number(engine_matrix[prev_row][char_idx])) and check_for_number(engine_matrix[prev_row][next_char]):
                    adjacent_numbers += 2
                else:
                    adjacent_numbers += 1
            elif check_for_number(engine_matrix[prev_row][char_idx]):
                adjacent_numbers += 1
            elif check_for_number(engine_matrix[prev_row][next_char]):
                adjacent_numbers += 1

        
        # If it's not the first char, check previous char
        if (char_idx > 0):
            if check_for_number(engine_matrix[row_idx][prev_char]):
                adjacent_numbers += 1
            
        # If it's not the last char, check next char
        if char_idx < (len(engine_matrix[row_idx]) - 1):
            if check_for_number(engine_matrix[row_idx][next_char]):
                adjacent_numbers += 1
            
        # If it's not the last row, check the next row
        if (row_idx < (len(engine_matrix) - 1)):
            if char_idx > 0 and check_for_number(engine_matrix[next_row][prev_char]):
                if not(check_for_number(engine_matrix[next_row][char_idx])) and check_for_number(engine_matrix[next_row][next_char]):
                    adjacent_numbers += 2
                else:
                    adjacent_numbers += 1
            elif check_for_number(engine_matrix[next_row][char_idx]):
                adjacent_numbers += 1
            elif check_for_number(engine_matrix[next_row][next_char]):
                adjacent_numbers += 1
        
        if adjacent_numbers == 2:
            if (row_idx > 0):
                if char_idx > 0 and check_for_number(engine_matrix[prev_row][prev_char]) and not(check_for_number(engine_matrix[prev_row][char_idx])) and check_for_number(engine_matrix[prev_row][next_char]):
                    first_number = find_whole_number(engine_matrix, prev_row, prev_char)
                    second_number = find_whole_number(engine_matrix, prev_row, next_char)

                    gear_power_numbers.append(int(first_number) * int(second_number))

                elif char_idx > 0 and check_for_number(engine_matrix[prev_row][prev_char]):
                    number = find_whole_number(engine_matrix, prev_row, prev_char)
                    
                    if (first_gear):
                        gear_power_numbers.append(int(first_gear) * int(number))
                    else:
                        first_gear = number
                    
                elif check_for_number(engine_matrix[prev_row][char_idx]):
                    number = find_whole_number(engine_matrix, prev_row, char_idx)
                    
                    if (first_gear):
                        gear_power_numbers.append(int(first_gear) * int(number))
                    else:
                        first_gear = number

                elif check_for_number(engine_matrix[prev_row][next_char]):
                    number = find_whole_number(engine_matrix, prev_row, next_char)
                    if (first_gear):
                        gear_power_numbers.append(int(first_gear) * int(number))
                    else:
                        first_gear = number

            if (char_idx > 0):
                if check_for_number(engine_matrix[row_idx][prev_char]):
                    number = find_whole_number(engine_matrix, row_idx, prev_char)
                    if (first_gear):
                        gear_power_numbers.append(int(first_gear) * int(number))
                    else:
                        first_gear = number

            if char_idx < (len(engine_matrix[row_idx]) - 1):
                if check_for_number(engine_matrix[row_idx][next_char]):
                    number = find_whole_number(engine_matrix, row_idx, next_char)
                    if (first_gear):
                        gear_power_numbers.append(int(first_gear) * int(number))
                    else:
                        first_gear = number
            
            if (row_idx < (len(engine_matrix) - 1)):
                if char_idx > 0 and check_for_number(engine_matrix[next_row][prev_char]) and not(check_for_number(engine_matrix[next_row][char_idx])) and check_for_number(engine_matrix[next_row][next_char]):
                    first_number = find_whole_number(engine_matrix, next_row, prev_char)
                    second_number = find_whole_number(engine_matrix, next_row, next_char)

                    gear_power_numbers.append(int(first_number) * int(second_number))

                elif char_idx > 0 and check_for_number(engine_matrix[next_row][prev_char]):
                    number = find_whole_number(engine_matrix, next_row, prev_char)
                    
                    if (first_gear):
                        gear_power_numbers.append(int(first_gear) * int(number))
                    else:
                        first_gear = number

                elif check_for_number(engine_matrix[next_row][char_idx]):
                    number = find_whole_number(engine_matrix, next_row, char_idx)
                    
                    if (first_gear):
                        gear_power_numbers.append(int(first_gear) * int(number))
                    else:
                        first_gear = number

                elif check_for_number(engine_matrix[next_row][next_char]):
                    number = find_whole_number(engine_matrix, next_row, next_char)
                    
                    if (first_gear):
                        gear_power_numbers.append(int(first_gear) * int(number))
                    else:
                        first_gear = number
    
    return gear_power_numbers

            

                    


    

def get_gear_coordinates(engine_matrix):
    gear_coordinates = []
    for row_idx, row in enumerate(engine_matrix):
        for char_idx, char in enumerate(row):
            if char == '*':
                gear_coordinates.append([row_idx, char_idx])
    return gear_coordinates


def main(input):
    engine_matrix = prep_board(input)
    part_number_sum = 0
    gear_power = 0

    for row_idx, row in enumerate(engine_matrix):
        numeric_indexes = get_all_numeric_indexes(row)
        valid_numeric_idexes = get_all_valid_numeric_indexes(engine_matrix, row_idx, numeric_indexes)
        valid_number_coordinates = get_all_valid_number_coordinates(engine_matrix, row_idx, valid_numeric_idexes)
        
        for coord in valid_number_coordinates:
            number = ''
            indexes = range(coord[0], coord[1] + 1)
            for d in indexes:
                number += engine_matrix[row_idx][d]
            
            part_number_sum += int(number)
    print(f"Part total... {part_number_sum}")

    potential_gear_locations = get_gear_coordinates(engine_matrix)
    gear_power_numbers = verify_gear_coords(engine_matrix, potential_gear_locations)
    for number in gear_power_numbers:
        gear_power += int(number)
    
    print(f"gear power is... {gear_power}")

    


main(input)
