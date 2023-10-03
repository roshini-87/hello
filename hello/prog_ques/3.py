import math

def BracketCombinations(num):
    # Calculate the nth Catalan number using the formula
    catalan_number = math.factorial(2 * num) // (math.factorial(num + 1) * math.factorial(num))
    return catalan_number

num = int(input())
result = BracketCombinations(num)
print("Number of valid combinations:", result)
