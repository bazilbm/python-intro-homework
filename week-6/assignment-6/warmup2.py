#Warmup 2: Functions that Return Values
#Write Celsius to Fahrenheit function with result. Used C as value.
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
#Write Fahrenheit to Celsius function with result. Used F as value.
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
#Print Celsius to Fahrenheit
print(f"0°C = {celsius_to_fahrenheit(0):.1f}°F")
print(f"30°C = {celsius_to_fahrenheit(30):.1f}°F")
#Print Fahrenheit to Celsius
print(f"32°F = {fahrenheit_to_celsius(32):.1f}°C")
print(f"75°F = {fahrenheit_to_celsius(75):.1f}°C")