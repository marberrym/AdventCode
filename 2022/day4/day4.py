f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

# Part One
def compareSections(firstSection, secondSection):
    firstSectionBoundaries = firstSection.split('-')
    secondSectionBounderies = secondSection.split('-')

    firstStart = int(firstSectionBoundaries[0])
    firstEnd = int(firstSectionBoundaries[1])
    secondStart = int(secondSectionBounderies[0])
    secondEnd = int(secondSectionBounderies[1])

    if (firstStart <= secondStart and firstEnd >= secondEnd) or (firstStart >= secondStart and firstEnd <= secondEnd):
        return True
    else:
        return False

def main(pairs):
    overlaps = 0
    for pair in pairs:
        assignedSections = pair.split(',')
        if compareSections(assignedSections[0], assignedSections[1]):
            overlaps += 1
        
    print(overlaps)

# Part Two
def compareSectionsForAnyOverlap(firstSection, secondSection):
    firstSectionBoundaries = firstSection.split('-')
    secondSectionBounderies = secondSection.split('-')

    firstStart = int(firstSectionBoundaries[0])
    firstEnd = int(firstSectionBoundaries[1])
    secondStart = int(secondSectionBounderies[0])
    secondEnd = int(secondSectionBounderies[1])

    if (firstStart <= secondStart and  firstEnd >= secondEnd) or (firstStart >= secondStart and firstEnd <= secondEnd) or (firstStart <= secondEnd and secondStart <= firstEnd):
        return True
    else:
        return False

def main2(pairs):
    overlaps = 0
    for pair in pairs:
        assignedSections = pair.split(',')
        if compareSectionsForAnyOverlap(assignedSections[0], assignedSections[1]):
            overlaps += 1

    print(overlaps)
main2(input)
