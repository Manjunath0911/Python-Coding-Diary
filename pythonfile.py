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

# 4. python program to find the largest element in the list

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Test the function
nums = [10, 5, 8, 20, 3]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}") 