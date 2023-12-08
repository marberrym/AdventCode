f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

def numeric(input):
    return input.isnumeric()

def find_win_count(winning_numbers, game_numbers):
    win_count = 0
    for number in game_numbers:
        if number in winning_numbers:
            win_count += 1
    return win_count

def find_point_value(win_count):
    points = 0
    if win_count > 0:
        points = 1
        multipliers = win_count - 1
        for _ in range(multipliers): points = points * 2
    return points

def play_card(game):
    winning_numbers, game_numbers = game.split("|")
    winning_numbers = list(filter(numeric, winning_numbers.strip().split(" ")))
    game_numbers = list(filter(numeric, game_numbers.strip().split(" ")))
    win_count = find_win_count(game_numbers, winning_numbers)
    return {
        'win_count': find_win_count(game_numbers, winning_numbers),
        'point_value': find_point_value(win_count)
    }


def play_additional_cards(card_counts, additional_cards, input):
    for x in additional_cards:
        results = play_card(input[x - 1].split(":")[1])

        if x in card_counts.keys(): card_counts[x] += 1
        else: card_counts[x] = 1

        if results['win_count'] > 0:
            additional_cards = range(x + 1, x + results['win_count'] + 1)
            card_counts = play_additional_cards(card_counts, additional_cards, input)

    return card_counts

def main(input):
    total_points = 0
    total_cards = 0
    card_counts = {}

    #P1
    for card in input:
        card_number, game = card.split(":")
        results = play_card(game)
        total_points += results['point_value']

    #P2
    for card_idx, card in enumerate(input):
        card_number, game = card.split(":")
        card_number = int(card_number.split()[1].strip())
        results = play_card(game)

        if card_number in card_counts.keys(): card_counts[card_number] += 1
        else: card_counts[card_number] = 1

        if results['win_count'] > 0:
            additional_cards = range(card_idx + 2, card_idx + results['win_count'] + 2)
            card_counts = play_additional_cards(card_counts, additional_cards, input)

    for val in card_counts.values(): total_cards += val 

    # P1
    print(f"Total points: {total_points}")
    # P2
    print(f"Total cards: {total_cards}")

main(input)
