#Warmup 3: Linear Search
#Hardcoded list of names.
names = ["Braden", "Brooklyn", "Brendon", "Blake", "Bobbie", "Hunter"]
#Ask user to enter a name to search for. Lower case or capitalization doesn't matter.
search_name = input("Enter a name to search for: ").capitalize()
#Define index
index = -1
#Loops through list checking to see if an index matches what user entered and if so stops and prints.
for i in range(len(names)):
    if names[i] == search_name:
        index = i
        break
    #Asks if index not equal to -1, print the found name and index.
if index != -1:
    print(f'Found "{search_name}" at index {index}.')
    #Catches if name was never found in loop and prints not in list.
else:
    print(f'"{search_name}" was not found in the list.')
