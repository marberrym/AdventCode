f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

openCharacters = ["(", "{", "[", "<"]
closeCharacters = [")", "}", "]", ">"]

syntaxScores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

closeScores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}





def main(input):
    print(input)
    syntaxScore = 0;
    closingScores = [];

    for chunk in input:
        result = testValidity(chunk)
        print(result)
        if type(result) is tuple and result[0] == "invalid":
            syntaxScore += syntaxScores[result[1]]
        elif type(result) is tuple and result[0] == "incomplete":
            closingScores.append(generateCloseScore(result[1]));
            print(f"generate score here with closing seq of {result[1]}")

    print(syntaxScore)
    print(closingScores)
    getPart2Answer(closingScores)

def getPart2Answer(closingScores):
    closingScores.sort();
    middleIndex = int((len(closingScores) - 1)  / 2)
    print(middleIndex)
    middleNumber = closingScores[middleIndex]
    print(middleNumber);
    print(closingScores);

def generateCloseScore(closeSequence):
    score = 0;
    print(closeSequence)
    for char in closeSequence:
        score = (score * 5) + closeScores[char]

    return score;


def testValidity(chunk):
    brackets = [];
    for char in chunk:
        if findType(char) == "open":
            brackets.append(char);
        else:
            if findOpenChar(char) == brackets[-1]:
                brackets.pop();
            else:
                return "invalid", char

    if len(brackets) == 0:
        return "valid"
    else:
        findClosingSequence(brackets)
        return "incomplete", findClosingSequence(brackets)

def findClosingSequence(brackets):
    closingSequence = []
    brackets.reverse()

    for bracket in brackets:
        closingSequence.append(findCloseChar(bracket))

    closingSequence.reverse()
    return closingSequence

def findOpenChar(char):
    if char == ">":
        return "<"
    elif char == "}":
        return "{"
    elif char == ")":
        return "("
    elif char == "]":
        return "["

def findCloseChar(char):
    if char == "<":
        return ">"
    elif char == "{":
        return "}"
    elif char == "(":
        return ")"
    elif char == "[":
        return "]"


def findType(char):
    if char in openCharacters:
        return "open"
    elif char in closeCharacters:
        return "close"

main(input)
