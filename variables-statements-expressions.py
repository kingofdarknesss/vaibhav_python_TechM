 
 def nums():
 #these are the different data types

  # Integer
    my_int = 42
    print(f"Integer: {my_int}")

    # Float
    my_float = 3.14
    print(f"Float: {my_float}")

    # Complex
    my_complex = 2 + 3j
    print(f"Complex: {my_complex}")

    # String
    my_string = "Hello, World!"
    print(f"String: {my_string}")

    # Boolean
    is_active = True
    print(f"Boolean: {is_active}")

    # List
    my_list = [1, 2, 3, "four", 5.0]
    print(f"List: {my_list}")

    # Tuple
    my_tuple = (1, 2, 3, "four", 5.0)
    print(f"Tuple: {my_tuple}")

    # Dictionary
    my_dict = {"name": "Alice", "age": 25}
    print(f"Dictionary: {my_dict}")
    print(f"Dictionary Value (name): {my_dict['name']}")
    print(f"Dictionary Value (age): {my_dict['age']}")

    # Set
    my_set = {1, 2, 3, 4, 4}  # Duplicate values are ignored
    print(f"Set: {my_set}")

    # NoneType
    my_none = None
    print(f"NoneType: {my_none}")

def opr():
    # The program for all the arithmetic and logical operations

    a = 10
    b = 3

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
    print("Exponentiation:", a ** b)

    x = True
    y = False

    print("Logical AND:", x and y)
    print("Logical OR:", x or y)
    print("Logical NOT:", not x)

# Simple Program Using Built-in Functions

def funccall():
    # Using inbuilt function len()
    name = "Alice"
    print(f"Is the name '{name}' longer than 4 characters? {len(name) > 4}")
    
    # Using abs() to compare absolute values
    num = -5
    print(f"Is the absolute value of {num} greater than 3? {abs(num) > 3}")
    # Assign the built-in len() function to a variable
    get_length = len

    # Call the function using the new variable
    my_string = "Hello"
    length = get_length(my_string)
    print(f"The length of '{my_string}' is: {length}")

def conv_types():
    # Convert integer to string
    num = 42
    str_num = str(num)
    print(f"Integer {num} converted to string: {str_num}")

    # Convert string to integer
    str_num = "42"
    num = int(str_num)
    print(f"String '{str_num}' converted to integer: {num}")

def variable_demons():
    # Initial assignment
    x = 10
    y = [1, 2, 3]
    print(f"Initial values -> x: {x}, y: {y}")

    # Reassigning variables
    x = "Hello"
    y.append(4)
    print(f"After reassignment -> x: {x}, y: {y}")

def update_var():
    count = 10
    print(f"Initial value of count: {count}")

# Reassignment
    count = 20
    print(f"Value of count after reassignment: {count}")

# Further Reassignment
    count = count + 5
    print(f"Value of count after adding 5: {count}")

# Changing Type (Dynamic Typing)
    count = "Twenty-five"
    print(f"Value of count after type change: {count}")

def inc_dec():
    score = 100
    score += 1000
    print(score)
    score -= 567
    print(score)














  

