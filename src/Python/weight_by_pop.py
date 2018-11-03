import csv

new_rows = []
with open('chemicals.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    i = 0
    for row in reader:
        new_row = row
        if new_row[2] == 'Non Detect':
            new_row.append('0.0')
        elif new_row[2] == 'Less than or equal MCL':
            new_row.append('0.0')
        else:
            new_row.append(str(1.0 * float(new_row[5])))
        new_rows.append(new_row)
        if i % 1000 == 0:
            # print(i + 'th row', end='\r', flush=True)
            print(i, new_row)
        i += 1

with open('new.csv', 'w') as f:
    # Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)
