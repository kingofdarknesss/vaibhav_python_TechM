from PIL import Image, ImageOps
image = Image.open("vinay-jilowa-Qwo81eAmsQQ-unsplash (1).jpg")
inverted_image = ImageOps.invert(image)
inverted_image.save("inverted_image.png")

# Print numbers from 1 to 10
for number in range(1, 11):
    print(number)

# Calculate the sum of squares from 1 to 100
sum_of_squares = 0
for number in range(1, 101):
    sum_of_squares += number ** 2

print("Sum of squares from 1 to 100:", sum_of_squares)  

# Create a multiplication table up to 10x10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end=' ')  
    print()  



# Function to count vowels in a string
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count


input_string = "brainstorm"
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)  # 

