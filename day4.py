#write a program that prints all the numbers from 0 to 6 except 3 and 6.

#Define the loop range
for num in range(0, 7):
    #check number is not equal to 3 or 6
    if num == 3 or num == 6:
        continue
    print(num, end=", ")
print("\n\nThese are the numbers from 0 to 6 except 3 and 6")
