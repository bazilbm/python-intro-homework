#Warmup 2: Functions that Return Values
#Write Celsius to Fahrenheight function with result. Used C as value.
def celsius_to_fahrenheight(c):
    return (c * 9/5) + 32
#Write Fahrenheight to Celsius function with result. Used F as value.
def fahrenheight_to_celsius(f):
    return (f - 32) * 5/9
#Print Celsius to Fahrenheight
print(f"0°C = {celsius_to_fahrenheight(0):.1f}°F")
print(f"30°C = {celsius_to_fahrenheight(30):.1f}°F")
#Print Fahrenheight to Celsius
print(f"32°F = {fahrenheight_to_celsius(32):.1f}°C")
print(f"75°F = {fahrenheight_to_celsius(75):.1f}°C")