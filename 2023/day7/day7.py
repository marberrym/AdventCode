f = open('input.txt', 'r');
puzzle_input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();
from collections import Counter

FIVE_OF_A_KIND = "Five of a kind"
FOUR_OF_A_KIND = "Four of a kind"
FULL_HOUSE = "Full house"
THREE_OF_A_KIND = "Three of a kind"
TWO_PAIR = "Two pair"
ONE_PAIR = "One pair"
HIGH_CARD = "High card"

card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

def remove_card(hand, card):
    return [c for c in hand if c != card]


def find_pair(hand):
    for idx, card in enumerate(hand):
        if hand.count(card) == 2:
            return True
        elif idx == len(hand) - 1:
            return False


def analyze_hand(hand):
    cards = list(hand)
    counts = sorted(Counter(cards).values(), reverse=True)

    if counts[0] == 5:
        return {"hand_type": FIVE_OF_A_KIND}
    if counts[0] == 4:
        return {"hand_type": FOUR_OF_A_KIND}
    if counts[0] == 3 and counts[1] == 2:
        return {"hand_type": FULL_HOUSE}
    if counts[0] == 3:
        return {"hand_type": THREE_OF_A_KIND}
    if counts[0] == 2 and counts[1] == 2:
        return {"hand_type": TWO_PAIR}
    if counts[0] == 2:
        return {"hand_type": ONE_PAIR}
    return {"hand_type": HIGH_CARD}

def sort_hands(hands):
    return sorted(hands, key=lambda hand: [card_values[c] for c in hand], reverse=True)


def main(puzzle_input):
    hands = {
        FIVE_OF_A_KIND: [],
        FOUR_OF_A_KIND: [],
        FULL_HOUSE: [],
        THREE_OF_A_KIND: [],
        TWO_PAIR: [],
        ONE_PAIR: [],
        HIGH_CARD: []
    }

    ranked_hands = []
    total_winnings = 0

    for line in puzzle_input:
        hand = line.split()[0]
        analyzed_hand = analyze_hand(hand)
        hand_type = analyzed_hand['hand_type']

        hands[hand_type].append(hand)

    for hand_type in hands.keys():
        hands[hand_type] = sort_hands(hands[hand_type])
        ranked_hands.extend(hands[hand_type])
        print(hand_type, hands[hand_type], "\n")

    for line in puzzle_input:
        hand, bid = line.split()
        ranking = list(reversed(ranked_hands)).index(hand) + 1
        winnings = ranking * int(bid)
        total_winnings += winnings
        print("Hand: ", hand, " Bid: ", bid, " Winnings: ", winnings, " Ranking... ", ranking)

    for idx, rank in enumerate(list(reversed(ranked_hands))):
        print (idx + 1, rank)


    print("Total winnings: ", total_winnings)

#  250950896
main(puzzle_input)

