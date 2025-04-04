"""
GOAL:
1. Read an integer, a double, and a string from input.
2. Add the integer to 4 and print the result.
3. Add the double to 4.0 and print the result (rounded to 1 decimal place).
4. Concatenate the string with "HackerRank " and print the result.

EXAMPLE:
Input: 
12
4.0
is the best place to learn and practice coding!

Output: 
16
8.0
HackerRank is the best place to learn and practice coding!
"""
# code starts from here.
i = 4
d = 4.0
s = 'HackerRank '

num1 = int(input())
num2 = float(input())
word = input()

print(num1 + i)
print(f"{num2 + d:.1f}")
print(f"{s}{word}")
