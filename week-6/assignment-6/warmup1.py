#Warmup 1: Default Parameters
#Greet function
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
#Call 1 with only a name argument    
greet("Blake")
#Call 2 with both name and custom greeting
greet("Blake", "Good Morning")
#Call 3 with the greeting passed as a keyword argument
greet("Blake", greeting="Greetings")
