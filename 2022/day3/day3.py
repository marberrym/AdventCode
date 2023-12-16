f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();
import string

# Common

def prepPriorities():
    priorities = {}
    priorityLevel = 1;
    for letter in list(string.ascii_lowercase):
        priorities[letter] = priorityLevel
        priorityLevel += 1
    for letter in list(string.ascii_uppercase):
        priorities[letter] = priorityLevel
        priorityLevel += 1
    return priorities

priorities = prepPriorities()


# Part one
def getDuplicateItems(firstCompartment, secondCompartment):
    duplicateItems = []
    firstPackContents = [*firstCompartment]
    for item in secondCompartment:
        if item in firstPackContents and item not in duplicateItems:
            duplicateItems.append(item)
    return duplicateItems

def main(packs):
    duplicatePrioritySum = 0
    prepPriorities()
    for pack in packs:
        firstCompartment = pack[slice(0, len(pack)//2)]
        secondCompartment = pack[slice(len(pack)//2, len(pack))]
        duplicates = getDuplicateItems(firstCompartment, secondCompartment)
        
        for duplicate in duplicates:
            duplicatePrioritySum += priorities[duplicate]
        

    print(duplicatePrioritySum)

# Part two
def splitIntoGroups(packs, groupSize):
    groups = []
    for i in range(0, len(packs), groupSize):
        groups.append(packs[i:i + groupSize])
    return groups

def findBadgeItem(group):
    badgeItem = None
    potentialBadgeItems = [];
    firstPackContents = [*group[0]]

    for item in group[1]:
        if item in firstPackContents and item not in potentialBadgeItems:
            potentialBadgeItems.append(item)

    for item in group[2]:
        if item in firstPackContents and item in potentialBadgeItems:
            badgeItem = item
        else:
            if item in potentialBadgeItems:
                potentialBadgeItems.remove(item)
    
    return badgeItem


def main2(packs):
    badgeItemPrioritySum = 0
    packsSplitByGroup = splitIntoGroups(packs, 3)

    for group in packsSplitByGroup:
        badgeItem = findBadgeItem(group)
        badgeItemPrioritySum += priorities[badgeItem]

    print(badgeItemPrioritySum)
    return badgeItemPrioritySum


main2(input)
