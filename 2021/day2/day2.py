f = open('input.txt', 'r');
readings = f.read().splitlines();


testStuff = ['forward 5',
'down 5',
'forward 8',
'up 3',
'down 8',
'forward 2',
]

def main1(instructions):
    horizontalMovement = 0;
    depthLevel = 0;

    for instruction in instructions:
        components = instruction.split();

        if (components[0] == "down"):
            depthLevel += int(components[1]);
        elif (components[0] == "up"):
            depthLevel -= int(components[1]);
        elif (components [0] == "forward"):
            horizontalMovement += int(components[1]);

    return horizontalMovement * depthLevel;

def main2(instructions):
    horizontalMovement = 0;
    depthLevel = 0;
    aim = 0;

    for instruction in instructions:
        components = instruction.split();

        if (components[0] == "down"):
            aim += int(components[1]);
        elif (components[0] == "up"):
            aim -= int(components[1]);
        elif (components [0] == "forward"):
            horizontalMovement += int(components[1]);
            depthLevel += aim * int(components[1]);

    return horizontalMovement * depthLevel;


print(main1(readings));
print(main2(readings));