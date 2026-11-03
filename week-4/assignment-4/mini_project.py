#Part 2: Mini-Project - Student Roster Analyzer
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
#Top Scorer
top_score = 0
top_scorer = ""
#Class size
total = 0
class_size = len(students)
# Set of subjects
subjects = set()
#List high scorers
high_scorers = []
#Looping through students
for student in students:
    score = student["score"]
    #update total amount of scores after its defined
    total += score
    subjects.add(student["subject"])
    #Calculating top scorer.
    if score > top_score:
        top_score = score
        top_scorer = student["name"]
    #Calculate high scorers.
    if student["score"] > 75:
        high_scorers.append(student["name"])
#After looping, calculate class average
class_average = total / class_size

print(f"Top scorer:     {top_scorer} ({top_score})")
print(f"Class average:  {class_average:.2f}")
print(f"Subjects offered: {subjects}")
print(f"High scorers:   {high_scorers}")
