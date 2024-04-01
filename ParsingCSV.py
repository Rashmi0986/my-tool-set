# Brute force solution
csv_mapping_list = []
with open("/path/to/data.csv") as my_data:
  line_count = 0
  for line in my_data:
    row_list = [val.strip() for val in line.split(",")]
    if line_count == 0:
      header = row_list
    else:
      row_dict = {key: value for key, value in zip(header, row_list)}
      csv_mapping_list.append(row_dict)
    line_count += 1

# CSV reader solution
import csv
csv_mapping_list = []
with open("/path/to/data.csv") as my_data:
    csv_reader = csv.reader(my_data, delimiter=",")
    line_count = 0
    for line in csv_reader:
        if line_count == 0:
            header = line
        else:
            row_dict = {key: value for key, value in zip(header, line)}
            csv_mapping_list.append(row_dict)
        line_count += 1

# CSV DictReader solution
import csv
with open("/path/to/dict.csv") as my_data:
    csv_mapping_list = list(csv.DictReader(my_data))
