import pandas as pd

# Load sales dataset
df=pd.read_csv(r"c:\Users\saniy\Downloads\sample-sales.csv")

# Display first 5 rows
print("Sales Data:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nSales Summary:")
print(df.describe())