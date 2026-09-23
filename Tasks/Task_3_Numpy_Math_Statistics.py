import numpy as np

# Create a numerical dataset
numbers = np.array([10, 20, 30, 40, 50])

print("Numerical Dataset:")
print(numbers)

# Mathematical Operations
print("\nMathematical Operations:")

print("Addition:", numbers + 5)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2)
print("Division:", numbers / 2)

# Statistical Operations
print("\nStatistical Operations:")

print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Standard Deviation:", np.std(numbers))
print("Sum:", np.sum(numbers))