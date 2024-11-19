import pandas as pd

# Step 1: Import the dataset from this address
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'
crime = pd.read_csv(url)

# Step 2: Assign it to a variable called crime
print("Dataset overview:")
print(crime.head())

# Step 3: What is the type of the columns?
print("\nColumn types:")
print(crime.dtypes)

# Step 4: Convert the type of the column Year to datetime64
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')
print("\nYear column converted to datetime:")
print(crime['Year'].head())

# Step 5: Set the Year column as the index of the dataframe
crime = crime.set_index('Year')
print("\nDataFrame with Year set as index:")
print(crime.head())

# Step 6: Delete the Total column
crime = crime.drop(columns=['Total'])
print("\nDataFrame after dropping 'Total' column:")
print(crime.head())

# Step 7: Group the year by decades and sum the values
decade_groups = (crime.resample('10YS').sum())
decade_groups['Population'] = crime['Population'].resample('10YS').max()
print("\nDecade-wise sum of values (with max population per decade):")
print(decade_groups)

# Step 8: What is the most dangerous decade to live in the US?
most_dangerous_decade = decade_groups.idxmax().drop('Population')
print("\nMost dangerous decade based on crime rates:")
print(most_dangerous_decade)
