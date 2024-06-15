"""1. Palindrome Checker (Word)

• Write a program to check if a given word is a palindrome (reads the same forwards and backwards).
• Expected output: If the input is "racecar", the output should be "racecar is a palindrome." If the input is "Python", the output should be "Python is not a palindrome.”
"""
print(" Palindrome Checker ")

def is_palindrome(s):
    s=s.replace(" ","").lower()
    return s == s[::-1]

string = input("Enter a string: ")

if is_palindrome(string):
    print(f"{string} is a palindrome ")
else:
    print(f"{string} is not a palindrome ")
print("\n")

"""  FizzBuzz
   - Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".
   - Expected output:
     1
     2
     Fizz
     4
     Buzz
     Fizz
     7
     8
     Fizz
     Buzz
     11
     Fizz
     13
     14
     FizzBuzz
"""
print(" Fizz Buzz")

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
        
print("\n")

"""Nth Fibonacci Number

• Write a program to find the nth Fibonacci number.
• Expected output: If the input is 10, the output should be "The 10th Fibonacci number is 55.”
"""
print(" Nth Fibonacci Number")
num_terms = int(input("How many terms? "))

a, b=1, 1

print("Fibonacci Sequence: ")

for _ in range(num_terms):
    print(a, end=' ')
    a, b= b, a+b
print("\n")

""" Prime Number Checker
   - Write a program to check if a given number is prime.
   - Expected output: If the input is 7, the output should be "7 is a prime number." If the input is 10, the output should be "10 is not a prime number."
"""
print(" Prime number")
num = int(input("Enter a number: "))

for i in range (2, num):
    if num % i == 0 :
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
       
print("\n")

"""Guess the Number Game
   - Write a program where the computer generates a random number, and the user has to guess it.
   - Expected output: The program should prompt the user to enter a guess and provide feedback on whether the guess is too high, too low, or correct.
"""
print(" Guess the number game")
import random

def guess_number():
    number_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_guess:
            print("Too low! Try again.")
        elif guess > number_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

guess_number()
print("\n")

"""List Comprehension
   - Write a program that uses list comprehension to create a list of squares of the first 10 integers.
   - Expected output: `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`
"""
print(" List Comprehension")

square = []

for j in range(1, 11):
    square.append(j**2)
    
print(square)
print("\n")

"""Palindrome Sentences
   - Write a program to check if a given sentence is a palindrome (reads the same forwards and backwards, ignoring spaces and punctuation).
   - Expected output: If the input is "A man, a plan, a canal: Panama", the output should be "A man, a plan, a canal: Panama is a palindrome." If the input is "Hello, world!", the output should be "Hello, world! is not a palindrome."
"""
print(" Palindrome Sentences")

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

str = input("Enter a sentence or phrase: ")

if is_palindrome(str):
    print(f"{str} is palindrome")
else:
    print(f"{str} is not a palindrome")
    
print("\n")

""" Anagram Checker
   - Write a program to check if two strings are anagrams (contain the same characters in a different order).
   - Expected output: If the two strings are "listen" and "silent", the output should be "listen and silent are anagrams." If the two strings are "python" and "java", the output should be "python and java are not anagrams."
"""
print(" Anagram Checker")

def Anagram(str1 , str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    
    return sorted(str1) == sorted(str2)

string1 = input("Enter 1st string: ")
string2 = input("Enter 2nd string: ")

if Anagram(string1, string2):
    print(f"{string1} and {string2} are anagram")
else:
    print(f"{string1} and {string2} are not anagram")

print("\n")

"""Reverse Words in a Sentence
   - Write a program to reverse the order of words in a given sentence.
   - Expected output: If the input sentence is "The quick brown fox jumps over the lazy dog.", the output should be "dog. lazy the over jumps fox brown quick The"
"""

print(" Reverse words in a sentence")
def reverse_words(sentence):
    words = sentence.split()

    reversed_words = words[::-1]
    
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

input_sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(input_sentence)

print(f"The reversed sentence is: '{reversed_sentence}'")
print("\n")

"""Temperature Converter
    - Write a program that can convert temperatures between Celsius, Fahrenheit, and Kelvin.
    - Expected output: If the input is 20 degrees Celsius, the output should be "20 degrees Celsius is equal to 68 degrees Fahrenheit and 293.15 degrees Kelvin."

These exercises cover more advanced Python concepts like conditional logic, loops, functions, data structures, and algorithmic thinking. They are designed to challenge intermediate-level students and help them develop more complex problem-solving skills.
"""
print(" Temperature Converter")

def celsius_to_fahrenheit(temp):
    Fahrenheit = temp * (9/5) + 32
    return Fahrenheit

def celsius_to_kelvin(temp):
    Kelvin = temp + 273.15
    return Kelvin

def fahrenheit_to_celsius(temp):
    Celsius = temp - 32 * (5/9)
    return Celsius

def fahrenheit_to_kelvin(temp):
    Kelvin = (temp - 32) * 5/7 + 273.15
    return Kelvin

def kelvin_to_celsius(temp):
    Celsius = temp - 273.15
    return Celsius

def kelvin_to_fahrenheit(temp):
    Fahrenheit = (temp - 273.15) * 9/5 +32
    return Fahrenheit


temperature = float(input("Enter temperature: \n"))
char = input("C - Celsius\nF - Fahrenheit\nK - Kelvin\n").upper()

if char == "C":
    Fahrenheit = celsius_to_fahrenheit(temperature)
    Kelvin = celsius_to_kelvin(temperature)
    print(f"{temperature} degree celsius is equal to {Fahrenheit} degree fahrenheit and {Kelvin} degree Kelvin")
elif char == "F":
    Celsius = fahrenheit_to_celsius(temperature)
    Kelvin = fahrenheit_to_kelvin(temperature)
    print(f"{temperature} degree fahrenheit is equal to {Celsius} degree celsius and {Kelvin} degree Kelvin")
elif char == "K":
    Celsius = kelvin_to_celsius(temperature)
    Fahrenheit = kelvin_to_fahrenheit(temperature)
    print(f"{temperature} degree kelvin is equal to {Celsius} degree celsius and {Fahrenheit} degree fahrenheit")
else:
    print("Wrong Input!")
    