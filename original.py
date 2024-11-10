# Original Code
def main():
    print("Starting the program...")

    for i in range(1, 101):
        if i % 2 == 0:
            print(f"{i} is even.")
        else:
            print(f"{i} is odd.")
            
    data = [i for i in range(1, 101)]
    total_sum = sum(data)
    print(f"Sum of numbers: {total_sum}")

    # Function to calculate factorial
    def factorial(n):
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    print(f"Factorial of 5: {factorial(5)}")

    # Handling a simple list
    fruits = ["apple", "banana", "cherry", "date"]
    for fruit in fruits:
        print(f"I like {fruit}")

    # Nested loops for matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in matrix:
        for element in row:
            print(f"Element: {element}")

    # Working with strings
    sentence = "The quick brown fox jumps over the lazy dog"
    words = sentence.split()
    for word in words:
        print(f"Word: {word}")

    # Simple number operations
    a = 10
    b = 20
    print(f"Sum of {a} and {b} is {a + b}")

    # Create a list of even numbers
    evens = [i for i in range(2, 101, 2)]
    print(f"Even numbers: {evens}")

    # Dictionary operations
    info = {"name": "John", "age": 30, "city": "New York"}
    for key, value in info.items():
        print(f"{key}: {value}")

    # Class definition
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hello, my name is {self.name} and I am {self.age} years old."

    person = Person("Alice", 25)
    print(person.greet())

    # Reading and writing files
    with open("sample.txt", "w") as f:
        f.write("This is a sample text.")

    with open("sample.txt", "r") as f:
        content = f.read()
        print(content)

    # Sorting a list
    unsorted_list = [5, 1, 9, 3, 7, 2]
    sorted_list = sorted(unsorted_list)
    print(f"Sorted list: {sorted_list}")

    # Simple loop example
    for i in range(10):
        print(f"Number {i}")

    # Function with multiple parameters
    def multiply(a, b):
        return a * b

    result = multiply(3, 4)
    print(f"Multiplication result: {result}")

    # Working with sets
    unique_numbers = {1, 2, 3, 4, 5}
    unique_numbers.add(6)
    print(f"Unique numbers: {unique_numbers}")

    # Lambda function
    square = lambda x: x * x
    print(f"Square of 4: {square(4)}")

    # Try-except block
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input, please enter a valid number.")

    # Fibonacci sequence
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    print(f"Fibonacci of 5: {fibonacci(5)}")

if __name__ == "__main__":
    main()
