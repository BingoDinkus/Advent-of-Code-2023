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

f = open(script_path / 'day6_input.txt')

results = []
line_ct = 1

log.debug('Reading file')
for line in f:
    # Look from character 13 on to cut out row header
    # Split on spaces, and ignore items that are only space/empty string
    l = [int(x) for x in line[12:].split(' ') if x.strip()]
    log.debug(f'[{line_ct}]: {len(l)} values read')

    # If the line starts with Time, put the values in the time list
    # Otherwise, throw them in the distance list
    if line.startswith('Time'):
        log.debug(f'Assigning values to time list: {l}')
        time = l
    else:
        log.debug(f'Assigning values to distance list: {l}')
        distance = l

    line_ct += 1

# Loop through the lists and determine the ways to win
race_ct = 1
for t, d in zip(time, distance):
    win_ct = 0
    # Loop through each millisecond in the time
    for ms_held in range(1, t+1):
        distance_traveled = ms_held * (t - ms_held)
        if distance_traveled > d:
            win_ct += 1
            log.debug(f'[{t}, {d}] Holding for {ms_held} ms gives us {distance_traveled} mm, which exceeds {d}. win_ct is now at {win_ct}.')
        else:
            log.debug(f'[{t}, {d}] Holding for {ms_held} ms gives us {distance_traveled} mm, which does not exceed {d}. win_ct is now at {win_ct}.')

    results.append(win_ct)
    log.debug(f'Race {race_ct} has {win_ct} ways to win')

    race_ct += 1

log.debug(f'The number of ways to win for each race are: {results}')

# Multiply all the values in the results list to get the final answer
final_answer = 1
for i in results:
    final_answer *= i
log.debug(f'The final answer is: {final_answer}')
