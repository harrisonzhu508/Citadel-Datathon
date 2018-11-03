import csv

counties_data = {'county_name' : {'year': [['other_stuff']]}}
states_to_examine = ['California', 'Connecticut', 'Florida']
compound_to_examine = 'Nitrates'

with open('chemicals.csv', 'r', encoding='utf-8') as f:
    next(f)
    reader = csv.reader(f)
    i = 0
    for row in reader:
        state = row[6]
        compound = row[1]
        if state in states_to_examine and compound == compound_to_examine:
            county_name = row[3] + ' County, ' + state
            year = row[9]
            if county_name in counties_data.keys():
                data = counties_data[county_name]
            else:
                data = {}
            if year in data.keys():
                yr_data = data[year]
            else:
                yr_data = []
            yr_data.append(row)
            data[year] = yr_data
            counties_data[county_name] = data
        i += 1
        if i%1000 == 0:
            print(i)

new_rows = []
with open('earnings.csv', 'r', encoding='utf-8', errors='ignore') as f:
    next(f)
    reader = csv.reader(f)
    i = 0
    for row in reader:
        county = row[2]
        year = row[-1]
        if county in counties_data.keys():
            if year in counties_data[county].keys():
                new_row_a = counties_data[county][year]
                for new_row in new_row_a:
                    new_row = new_row + row[3:-1]
                    new_rows.append(new_row)

with open('chemicals.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        header_row = row
        break

with open('earnings.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        header_row += row[3:-1]
        break

print(header_row)
# print(type(new_rows))
# header_row.append(new_rows)
# new_rows = header_row
# print(type(new_rows))
# print(new_rows[0], new_rows[5])
name = compound_to_examine + 'ben_data.csv'

with open(name, 'w') as f:
    # Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerow(header_row)
    writer.writerows(new_rows)
