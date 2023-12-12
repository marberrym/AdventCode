f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def get_next_line(line):
    next_line = []
    for idx, value in enumerate(line):
        if idx < len(line) - 1:
            next_line.append(line[idx + 1] - value)
    return next_line

def check_if_schema_complete(line):
    if all([x == 0 for x in line]): return True
    else: return False

def check_for_same_values(line):
    target = line[0]
    if all([x == target for x in line]): return True
    else: return False

def find_next_schema(schematic):
    reversed_schema = list(reversed(schematic))
    value_to_be_added = 0
    
    for line in reversed_schema:
        next_value = line[-1] + value_to_be_added
        line.append(next_value)
        value_to_be_added = next_value
        print(line)

    return reversed_schema

def find_prev_schema(schematic):
    reversed_schema = list(reversed(schematic))
    value_to_be_subtracted = 0

    for line in reversed_schema:
        prev_value = line[0] - value_to_be_subtracted
        line.insert(0, prev_value)
        value_to_be_subtracted = prev_value
        print(line)
    return reversed_schema


def main(input):
    next_value_sum = 0
    difference_sum = 0

    for line in input:
        schematic = []
        current_line = [int(x) for x in line.split()]
        schematic.append(current_line)

        # Build schematic
        while not check_if_schema_complete(current_line):
            next_line = get_next_line(current_line)
            schematic.append(next_line)
            current_line = next_line

        next_schema = find_next_schema(schematic)
        next_value_sum += next_schema[-1][-1]

        prev_schema = find_prev_schema(schematic)
        difference_sum += prev_schema[-1][0]


    print("P1: Next value sum is... ", next_value_sum)
    print("P2: Prev value sum is... ", difference_sum)

main(input)
