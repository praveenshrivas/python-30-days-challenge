# HackerRank Challenge: Loops - Multiplication Table
# --------------------------------------------------
# 🎯 Goal:
# Given an integer `n`, print its first 10 multiples.
# Each multiple should be printed in the format:
# n x i = result, where i ranges from 1 to 10
#
# 📥 Input:
# A single positive integer `n` (1 ≤ n ≤ 100)
#
# 📤 Output:
# Print 10 lines in the format:
# n x i = result
#
# 💡 Example:
# Input: 2
# Output:
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 10 = 20
#
# --------------------------------------------------
n = int(input())

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
