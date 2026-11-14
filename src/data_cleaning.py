
import pandas as pd
import numpy as np

# Load original dataset
df = pd.read_csv(
    "data/raw/construction_cost_estimation_dataset.csv"
)

# 1. Dataset overview
print("\n========== DATASET OVERVIEW ==========")

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# 2. Column information
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# 3. Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 4. Duplicate records
print("\n========== DUPLICATES ==========")
print("Total duplicates:", df.duplicated().sum())

# 5. Statistical summary
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# 6. Unique values in categorical columns
print("\n========== CATEGORICAL VALUES ==========")

categorical_columns = df.select_dtypes(
    include=["object", "str"]
).columns

for col in categorical_columns:
    print(f"\n{col}:")
    print(df[col].value_counts())

print("\n========== INSPECTION COMPLETE ==========")

import pandas as pd
import numpy as np

# Load original dataset
df = pd.read_csv(
    "data/raw/construction_cost_estimation_dataset.csv"
)

# 1. Dataset overview
print("\n========== DATASET OVERVIEW ==========")

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# 2. Column information
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# 3. Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 4. Duplicate records
print("\n========== DUPLICATES ==========")
print("Total duplicates:", df.duplicated().sum())

# 5. Statistical summary
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# 6. Unique values in categorical columns
print("\n========== CATEGORICAL VALUES ==========")

categorical_columns = df.select_dtypes(
    include=["object", "str"]
).columns

for col in categorical_columns:
    print(f"\n{col}:")
    print(df[col].value_counts())

print("\n========== INSPECTION COMPLETE ==========")
python src/data_cleaning.py