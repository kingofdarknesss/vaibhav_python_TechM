



# Values and Data Types

In Python, a **value** refers to the data or object assigned to a variable. It is the actual content stored in memory that the variable represents.  
For example, in the statement `x = 42`, the **value** is `42`, and the variable `x` is a reference to that value.

## Data Types in Python

### Primitive Data Types:

- **str**: Represents a sequence of characters (strings).  
  *Example:* `"Hello, World!"`

- **int**: Represents integers (whole numbers).  
  *Example:* `42`

- **float**: Represents floating-point numbers (numbers with decimals).  
  *Example:* `3.14`

- **complex**: Represents complex numbers with real and imaginary parts.  
  *Example:* `2 + 3j`

### Collection Data Types:

- **list**: Mutable, ordered collection of items.  
  *Example:* `[1, 2, 3]`

- **tuple**: Immutable, ordered collection of items.  
  *Example:* `(1, 2, 3)`

- **range**: Represents a sequence of numbers.  
  *Example:* `range(5)`

- **dict**: Represents key-value pairs.  
  *Example:* `{"name": "Alice", "age": 25}`

- **set**: Unordered collection of unique items.  
  *Example:* `{1, 2, 3}`

### Other Data Types:

- **bool**: Represents truth values (`True` or `False`).  
  *Example:* `is_active = True`

- **bytes**: Immutable sequence of bytes.  
  *Example:* `b"Hello"`

- **NoneType**: Represents the absence of a value or null value.  
  *Example:* `x = None`

---

## Arithmetic Operators:

- `+` : Addition  
- `-` : Subtraction  
- `*` : Multiplication  
- `/` : Division  
- `//` : Floor Division  
- `%` : Modulus (remainder)  
- `**` : Exponentiation (power)  

---

## Logical Operators:

- `and`: Logical AND  
- `or`: Logical OR  
- `not`: Logical NOT  

---

## Dynamic Typing in Python

Python is **dynamically typed**, meaning:

1. **Type Determination**: The type of a variable is determined at runtime, not during compilation.
2. **No Explicit Declarations**: Variables do not need explicit type declarations.
3. **Type Changes**: The type of a variable can change based on the assigned value.

```python
a = 10
b = 'Python'
c = 3.14
print(type(a), type(b), type(c))
```

# Type Conversion

## 1. Implicit Type Conversion
- Python **automatically converts** data types when necessary to avoid data loss.
- Typically occurs when combining different data types (e.g., adding an integer and a float).

## 2. Explicit Type Conversion
- The programmer **manually converts** one data type into another using built-in functions.
- Common functions include `int()`, `float()`, and `str()`.

---

# Variables

- **Primitive Data Types** (e.g., integers, floats): Stored on the **stack** for efficient memory allocation since their size is fixed.
- **Non-Primitive Data Types** (e.g., lists, dictionaries): Stored on the **heap**. The variable itself holds a reference (pointer) to the memory location on the heap.
- **Memory Management**: Python's memory manager handles allocation and deallocation automatically using techniques like **garbage collection** to free unused memory.
- **Dynamic Typing**: Variables in Python are **dynamically typed**, meaning their type is determined at runtime and can change.

**Note:** If we use **reserved keywords** as variable names, we get an **invalid syntax error**.

---

# Importance of Good Variable Names

Using meaningful variable names improves:

1. **Readability** – `total_price` clearly indicates what the variable represents, making the code easier to understand.
2. **Maintainability** – Meaningful names help others quickly grasp the purpose of each variable when modifying or extending the code.

Example:

```python
total_price = 100  # Good variable name
tp = 100           # Less readable variable name
```
# Statements vs Expressions

- **Statement**: An instruction that the Python interpreter can execute. It performs an action but does not necessarily return a value.
- **Expression**: A combination of values, variables, and operators that is evaluated to produce a result.

### Example:

```python
x = 5 + 3
print(x)
```



