"""
Write a program that accepts a sentence and calculate
the number of uppercase letters and lowercase letters.
"""

sentence = raw_input("Please enter your sentence:")

lower_case = 0
upper_case = 0

for i in range(len(sentence)):
    if 122 >= ord(sentence[i]) >= 97: lower_case += 1
    if 92 >= ord(sentence[i]) >= 65: upper_case += 1

print 'There are %d upper-case and %d lower-case letters in your sentence.' % (
upper_case, lower_case)


"""
import re

num = 4


def case_counter(sentence):
    lw = re.findall('[a-z]', sentence)
    print 'There are ' + str(len(lw)) + ' lower-case letters in your sentence'

    uc = re.findall('[A-Z]', sentence)
    print 'There are ' + str(len(uc)) + ' upper-case letters in your sentence'


case_counter()
"""

