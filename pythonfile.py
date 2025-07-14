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
nums = [10, 5, 8, 20, 3]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}") 

# 5. Python program to reverse a string.

def reverse_string(string):
    return string[::-1]
text = "Hello, Manju"
reversed_text = reverse_string(text)
print(reversed_text)

# 6. python program to seperate the digits from the string and return the sum of the numbers

def digit_sepearble(string):
    digits = [int(char) for char in string if char.isdigit()]
    total = sum(digits)
    return total
string = 'kukofm262'
print(digit_sepearble(string))

# 7. python program to count the frequency of the number

def frequency_count(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency
numbers = [1,2,4,5,2,4,5,1,7,8,5]
print(frequency_count(numbers))

# 8. python program to check whether it is a prime number or not

def prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
num = 10
print(prime_number(num))

# 9 . Python program to find the common elements between two lists.

def common_elements(lst1, lst2):
    common_num = []
    for num in lst1:
        if num in lst2:
            common_num.append(num)
    return common_num
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
print(common_elements(lst1, lst2))

# 10. python program to check if it is even:

def even_num(num):
    if num % 2 == 0:
        return True
    else:
        return False
num = 25
even_num(num)
