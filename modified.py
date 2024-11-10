# Modified Code
def start_program():
    print("Initializing the program...")

    for i in range(1, 101):
        if i % 2 != 0:
            print(f"Odd number: {i}")
        else:
            print(f"Even number: {i}")
            
    data = [i for i in range(1, 101)]
    total_sum = sum(data)
    print(f"Total sum of list: {total_sum}")

    # Factorial computation
    def calculate_factorial(n):
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    print(f"Factorial of 6: {calculate_factorial(6)}")

    # Handle fruits list
    fruits = ["orange", "banana", "grapes", "date"]
    for fruit in fruits:
        print(f"Enjoying {fruit}")

    # Matrix manipulation
    matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    for row in matrix:
        for item in row:
            print(f"Item: {item}")

    # Process sentence
    sentence = "A quick brown fox jumps over the lazy dog"
    words = sentence.split()
    for word in words:
        print(f"Extracted word: {word}")

    # Simple math
    x = 15
    y = 25
    print(f"Sum of {x} and {y}: {x + y}")

    # Generate list of even numbers
    even_numbers = [i for i in range(2, 101, 2)]
    print(f"Even numbers generated: {even_numbers}")

    # Working with a dictionary
    user_info = {"name": "Alice", "age": 28, "location": "California"}
    for key, value in user_info.items():
        print(f"{key}: {value}")

    # Person class
    class Individual:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def introduce(self):
            return f"Hi, I'm {self.name} and I'm {self.age} years old."

    individual = Individual("Bob", 32)
    print(individual.introduce())

    # File operations
    with open("example.txt", "w") as file:
        file.write("This is an example text file.")

    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

    # Sorting numbers
    unordered_list = [8, 3, 4, 6, 1]
    ordered_list = sorted(unordered_list)
    print(f"Sorted numbers: {ordered_list}")

    # Loop demonstration
    for i in range(5):
        print(f"Loop index {i}")

    # Function with arguments
    def division(a, b):
        return a / b

    division_result = division(20, 4)
    print(f"Division result: {division_result}")

    # Working with sets
    unique_elements = {1, 2, 3, 4, 5}
    unique_elements.add(7)
    print(f"Set elements: {unique_elements}")

    # Lambda function
    double = lambda x: x * 2
    print(f"Double of 5: {double(5)}")

    # Exception handling
    try:
        value = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")

    # Fibonacci sequence
    def fibonacci_sequence(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)

    print(f"Fibonacci of 6: {fibonacci_sequence(6)}")

if __name__ == "__main__":
    start_program()
