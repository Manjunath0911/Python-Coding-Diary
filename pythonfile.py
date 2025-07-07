# this file is designed to upload algorithms

# 1. Program to find even or not

def even_number(num):
    if num % 2 == 0:
        return print(f"{num} is even number")
    else:
        return print(f"{num} is not even number")
even_number(4)

# 2. Python program to check if a string is a palindrome.

def palindrome(string):
   rev_string = string[::-1]
   if string == rev_string:
       print(f'{string} is a palindrome')
   else:
       print(f'{string} is not a palindrome')
string = "MALAYALAM"
palindrome(string)

# 3. python program to find the factorial of a number

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)
print(factorial(5))

 