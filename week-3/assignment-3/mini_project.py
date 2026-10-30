#Part 2: Mini-Project - Day Planner
#Ask user for day of the week and time of day.
day = input("Day of the week? ").lower()
time = input("Using morning, afternoon, or evening, what time of day is it? ").lower()
print (f"What day is it?  {day}")
print (f"What time of day? {time}")
#Any time for monday offers the same suggestion.
if day == "monday" and time == "morning":
    print("Suggestion: Monday is just the start. Take it easy to get through the rest of the week!")
elif day == "monday" and time == "afternoon":
    print("Suggestion: Steady! Pace your self with the tasks of the week.")
elif day == "monday" and time == "evening":
    print("Suggestion: Got through without a case of the Mondays! Be ready to hit it hard the rest of the week.")    
elif day == "tuesday" and time == "morning":
    print("Suggestion: Rise and shine. Get started with a morning workout!")
elif day == "tuesday" and time == "afternoon":
    print("Suggestion: Get your tasks done today as you're feeling great from you morning workout!")
elif day == "tuesday" and time == "evening":
    print("Suggestion: No better day to keep tasking; homework, housework, yard work...get it all done today!")
elif day == "wednesday" and time == "morning":
    print("Suggestion: Hump day! Great time to reflect on tasks for the rest of the week.")
elif day == "wednesday" and time == "afternoon":
    print("Suggestion: Keep forging along. The week is half over and it's a great time to stay ahead of your weekly plan!")
elif day == "wednesday" and time == "evening":
    print("Suggestion: Rejuvenate! Attend a midweek service and fellowship with friends!")
elif day == "friday" and time == "morning":
    print("Suggestion: Finally Friday! Finish strong, and complete anything on your plan that needs to be finished.")
elif day == "friday" and time == "afternoon":
    print("Suggestion: Almost there! Great time to set a plan for next week.")
elif day == "friday" and time == "evening":
    print("Suggestion: TGIF! Perfect time to wind down and relax from a busy week!")
elif day == "saturday" or day == "sunday":
    #Any time for saturday or sunday reflects the same suggestion.
    print("Suggestion: It's the weekend! Enjoy the morning, afternoon, and evening!")
else:
    print("Sorry, you have entered an unrecognized day or time. Please enter another day or time.")
