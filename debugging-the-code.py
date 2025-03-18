# 1.Error classification
for i in range(5):
    print(i)


if(y!=0):
    x = 10 / y

def calculate_area(radius):
    return  3.14 * radius ** 2 

# 2.debugging complex functions
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

# 3.advanced debugging challenge
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

#8. Memory Leaks and Performance Debugging



import time
def efficient_function():
    result = []
    for i in range(100000):
        result.append(i * 2) # the function sleeps for 2 seconds hence inefficent
    return result

print(len(efficient_function()))



#9.Debug why the function returns `None`:


def add(a, b):
    return result = a + b #missing return
print(add(3, 4))

# 10. Silent Failures

try:
    result = 10 / 0
except:
    print ("error detected") # this except block does not handle the divide by zero error and the try block does not allow the expression to raise an error becuase it expects the except block to handle it 
#print("No error detected!")