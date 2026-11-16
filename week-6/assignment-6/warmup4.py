#Warmup 4: Validation Function
#Function that returns True if score is an integer between 0 and 100 and False otherwise.
def is_valid_score(score):
    """Check for an integer between 0 and 100."""
    return isinstance(score, int) and 0 <= score <= 100
"""Prompt user for a score and convert to an integer."""
score = int(input("Enter a score: "))
"""Check if score is valid, and if so print 'Valid score.'"""
if is_valid_score(score):
    print("Valid score.")
#If score is invalid print "Invalid score - must be between 0 and 100."
else:
    print("Invalid score - must be between 0 and 100.")
