f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def getDirection(init, seq):
    return init < seq;

def convertToInt(x): return int(x);

def iterateNumbers(numbers):
    isAdditive = getDirection(numbers[0], numbers[1]);
    numCount = len(numbers);
    isSafe = True;
    errorCount = 0;
    errorIndex = None;

    for idx, x in enumerate(numbers):
        if idx < numCount - 1:
            nextNum = numbers[idx + 1];
            difference = abs(x - nextNum);
            if ((difference > 3 or difference == 0) or (getDirection(x, nextNum) != isAdditive)):
                # print (f"ERROR IDX: {idx}")
                isSafe = False;
                errorCount += 1;
                if errorIndex == None: errorIndex = idx;

    return {
        "isSafe": isSafe,
        "errorCount": errorCount,
        "errorIndex": errorIndex,
        "numCount": numCount,
    }

def checkIfSafe(numbers):
    results = iterateNumbers(numbers);    
    return results["isSafe"];

def checkIfSafeWithDampener(numbers):
    results = iterateNumbers(numbers);
    errorCount = results["errorCount"];
    errorIndex = results["errorIndex"];
    isSafe = results["isSafe"];
    numCount = results["numCount"];
    
    if not isSafe:
        print(results);
        print(numbers);
        numbersClone = numbers[0:errorIndex] + numbers[errorIndex + 1:numCount - 1];
        numbersFirstRemoved = numbers[1:];
        dampenedResults = iterateNumbers(numbersClone);
        dampenedResults2 = iterateNumbers(numbersFirstRemoved);
        if dampenedResults["isSafe"] or dampenedResults2["isSafe"]:
            print("SAFE") 
            isSafe = True;
        else:
            print("UNSAFE") 
            print(numbersClone);
    
    return isSafe;


def main(input):
    partOneSafeEntries = 0;
    partTwoSafeEntries = 0;
    for line in input:
        numbers = list(map(convertToInt, line.split()));
        isSafe = checkIfSafe(numbers);
        isSafeWithDampeners = checkIfSafeWithDampener(numbers);

        if isSafe:
            partOneSafeEntries += 1;
    
        if isSafeWithDampeners:
            partTwoSafeEntries += 1;

    print(f"Part one safe entries: {partOneSafeEntries}");
    print(f"Part two safe entries: {partTwoSafeEntries}");

main(input)
