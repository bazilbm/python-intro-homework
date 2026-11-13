#Part 2: Mini-Project - Number Cruncher
#Data file provided
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
#Number Cruncher Menu
while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    #User picks an option
    option = input("Choose an option (1-5): ")
    #Option 1: Find minimum
    if option == "1":
        smallest = numbers[0]

        for num in numbers:
            if num < smallest:
                smallest = num
        print("Minimum number:", smallest)
    #Option 2: Find Maximum
    elif option == "2":
        largest = numbers[0]

        for num in numbers:
            if num > largest:
                largest = num
        print("Maximum number:", largest)
    #Option 3: Search for a number using a linear search loop.
    elif option == "3":
        search_num = int(input("Enter a number to search: "))
        found = False
        for i in range(len(numbers)):
            if numbers[i] == search_num:
                print(f"Found {search_num} at index {i}.")
                found = True
                break
        if not found:
            print(f"{search_num} was not found in the list.")
    #Option 4: Sort - bubble sort or repeatedly compare neighboring pairs and swap them if they're out of order.
    elif option == "4":
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True
        print("Sorted list:", numbers)
    #Option 5: Quit - print a goodbye message and exit loop.
    elif option == "5":
        print("Process complete. Thank you for using Number Cruncher. Goodbye!")
        break
    else:
        print("Invalid input. Please choose an option between 1 and 5.")