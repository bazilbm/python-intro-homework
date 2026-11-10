#Warmup 4: FizzBuzz
#Loop 1 to 30
for i in range(1, 31):
    #Check combined (divisible by both 3 and 5) case first.
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    #Check if divisible by 3 only.
    elif i % 3 == 0:
        print("Fizz")
    #Check if divisible by 5 only.
    elif i % 5 == 0:
        print("Buzz")
    #Print the number itself otherwise.
    else:
        print(i)
    