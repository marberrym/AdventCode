f = open('input.txt', 'r');
readings = f.read().splitlines();


testStuff = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010',
]

def main1(numbers):
    gammaRateString = "";

    for x in range(5):
        gammaRateString += getNumber(numbers, x);

    epsilonRateString = getEpislonString(gammaRateString);

    print(gammaRateString);
    print(epsilonRateString);
    gammaRateInt = int(gammaRateString, 2);
    epsilonRateInt = int(epsilonRateString, 2);

    return gammaRateInt * epsilonRateInt;

def getNumber(numbers, position):
    zeroCount = 0;
    oneCount = 0;

    for number in numbers:
        if (number[position] == '0'):
            zeroCount += 1;
        elif (number[position] == '1'):
            oneCount += 1;

    print("zero count", zeroCount);
    print("one count", oneCount);
    if (zeroCount >= oneCount):
        return '0';
    else:
        return '1';


def getEpislonString(gammaValue):
    epsilonString = "";
    for x in range(5):
        if gammaValue[x] == '0':
            epsilonString += '1';
        else:
            epsilonString += '0';
    return epsilonString;

# def main2(instructions):

print(main1(testStuff));
print(main1(readings));
# print(main2(readings));