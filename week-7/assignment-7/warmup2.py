#Warmup 2: Read a CSV with DictReader
import csv
"""Open the file as read only and automatically close it when the block exits."""
with open("../data/students.csv", "r") as file:
    """Read the file row by row as a dictionary using header row as key."""
    reader = csv.DictReader(file)
    """Loop through the file one line at a time."""
    for row in reader:
        """Print each name followed by a colon and score"""
        #Used an f-string for a cleaner look as a comma with colon in quotation marks created a space between the name a colon.
        print(f"{row['name']}: {row['score']}")