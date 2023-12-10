# https://adventofcode.com/2023/day/5

import logging.config
from pathlib import Path
import re

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

logging.config.fileConfig(fname=logging_config_path, disable_existing_loggers=False)
log = logging.getLogger(__name__)

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'
log.setLevel(logging.INFO)

f = open(script_path / 'day6_input.txt')

line_ct = 1

log.debug('Reading file')
for line in f:
    # Look from character 13 on to cut out row header
    # Split on spaces, and ignore items that are only space/empty string
    l = [x for x in line[12:].split(' ') if x.strip()]
    log.debug(f'[{line_ct}]: {len(l)} values read')

    # If the line starts with Time, put the values in the time list
    # Otherwise, throw them in the distance list
    if line.startswith('Time'):
        log.debug(f'Concatenating and assigning values to time list: {l}')
        time = int(''.join(l))
        log.debug(f'Time: {time}')
    else:
        log.debug(f'Concatenating and assigning values to distance list: {l}')
        distance = int(''.join(l))
        log.debug(f'Distance: {distance}')

    line_ct += 1

win_ct = 0
# Loop through each millisecond in the time
for ms_held in range(1, time + 1):
    distance_traveled = ms_held * (time - ms_held)
    if distance_traveled > distance:
        win_ct += 1
        log.debug(f'[{time}, {distance}] Holding for {ms_held} ms gives us {distance_traveled} mm, which exceeds {distance}. win_ct is now at {win_ct}.')
    else:
        log.debug(f'[{time}, {distance}] Holding for {ms_held} ms gives us {distance_traveled} mm, which does not exceed {distance}. win_ct is now at {win_ct}.')

log.info(f'Race has {win_ct} ways to win')

print(f'The final answer is {win_ct}')