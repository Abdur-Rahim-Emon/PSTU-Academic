import pandas as pd
import os

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "rui_fish_dataset.csv")

# Read the CSV
data = pd.read_csv(csv_path)

# Print everything
print("Column names:", data.columns.tolist())
print("\nShape (rows, columns):", data.shape)
print("\nFirst 5 rows:")
print(data.head())

print("\nFull data:")
print(data)