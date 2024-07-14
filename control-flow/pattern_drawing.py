def pattern_drawing():
    size = int(input("Enter the size of the pattern: "))

    # Initialize row counter
    row = 0

    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print asterisks in each row
        for _ in range(size):
            print("*", end="")
        # Print a newline character after each row
        print()
        # Increment the row counter
        row += 1

#Run the function
pattern_drawing()
