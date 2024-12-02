# Get user input for the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Generate squares of numbers within the range
squares = [x**2 for x in range(start, end + 1)]

# Separate odd and even squares
odd_squares = [num for num in squares if num % 2 != 0]
even_squares = [num for num in squares if num % 2 == 0]

# Print the results
print("Squares of numbers in the range:", squares)
print("Odd squares:", odd_squares)
print("Even squares:", even_squares)
