import numpy

f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def get_race_total(list):
    total = ''
    for val in list:
        total += val.strip()
    return total

def main(input):
    print(input)
    race_times = input[0].split(":")[1].split()
    race_distances_to_beat = input[1].split(":")[1].split()
    race_ways_to_win = []

    for idx, time in enumerate(race_times):
        options = range(int(time))
        ways_to_win = 0
        for opt in options:
            velocity = opt
            time_to_travel = int(time) - opt
            if velocity * time_to_travel > int(race_distances_to_beat[idx]): ways_to_win += 1
        race_ways_to_win.append(ways_to_win)
    
    print(numpy.prod(race_ways_to_win))

    race_time = get_race_total(input[0].split(":")[1])
    race_distance = get_race_total(input[1].split(":")[1])
    
    options = range(int(race_time))
    ways_to_win = 0

    for opt in options:
        velocity = opt
        time_to_travel = int(race_time) - opt
        if velocity * time_to_travel > int(race_distance): ways_to_win += 1

    print("Ways to win...", ways_to_win)

main(input)
