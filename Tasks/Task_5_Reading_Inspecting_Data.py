import pandas as pd

# Read the CSV file
df = pd.read_csv(r"C:\Users\User\Documents\intwernova internship\Internnova_Week_2_Numpy_Pandas\students.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Display number of rows and columns
print("\nNumber of Rows and Columns:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())