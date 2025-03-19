# main.py

import simple_module

def main():
    name = input("Enter your name: ")

    # Check if the 'greet' function exists in the simple_module
    if hasattr(simple_module, 'greet'):
        greet_function = getattr(simple_module, 'greet')  # Get the function
        greeting_message = greet_function(name)  # Call the function
        print(greeting_message)
    else:
        print("The 'greet' function does not exist in simple_module.")

if __name__ == "__main__":
    main()
