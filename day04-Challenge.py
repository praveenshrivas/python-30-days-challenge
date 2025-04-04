# HackerRank Challenge: Conditional Statements
# --------------------------------------------
# 🎯 Goal:
# Given an integer `n`, determine if it is "Weird" or "Not Weird" using the following rules:
#
# - If `n` is odd → print "Weird"
# - If `n` is even and in the inclusive range of 2 to 5 → print "Not Weird"
# - If `n` is even and in the inclusive range of 6 to 20 → print "Weird"
# - If `n` is even and greater than 20 → print "Not Weird"
#
# 📥 Input:
# A single positive integer `n` (1 ≤ n ≤ 100)
#
# 📤 Output:
# Print either:
# - "Weird"
# - or "Not Weird"
#
# 💡 Examples:
# Input: 3        Output: Weird
# Input: 24       Output: Not Weird
#
# --------------------------------------------

n = int(input())  # Read input from user

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
