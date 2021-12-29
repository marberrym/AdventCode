f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def main(input):
    simpleDigits = 0;
    totalOutput = 0;
    for entry in input:
        output = entry.split("|")[1].strip()
        signalPattern = entry.split("|")[0].strip()
        signalDigits = signalPattern.split()
        outputDigits = output.split()
        numbers = {}

        for digit in signalDigits:
            analyzeSimpleNumbers(digit, numbers)

        twoThreeFives = list(filter(checkGroup1, signalDigits));
        zeroSixNines = list(filter(checkGroup2, signalDigits));

        analyzeGroup1(twoThreeFives, numbers)
        analyzeGroup2(zeroSixNines, numbers)

        totalOutput += analyzeOutputDigits(outputDigits, numbers);

    print(f"answer is...{totalOutput}")

def analyzeOutputDigits(digits, numbers):
    output = ''
    for digit in digits:
        if len(digit) == 2:
            output += '1';
        if len(digit) == 3:
            output += '7';
        if len(digit) == 4:
            output += '4';
        if len(digit) == 7:
            output += '8';

        if len(digit) == 5:
            if checkMatches(digit, numbers[2]): output += '2'; continue
            if checkMatches(digit, numbers[3]): output += '3'; continue
            if checkMatches(digit, numbers[5]): output += '5'; continue

        if len(digit) == 6:
            if checkMatches(digit, numbers[6]): output += '6'; continue
            if checkMatches(digit, numbers[9]): output += '9'; continue
            if checkMatches(digit, numbers[0]): output += '0'; continue

    print(f"OUTPUT is {output}")
    return int(output);


def checkMatches(digit, key):
    matches = 0;
    length = len(key);
    for i in digit:
        if i in key:
            matches += 1;

    if matches == length:
        return True
    return False;


def analyzeGroup1(unknowns, numbers):
    for unknown in unknowns:
        if numbers[1][0] in unknown and numbers[1][1] in unknown:
            numbers[3] = unknown
        else:
            fourClone = numbers[4]
            matches = 0
            for letter in unknown:
                if letter in fourClone: matches += 1
            if matches == 2:
                numbers[2] = unknown
            elif matches == 3:
                numbers[5] = unknown

def analyzeGroup2(unknowns, numbers):
    for unknown in unknowns:
        if numbers[1][0] not in unknown or numbers[1][1] not in unknown:
            numbers[6] = unknown
        else:
            fourClone = numbers[4]
            matches = 0
            for letter in unknown:
                if letter in fourClone: matches += 1
            if matches == 4:
                numbers[9] = unknown
            elif matches == 3:
                numbers[0] = unknown

def checkGroup1(number):
    if len(number) == 5: return True
    return False

def checkGroup2(number):
    if len(number) == 6: return True
    return False

def analyzeSimpleNumbers(digit, numbers):
    if len(digit) == 2:
        numbers[1] = digit;
    if len(digit) == 3:
        numbers[7] = digit;
    if len(digit) == 4:
        numbers[4] = digit;
    if len(digit) == 7:
        numbers[8] = digit;

def analyzeNumbers(numbers):
    None


main(input)
