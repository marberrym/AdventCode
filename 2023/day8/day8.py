import re
import numpy

f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def check_current_node(node):
    if node[-1] == "Z": return True
    else: return False

def main(input):
    node_mapping = {}
    instructions = list(input[0].strip())
    move_count = 0
    current_node = 'AAA'

    nodes = []
    steps_required = []

    for node in input[2::]:
        key, options = node.split("=")
        key = key.strip()
        option1, option2 = re.sub("[()]", "", options).split(",")

        if (key[-1] == 'A'):
            nodes.append(key)

        node_mapping[key] = {
            "L": option1.strip(),
            "R": option2.strip()
        }
    
    # P1
    while current_node != 'ZZZ':
        for instruction in instructions:
            current_node = node_mapping[current_node][instruction]
            move_count += 1

    # P2
    for node in nodes:
        steps = 0
        current_node = node 
        while not check_current_node(current_node):
            for instruction in instructions:
                current_node = node_mapping[current_node][instruction]
                steps += 1
        steps_required.append(steps)


    print("Part one move count... ", move_count)
    print("Part two move count... ", numpy.lcm.reduce(steps_required))

main(input)
