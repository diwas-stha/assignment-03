import csv
import os


def filter_adults(input_filename, output_filename):
    if not os.path.exists(input_filename):
        print(f"Input file '{input_filename}' does not exist.")
        return

    with open(input_filename, 'r', newline='') as input_file:
        read = csv.DictReader(input_file)
        adults_data = [row for row in read if int(row['Age']) >= 18]

    if not os.path.exists(output_filename):
        with open(output_filename, 'w', newline='') as output_file:
            fields = ['Name', 'Age']
            write = csv.DictWriter(output_file, fieldnames=fields)
            write.writeheader()

    with open(output_filename, 'a', newline='') as output_file:
        write = csv.DictWriter(output_file, fieldnames=fields)
        write.writerows(adults_data)


input_filename = "data.csv"
output_filename = "adults.csv"
filter_adults(input_filename, output_filename)
