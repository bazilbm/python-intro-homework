#Warmup 1: Validate Numberic Input
#Create a loop that keeps asking for input until break.
while True:
    user_input = input("Enter a number: ")
    try:
        #Attempts to convert the input string into a number.
        number = float(user_input)
        #Prints if it's able to be converted to a number.
        print(f"You entered: {number}")
        #Exits the loop once conversion is made and printed.
        break
    #Catches the error if the input is something that can't be converted to a number. 
    except ValueError:
        #Prints a message saying it's not a valid number and asks for input again.
        print("That's not a valid number. Please try again.")