import sys

print(len(sys.argv[1:]))

country = sys.argv[3]

with open('Olympic Athletes - athlete_events.tsv', 'r') as file:
    lines = file.readlines()
    next_line = file.readline()
    while next_line:
        # do stuff with line
        next_line = file.readline()