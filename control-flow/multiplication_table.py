def multiplication():
    #Prompt user for number
    number = int(input("Enter a number to see its multiplication table: "))

    #Generate and print multiplication table
    for i in range(1, 10+1):
        product = number * i
        print(f"{number} * {i} = {product}")

#Run the function
multiplication()