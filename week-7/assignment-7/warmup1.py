#Warmup 1: Read a Text File Line by Line
"""Open the file in as read only and automatically close it when the block exits."""
with open("../data/notes.txt", "r") as file:
    """Convert all lines from the file to a list."""
    lines = file.readlines()
    """Define starting counter variable."""
    line_num = 1
    """Loop through the file one line at a time."""
    for line in lines:
        """Print the current counter value with a label and no space."""
        print(f"Line {line_num}: {line.strip()}")
        """Add 1 to variable for each line after each pass."""
        line_num += 1