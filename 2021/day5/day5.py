f = open('input.txt', 'r');
readings = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();


def main(plots):
    floor = []
    hitPoints = dict();
    for plot in plots:
        points = plot.split(' -> ')
        startPoint = points[0].split(',')
        endPoint = points[1].split(',')

        # print(startPoint)
        # print(endPoint)
        # print(points)
        if (checkValidity(startPoint, endPoint) == True):
            analyzePath(startPoint, endPoint, hitPoints)

    print(hitPoints)

def analyzePath(start, end, points):
    if start[0] == end[0]:
        print("Drawing path for...", start, end)
        for x in range(int(start[1]), int(end[1]) + 1), -1 if int(start[1]) > int(end[1]) else 1):
            key = f"{start[0]},{str(x)}"
            if key in points:
                points[key] += 1
            else:
                points[key] = 1
    elif start[1] == end[1]:
        print("Drawing path for...", start, end)
        for x in range(int(start[0]), int(end[0]) + 1, -1 if int(start[0]) > int(end[0]) else 1):
            key = f"{str(x)},{start[1]}"
            if key in points:
                points[key] += 1
            else:
                points[key] = 1



def checkValidity(start, end):
    if start[0] == end[0] or start[1] == end[1]:
        return True
    return False


main(test)