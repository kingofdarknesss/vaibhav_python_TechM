# 1.Error classification
```Python
for i in range(5):
    print(i)


if(y!=0):
    x = 10 / y

def calculate_area(radius):
    return  3.14 * radius ** 2 
```
-There is a missing colon on the for loop
-The divide by zero error was not handled
-The formula for area was incorrect

# 2.debugging complex functions
```Python
def process_data(data):
    total = 0
    for item in data:
        try:
            total += int(item)  # Try converting the string to a float
            print("valid string literal :",item)
            
        except ValueError:
            print("invalid string literal :",item)

    return total / len(data)

print(process_data(['10', '20', 'abc', '30']))  
```
-There was no checks performed as to what is the item before converting it to integer wo I implemented a try-except block to perform this check and the values comes right for the items that can be converted to integer


# 3.advanced debugging challenge
```Python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # lock counter variable before modifying counter
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)
```
This is a classic operating system problem know as race condition where two diffrent threads try to access the same variable at the same time resulting in the wrong operation on the variable
-By locking the variable before performing the operation ensures that atomicity is maintained

#8. Memory Leaks and Performance Debugging


```python
import time
def efficient_function():
    result = []
    for i in range(100000):
        result.append(i * 2) # the function sleeps for 2 seconds hence inefficent
        time.sleep(2)
    return result

print(len(efficient_function()))
```
-This function sleeps for 2 milliseconds which for a large for loop creates a lot of time inefficiency

# 9.Debug why the function returns `None`:

```python
def add(a, b):
    return result = a + b #missing return
print(add(3, 4))
```
there was a missing retun statement in the function hence when printed it showed a none type as output 

# 10. Silent Failures

```python
try:
    result = 10 / 0
except:
    pass
print("No error detected!")
```
- this except block does not handle the divide by zero error and the try block does not allow the expression to raise an error becuase it expects the except block to handle it 
