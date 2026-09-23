import numpy as np

# Create a NumPy array containing 10 numbers
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("NumPy Array:")
print(numbers)

# Display shape, size and data type
print("\nShape:", numbers.shape)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)

# Create a one-dimensional array
one_d_array = np.array([1, 2, 3, 4, 5])

print("\nOne-Dimensional Array:")
print(one_d_array)

# Create a two-dimensional array
two_d_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nTwo-Dimensional Array:")
print(two_d_array)