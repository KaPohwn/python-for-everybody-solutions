"""
Exercise 5.1: Write another program that prompts for a list of numbers as
above and at the end prints out both the maximum and minimum of the numbers
instead of the average.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 28, 2017
"""

count = 0
total = 0
smallest = None
largest = None
while True:
    entry = input("Please enter a number or type 'done': ")
    if entry == 'done': break
    try:
        number = float(entry)
    except:
        print("Please type a number using numeric characters or type 'done': ")
        continue
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
    count = count + 1
    total = total + number
    average = total / count
print('You entered ' + str(count) + ' numbers. The smallest number you entered is: ' + str(smallest) + '. The largest number you entered is: ' + str(largest) + '. The sum total of all the numbers you entered is: ' + str(total) + '. The average of all the numbers you entered is: ' + str(average) + '.')
