# HackerRank Challenge: Arithmetic Operators
# -------------------------------------------
# Problem Statement:
# Given:
# 1. The base cost of a meal (meal_cost) as a floating-point number.
# 2. The tip percentage (tip_percent) as an integer.
# 3. The tax percentage (tax_percent) as an integer.
#
# Task:
# - Compute the total meal cost including tip and tax.
# - Round the final cost to the nearest integer.
# - Print the final rounded value.
#
# Formula:
# total_cost = meal_cost + (meal_cost * tip_percent / 100) + (meal_cost * tax_percent / 100)
#
# Input Format:
# - A float (meal_cost)
# - An integer (tip_percent)
# - An integer (tax_percent)
#
# Output Format:
# - A single integer (total meal cost rounded)
#
# Example:
# Input:
# 12.00
# 20
# 8
#
# Output:
# 15
#
# Explanation:
# - Tip: 12 * (20/100) = 2.4
# - Tax: 12 * (8/100) = 0.96
# - Total Cost: 12 + 2.4 + 0.96 = 15.36
# - Rounded Output: 15
#
# -------------------------------------------
# Code starts from here

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    total_cost = round(meal_cost + tip + tax)
    print(total_cost)

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

solve(meal_cost, tip_percent, tax_percent)



