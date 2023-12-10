# https://adventofcode.com/2023/day/4

import logging.config
from pathlib import Path

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

logging.config.fileConfig(fname=logging_config_path, disable_existing_loggers=False)
log = logging.getLogger(__name__)

script_path = Path(__file__).parent
logging_config_path = script_path.parent / 'logging_config.ini'

f = open(script_path / 'day4_input.txt')

total_wins_ct = 0
total_points = 0

# Each line is a separate "game"
for card in f:
    card_wins_ct = 0

    # Card number is always in this position
    # Casting as int will strip out the spaces
    card_number = int(card[4:8])

    # Split the remaining card info at the pipe
    # Take the left side store winning numbers as a list (split on spaces)
    # Take the right side store "your numbers" as a list (split on spaces, strip out the line break)
    winning_numbers = card[10:].split(' | ')[0].split(' ')
    your_numbers = card[10:].split(' | ')[1].replace('\n', '').split(' ')

    # Overwrite winning numbers as a new list without empty/white-space strings
    winning_numbers = [x for x in winning_numbers if x.strip()]

    for n in your_numbers:
        if n in winning_numbers:
            card_wins_ct += 1
            total_wins_ct += 1
            log.debug(f'Card {card_number}: {n} wins! Card wins: {card_wins_ct}; Total wins: {total_wins_ct}')

    if card_wins_ct == 0:
        card_points = 0
    else:
        card_points = 2 ** (card_wins_ct - 1)
        total_points += card_points

    log.debug(f'Card {card_number}: has {total_wins_ct} wins and is worth {card_points}')
    log.debug(f'Total points: {total_points}')