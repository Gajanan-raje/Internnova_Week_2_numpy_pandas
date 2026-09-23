import pandas as pd

# Read the CSV file
df = pd.read_csv(r"C:\Users\User\Documents\intwernova internship\Internnova_Week_2_Numpy_Pandas\students_missing.csv")

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Display rows containing missing values
print("\nRows with Missing Values:")
print(df[df.isnull().any(axis=1)])

# Remove rows with missing values
df_drop = df.dropna()

print("\nDataset After Removing Missing Values:")
print(df_drop)

# Fill missing numerical values with the mean
df_fill = df.copy()
df_fill["Age"] = df_fill["Age"].fillna(df_fill["Age"].mean())
df_fill["Marks"] = df_fill["Marks"].fillna(df_fill["Marks"].mean())

# Fill missing City with "Unknown"
df_fill["City"] = df_fill["City"].fillna("Unknown")

print("\nDataset After Filling Missing Values:")
print(df_fill)