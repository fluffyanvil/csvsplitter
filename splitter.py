import csv
import argparse

parser = argparse.ArgumentParser(description="Split csv grouped by specified column",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-c", "--column", type=int, help="column number (starts from 0, i.e. if you want split by 10th column, use 9)", default=9)
parser.add_argument("-f", "--file", help="input .csv file", required=True, default="test.csv")
args = parser.parse_args()
config = vars(args)
print(config)

column = args.column if args.column else 9
file = args.file

# Open the original CSV file
with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='|')
    
    # Find all unique values in the 10th column
    unique_values = set()
    for row in csv_reader:
        unique_values.add(row[column])
        
    # Reset the file pointer to the beginning of the CSV file
    csvfile.seek(0)
    
    # Create a dictionary to store the rows for each unique value in column J
    rows_by_value = {value: [] for value in unique_values}
    
    # Split the rows by unique value in column J
    for row in csv_reader:
        rows_by_value[row[column]].append(row)
        
    # Save each group of rows to a separate CSV file
    for value, rows in rows_by_value.items():
        filename = f'test_{value}.csv'
        with open(filename, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile, delimiter='|')
            csv_writer.writerows(rows)
