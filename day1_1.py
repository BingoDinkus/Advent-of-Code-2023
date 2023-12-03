running_total = 0
f = open('day1_calibration.txt', 'r')

# Loop through each line in the file
for l in f:
    # Loop through in character in the line
    first_num = None
    last_num = None
    for c in l:
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

# Output the answer
print(running_total)