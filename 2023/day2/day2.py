f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def main(input):
    valid_game_ids = []
    valid_game_sum = 0
    required_cubes_per_game = {}
    power_sum = 0
    
    for game in input:
        min_cube_values = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        is_game_valid = True;
        game_id = game.split(":")[0].split()[1]
        rounds = game.split(":")[1].split(";")
        for round in rounds:
            draws = round.split(',');
            for draw in draws:
                quantity = draw.split()[0]
                color = draw.split()[1]

                if int(quantity) > LIMITS[color]:
                    is_game_valid = False;
        
                if int(quantity) > min_cube_values[color]:
                    min_cube_values[color] = int(quantity)

        required_cubes_per_game[game_id] = min_cube_values
                
        if is_game_valid:
            valid_game_ids.append(game_id)

    for game in valid_game_ids:
        valid_game_sum += int(game)

    for key in required_cubes_per_game:
        game_id = key
        min_red_cubes = required_cubes_per_game[game_id]["red"]
        min_green_cubes = required_cubes_per_game[game_id]["green"]
        min_blue_cubes = required_cubes_per_game[game_id]["blue"]
        power_of_cubes = min_blue_cubes * min_green_cubes * min_red_cubes
        power_sum += power_of_cubes
    
    print(f"valid game sum... {valid_game_sum}")
    print (f"power sum is... {power_sum}")
            
main(input)
