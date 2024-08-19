# Dynamic Simple Calculator in Python

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            numbers = list(map(float, input("Enter numbers separated by space: ").split()))

            if choice == '1':
                print(f"The result is: {add(numbers)}")
            elif choice == '2':
                print(f"The result is: {subtract(numbers)}")
            elif choice == '3':
                print(f"The result is: {multiply(numbers)}")
            elif choice == '4':
                print(f"The result is: {divide(numbers)}")
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
