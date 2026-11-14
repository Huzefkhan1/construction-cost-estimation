import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import dataset
df = pd.read_csv("data/construction_cost_estimation_cleaned.csv")

# Display dataset
print(df.head(10))

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns.tolist())