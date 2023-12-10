# https://adventofcode.com/2023/day/9

import logging.config
from pathlib import Path

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

logging.config.fileConfig(fname=logging_config_path, disable_existing_loggers=False)
log = logging.getLogger(__name__)

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'
log.setLevel(logging.DEBUG)

def extrapolate(l):
    seq = []
    for i in range(1, len(l)):
        seq.append(l[i] - l[i - 1])

    all_zeros = True
    for x in seq:
        if x != 0:
            all_zeros = False
            continue

    return seq, all_zeros

line_ct = 1
final_list = []
f = open(script_path / 'input.txt')

for line in f:
    seq = []
    # Split the line into a list of numbers
    seq.append([int(n) for n in line.split(' ')])

    finished = False
    while not finished:
        # Extrapolate data for the last line
        ex, all_zeros = extrapolate(seq[-1])
        seq.append(ex)

        # If the sum of the list is 0, then all elements are 0
        # and we're done extrapolating
        finished = all_zeros

    if line_ct == 1:
        log.debug(f'Phase 1:')
        for r in seq:
            row_output = ''
            for c in r:
                row_output += f'{c:7}'
            log.debug(row_output)


    # Loop through list backwards, starting with the second from the bottom
    for i in range(len(seq) - 2, -1, -1):
        curr_row_first = seq[i][0]
        next_row_first = seq[i  + 1][0]
        new_value = curr_row_first - next_row_first
        log.debug(f'[{line_ct:3}] Row {i}, {curr_row_first} - {next_row_first} = {new_value}')
        seq[i].insert(0, new_value)


    if line_ct == 1:
        log.debug(f'Phase 2:')
        for r in seq:
            row_output = ''
            for c in r:
                row_output += f'{c:7}'
            log.debug(row_output)

    # Take the final element from the first row and add it to our final list
    final_list.append(seq[0][0])

    line_ct += 1

log.debug(final_list)

# Now that all the extrapolation has been completed
# Sum the final element of each row in the final list
final_answer = 0
for n in final_list:
    final_answer += n

print(f'The final answer is: {final_answer}')