# HackerRank Challenge: Maximum Consecutive 1s in Binary  
# --------------------------------------------------  
# 🎯 Goal:  
# Given an integer, convert it to binary and print the maximum number of consecutive 1s in the binary representation.

# 📥 Input:  
# - A single integer `n`

# 📤 Output:  
# - An integer representing the **maximum count of consecutive 1s** in the binary representation of `n`

# 💡 Example:  
# Input:  
# 5  
# Output:  
# 1  
#
# Input:  
# 13  
# Output:  
# 2  
#
# 🧠 Explanation:  
# - 5 in binary is `101`, which has one group of 1s (max consecutive: 1)  
# - 13 in binary is `1101`, which has a group of two 1s (max consecutive: 2)

# --------------------------------------------------  

n = int(input())
binary = bin(n)[2:]               # Convert to binary and remove '0b' prefix
max_consecutive_1s = max(map(len, binary.split('0')))
print(max_consecutive_1s)
