''' 

write a python program to construct the following pattern, using for loop.

*
* *
* * *
* * * *
* * * * *
* * * * 
* * * 
* *
* 

'''

# Define the number of rows for the pattern
n = 5

# print the upper part of the pattern
for i in range (1, n + 1):
    print("* " * i)

#print the lower part of the pattern
# range(start, stop, step):

for i in range(n-1, 0, -1):
    print("* " * i)