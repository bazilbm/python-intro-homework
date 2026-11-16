#Warmup 3: Scope in Action
#A variable scope with two short examples in one file
def set_name(): #Initial print #Stayed same for 2nd print
    name = "Blake Bazille" #Initial print #Stayed same for 2nd print
    return name #Added for 2nd print
#set_name() #Initial print #Commented out for 2nd print
result = set_name() #Added for 2nd print
#print(name) #Initial print #commented out for 2nd print
#Initial print results in this error because it only existed during the function call or is local to that function - NameError: name 'name' is not defined
print(result) #Added for 2nd print resulting in correct output using return to access the in an outer-scope variable
#Printed Blake Bazille