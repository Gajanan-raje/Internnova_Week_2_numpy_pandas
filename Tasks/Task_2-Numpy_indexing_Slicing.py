import numpy as np

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:")
print(numbers)

# Indexing
print("\nIndexing:")
print("First element:", numbers[0])
print("Fifth element:", numbers[4])

# Slicing
print("\nSlicing:")
print("Elements from index 2 to 6:", numbers[2:7])

# Create a two-dimensional array
two_d_array = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nTwo-Dimensional Array:")
print(two_d_array)

# Access specific rows and columns
print("\nRows and Columns:")
print("First row:", two_d_array[0])
print("Second column:", two_d_array[:, 1])
print("Element at row 2, column 3:", two_d_array[1, 2])

# Reshape the array
original_array = np.array([1, 2, 3, 4, 5, 6])

reshaped_array = original_array.reshape(2, 3)

print("\nOriginal Array for Reshaping:")
print(original_array)

print("\nReshaped Array:")
print(reshaped_array)