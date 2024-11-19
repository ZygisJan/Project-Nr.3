# Step 1: Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Import the dataset
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url)

# Step 3: Check out the type of the columns
print("Column types before transformation:")
print(apple.dtypes)

# Step 4: Transform the Date column as a datetime type
apple['Date'] = pd.to_datetime(apple['Date'])

# Step 5: Set the date as the index
apple.set_index('Date', inplace=True)

# Step 6: Is there any duplicate dates?
duplicate_dates = apple.index.duplicated().any()
print(f"Are there any duplicate dates? {'Yes' if duplicate_dates else 'No'}")

# Step 7: Sort the index so that the first entry is the oldest date
apple.sort_index(inplace=True)

# Step 8: Get the last business day of each month
last_business_day = apple.resample('ME').last()
print("\nLast business day of each month:")
print(last_business_day.head())

# Step 9: What is the difference in days between the first day and the oldest
date_diff = (apple.index[-1] - apple.index[0]).days
print(f"\nDifference in days between the first and last date: {date_diff} days")

# Step 10: How many months in the data we have?
num_months = apple.resample('ME').size().shape[0]
print(f"\nNumber of months in the data: {num_months}")

# Step 11: Plot the 'Adj Close' value
plt.figure(figsize=(13.5, 9))
plt.plot(apple['Adj Close'], label='Adj Close')
plt.title('Apple Stock - Adjusted Close Price')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.show()
