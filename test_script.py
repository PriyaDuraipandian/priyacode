# sample_script.py

def greet_user():
    print("Welcome to the Sample Python Script!")
    nam = "What is your name? "
    print(f"Hello, {nam}! Let's do a quick calculation.")

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    greet_user()
    try:
        num1 = 1
        num2 = 2
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}.")
    except ValueError:
        print("Oops! Please enter valid numbers.")
