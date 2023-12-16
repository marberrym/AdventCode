f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

# Common
ROCK = "rock"
SCISSORS = "scissors"
PAPER = "paper"

opponentValues = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS
}

scoreValues = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
    "W": 6,
    "D": 3,
    "L": 0,
}

outcomesByOpponentChoice = {
    ROCK: {
        "W": PAPER,
        "L": SCISSORS,
        "D": ROCK
    },
    PAPER: {
        "W": SCISSORS,
        "L": ROCK,
        "D": PAPER
    },
    SCISSORS: {
        "W": ROCK,
        "L": PAPER,
        "D": SCISSORS
    }
}

def calculateScore(playedValue, gameResult):
    return scoreValues[playedValue] + scoreValues[gameResult]

# Part 1
myValues = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}

def analyzeGame(opponentValue, myValue):
    if (opponentValue == myValue):
        return calculateScore(myValue, "D")

    if myValue == outcomesByOpponentChoice[opponentValue]["W"]:
        return calculateScore(myValue, "W")
    else:
        return calculateScore(myValue, "L")

def main(input):
    totalScore = 0;
    for game in input:
        playedValues = game.split()
        totalScore += analyzeGame(opponentValues[playedValues[0]], myValues[playedValues[1]])
        print(f"Score is... {totalScore}")

# Part 2
desiredOutcome = {
    "X": "L",
    "Y": "D",
    "Z": "W",
}

def analyzeGameP2(opponentValue, desiredOutcome):
    myChoice = outcomesByOpponentChoice[opponentValue][desiredOutcome]
    return calculateScore(myChoice, desiredOutcome)

def main2(input):
    totalScore = 0;
    for game in input:
        playedValues = game.split()
        totalScore += analyzeGameP2(opponentValues[playedValues[0]], desiredOutcome[playedValues[1]])
        print(f"Score is... {totalScore}")

# main(input)
main2(input)


