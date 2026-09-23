import pandas as pd

# Create first DataFrame
student_details = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "Department": ["BCA", "BCA", "BCA", "BCA", "BCA"]
})

# Create second DataFrame
student_marks = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5],
    "Marks": [75, 82, 68, 90, 77],
    "City": ["Nanded", "Pune", "Nanded", "Mumbai", "Nashik"]
})

# Merge DataFrames
merged_df = pd.merge(student_details, student_marks, on="Student_ID")

print("Merged DataFrame:")
print(merged_df)

# Create another DataFrame for concatenation
more_students = pd.DataFrame({
    "Student_ID": [6, 7],
    "Name": ["Neha", "Karan"],
    "Department": ["BCA", "BCA"]
})

# Concatenate DataFrames
concatenated_df = pd.concat([student_details, more_students], ignore_index=True)

print("\nConcatenated DataFrame:")
print(concatenated_df)

# GroupBy operation
grouped_data = merged_df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(grouped_data)

# Pivot Table
pivot_table = pd.pivot_table(
    merged_df,
    values="Marks",
    index="Department",
    columns="City",
    aggfunc="mean"
)

print("\nPivot Table:")
print(pivot_table)