""" Recursive Factorial
   - Write a recursive function to calculate the factorial of a given number.
   - Expected output: If the input is 5, the output should be "The factorial of 5 is 120."
"""
print(" Recursive Factorial")

def recursive_function(number):
   if number == 0 or number == 1:
      return 1
   else:
      return number * recursive_function(number -1)
   
   
n = int(input("Enter a number for recursive factorial: "))
factorial = recursive_function(n)

print(f"The factorial of {n} is {factorial}")
print("\n")

"""Palindrome Linked List
   - Write a program to determine if a given linked list is a palindrome.
   - Expected output: If the linked list is `1 -> 2 -> 3 -> 2 -> 1`, the output should be "The linked list is a palindrome." If the linked list is `1 -> 2 -> 3 -> 4 -> 5`, the output should be "The linked list is not a palindrome."
"""
print(" Palindrome Linked List")

def palindrome_list(e):
    return e == e[::-1]

l1 = [ 1, 2 , 3, 2, 1]
l2 = [ 1, 2 , 3, 4, 5]

if palindrome_list(l1):
    print("The 1st linked list is a palindrome")
else:
    print("The 1st linked list is not a palindrome")

if palindrome_list(l2):
    print("The 2nd linked list is a palindrome")
else:
    print("The 2nd linked list is not a palindrome")
print("\n")    

"""Merge Sorted Arrays
   - Write a function that takes two sorted arrays and merges them into a single sorted array.
   - Expected output: If the two input arrays are `[1, 3, 5]` and `[2, 4, 6]`, the output should be `[1, 2, 3, 4, 5, 6]`.
"""
print(" Merge Sorted Arrays")
def Merge_Arrays(arr1 , arr2):
    merged_arrays = []
    i = 0
    j = 0 
      
    while i < len(arr1):
        merged_arrays.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_arrays.append(arr2[j])
        j += 1
            
    return merged_arrays

array1 = [1 , 3, 5]
array2 = [2 , 4, 6]

merged = Merge_Arrays(array1, array2)

print(merged)
print("\n")

"""Binary Search Tree
   - Implement a Binary Search Tree (BST) data structure, including methods for insertion, deletion, and search.
   - Expected output: The program should be able to perform various BST operations and print the results.
"""
print(" Binary Search Tree")
def Create_node(value):
    {"value" : value , "left" : None , "right" : None}
    
def insertion(root, key):
    if root is None:
        return Create_node(key)
    if key < root["value"]:
        root["left"] = insertion(root["left"], key)
    else:
        root["right"] = insertion(root["right"], key)
    return root

def searching(root , key):
    if root is None or root["value"] == key:
        return root
    if key < root["value"]:
        return searching(root["left"], key)
    return searching(root["right"], key)

def Min_search(node):
    current = node
    while current and current["left"] is not None:
        current = current["left"]
    return current

def deletion(root, key):
    if root is None:
        return root
    if key < root["value"]:
        root["left"] = deletion(root["left"], key)
    elif key > root["value"]:
        root["right"] = deletion(root["right"], key)
    else:
        if root["left"] is None:
            return root["right"]
        elif root["right"] is None:
            return root["left"]
        temp = Min_search(root["right"])
        root["value"] = temp["value"]
        root["right"] = deletion(root["right"], temp["value"])
    return root

def InOrder(root):
    if root:
        return InOrder(root["left"]) + root["value"] + InOrder(root["right"])
    else:
        return []

root = None
data= [50, 30, 20, 40, 70, 60, 80]
for key in data:
    root = insertion(root, key)
    
print("In order traversal", InOrder(root))

data_search = 40
search_result = searching(root , data_search)
if search_result:
    print(f"Data {data_search} is found in BST")
else:
    print(f"Data {data_search} is not found in BST")
    
data_delete = 20
delete_result = deletion(root, data_delete)
print(f"In order traversal after deleting {data_delete} : ", InOrder(root))
print("\n")

"""Longest Palindromic Substring
   - Write a program to find the longest palindromic substring within a given string.
   - Expected output: If the input string is "babad", the output should be "bab" or "aba". If the input string is "cbbd", the output should be "bb".
"""
print(" Longest Palindromic Substring")

def expand_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longest_palindromic_substring(s):
    longest = ""
    for i in range(len(s)):
        palindrome1 = expand_center(s, i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1

        palindrome2 = expand_center(s, i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

input_string1 = "babad"
input_string2 = "cbbd"

print(f"The longest palindromic substring in '{input_string1}' is '{longest_palindromic_substring(input_string1)}'")
print(f"The longest palindromic substring in '{input_string2}' is '{longest_palindromic_substring(input_string2)}'")
print("\n")

""". Merge Intervals
   - Write a program to merge overlapping intervals in a list of intervals.
   - Expected output: If the input is `[(1, 3), (2, 6), (8, 10), (15, 18)]`, the output should be `[(1, 6), (8, 10), (15, 18)]`.
"""
print(" Merge Intervals")
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    
    return merged

input_intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
output_intervals = merge_intervals(input_intervals)

print("Merged intervals:", output_intervals)
print("\n")

"""Maximum Subarray
   - Write a program to find the maximum sum of a contiguous subarray within a given array.
   - Expected output: If the input array is `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, the output should be `6`, as the maximum subarray is `[4, -1, 2, 1]`.
"""
print(" Maximum Subarray")
def max_subarray_sum(nums):
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        
        max_sum = max(max_sum, current_sum)
    
    return max_sum

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(array)
print("The maximum sum of a contiguous subarray is:", result)
print("\n")

""". Minimum Edit Distance
   - Write a program to calculate the minimum number of operations (insertions, deletions, or substitutions) required to transform one string into another.
   - Expected output: If the two input strings are "kitten" and "sitting", the output should be `3`.
"""
print(" Minimum Edit Distance")
def min_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,  
                               dp[i][j - 1] + 1,   
                               dp[i - 1][j - 1] + 1) 
    
    return dp[m][n]

str1 = "kitten"
str2 = "sitting"
result = min_edit_distance(str1, str2)
print(f"The minimum edit distance between '{str1}' and '{str2}' is {result}")
print("\n")

"""Boggle Game
    - Implement a program that solves the Boggle game, given a board and a list of words.
    - Expected output: The program should print all the words found in the Boggle board.
"""
print(" Boggle Games")
board = [
    ['T', 'W', 'Y', 'R'],
    ['E', 'N', 'P', 'H'],
    ['G', 'Z', 'Q', 'R'],
    ['O', 'N', 'T', 'A']
]

word_list = ["TEN", "TWO", "ONE", "GO", "TON", "PEN", "PRONG", "TEAR", "NOTE"]

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def is_valid(x, y, visited, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and not visited[x][y]

def dfs(board, word, x, y, visited, index):
    if index == len(word):
        return True

    if not is_valid(x, y, visited, board) or board[x][y] != word[index]:
        return False

    visited[x][y] = True

    for dx, dy in directions:
        if dfs(board, word, x + dx, y + dy, visited, index + 1):
            return True

    visited[x][y] = False
    return False

def find_words(board, word_list):
    found_words = []
    for word in word_list:
        found = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = [[False] * len(board[0]) for _ in range(len(board))]
                if dfs(board, word, i, j, visited, 0):
                    found_words.append(word)
                    found = True
                    break
            if found:
                break
    return found_words

found_words = find_words(board, word_list)
print("Words found in the Boggle board:", found_words)
