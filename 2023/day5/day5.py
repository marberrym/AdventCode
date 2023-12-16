from functools import reduce

f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

seeds, *mappings = open('testCase.txt').read().split('\n\n')
seeds = map(int, seeds.split()[1:])

def lookup(start, mapping):
    for m in mapping.split('\n')[1:]:
        dst, src, len = map(int, m.split())
        delta = start - src
        if delta in range(len):
            return dst + delta
        else: return start

locs = []
for s in seeds:
    locs.append(reduce(lookup, mappings, int(s)))

print(min(locs))

def main(input):
    seeds = []
    growth_maps = {}
    current_map = ''
    seed_locations = []


    def find_output(map_name, input):
        output = 0
        if input in growth_maps[map_name].keys(): output = growth_maps[map_name][input]
        else: output = input
        return output
    
    # Generate maps
    for inst_idx, instruction in enumerate(input):
        if inst_idx == 0:
            seeds = instruction.split(":")[1].split()
        elif instruction == '': continue
        elif ":" in instruction:
            current_map = instruction[:-1]
            growth_maps[current_map] = {}
        else:
            destination_range, source_range, range_length = instruction.split()
            for i in range(int(range_length)):
                growth_maps[current_map][int(source_range) + i] = int(destination_range) + i
    
    for seed in seeds:
        soil_number = find_output('seed-to-soil map', int(seed))
        fertilizer_number = find_output('soil-to-fertilizer map', soil_number)
        water_number = find_output('fertilizer-to-water map', fertilizer_number)
        light_number = find_output('water-to-light map', water_number)
        temperature_number = find_output('light-to-temperature map', light_number)
        humidity_number = find_output('temperature-to-humidity map', temperature_number)
        location_number = find_output('humidity-to-location map', humidity_number)
        seed_locations.append(location_number)
        print("Seed ", seed, "soil ", soil_number, "fert ", fertilizer_number, "water ", water_number, "light ", light_number, "temp ", temperature_number, "humidity ", humidity_number, "location ", location_number)

    print(min(seed_locations))
    
main(input)
