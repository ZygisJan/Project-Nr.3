# Step 1: Import the necessary libraries
import pandas as pd
import numpy as np

# Step 2: Import the dataset from the provided address
# Step 3: Assign it to a variable called wine
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
wine = pd.read_csv(url, header=None)

# Step 4: Delete the first, fourth, seventh, ninth, eleventh, thirteenth, and fourteenth columns
wine.drop(columns=[0, 3, 6, 8, 10, 12, 13], inplace=True)

# Step 5: Assign the columns as below
wine.columns = [
    'alcohol',
    'malic_acid',
    'alcalinity_of_ash',
    'magnesium',
    'flavanoids',
    'proanthocyanins',
    'hue'
]

# Step 6: Set the values of the first 3 rows from alcohol as NaN
wine.loc[:2, 'alcohol'] = np.nan

# Step 7: Set the value of the rows 3 and 4 of magnesium as NaN
wine.loc[2:3, 'magnesium'] = np.nan

# Step 8: Fill the NaN values with 10 in alcohol and 100 in magnesium
wine.loc[:, 'alcohol'] = wine['alcohol'].fillna(10)
wine.loc[:, 'magnesium'] = wine['magnesium'].fillna(100)

# Step 9: Count the number of missing values
missing_values_count = wine.isna().sum().sum()
print(f"Number of missing values: {missing_values_count}")

# Step 10: Create an array of 10 random numbers up until 10
random_indices = np.random.randint(0, len(wine), 10)

# Step 11: Use random numbers generated as an index and assign NaN value to each of these cells
for i in random_indices:
    col = np.random.choice(wine.columns)
    wine.loc[i, col] = np.nan

# Step 12: Count the number of missing values again
missing_values_count_after = wine.isna().sum().sum()
print(f"Number of missing values after random assignment: {missing_values_count_after}")

# Step 13: Delete the rows that contain missing values
wine.dropna(inplace=True)

# Step 14: Print only the non-null values in alcohol
print("\nNon-null values in 'alcohol':")
print(wine['alcohol'].dropna())

# Step 15: Reset the index
wine.reset_index(drop=True, inplace=True)
print("\nDataFrame after resetting index:")
print(wine.head())
