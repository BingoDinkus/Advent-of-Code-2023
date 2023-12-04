# https://adventofcode.com/2023/day/3

import logging.config
from pathlib import Path
import re

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

logging.config.fileConfig(fname=logging_config_path, disable_existing_loggers=False)
log = logging.getLogger(__name__)

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

part_number_tally = 0
symbols_set = {'@', '#', '$', '%',  '&',  '*', '-', '/', '+', '='}

prev_line = None
curr_line = None
next_line = None

def symbol_check(line):
    for c in line:
        if c in symbols_set:
            return c

    return None

log.debug('Reading file')
lines = open(script_path / 'day3_input.txt', 'r').read().splitlines()


for r in range(len(lines)):
    line_number = r + 1
    curr_line = lines[r]

    if r > 0:
        prev_line = lines[r - 1]

    if r < len(lines) - 1:
        next_line = lines[r + 1]

    for m in re.finditer(r'(\d+)', curr_line):
        log.debug(f'[{line_number:3}] Match found: [{m.group()}]')

        # If the match is on the beginning of the line,
        # we can't check in front of it
        if m.start() == 0:
            start = 0
        else:
            start = m.start()  - 1

        # Similarly, if the match touches the end of the line,
        # we can 't check after it
        if m.end() == len(curr_line):
            end = m.end() - 1 # Same as len - 1
        else:
            end = m.end()

        # Check current line
        symbol = symbol_check(curr_line[start])
        if symbol:
            log.debug(f'[{line_number:3} ✔️ Part No. {m.group()} is valid due to {symbol} symbol before the number')
            part_number_tally += int(m.group())
            continue

        symbol = symbol_check(curr_line[end])
        if symbol:
            log.debug(f'[{line_number:3}] ✔️ Part No. {m.group()} is valid due to {symbol} symbol after the number')
            part_number_tally += int(m.group())
            continue

        if prev_line:
            # String slicing is non-inclusive
            # Add one to the end point
            symbol = symbol_check(prev_line[start:end + 1])
            if symbol:
                log.debug(f'[{line_number:3}] ✔️ Part No. {m.group()} is valid due to {symbol} symbol on the previous line')
                part_number_tally += int(m.group())
                continue

        if next_line:
            # String slicing is non-inclusive
            # Add one to the end point
            symbol = symbol_check(next_line[start:end + 1])
            if symbol:
                log.debug(f'[{line_number:3}] ✔️ Part No. {m.group()} is valid due to {symbol} symbol on the next line')
                part_number_tally += int(m.group())
                continue

        # If we haven't already aborted loop, match is not valid
        log.debug(f'[{line_number:3}] ❌ Part No. {m.group()} is NOT valid')

    # Line processing complete
    log.debug(f'-> After line {line_number}, tally is: {part_number_tally}')
    line_number += 1

# Final answer
log.debug(f'The final answer is: {part_number_tally}')
print(f'The final answer is: {part_number_tally}')