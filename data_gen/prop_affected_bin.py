import csv

new_rows = []
data = {'0': {'fips': ('state_name', 'county_name', 'county_pop', 'severity')}}
yrs = []
threshold = 0.01
compound_to_examine = 'Arsenic'
states_to_examine = ['California', 'Connecticut', 'Florida']


with open('new.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    i = 0
    for row in reader:
        county_name = row[3]
        state = row[6]
        fips = row[10]
        year = row[9]
        pop_served = row[5]
        severity = row[12]
        compound = row[1]
        if compound == compound_to_examine and state in states_to_examine:
            if year in data.keys():
                data_for_yr = data[year]
            else:
                data[year] = {}
                data_for_yr = data[year]
            if fips in data_for_yr.keys():
                data_for_fips = data_for_yr[fips]
                data_for_fips = (state, county_name, data_for_fips[2] + float(pop_served),
                                 data_for_fips[3] + float(severity))
            else:
                data_for_fips = (state, county_name, float(pop_served), float(severity))
            data_for_yr[fips] = data_for_fips
            data[year] = data_for_yr
        if i % 1000 == 0:
            # print(i + 'th row', end='\r', flush=True)
            print(i)
        i += 1

header_row = ['year', 'county', 'state', 'contamination_proportion']
to_write=[]
data.pop('0')
for year, datum in data.items():
    for fips, county_data in datum.items():
        bin_flag = 0.0
        if county_data[2] != 0:
            if county_data[3] / county_data[2] > threshold:
                bin_flag = 1.0
            new_entry = [year, county_data[1], county_data[0], bin_flag]
            to_write.append(new_entry)

print(to_write[0], to_write[5], len(to_write))
name = compound_to_examine + 'proportion_affected_binary.csv'

with open(name, 'w') as f:
    # Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerow(header_row)
    writer.writerows(to_write)

counties_data = {'county_name' : {'year': [['other_stuff']]}}

with open(name, 'r', encoding='utf-8') as f:
    next(f)
    reader = csv.reader(f)
    i = 0
    for row in reader:
        state = row[2]
        if state in states_to_examine:
            county_name = row[1] + ' County, ' + state
            year = row[0]
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
            print(counties_data[county_name])
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

with open(name, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        header_row = row
        break

with open('earnings.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        header_row += row[3:-1]
        break

# print(type(new_rows))
# header_row.append(new_rows)
# new_rows = header_row
# print(type(new_rows))
# print(new_rows[0], new_rows[5])
name = compound_to_examine + 'prop_affected_bin_new.csv'

with open(name, 'w') as f:
    # Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerow(header_row)
    writer.writerows(new_rows)
