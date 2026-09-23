import pandas as pd

# 1. Load the dataset
df = pd.read_csv(
    r"C:\Users\User\Documents\intwernova internship\Internnova_Week_2_Numpy_Pandas\students.csv"
)

print("===== MINI DATA ANALYSIS PROJECT =====")

# 2. Data Inspection
print("\n1. First 5 Rows:")
print(df.head())

print("\n2. Dataset Information:")
df.info()

print("\n3. Statistical Summary:")
print(df.describe())

# 3. Check Missing Values
print("\n4. Missing Values:")
print(df.isnull().sum())

# 4. Handle Missing Values
df_cleaned = df.copy()

df_cleaned["Age"] = df_cleaned["Age"].fillna(
    df_cleaned["Age"].mean()
)

df_cleaned["Marks"] = df_cleaned["Marks"].fillna(
    df_cleaned["Marks"].mean()
)

df_cleaned["City"] = df_cleaned["City"].fillna("Unknown")

print("\n5. Cleaned Dataset:")
print(df_cleaned)

# 5. Select Specific Columns
print("\n6. Selected Columns:")
print(df_cleaned[["Name", "Marks", "City"]])

# 6. Filter Data
print("\n7. Students with Marks Greater Than 80:")
high_scorers = df_cleaned[df_cleaned["Marks"] > 80]
print(high_scorers)

# 7. Sort Data
print("\n8. Students Sorted by Marks:")
sorted_students = df_cleaned.sort_values(
    by="Marks",
    ascending=False
)
print(sorted_students)

# 8. GroupBy Analysis
print("\n9. Average Marks by Department:")
grouped_data = df_cleaned.groupby("Department")["Marks"].mean()
print(grouped_data)

# 9. Pivot Table
print("\n10. Pivot Table - Average Marks by City:")
pivot_table = pd.pivot_table(
    df_cleaned,
    values="Marks",
    index="City",
    aggfunc="mean"
)
print(pivot_table)

# 10. Key Insights
highest_marks = df_cleaned["Marks"].max()
lowest_marks = df_cleaned["Marks"].min()
average_marks = df_cleaned["Marks"].mean()

top_student = df_cleaned.loc[
    df_cleaned["Marks"].idxmax(), "Name"
]

print("\n===== KEY INSIGHTS =====")
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", round(average_marks, 2))
print("Top Performing Student:", top_student)

# 11. Export Cleaned Dataset
output_file = (
    r"C:\Users\User\Documents\intwernova internship"
    r"\Internnova_Week_2_Numpy_Pandas\cleaned_students.csv"
)

df_cleaned.to_csv(output_file, index=False)

print("\nCleaned dataset exported successfully.")
print("File: cleaned_students.csv")