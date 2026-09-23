import pandas as pd

# Read the CSV file
df = pd.read_csv(r"C:\Users\User\Documents\intwernova internship\Internnova_Week_2_Numpy_Pandas\students.csv")

print("Original Data:")
print(df)

# Sort students by Marks in descending order
processed_df = df.sort_values(by="Marks", ascending=False)

print("\nProcessed Data:")
print(processed_df)

# Export the processed data to a new CSV file
processed_df.to_csv(
    r"C:\Users\User\Documents\intwernova internship\Internnova_Week_2_Numpy_Pandas\processed_students.csv",
    index=False
)

print("\nData exported successfully to processed_students.csv")

# Read the exported file to verify
check_df = pd.read_csv(
    r"C:\Users\User\Documents\intwernova internship\Internnova_Week_2_Numpy_Pandas\processed_students.csv"
)

print("\nExported File:")
print(check_df)