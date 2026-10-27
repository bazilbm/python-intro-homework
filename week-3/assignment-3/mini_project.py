#Part 2: Mini-Project - Day Planner
#Ask user for day of the week and time of day.
day = input("Day of the week? ").lower()
time = input("Using morning, afternoon, or evening, what time of day is it? ").lower()
print (f"What day is it?  {day}")
print (f"What time of day? {time}")
if day == "monday":
    print("Suggestion: Monday is just the start. Take it easy to get through the rest of the week!")
elif day == "tuesday" and time == "morning":
    print("Suggestion: Rise and shine. Get started with a morning workout!")
elif day == "wednesday" and time == "afternoon":
    print("Suggestion: Hump day! Great time to reflect on tasks for the rest of the week.")
elif day == "friday" and time == "evening":
    print("Suggestion: TGIF! Perfect night to wind down and relax from a busy week!")
elif day == "saturday" or day == "sunday":
    print("Suggestion: It's the weekend! Enjoy the morning, afternoon, and evening!")
else:
    print("Sorry, you have entered an unrecognized day or time. Please enter another day.")
