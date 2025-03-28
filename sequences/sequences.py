# 1.->A sequence in Python is an ordered collection of elements accessible by indexing. Common types include strings (immutable text), lists (mutable collections), tuples (immutable collections)
#2.-> strings lists and tuples are different in mutability and types strings and tuples are immutable and string can only have charecters while lists are mutable and can have anything as an element
#3.-> indexing in python is zero based and can be accessed using [] square brackets
text = "hello"
print(text[0])  # Output: 'h'
# 4.-> if we use negative characters the indexing starts from last
text = "hello"
print(text[-1])  # Output: '0'  

#5.->
numbers = [10, 20, 30, 40]
print(numbers[2])  

#6.->
len([1, [2, 3], 4])
#the out put is three as there are three distinct elemnts in the len function

#7.-> slicing example
data = [10, 20, 30, 40]
print(data[1:3])  # Output: 20, 30

#8.-> reverse a string using slicing
text = "mclaren
print(text[::-1])

#9-> list concatenation and repetition 

list1 = [1, 2] + [3, 4]  # Result: [1, 2, 3, 4][2]

list2 = [1, 2] * 2  # Result: [1, 2, 1, 2][2]

#10.-> count occurences
numbers = [1, 2, 2, 3]
print(numbers.count(2))

#11.->
my_tuple = (1, 2, 3); print(my_tuple[1:])
#the output is (2,3)

#12.-> append vs extends
# Append adds the  iterable as one element
a = [1, 2]
a.append([3, 4])  
print(a)  # Output: [1, 2, [3, 4]]

# Extend adds elements from the iterable individually
b = [1, 2]
b.extend([3, 4])  
print(b)  # Output: [1, 2, 3, 4]

#13.->
sentence = "Learn Python step by step!"
words = sentence.split()  
print(words)  

#14.->
words = ['Python', 'is', 'fun']
combined = ' '.join(words)  
print(combined)  # Output: "Python is fun"

#15.->
numbers = [1, 2, 2, 3, 4, 2]
index = numbers.index(2)  
print(index)  # Output: 1

#16.-> palindrome checker
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("madam"))

#17.-> length of the longest word
def longest_word(sentence):
    words = sentence.split()
    return max(len(word) for word in words)

print(longest_word("Python is awesome"))  

#18.-># nested lists
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])  

19.->
chars = ['p', 'y', 'c']
string = ''.join(chars)  
print(string)  # Output: "pyc"

20.->
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates([1, 2, 2, 3]))  # Output: [1, 2, 3]

21->
22.->def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3]]]))  # Output: [1, 2, 3]

23.->
def rotate_right(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3], 1))  # Output: [3, 1, 2]
24.->
def are_anagrams(a, b):
    return sorted(a.lower()) == sorted(b.lower())

print(are_anagrams("listen", "silent"))  # Output: True

25.->
def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

print(chunk_list([1, 2, 3, 4], 2))  # Output: [[1, 2], [3, 4]]

26.->
def merge_sorted(a, b):
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged += a[i:] + b[j:]
    return merged

print(merge_sorted([1, 3], [2, 4]))  # Output: [1, 2, 3, 4]

# pipleline data validator
# Define the function to analyze pipelines
def analyze_pipelines(pipelines, threshold):
    # Find the longest pipeline
    longest_pipeline = ""
    max_time = 0
    
    for name, time in pipelines:
        if time > max_time:
            max_time = time
            longest_pipeline = name
    
    # Find pipelines exceeding the threshold
    exceeding = []
    for name, time in pipelines:
        if time > threshold:
            exceeding.append(name)
    
    return longest_pipeline, exceeding

# Sample input
pipelines = [
    ("Data Ingestion", 30),
    ("Preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20)
]
threshold = 40


longest, exceeding = analyze_pipelines(pipelines, threshold)

print("Longest Pipeline:", longest)
print("Pipelines exceeding threshold:", exceeding)


def extract_unique_error_codes(logs):
    
    error_codes = set()
    
    
    for line in logs.strip().split('\n'):
        if line.startswith("ERROR"):
            
            parts = line.split()
            error_code = parts[1]  # 
            error_codes.add(error_code)
    
    return list(error_codes)


logs = """ERROR 404: Not Found
INFO: Connection established
ERROR 500: Internal Server Error
ERROR 404: Not Found
"""


unique_error_codes = extract_unique_error_codes(logs)
print("Unique Error Codes:", unique_error_codes)

# config file reader
def parse_config(config):
    
    pairs = config.split(';')
    

    result = []
    for pair in pairs:
        if '=' in pair:  
            key, value = pair.split('=', 1)  
            result.append((key.strip(), value.strip()))  
    
    return result


config = "host=127.0.0.1;port=8080;mode=debug"


parsed_pairs = parse_config(config)
print(parsed_pairs)

#social modeia cleaner
def extract_unique_hashtags(post):
    
    words = post.split()
    
    
    hashtags = set()
    
    
    for word in words:
        if word.startswith('#'):
            hashtags.add(word)
    
    
    return list(hashtags)


post = "Loving the new #Python course! #Coding #Python #Learning"


unique_hashtags = extract_unique_hashtags(post)
print(unique_hashtags)

# secret message decoder
def decode_secret_code(secret_message):
    
    decoded_message = secret_message[2::3]
    return decoded_message


secret_message = "hweollrolwd"


decoded_output = decode_secret_code(secret_message)
print(decoded_output)

# invertory tracker
def find_highest(inventory):
    
    highest_product = ""
    highest_quantity = 0
    
    
        if quantity > highest_quantity:
            highest_quantity = quantity
            highest_product = product
    
    return highest_product


inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
]


highest_product = find_highest(inventory)
print(highest_product)

# survey strings


def analyze_survey_data(survey_data):
    
    scores = list(map(int, survey_data.split(',')))  
    
    
    max_score = max(scores)
    min_score = min(scores)
    
    return max_score, min_score


survey_data = "5,3,4,1,2"


max_score, min_score = analyze_survey_data(survey_data)
print(f"Max Score: {max_score}, Min Score: {min_score}")

# access control manager
def manage_user_access(users, roles):
    
    access_levels = []
    
    
    for user, role in zip(users, roles):
        access_levels.append(f"{user}: {role}")  
    
    
    return ', '.join(access_levels)


users = ["Alice", "Bob", "Charlie"]
roles = ("Admin", "Editor", "Viewer")


output = manage_user_access(users, roles)
print(output)


def categorize_ticket(message):
    length = len(message)
    
    if length < 20:
        category = "Short"
    elif 20 <= length <= 50:
        category = "Medium"
    else:
        category = "Long"
    
    return category

message = "My account is locked, please help!"

category = categorize_ticket(message)
print(f"Category: {category}")

# product backlog manager
def find_longest_name(products):
    
    longest_product = max(products, key=len)
    return longest_product


products = ["Laptop", "Smartphone", "Wireless Headphones"]

longest_name = find_longest_name(products)
print(longest_name)
# sensor data analyzer
def cdalr(sensor_readings):
    
    last_readings = sensor_readings[-10:]   
    average = sum(last_readings) / len(last_readings) if last_readings else 0
    return average


sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]


average_reading = cdalr(sensor_readings)
print(f"Average: {average_reading:.0f}")  

 # transaction reciever
 def reverse_transactions(transactions):
    # Reverse the list of transactions
    reversed_list = transactions[::-1]
    return reversed_list


transactions = [100, -50, 200, -150, 50]


reversed_transactions = reverse_transactions(transactions)
print(reversed_transactions)




# pattern genarator
def generate_pattern(symbol, count):
    
    pattern = symbol*count 
    return pattern

# Sample input
symbol = "*"
count = 5


pattern_output = generate_pattern(symbol, count)
print(pattern_output)

# custormer feedback analyzer
def count_keyword_occurrences(feedback, keyword):

    words = feedback.lower().split()
    
    
    count = words.count(keyword.lower())
    
    return count


feedback = "The product is excellent, absolutely excellent!"
keyword = "excellent"


keyword_count = count_keyword_occurrences(feedback, keyword)
print(f"'{keyword}' count: {keyword_count}")


def find_error_index(log):
    
    index = log.lower().find("error")
    return index

log = "INFO: All systems go. ERROR: Failed to start service."


error_index = find_error_index(log)
print(f"Index: {error_index}")

#CSV parser
def parse_csv(csv_data):
    
    lines = csv_data.strip().split('\n')
    
    
    parsed_data = [line.split(',') for line in lines]
    
    return parsed_data


csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"


parsed_output = parse_csv(csv_data)
print(parsed_output)

#username generator
def generate_usernames(names):
    
    usernames = [f"{name[0]}{name.split()[1]}" for name in names]
    return [username.capitalize() for username in usernames]


names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]


usernames_output = generate_usernames(names)
print(usernames_output)


def count_messages_per_user(chat_logs):

    message_count = {}
    

    for log in chat_logs:
        user, _ = log.split(':', 1)  
        user = user.strip()  
        

        if user in message_count:
            message_count[user] += 1
        else:
            message_count[user] = 1
    
    
    result = []
    for user, count in message_count.items():
        message_label = "message" if count == 1 else "messages"  
        result.append(f"{user}: {count} {message_label}")
    
    return ', '.join(result)


chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]


output = count_messages_per_user(chat_logs)
print(output)


def compress_repeated_substrings(data):
    
    for i in range(1, len(data) // 2 + 1):
        substring = data[:i]
        if substring * (len(data) // len(substring)) == data:
            return f"'{substring}' repeated {len(data) // len(substring)} time"
    return "No repeating substring found"


data = "abababababab"


print(compress_repeated_substrings(data))







