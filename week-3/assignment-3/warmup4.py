#Warmup 4: Sign and Parity
#Ask the user for a number.
number = int(input("Enter a number? "))
print (f"Enter a number: {number}")
#Sign Block
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.") #Own sign case. Neither positive or negative.
#Parity Block
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

