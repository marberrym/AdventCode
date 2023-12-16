f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

# Part One
def main(collections):
    largestCalCollection = 0;
    currentCalCollection = 0;
    for collection in collections:
        for item in collection:
            currentCalCollection += int(item)

        if currentCalCollection > largestCalCollection:
            largestCalCollection = currentCalCollection

        currentCalCollection = 0

    return largestCalCollection

# Part Two
def main2(collections, topAmount):
    allCollections = []
    currentCalCollection = 0

    for collection in collections:
        for item in collection:
            currentCalCollection += int(item)

        allCollections.append(currentCalCollection)
        currentCalCollection = 0

    return checkCollections(allCollections, topAmount)

# Check for answer
def checkCollections(collections, topAmount):
    collections.sort(reverse=True)
    totalCals = 0

    for i in range(topAmount):
        totalCals += collections[i]

    return totalCals

# Data massaging
def prepData(entries):
    arrayOfCollections = [];
    currentCollection = [];

    for i in range(len(entries)):
        if entries[i] and int(entries[i]) > 0 and i != (len(entries) - 1):
            currentCollection.append(entries[i])
        elif i == (len(entries) - 1):
            currentCollection.append(entries[i])
            arrayOfCollections.append(currentCollection)
        else:
            arrayOfCollections.append(currentCollection)
            currentCollection = []

    return arrayOfCollections



print(main(prepData(test)))
print(main2(prepData(input), 3))