#Mini-Project — Defensive CSV Reader
import os
import csv
import sys
#Try to locate and read the csv file into a list of dictionaries
try:
    path = os.path.join("..","data", "messy_data.csv")
    with open(path, "r") as file:
        #Maps each row to a dictionary using the first row as keys
        reader = csv.DictReader(file)
        rows = list(reader)
#If the file is missing, print an error message and stop.
except FileNotFoundError:
    sys.exit("File does not exist.")
#Run data if the file was successfully loaded.
else:
    skipped_rows = []
    clean_rows = []
    #Loop through each row, starting the counter at 1.
    for row_number, row in enumerate(rows, start=1):
        #Store extra columns under a None key.
        if None in row:
            key_error_message = f"Row {row_number}: extra column detected — skipped"
            skipped_rows.append(key_error_message)
            continue #Skip to the next row.
        #Validate and convert row values into the expected data types
        try:
            entry = {
                "name" : row["name"], 
                "category" : row["category"],
                "amount" : float(row["amount"]) #Fail if not a float.
            }
            clean_rows.append(entry)
        #Catch all for rows that can't be converted to a float.
        except ValueError as e:
            value_error_message = f"Row {row_number}: ValueError — {e}"
            skipped_rows.append(value_error_message)
        #Catch rows missing an expected column key.
        except KeyError as e:
            key_error_message = f"Row {row_number}: KeyError — missing key {e}"
            skipped_rows.append(key_error_message)
    #Calculate summary counts.
    skipped_total = len(skipped_rows)
    clean_total = len(clean_rows)
    total = skipped_total + clean_total
#Display summary report.        
print(f"===CSV Report===")
print(f"Rows attempted: {total}")
print(f"Rows Parsed:    {clean_total}")
print(f"Rows Skipped:   {skipped_total}")
#Line Space.
print()
#Display all skipped row error messages.
print(f'Skipped rows:')
for row in skipped_rows:
    #print(f" {row}")
    print(row)
#Line Space.
print()
#Display formatted valid rows with amounts rounded two decimal places.
print(f"Clean data:")
for row in clean_rows:
    print(f"{row['name']} | {row['category']} | ${row['amount']:.2f}")