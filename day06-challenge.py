# HackerRank Challenge: String Split Based on Index
# --------------------------------------------------
# 🎯 Goal:
# For each string input, print its even-indexed characters
# followed by its odd-indexed characters, space-separated.
#
# 📥 Input:
# - First line: An integer `t`, number of test cases
# - Next `t` lines: One string `s` per line
#
# 📤 Output:
# - For each string, print: "<even_chars> <odd_chars>"
#
# 💡 Example:
# Input:
# 2
# Hacker
# Rank
#
# Output:
# Hce akr
# Rn ak
#
# --------------------------------------------------
t = int(input())

for _ in range(t):
    s = input()
    even_chars = s[::2]
    odd_chars = s[1::2]
    print(f"{even_chars} {odd_chars}")
# ##########################################
# Read all input at once
inputs = [input() for _ in range(int(input()))]

# Process and print outputs
for s in inputs:
    even_chars = s[::2]
    odd_chars = s[1::2]
    print(f"{even_chars} {odd_chars}")
