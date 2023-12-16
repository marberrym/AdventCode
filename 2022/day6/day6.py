f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def analyzeMarkers(markers):
    cleared = False
    for i in range(0, len(markers)):
        if markers.count(markers[i]) > 1:
            break
        if i == len(markers) - 1:
            cleared = True

    return cleared
            

def shiftMarkers(markers, newItem):
    for i, item in enumerate(markers):
        if i < len(markers) - 1:
            markers[i] = markers[i + 1]
        else:
            markers[i] = newItem


def analyzeSignal(signal, packetSize):
    markers = []
    startSequenceIndex = None;
    for i, item in enumerate(signal):
        if i < packetSize:
            markers.append(item)
            if i == packetSize - 1:
                if analyzeMarkers(markers):
                    startSequenceIndex = i
                    break
        else:
            if analyzeMarkers(markers):
                    startSequenceIndex = i
                    break
            shiftMarkers(markers, item)

    return startSequenceIndex


def main(input):
    for  signal in input:
        answer = analyzeSignal(signal, 4)
        print(f"Found our thing {answer}")
        return answer

def main2(input):
    for signal in input:
        answer = analyzeSignal(signal, 14)
        print(f"found our answer {answer}")


main2(input)
