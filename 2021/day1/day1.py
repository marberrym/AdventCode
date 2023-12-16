from os import read


f = open('input.txt', 'r');
readings = f.read().splitlines();


testStuff = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263,
]

def main1(readings):
    descents, prevReading = 0, None;

    for reading in readings:
        if prevReading is not None:
            if int(reading) > prevReading:
                descents += 1

        prevReading = int(reading)

    return descents

def main2(readings):
    descents, prevReading, reading = 0, None, None;

    for x in range(len(readings)):
        if (x!=0 and x!=len(readings) - 1):
            reading = int(readings[x] + readings[x-1] + readings[x+1])

        if reading is not None and prevReading is not None:
            if reading > prevReading:
                descents += 1

        prevReading = reading
    return descents


# print(readings);
print(main1(readings));
print(main2(readings));
