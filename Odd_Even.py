# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input a number
num = int(input("Enter a number: "))

# Check if the number is odd or even and print the result
result = check_odd_even(num)
print(f"The number {num} is {result}.")