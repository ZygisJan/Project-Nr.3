import pandas as pd

# Step 1: Import the dataset from the given address
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, delimiter='|')

# Step 2: Assign it to a variable called users and use 'user_id' as index
users = users.set_index('user_id')

# Step 3: See the first 25 entries
print("First 25 entries:")
print(users.head(25))

# Step 4: See the last 10 entries
print("\nLast 10 entries:")
print(users.tail(10))

# Step 5: What is the number of observations in the dataset?
print("\nNumber of observations in the dataset:")
print(users.shape[0])

# Step 6: What is the number of columns in the dataset?
print("\nNumber of columns in the dataset:")
print(users.shape[1])

# Step 7: Print the name of all the columns
print("\nNames of all columns:")
print(users.columns.tolist())

# Step 8: How is the dataset indexed?
print("\nIndex of the dataset:")
print(users.index)

# Step 9: What is the data type of each column?
print("\nData types of each column:")
print(users.dtypes)

# Step 10: Print only the occupation column
print("\nOccupation column:")
print(users['occupation'])

# Step 11: How many different occupations are in this dataset?
print("\nNumber of unique occupations:")
print(users['occupation'].nunique())

# Step 12: What is the most frequent occupation?
print("\nMost frequent occupation:")
print(users['occupation'].mode()[0])

# Step 13: Summarize the DataFrame
print("\nDataFrame summary:")
print(users.describe(include='all'))

# Step 14: Summarize all the columns
print("\nSummary of all columns:")
print(users.describe(include='all'))

# Step 15: Summarize only the occupation column
print("\nSummary of the occupation column:")
print(users['occupation'].describe())

# Step 16: What is the mean age of users?
print("\nMean age of users:")
print(users['age'].mean())

# Step 17: What is the age with the least occurrence?
print("\nAge with the least occurrence:")
print(users['age'].value_counts().idxmin())
