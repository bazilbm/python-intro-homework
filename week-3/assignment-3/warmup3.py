#Warmup 3: Boolean Expression Practice

print(not True and False) #False 
#not evaluates first and inverts a boolean value so True becomes False; False and False is False. 

print(True or False and False) #True
#or returns True when at least one condition is True. It only returns False when both conditions are False.

print(not (5 > 3)) #False
#Compare 5 > 3 first since in parenthesis so True; then not True makes it False.

print(10 == 10 and 4 != 4) #False
#Compare 10 == 10 is True 4 != 4 is False; and returns True only if both are True so it's False.

print(not False or not True) #True
#not inverts a boolean value so False becomes True and True becomes False; or returns True when at least one condition is True.