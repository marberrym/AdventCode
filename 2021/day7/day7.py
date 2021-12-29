import statistics
import math

f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

input = [int(i) for i in input[0].split(",")];
test = [int(i) for i in test[0].split(",")];

def main(positions):
    state_map ={}
    fuelNeeded = 0;

    median = statistics.median(positions)
    mean = math.floor(statistics.mean(positions))

    for pos in positions:
        state_map[pos] = positions.count(pos);

    for key in state_map:
        # fuelNeeded += (abs((key - median)) * state_map[key]); -- Part 1
        fuelNeeded += sum(range(abs(key - mean) + 1))  * state_map[key];

    return fuelNeeded;

main(input)
