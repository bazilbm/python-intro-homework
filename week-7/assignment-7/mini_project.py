#Part 2: Mini-Project — Expense Report Generator
import csv
import os
from datetime import datetime
now = datetime.now()
#1. Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. If it doesn't, print an error message and stop.
if os.path.exists("../data/expenses.csv"):
    print("Found it!")
else:
    print("File not found.")
    exit()
#2. Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.
with open("../data/expenses.csv", "r") as file:
    #Read the file row by row as a dictionary using header row as key.
    records = list(csv.DictReader(file))
#Loop through the file one line at a time.
for item in records:
    #3. Convert the amount field to float for each row.
    item["amount"] = float(item["amount"])
#4. Filter the list to only rows where category is "Food"
food = [item for item in records if item["category"] == "Food"]
#5. Calculate the total amount spent on Food.
total = sum(item["amount"] for item in food)
print(f"Food: ${total:.2f}")
#6. Write a report to food_report.txt with this structure:
report_name = "food_report.txt"
with open(report_name, "w") as report:
    #First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
    report.write(f"Food Expense Report — generated {now.strftime("%B %d, %Y")}\n")
    #One line per food expense: [date]: $[amount]
    for row in food:
        report.write(f"{row['date']}: ${row['amount']:.2f}\n")
        #Last line: Total: $[total to 2 decimal places]
    report.write(f"Total: ${total:.2f}")