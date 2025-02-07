f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def prepData(input):
    leftList = [];
    rightList = [];

    for row in input:
        entries = row.split();
        leftList.append(int(entries[0]));
        rightList.append(int(entries[1]));
    
    return {
        "left": sorted(leftList),
        "right": sorted(rightList),
    }

def findDiffs(lists):
    diffs = [];
    leftList = lists["left"];
    rightList = lists["right"];

    for idx, x in enumerate(leftList):
        diff = abs(x - rightList[idx]);
        diffs.append(diff);

    return diffs

def findSimilarityScore(lists):
    similarityScores = [];
    leftList = lists["left"];
    rightList = lists["right"];

    for idx, x in enumerate(leftList):
        similarityScore = x * rightList.count(x);
        similarityScores.append(similarityScore);

    return similarityScores;

def main(input):
    lists = prepData(input);
    diffs = findDiffs(lists);
    similarityScores = findSimilarityScore(lists);

    partOneSolution = sum(diffs);
    partTwoSolution = sum(similarityScores);

    print(f"Part one solution: {partOneSolution}");
    print(f"Part one solution: {partTwoSolution}");

main(input);
