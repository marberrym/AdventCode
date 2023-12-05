f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

DIGITS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def reverse_string(string):
    return string[::-1]

def find_first_digit(command):
    letters = "";
    target_digit = None;
    spelled_digits = DIGITS.keys();
    for char in command:
        if char.isnumeric():
            return char
        else:
            letters += char
            for number in spelled_digits:
                if number in letters or reverse_string(number) in letters:
                    return DIGITS[number]


def main(input):
    callibration_values = []
    callibration_sum = 0

    for command in input:
        first_digit = find_first_digit(list(command))
        last_digit = find_first_digit(list(reversed(command)))
        callibration_values.append(f"{first_digit}{last_digit}")
    
    for value in callibration_values:
        callibration_sum += int(value)
    
    print(f"Callibration sum is: {callibration_sum}")
    return callibration_sum

main(input)
