#write a python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

#Define the range endpoints
#Initiate a for loop to iterate through the range of numbers as specified
#within the loop, check if the number is divisible by 7 and a multiple of 5
#If both conditions are met, print the numbers &

start = 1500
end = 2700

for num in range(start, end +1):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end=",")

print("\n\nThese are the numbers that are divisible by 7 and multiple of 5 between 1500 and 2700")