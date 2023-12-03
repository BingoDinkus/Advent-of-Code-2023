import logging.config
from pathlib import Path
import re

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

logging.config.fileConfig(fname=logging_config_path, disable_existing_loggers=False)
log = logging.getLogger(__name__)

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

possible_game_tally = 0
max_red_cubes = 12
max_green_cubes = 13
max_blue_cubes = 14

f = open(script_path / 'day2_input.txt')

def test_game(game):
    red_cubes = 0
    green_cubes = 0
    blue_cubes = 0

    game_number = int(re.findall(r'^Game (\d+):', game)[0])

    red_pulls = re.findall(r'(\d+) red', game)
    for r in red_pulls:
        red_cubes = int(r)
        if red_cubes > max_red_cubes:
            # Game is not possible, skip to next game
            log.debug(f'{red_cubes} red cubes. Game {game_number} not possible. Tally: {possible_game_tally}')
            return 0

    green_pulls = re.findall(r'(\d+) green', game)
    for r in green_pulls:
        green_cubes = int(r)
        if green_cubes > max_green_cubes:
            # Game is not possible, skip to next game
            log.debug(f'{green_cubes} green cubes. Game {game_number} not possible. Tally: {possible_game_tally}')
            return 0

    blue_pulls = re.findall(r'(\d+) blue', game)
    for r in blue_pulls:
        blue_cubes = int(r)
        if blue_cubes > max_blue_cubes:
            # Game is not possible, skip to next game
            log.debug(f'{blue_cubes} blue cubes. Game {game_number} not possible. Tally: {possible_game_tally}')
            return 0

    # If we've gotten this far, the game is possible
    # Return the ID number to be added to the tally
    log.debug(f'Game {game_number} is possible. Tally: {possible_game_tally}')
    return game_number

# Each line is a separate "game"
for game in f:
    possible_game_tally += test_game(game)


print(f'Sum of possible game IDs: {possible_game_tally}')