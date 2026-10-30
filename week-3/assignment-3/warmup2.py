#Warmup 2: Age Categories
age = int(input("How old are you? "))
print (f"Enter your age: {age}")

if age <= 12:
    print("You are a Child.")
elif age <= 17:
    print("You are a Teen.")
elif age <= 64:
    print("You are an Adult")
else:
    print("You are a Senior")
