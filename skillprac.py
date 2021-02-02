import csv

with open('airlines.csv.xls') as airlines_file:
    csv_reader = csv.reader(airlines_file, delimiter=',')
    line_count, data_dicts = 0, {}
    for row in csv_reader:
        if line_count > 0:
            if row[1] not in data_dicts.keys():
                data_dicts[row[1]] = 1
            else:
                data_dicts[row[1]] += 1
        line_count += 1
    print(data_dicts)
    print(max(data_dicts, key=lambda a: data_dicts[a]), max(data_dicts.values()))
    print(min(data_dicts, key=lambda a: data_dicts[a]), min(data_dicts.values()))