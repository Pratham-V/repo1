# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to interact with the user
def main():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Operations:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            operation = input("Enter operation number (1-4): ")

            if operation == "1":
                print("Result: " + str(add(num1, num2)))
            elif operation == "2":
                print("Result: " + str(subtract(num1, num2)))
            elif operation == "3":
                print("Result: " + str(multiply(num1, num2)))
            elif operation == "4":
                print("Result: " + str(divide(num1, num2)))
            else:
                print("Invalid operation. Please try again.")
            
            another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another_calculation != "yes":
                print("Exiting the calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print("An error occurred: " + str(e))

# Run the main function
if __name__ == "__main__":
    main()
