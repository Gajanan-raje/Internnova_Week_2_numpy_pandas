import pandas as pd

# Read the CSV file
df = pd.read_csv(r"C:\Users\User\Documents\intwernova internship\Internnova_Week_2_Numpy_Pandas\students.csv")

# Select specific columns
print("Selected Columns:")
print(df[["Name", "Marks"]])

# Select specific rows
print("\nSelected Rows:")
print(df.iloc[0:3])

# Filter students with marks greater than 80
print("\nStudents with Marks Greater Than 80:")
print(df[df["Marks"] > 80])

# Filter using multiple conditions
print("\nStudents with Marks Greater Than 75 and Age Less Than 22:")
print(df[(df["Marks"] > 75) & (df["Age"] < 22)])

# Sort by Marks in ascending order
print("\nSorted by Marks - Ascending:")
print(df.sort_values(by="Marks"))

# Sort by Marks in descending order
print("\nSorted by Marks - Descending:")
print(df.sort_values(by="Marks", ascending=False))