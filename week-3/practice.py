name = input("What is your name? ")
age = int(input("How old are you? "))
medication = input("Do you take any medication? (yes/no): ").lower()

if age < 19:
    print("Sorry, " + name + ", intermittent fasting is not recommended due to active growth and high nutrient demands.")
elif age < 40 and medication == "yes":
    print("Caution, " + name + "! Check with your healthcare provider before starting intermittent fasting.")
elif age < 40 and medication == "no":
    print("Hello, " + name + "! 16:8 or 16 hours fasting and 8 hours eating is a great way for you to achieve goals such as weight loss, elevated energy, and blood sugar balance.")
elif age <= 70 and medication == "yes":
    print("Caution, " + name + "! Check with your healthcare provider before starting intermittent fasting.")
elif age <= 70 and medication == "no":
    print("Hello, " + name + "! 12:12 or 12 hours fasting and 12 hours eating is a great way for you to achieve goals such as weight loss, elevated energy, and blood sugar balance.")
if age >= 71:
    print("Caution, " + name + "! Intermittent fasting should be approached with caution under supervision of your medical provider or avoided all together.")
