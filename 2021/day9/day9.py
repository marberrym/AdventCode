f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def main(matrix):
    # print(matrix)

    validLowPointHeights = []
    lowPoints = []
    basins = []

    for i in range(len(matrix)):
        potentialLowPoints = getPotentialLowPoints(matrix[i]);
        validatedLowPoints = validateLowPoints(matrix, i, potentialLowPoints);

        for point in validatedLowPoints:
            validLowPointHeights.append(matrix[i][point]);
            lowPoints.append([i, point])

    for lowPoint in lowPoints:
        basinSize = searchBasin(matrix, lowPoint);
        basins.append(basinSize);

    basins.sort();

    part2answer = basins[-1] * basins[-2] * basins[-3]

    print(part2answer)

    return getRiskFactor(validLowPointHeights);


def searchBasin(matrix, point):
    basin = checkAdjacentPoints(matrix, point, [point], [point]);
    return len(basin);

def checkAdjacentPoints(matrix, point, checkedPoints, validPoints):
    row = point[0]
    column = point[1]
    originValue = matrix[row][column];

    firstRow = row == 0;
    lastRow = row == len(matrix) - 1;
    firstColumn = column == 0;
    lastColumn = column == len(matrix[row]) - 1;

    pointsToCheck = getPointsToCheck(row, column, firstRow, lastRow, firstColumn, lastColumn);
    nextPointsToCheck = [];

    for coord in pointsToCheck:
        row = coord[0];
        col = coord[1];
        coordValue = matrix[row][col];

        if coordValue > originValue and int(coordValue) != 9:
            if coord not in checkedPoints:
                checkedPoints.append([row, col]);
            if coord not in validPoints:
                validPoints.append([row, col]);
            nextPointsToCheck.append(coord);
        else:
            if coord not in checkedPoints:
                checkedPoints.append([row, col]);

    if len(nextPointsToCheck) > 0:
        for coord in nextPointsToCheck:
            checkAdjacentPoints(matrix, coord, checkedPoints, validPoints)

    return validPoints

def getPointsToCheck(row, col, firstRow, lastRow, firstCol, lastCol):
    pointsToCheck = [[row-1, col], [row, col-1], [row+1, col], [row, col+1]];
    if firstRow:
        pointsToCheck.remove([row-1, col]);

    if lastRow:
        pointsToCheck.remove([row+1, col]);

    if firstCol:
        pointsToCheck.remove([row, col-1]);

    if lastCol:
        pointsToCheck.remove([row, col+1]);

    return pointsToCheck;

def getPotentialLowPoints(row):
    potentialLowPoints = []

    for i in range(len(row)):
        currentPoint = row[i];
        if i != 0 and i != len(row) - 1:
            if row[i-1] > currentPoint and row[i+1] > currentPoint:
                potentialLowPoints.append(i);
        elif i == 0:
            if row[i+1] > currentPoint:
                potentialLowPoints.append(i);
        elif i==len(row) - 1:
            if row[i-1] > currentPoint:
                potentialLowPoints.append(i);

    # print(potentialLowPoints);
    return potentialLowPoints

def validateLowPoints(matrix, rowInd, potentialPoints):
    validatedPoints = [];

    if rowInd != 0 and rowInd != len(matrix) - 1:
        for i in potentialPoints:
            if matrix[rowInd - 1][i] > matrix[rowInd][i] and matrix[rowInd + 1][i] > matrix[rowInd][i]:
                validatedPoints.append(i)
    elif rowInd == 0:
        for i in potentialPoints:
            if matrix[rowInd + 1][i] > matrix[rowInd][i]:
                validatedPoints.append(i)
    elif rowInd == len(matrix) - 1:
        for i in potentialPoints:
            if matrix[rowInd - 1][i] > matrix[rowInd][i]:
                validatedPoints.append(i)

    return validatedPoints;

def getRiskFactor(lowPointHeights):
    total = 0;
    for height in lowPointHeights:
        total += int(height) + 1;
    return total;





main(input)
