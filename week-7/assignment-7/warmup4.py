#Warmup 4: Use the datetime Module
from datetime import datetime
now = datetime.now() #Variable that gets and stores the current date and time from your computer. 
print(f"Today is {now.strftime("%B %d, %Y")}.") #Formats date as a readable string using codes for month, day, and year.
