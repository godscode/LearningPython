# Write a python program that accepts a string and calculates the number of digits and letters in the string.

#Define input string 
text = input("Enter a string: ")

#initialise the counters for letters and digits
letter_count = 0
digit_count = 0
white_space = 0

for char in text:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        white_space += 1
    else:
        print("invalid character", char)

print("Number of Letters:", letter_count)
print("Number of Digits:", digit_count)
print("Number of Space:", white_space)