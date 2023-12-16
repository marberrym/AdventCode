f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().split('\n\n');

def populateStackMap(map):
    stackMap = []
    print(map)
    for row in map[0]:
        print(row)

def main(data):
    map = data[0].split('\n'),
    instructions = data[1].split('\n')
    populateStackMap(map)
    # print(map)
    # print(instructions)

main(test)
