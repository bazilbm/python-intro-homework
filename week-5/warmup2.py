#Warmup 2: Input Validation with a While Loop
#Ask user to input a positive integer
while True:
    try:
        entry = int(input("Enter a positive integer: "))
    except:
        print (f"That's not a positive integer. Try again.")
        continue
    if entry <= 0:
        print (f"That's not a positive integer. Try again.")
    if entry > 0:
        print(f"Got it: {entry}")
        break
