import pandas as pd

# Create a Pandas Series
marks = pd.Series([75, 82, 68, 90, 77])

print("Pandas Series:")
print(marks)

# Create a DataFrame
students = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [75, 82, 68, 90, 77]
}

df = pd.DataFrame(students)

print("\nStudent DataFrame:")
print(df)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display index
print("\nIndex:")
print(df.index)

# Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

print("\nUpdated DataFrame:")
print(df)