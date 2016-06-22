"""
Write a program that prints the numbers from 1 to N. But for multiples of three prints
sum of all numbers up to now instead of the number and for the multiples of five prints
multiplication of all numbers up to now. For numbers which are multiples of both three
and five prints average of all numbers up to now.
"""

sum = 0


def mult_of_three(num):
    if num == 1:
        return 1
    else:
        return mult_of_three(num - 1) + num


def mult_of_five(num):
    if num == 1:
        return 1
    else:
        return mult_of_five(num - 1) * num


def mult_of_three_five(sum, num):
    return sum / num


number = int(raw_input("Please enter your number: "))
for current_number in range(1, number + 1):
    sum += current_number
    if (current_number % 3 == 0) and (current_number % 5 == 0):
        print mult_of_three_five(sum, current_number)
    elif current_number % 3 == 0:
        print mult_of_three(current_number)
    elif current_number % 5 == 0:
        print mult_of_five(current_number)
    else:
        print current_number
