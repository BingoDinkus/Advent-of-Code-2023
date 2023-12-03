# https://adventofcode.com/2023/day/1

import logging
import logging.config
from pathlib import Path

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

logging.config.fileConfig(fname=logging_config_path, disable_existing_loggers=False)
log = logging.getLogger(__name__)

line_ct = 0
running_total = 0
f = open(script_path / 'day1_calibration.txt', 'r')

# To be as lazy as possible, swap spelled out numbers
# with actual numbers
words = {
    'one': '1'
    , 'two': '2'
    , 'three': '3'
    , 'four': '4'
    , 'five': '5'
    , 'six': '6'
    , 'seven': '7'
    , 'eight': '8'
    , 'nine': '9'
}

# Loop through each line in the doc
for l in f:
    line_ct += 1
    first_num = None
    last_num = None
    cleaned_line = ''

    for x in range(len(l)):
        if l[x].isdigit():
            cleaned_line += l[x]
        else:
            for k, v in words.items():
                if l[x:x + len(k)] == k:
                    cleaned_line += v

    log.debug(f'[{line_ct:4}] -> {cleaned_line}')

    # Loop through in character in the line
    for c in cleaned_line:
        if c.isdigit():
            # If first_char is None, this is the first match
            # The spec is tricky... there's not always two numbers
            # The first match is also the final match if there's only one number
            if not first_num:
                first_num = c
                last_num = c
            # Otherwise this is not the first match
            # Store it in last char and let it get
            # overwritten if more matches are found
            else:
                last_num = c

    # If both numbers are found, concatenate them
    # and add the result to the running total
    if first_num and last_num:
        running_total += int(first_num + last_num)

    log.debug(f'[{line_ct:4}] [{first_num} | {last_num}] [{running_total}]: {l}')

# Output the answer
print(f'Final Answer: {running_total}')