"""Exercise: Sum of Two Numbers
Task: Write a program that takes two numbers from the user and prints their sum.

Expected Output:
Enter first number: 3
Enter second number: 4
The sum is: 7.0"""

print(" Adding 2 numbers")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

sum=float(num1+num2)

print(f"The sum is: {sum}")
print("\n") 

"""Exercise : Area of a Circle
Task: Write a program to calculate the area of a circle given its radius.

Expected Output:
Enter the radius of the circle: 5
The area of the circle is: 78.53981633974483"""

import math

print(" Area of Cirlce")
radius = float(input("Enter radius of circle: "))
area = math.pi*radius**2

print(f"The area of the circle is: {area}")
print("\n") 

"""Exercise: Even or Odd
Task: Write a program that checks if a number is even or odd.

Expected Output:
Enter a number: 7
7 is odd"""

print(" Even or Odd Number")
num = int(input("Enter a number: "))
if num % 2 ==0 :
    print("Even")
else:
    print("Odd")
    
print("\n")
    
"""Exercise: Simple Calculator
Task: Write a program that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.

Expected Output:
Enter first number: 10
Enter second number: 3
Enter operation (+, -, *, /): /
The result is: 3.3333333333333335"""

print(" basic Calculator")
def calculator (x, y , operation):
    if operation == '+':
        return (x+y)
    elif operation == '-':
        return x-y
    elif operation == '*':
        return x*y
    elif operation =='/':
        if y!= 0:
            return x/y
        else:
            return "Error"
    else:
        return "Wrong Operation"      
        

x=float(input("Enter 1st number: "))
y=float(input("Enter 2nd number: "))
operation = input("Enter operation (+ , - , * , / ): ")

result = calculator(x, y, operation)

print(f"The result is: {result}")
print("\n") 

"""Exercise: Find the Largest Number
Task:Write a program to find the largest of three numbers.

Expected Output:
Enter first number: 7
Enter second number: 15
Enter third number: 10
The largest number is: 15
"""
print(" Largest Number of 3 numbers")
def maximum(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n3 and n2 >= n1:
        return n2
    else:
        return n3
    

n1 =int(input("Enter first number: "))
n2 = int(input("Enter second numer: "))
n3 = int(input("Enter third number: "))

largest = maximum(n1 , n2, n3)

print(f"The largest number is: {largest}")
print("\n") 


"""Exercise: Reverse a String
Task: Write a program that takes a string from the user and prints it in reverse.

Expected Output:
Enter a string: hello
The reversed string is: olleh
"""
print(" Reverse String")
string = input("Enter a string: ")

reverse = string[::-1]

print(f"The reversed string is: {reverse}")
print("\n")


"""Exercise: Count Vowels
Task: Write a program that counts the number of vowels in a given string.

Expected Output:
Enter a string: Nimra Waqar
The number of vowels is: 4"""
print(" Vowels Counting")
def count(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count +=1
    return count

str = input("Enter a string: ")

vowel_count = count(str)

print(f"The number of vowels is: {vowel_count}")
print("\n")

"""Exercise : Fibonacci Sequence
Task: Write a program to print the Fibonacci sequence up to n terms.

Expected Output:
How many terms? 5
Fibonacci sequence:
0 1 1 2 3
"""
print(" Fibonacci Sequence")
num_terms = int(input("How many terms? "))

a, b=0, 1

print("Fibonacci Sequence: ")

for _ in range(num_terms):
    print(a, end=' ')
    a, b= b, a+b
print("\n")

"""Exercise: Check for Palindrome
Task: Write a program to check if a given string is a palindrome.

Expected Output:
Enter a string: radar
radar is a palindrome
"""
print(" Palindrome String")

def palindrome(s):
    s = s.replace(" ","").lower()
    return s==s[::-1]

string1 = input("Enter a string: ")
if palindrome(string1):
    print(f"{string1} is a palindrome")
else:
    print(f"{string1} is not a palindrome")
