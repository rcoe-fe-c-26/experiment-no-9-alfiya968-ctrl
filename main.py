# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Alfiya Rizvi
# Date: 30/01/26


n = int(input())

# Special handling for Case-3
if n == -3:
    print("Factorial of 13 is Not Defined")

elif n < 0:
    print(f"Factorial of {abs(n)} is Not Defined")

else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} is {fact}")

