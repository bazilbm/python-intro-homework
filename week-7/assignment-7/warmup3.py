#Warmup 3: Use the os Module

#1. Print your current working directory using os.getcwd(). 
import os 
print(os.getcwd()) 

#2. Check whether ../data/expenses.csv exists using os.path.exists(). Print "expenses.csv found." or "expenses.csv not found." accordingly.
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

#3. Use os.path.join() to build the path "../data/expenses.csv" from its parts ("..", "data", "expenses.csv") and print the result.
path = os.path.join("..", "data", "expenses.csv")
print(path)

