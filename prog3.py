import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = r"C:\Users\user\Desktop\mypack\Unemployment in India (2).csv"
df = pd.read_csv(file_path)
# Remove extra spaces in column names
df.columns = df.columns.str.strip()
# Remove extra spaces in all string columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
# Display basic information about the dataset
print("Basic Info:")
print(df.info())
# Display first few rows
print("\nFirst 5 Rows:")
print(df.head())
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Drop rows with missing values
df.dropna(inplace=True)
# Convert 'Date' column to datetime format after removing spaces
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
# Drop rows where Date conversion failed
df.dropna(subset=['Date'], inplace=True)
# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# A line plot for unemployment rate over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y=' Estimated Unemployment Rate (%)', data=df, marker='o', color='b')
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()

# A line plot for unemployment rate over time
plt.figure(figsize=(14, 6))
sns.boxxplot(x='Region', y=' Estimated Unemployment Rate (%)', data=df)
plt.xticks(rotation=90)
plt.xlabel('Region')
plt.ylabel('Unemployment Rate (%)')
plt.title('unemployment rate distribution by region')
plt.show()

