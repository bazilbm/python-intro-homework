#Warmup 2: Safe Division
#Ask the user for two numbers.
while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        #Compute the result of dividing the first by the second.
        result = numerator / denominator
        #If denominator is not zero, print normal and break.
        print(f"{numerator} ÷ {denominator} = {result}")
        break
    #Catch the crash that normally happens when dividing by zero and print message to try a non-zero denominator.
    except ZeroDivisionError:
        print("Can't divide by zero. Please try a non-zero denominator.")