import math

f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

input = [int(i) for i in input[0].split(",")];
test = [int(i) for i in test[0].split(",")];

def main(fishies, days):
    day = 0
    state = fishies;
    while day < days:
        state = passDay(fishies);
        print(day);
        day += 1;
    fishCount = len(state);
    print(fishCount);
    return fishCount;

def passDay(fishies):
    newState = fishies;
    for i in range(len(fishies)):
        if int(fishies[i]) > 0:
            newState[i] = int(fishies[i]) - 1;
        else:
            newState.append(8);
            newState[i] = 6;

    return newState

def main2(fishies, days):
    day = 0;
    totalFish = 0

    current_state = {
        0: fishies.count(0),
        1: fishies.count(1),
        2: fishies.count(2),
        3: fishies.count(3),
        4: fishies.count(4),
        5: fishies.count(5),
        6: fishies.count(6),
        7: fishies.count(7),
        8: fishies.count(8),
    }

    for i in range(days):
        next_state = {
            0: current_state[1],
            1: current_state[2],
            2: current_state[3],
            3: current_state[4],
            4: current_state[5],
            5: current_state[6],
            6: current_state[7],
            7: current_state[8],
            8: current_state[0],
        }

        if current_state[0] > 0:
            next_state[6] += current_state[0];

        current_state = next_state
        next_state = {}

    for fish in current_state:
        totalFish += current_state[fish];

    print(totalFish);
    return totalFish;

# main(input, 256)

main2(input, 256)
