import logging.config
from pathlib import Path
import re

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

logging.config.fileConfig(fname=logging_config_path, disable_existing_loggers=False)
log = logging.getLogger(__name__)

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

total_power = 0

f = open(script_path / 'day2_input.txt')

# Each line is a separate "game"
for game in f:
    max_red_cubes = None
    max_green_cubes = None
    max_blue_cubes = None

    game_number = int(re.findall(r'^Game (\d+):', game)[0])

    red_pulls = re.findall(r'(\d+) red', game)
    for r in red_pulls:
        red_cubes = int(r)
        if not max_red_cubes or red_cubes > max_red_cubes:
            max_red_cubes = red_cubes

    green_pulls = re.findall(r'(\d+) green', game)
    for r in green_pulls:
        green_cubes = int(r)
        if not max_green_cubes or green_cubes > max_green_cubes:
            max_green_cubes = green_cubes

    blue_pulls = re.findall(r'(\d+) blue', game)
    for r in blue_pulls:
        blue_cubes = int(r)
        if not max_blue_cubes or blue_cubes > max_blue_cubes:
            max_blue_cubes = blue_cubes

    # If we've gotten this far, the game is possible
    # Return the ID number to be added to the tally
    power = max_red_cubes * max_green_cubes * max_blue_cubes
    total_power += power
    log.debug(f'Game {game_number} mins: {max_red_cubes} | {max_green_cubes} | {max_blue_cubes}. Power: {power} | {total_power}')

print(f'Total Power: {total_power}')