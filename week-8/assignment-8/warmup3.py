#Warmup 3: Handle a Missing File
#Look for a file named ../data/missing.txt and tells to read in read only mode.
try:
    with open("../data/missing.txt", "r") as f:
        content = f.read()
    #If file exists, save into a variable named content and print "File read successfully."
    print("File read successfully.")
    #If file does note exist, print FileNotFound Error.
except FileNotFoundError:
    print("Error: 'missing.txt' was not found. Please check the file path and try again.")
