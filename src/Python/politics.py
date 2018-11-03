# -*- coding: utf-8 -*-
import csv

governor_at_year = {'0': {'state_name':'R/D'}}
to_write = []

with open('states_party_strength_cleaned.csv', 'r', encoding="utf-8") as f:
    next(f)
    reader = csv.reader(f)
    i = 0
    for row in reader:
        yr = row[1]
        state = row[0]
        party = row[7]
        if party != 'R' and party != 'D':
            party = 'I'
        if yr in governor_at_year.keys():
            state_dict = governor_at_year[yr]
        else:
            state_dict = {}
        state_dict[state.title()] = party
        governor_at_year[yr] = state_dict
        if i % 1000 == 0:
            # print(i + 'th row', end='\r', flush=True)
            print(i)
        i += 1

print(governor_at_year['1999'])
new_rows = [['year', 'county', 'state', 'contamination_proportion', 'party']]

with open('county.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    i = 0
    for row in reader:
        new_row = row
        print(row[2])
        print(row[0])
        if row[0] != '2016':
            new_row.append(governor_at_year[row[0]][row[2]])
            new_rows.append(new_row)
        if i % 1000 == 0:
            # print(i + 'th row', end='\r', flush=True)
            print(i, new_row)
        i += 1

with open('political_data.csv', 'w', encoding="utf-8") as f:
    # Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)
