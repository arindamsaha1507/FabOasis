import csv
import sys

def update_calcrule(csv_file, new_calcrule):
    # Read the CSV data
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]

    # Update calcrule value
    for row in rows:
        row['calcrule'] = new_calcrule

    # Write the updated data back to the CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <csv_file> <new_calcrule_value>")
        sys.exit(1)

    csv_filename = sys.argv[1]
    new_calcrule_value = sys.argv[2]
    update_calcrule(csv_filename, new_calcrule_value)
