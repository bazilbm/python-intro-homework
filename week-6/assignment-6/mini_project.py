#Part 2: Mini-Project - Refactor the Number Cruncher
#Data file provided
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

#Task 1: Find minimum using a loop
"""Find and return the smallest number in the list using a loop"""
def find_min(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
    
#Task 2: Find maximum using a loop
"""Find and return the largest number in the list using a loop"""
def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
#Task 3: Linear search 
"""Search for a target value in the list using a linear search and return the index if found or -1 if not"""
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1
        
#Task 4: Bubble sort
"""Sort the list of numbers in order using bubble sort, and return a new sorted list."""
def bubble_sort(numbers):
    sorted_numbers = numbers.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
                swapped = True
    return sorted_numbers
       
#Task 5: Show menu and ask for user's choice
def show_menu():
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    option = input("Choose an option (1-5): ")
    return option

#Task 6: Main Function
"""Run the main program loop for the Number Cruncher application"""
def main():
    while True:
        option = show_menu()

        #Option 1: Find minimum
        if option == "1":
            result = find_min(numbers)
            print("Minimum number:", result)

        #Option 2: Find Maximum
        elif option == "2":
            result = find_max(numbers)
            print("Maximum number:", result)
            
        #Option 3: Search for a number using a linear search loop.
        elif option == "3":
            try:   
                search_num = int(input("Enter a number to search: "))
                index = search(numbers, search_num)
                if index != -1:
                    print(f"Found {search_num} at index {index}.")
                else:
                    print(f"{search_num} was not found in the list.")
            except:
                print("Invalid input. Enter a number to search. ")
                
        #Option 4: Sort - Bubble sort or repeatedly compare neighboring pairs and swap them if they're out of order.
        elif option == "4":
            result = bubble_sort(numbers)
            print("Original list:", numbers)
            print("Sorted list:", result) 
        
        #Option 5: Quit - print a goodbye message and exit loop.
        elif option == "5":
            print("Process complete. Thank you for using Number Cruncher. Goodbye!")
            break
        else:
            print("Invalid input. Please choose an option between 1 and 5.")

main()